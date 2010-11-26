from __future__ import with_statement

import sys
import elementflow

from opster import command

from . utils import nice, CData, patch_elemenflow, unicode_csv_reader

def write_tags(xml, text, domain):
    """ Splits comma-separated tags or categories
        and writes them to the XML.
    """
    for tag in text.split(','):
        tag = tag.strip()
        if tag != '':
            if domain == 'category':
                # skip domain for the 'category' domain and
                # item without namespaces
                attrs = {}
            else:
                attrs = dict(domain = domain)

            xml.element(
                'category',
                attrs = attrs,
                text = CData(tag)
            )
            xml.element(
                'category',
                attrs = dict(
                    domain = domain,
                    nicename = nice(tag),
                ),
                text = CData(tag)
            )


def write_item(xml, item):
    """ This function writes single item into the xml stream.
    """
    with xml.container('item') as c:
        custom_fields = [
            (key[13:], value)
            for key, value in item.iteritems()
            if key.startswith('custom_field')
        ]
        if custom_fields:
            with c.container('wp:postmeta') as meta:
                for key, value in custom_fields:
                    c.element('wp:meta_key', text = CData(key))
                    c.element('wp:meta_value', text = CData(value))

        c.element('title', text = CData(item.get('post_title', '')))
        c.element('content:encoded', text = CData(item.get('post_post', '')))
        c.element('excerpt:encoded', text = CData(item.get('post_excerpt', '')))

        write_tags(c, item.get('post_categories', ''), 'category')
        write_tags(c, item.get('post_tags', ''), 'tag')


def convert(input_file, output_file, indent = False):
    """ This function converts data from CSV file
        to the WXR.
    """
    reader = unicode_csv_reader(input_file)

    with elementflow.xml(
            output_file,
            'rss',
            attrs = dict(version = '2.0'),
            namespaces = dict(
                excerpt = "http://wordpress.org/export/1.0/excerpt/",
                content = "http://purl.org/rss/1.0/modules/content/",
                wfw = "http://wellformedweb.org/CommentAPI/",
                dc = "http://purl.org/dc/elements/1.1/",
                wp = "http://wordpress.org/export/1.0/",
            ),
            indent = indent,
    ) as xml:
        for item in reader:
            write_item(xml, item)


@command(usage = '%name -i input.csv -o output.wxr')
def main(
    input_filename = ('i', 'STDIN', 'Input filename'),
    output_filename = ('o', 'STDOUT', 'Output filename'),
    format = ('f', False, 'Format output'),
):
    """ Converts from CSV format to the WXR
(Wordpress's import/export format)
    """
    patch_elemenflow()

    with input_filename == 'STDIN' and sys.stdin or \
         open(input_filename) as input_file:
        with output_filename == 'STDOUT' and sys.stdout or \
             open(output_filename, 'w') as output_file:
            convert(input_file, output_file, indent = format)



import re
import string
import elementflow

from csv import DictReader

NICE_RE = re.compile(
    r'[\s%s]+' % ''.join(map(lambda x: '\\' + x, string.punctuation))
)

def nice(tag):
    """ Replaces whitespaces and punctuations with -
        and lowercases the string:

        >>> nice('Ed Stelmach (Alberta Premier)')
        'ed-stelmach-alberta-premier'
    """
    return NICE_RE.sub('-', tag).strip('-').lower()


class CData(unicode):
    pass


def patch_elemenflow():
    elementflow_escape = elementflow.escape

    def escape(text):
        if isinstance(text, CData):
            return '<![CDATA[%s]]>' % text
        return elementflow_escape(text)
    elementflow.escape = escape


def unicode_csv_reader(*args, **kwargs):
    """ This is a generator which decodes
        readed strings from utf-8 to unicode
        on the fly.
    """
    reader = DictReader(*args, **kwargs)

    def force_unicode(value):
        if isinstance(value, str):
            return value.decode('utf-8')
        return value

    for line in reader:
        yield dict(
            (key.strip(), force_unicode(value))
            for key, value in line.items()
        )


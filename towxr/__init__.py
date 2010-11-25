from __future__ import with_statement

from csv import DictReader
from opster import command

@command(usage = '%name input.csv output.wxr')
def main(input_filename, output_filename):
    """ Converts from CSV format to the WXR
(Wordpress's import/export format)
    """
    with open(input_filename) as f:
        reader = DictReader(f)
        data = list(reader)
        print len(data)

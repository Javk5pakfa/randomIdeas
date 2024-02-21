# A helper tool for generating a pip install --update command with a large
# amount of packages to be updated using a textfile of the list of packages
# currently outdated.

import pandas as pd
import argparse as arg

parser = arg.ArgumentParser(description='Parse pip text file.')
parser.add_argument('--fn',
                    type=str,
                    help='The file path of the text file.',
                    required=True,
                    nargs=1)
args = parser.parse_args()

with open(args.fn[0], 'r') as file:
    data = pd.read_table(file,
                         sep='\s+',
                         skiprows=2,
                         header=None,
                         names=["Package", "Version", "Latest", "Type"])

package_names = ' '.join(data['Package'].tolist())
print('pip3 install --upgrade ' + package_names)

# A helper tool for generating a pip install --update command with a large
# amount of packages to be updated using a text file of the list of packages
# currently outdated.

import pandas as pd
import argparse
from pathlib import Path

# Set up the argument parser
parser = argparse.ArgumentParser(description='Parse pip text file.')
parser.add_argument(
    '--fn',
    type=Path,
    help='The file path of the text file.',
    required=True
)
args = parser.parse_args()

# Read the file using pandas
file_path = args.fn
with file_path.open('r') as file:
    data = pd.read_table(
        file,
        sep=r'\s+',
        skiprows=2,
        header=None,
        names=["Package", "Version", "Latest", "Type"]
    )

# Generate the pip install command
package_names = ' '.join(data['Package'].tolist())
print(f'pip3 install --upgrade {package_names}')

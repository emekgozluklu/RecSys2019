import os
import sys
import time
"""
Used to randomly sample huge CSV file with given sample rate.

Usage:
    python3 sample_data.py <filepath> <nrows>

Output:
    <file>_sampled.csv
"""

if len(sys.argv) != 3:
    raise "Error. Proper usage: python3 sample_data.py <filepath> <ratio>"

filepath = sys.argv[1]
ratio = float(sys.argv[2])

lines = int(os.popen(f'wc -l < {filepath}').read())

if ratio >= 1:
    ratio /= 100

sample_size =  int(ratio*lines)

out_file = filepath.replace(".csv", "_sampled.csv")
out_path = os.path.sep.join(out_file.split(os.path.sep)[:-1]) + "/sampled/"

try:
    os.mkdir(out_path)
except FileExistsError:
    pass

out_file = out_path + out_file.split(os.path.sep)[-1]
print(f"Sampling started.\nRows in original file: {lines}\nRows in sample : {sample_size}")
os.system(f"shuf -n {sample_size} {filepath} > {out_file}")

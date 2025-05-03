import argparse
import csv
from types import SimpleNamespace
from towers import MediumBananaFarm

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--csv-income-filename', required=True, help='CSV to read income from')
parser.add_argument('-r', '--round', default=40, type=int, help='compute until round N')
args = parser.parse_args()
print(args)


rows = []
with open(args.csv_income_filename, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(SimpleNamespace(**row))
incomes = []
for i in range(1, args.round):
    ri = rows[i]
    rp = rows[i-1]
    mp = int(rp.After or rp.Funds)
    mi = int(ri.Funds)
    earn = mi - mp
    incomes.append(earn)

bf = MediumBananaFarm()
print(bf)

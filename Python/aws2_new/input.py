import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--first", help='First data for calculation')
parser.add_argument("-s", "--second", help="Second data for calculation")
parser.add_argument("-t", "--type", help="Type for calculation")

args = parser.parse_args()

num1 = int(args.first)
num2 = int(args.second)
operation = args.type
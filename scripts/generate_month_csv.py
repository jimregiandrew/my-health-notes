"""Generate a blank monthly CSV template for health diary tracking."""

import argparse
import calendar
import csv
import sys


def parse_month(value):
    parts = value.split("-")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(f"Invalid month format '{value}'. Expected YYYY-MM.")
    try:
        year, month = int(parts[0]), int(parts[1])
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid month format '{value}'. Expected YYYY-MM.")
    if month < 1 or month > 12:
        raise argparse.ArgumentTypeError(f"Month must be between 01 and 12, got '{parts[1]}'.")
    return year, month


def main():
    parser = argparse.ArgumentParser(description="Generate a blank monthly CSV template.")
    parser.add_argument("month", type=parse_month, help="Month in YYYY-MM format")
    parser.add_argument("-c", "--columns", nargs="+", default=[], help="Additional column names")
    parser.add_argument("-o", "--output", help="Output file path (default: YYYY-MM.csv)")
    args = parser.parse_args()

    year, month = args.month
    num_days = calendar.monthrange(year, month)[1]
    output = args.output or f"{year}-{month:02d}.csv"

    header = ["date"] + args.columns
    with open(output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for day in range(1, num_days + 1):
            writer.writerow([f"{year}-{month:02d}-{day:02d}"] + [""] * len(args.columns))

    print(output)


if __name__ == "__main__":
    main()

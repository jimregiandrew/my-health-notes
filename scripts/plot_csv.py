"""Plot one or more numeric columns from monthly CSV diary files."""

import argparse
import sys

import pandas as pd
import matplotlib.pyplot as plt


def read_csvs(files: list[str]) -> pd.DataFrame:
    """Read and combine one or more CSV diary files into a single DataFrame."""
    frames = []
    for path in files:
        df = pd.read_csv(path, skipinitialspace=True)
        df.columns = df.columns.str.strip().str.lower()
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    combined["date"] = pd.to_datetime(combined["date"])
    combined = combined.sort_values("date").reset_index(drop=True)
    return combined


def plot_cols(df: pd.DataFrame, columns: list[str]) -> None:
    """Plot the requested columns as lines over the date axis."""
    missing = [c for c in columns if c not in df.columns]
    if missing:
        sys.exit(f"Error: columns not found in data: {', '.join(missing)}")

    for col in columns:
        plt.plot(df["date"], pd.to_numeric(df[col], errors="coerce"), label=col)

    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(", ".join(columns))
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Plot columns from CSV diary files.")
    parser.add_argument("files", nargs="+", help="CSV file paths")
    parser.add_argument("-c", "--columns", nargs="+", required=True,
                        help="Column names to plot")
    args = parser.parse_args()

    df = read_csvs(args.files)
    plot_cols(df, [c.lower() for c in args.columns])


if __name__ == "__main__":
    main()

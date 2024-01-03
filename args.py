import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Optimize action investments from a CSV file.")
    parser.add_argument("file_path", help="Path to the CSV file containing action data.")
    parser.add_argument("algorithms", nargs='+', choices=['bruteforce', 'glouton', 'dynamic'], 
                        help="Algorithms to run. Choose from 'bruteforce', 'glouton', 'dynamic'.")
    return parser.parse_args()
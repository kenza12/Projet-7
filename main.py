"""
Investment Optimization Program

This program utilizes different algorithms (bruteforce, glouton, and dynamic) to 
optimize investment strategies based on provided action data. It loads and cleans 
the data, then applies the selected algorithms to find the best combination of actions 
that maximize profit without exceeding a specified budget.
"""

import time
from bruteforce import bruteforce
from optimized import glouton
from dynamic import dynamic
from args import parse_args
from utils import load_data, clean_data, display_results

# Parse arguments from command line
args = parse_args()

# Load data from the specified CSV file
data = load_data(args.file_path)

# Clean and preprocess the data
cleaned_data = clean_data(data)

# Execute Bruteforce algorithm if selected
if 'bruteforce' in args.algorithms:
    start = time.time()
    best_combination, best_profit, best_cost = bruteforce(cleaned_data)
    end = time.time()
    display_results("Bruteforce", best_combination, best_profit, best_cost, end - start)

# Execute Glouton algorithm if selected
if 'glouton' in args.algorithms:
    start = time.time()
    best_combination, best_profit, best_cost = glouton(cleaned_data)
    end = time.time()
    display_results("Glouton", best_combination, best_profit, best_cost, end - start)

# Execute Dynamic algorithm if selected
if 'dynamic' in args.algorithms:
    start = time.time()
    best_combination, best_profit, best_cost = dynamic(cleaned_data)
    end = time.time()
    display_results("Dynamic", best_combination, best_profit, best_cost, end - start)
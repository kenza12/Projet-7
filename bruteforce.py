import pandas as pd
import itertools
import argparse


def load_data(file_path):
    """
    Load and clean action data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing action data.

    Returns:
        DataFrame: A pandas DataFrame containing the cleaned action data.
    """
    df = pd.read_csv(file_path)
    # Standardize column names
    df.columns = ['name', 'price', 'profit']
    # Handle 'profit' column which might be in percentage format
    df['profit'] = df['profit'].replace('%', '', regex=True).astype('float') / 100
    # Convert 'price' to numeric, coercing errors to NaN
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    # Drop rows with NaN values
    df.dropna(inplace=True)
    # Keep rows with positive 'price' and 'profit'
    df = df[(df['price'] > 0) & (df['profit'] > 0)]
    return df


def calculate_profit(actions):
    """
    Calculate the total cost and profit for a given combination of actions.

    Args:
        actions (list): A list of dictionaries, where each dictionary represents an action with its price and profit percentage.

    Returns:
        tuple: A tuple containing the total cost and total profit for the given combination of actions.
    """
    total_cost = sum(action['price'] for action in actions)
    total_profit = sum(action['price'] * action['profit'] for action in actions)
    return total_cost, total_profit


def bruteforce(file_path, max_investment=500):
    """
    Find the best combination of actions that maximizes profit without exceeding the maximum investment limit.

    Args:
        file_path (str): Path to the CSV file containing stock data.
        max_investment (int, optional): The maximum amount to be invested. Defaults to 500.

    Returns:
        tuple: A tuple containing the best combination of actions, the corresponding total profit and total invested cost.
    """
    # Load the actions data from the CSV file
    actions_data = load_data(file_path)

    # Initialize variables for tracking the best profit and combination
    best_profit = 0
    best_combination = []

    # Iterate through all possible combinations of actions
    for r in range(1, len(actions_data) + 1):
        for combination in itertools.combinations(actions_data.to_dict('records'), r):
            cost, profit = calculate_profit(combination)
            if cost <= max_investment and profit > best_profit:
                best_profit = profit
                best_combination = combination
                best_cost = cost

    return best_combination, best_profit, best_cost


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate action investments from a CSV file.")
    parser.add_argument("file_path", help="Path to the CSV file containing action data.")

    args = parser.parse_args()

    # Call bruteforce function with file path argument
    best_combination, best_profit, best_cost = bruteforce(args.file_path)
    print("Best Combination:", [(a['name'], a['price'], a['profit']) for a in best_combination])
    print("Best Profit:", best_profit)
    print("Total Invested Cost:", best_cost)

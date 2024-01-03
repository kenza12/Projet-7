import pandas as pd
from tabulate import tabulate


def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    df = pd.read_csv(file_path)
    df.columns = ['name', 'price', 'profit']
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans data by converting columns and removing invalid rows.

    Args:
        df (pd.DataFrame): DataFrame to be cleaned.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df['profit'] = df['profit'].replace('%', '', regex=True).astype('float') / 100
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.dropna(inplace=True)
    df_cleaned = df[(df['price'] > 0) & (df['profit'] > 0)]
    return df_cleaned


def calculate_profit(actions: list) -> float:
    """
    Calculates the total profit from a list of actions.

    Args:
        actions (list): A list of actions where each action is a dictionary containing 'price' and 'profit'.

    Returns:
        float: The total profit from the given actions.
    """
    total_profit = sum(action['price'] * action['profit'] for action in actions)
    return total_profit


def calculate_cost(actions: list) -> float:
    """
    Calculates the total cost of a list of actions.

    Args:
        actions (list): A list of actions where each action is a dictionary containing 'price'.

    Returns:
        float: The total cost of the given actions.
    """
    total_cost = sum(action['price'] for action in actions)
    return total_cost


def display_results(algorithm_name: str, best_combination: list, best_profit: float, best_cost: float, delta_time: float):
    """
    Displays the results in a formatted way.

    Args:
        algorithm_name (str): The name of the algorithm used.
        best_combination (list): List of selected actions.
        best_profit (float): The best profit achieved.
        best_cost (float): The total cost of the selected actions.
        delta_time (float): Execution time of the algorithm.
    """
    print(f"\n{'#' * 10} {algorithm_name.upper()} {'#' * 10}\n")
    print(f"Execution Time: {delta_time:.4f} seconds")
    print(f"Best Profit: {best_profit:.4f}€")
    print(f"Total Invested Cost: {best_cost:.3f}€\n")
    table = [(a['name'], f"{a['price']}€", f"{a['profit'] * 100:.2f}%") for a in best_combination]
    print(tabulate(table, headers=["Action", "Price", "Profit"], tablefmt="pretty"))

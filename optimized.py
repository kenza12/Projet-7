import pandas as pd
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
    # Remove rows with NaN values
    df.dropna(inplace=True)
    # Keep rows with positive 'price' and 'profit'
    df = df[(df['price'] > 0) & (df['profit'] > 0)]
    return df


def greedy_optimize(file_path, max_investment=500):
    """
    Optimize action investments using a greedy approach.

    This function reads action data from a CSV file and selects a combination of actions
    that maximizes profit without exceeding a specified maximum investment limit.

    Args:
        file_path (str): Path to the CSV file containing action data.
        max_investment (int, optional): Maximum amount to invest. Defaults to 500.

    Returns:
        list, float, float: A list of selected actions, the total estimated profit, and the total cost invested.
    """

    # Load action data from the CSV file
    actions_data = load_data(file_path)

    # Filter out actions that are too expensive
    actions_data = actions_data[actions_data['price'] <= max_investment]

    # Calculate the actual monetary profit for each action
    actions_data['actual_profit'] = actions_data['price'] * actions_data['profit']

    # Sort actions first by their profit percentage and then by their actual profit, both in descending order
    actions_data_sorted = actions_data.sort_values(by=['profit', 'actual_profit'], ascending=False)

    selected_actions = []
    total_cost = 0
    total_profit = 0

    # Iterates over sorted actions, appending actions to the selected list and accumulating cost and profit as long as the total cost does not exceed the investment limit.
    for _, action in actions_data_sorted.iterrows():
        if total_cost + action['price'] <= max_investment:
            selected_actions.append(action)
            total_cost += action['price']
            total_profit += action['actual_profit']

    return selected_actions, total_profit, total_cost


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize action investments from a CSV file.")
    parser.add_argument("file_path", help="Path to the CSV file containing action data.")

    args = parser.parse_args()

    # Call greedy_optimize function with file path argument
    selected_actions, total_profit, total_cost = greedy_optimize(args.file_path)
    print("Selected actions:", [(a['name'], a['price'], a['profit']) for a in selected_actions])
    print("Total profit:", total_profit)
    print("Total cost invested:", total_cost)

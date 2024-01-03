import numpy as np
from utils import calculate_profit, calculate_cost


def dynamic(actions_data: 'pd.DataFrame', max_investment: int = 500) -> (list, float, float):
    """
    Optimizes action investments using dynamic programming.

    This function applies dynamic programming to select a combination of actions that maximizes profit 
    without exceeding the specified maximum investment limit.

    Args:
        actions_data (pd.DataFrame): DataFrame containing data of actions.
        max_investment (int, optional): Maximum allowed investment. Defaults to 500.

    Returns:
        list: Selected actions as a list of dictionaries.
        float: Total estimated profit from the selected actions.
        float: Total cost of the selected actions.
    """
    n = len(actions_data)  # Number of actions

    # Convert max investment to cents for precision
    max_investment *= 100

    # Sort actions by price and convert prices and profits to Numpy arrays
    actions_data = actions_data.sort_values(by='price').reset_index(drop=True)
    profits = (actions_data['price'] * actions_data['profit'] * 100).to_numpy()
    prices = (actions_data['price'] * 100).astype(int).to_numpy()

    # Initialize dynamic programming table
    dp = np.zeros((n, max_investment + 1), dtype=int)
    dp[0, prices[0]:] = profits[0]  # Initial fill for the first action

    # Fill the table for each action and each possible budget
    for i in range(1, n):
        dp[i, :prices[i]] = dp[i - 1, :prices[i]]
        dp[i, prices[i]:] = np.maximum(dp[i - 1, prices[i]:], profits[i] + dp[i - 1, :-prices[i]])

    # Reconstruct chosen actions to achieve maximum profit
    chosen_actions = []
    w = max_investment
    for i in reversed(range(n)):
        if w >= prices[i] and dp[i, w] != dp[i - 1, w]:
            chosen_actions.append(actions_data.iloc[i])
            w -= prices[i]

    # Calculate total profit and total cost
    total_profit = calculate_profit(chosen_actions)
    total_cost = calculate_cost(chosen_actions)

    return chosen_actions, total_profit, total_cost
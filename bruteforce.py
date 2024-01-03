import itertools
from utils import calculate_profit, calculate_cost


def bruteforce(actions_data: 'pd.DataFrame', max_investment: int = 500) -> (list, float, float):
    """
    Finds the best combination of actions that maximizes profit without exceeding the maximum investment limit
    using a brute force approach.

    This function iteratively evaluates all possible combinations of actions to identify the combination that 
    offers the highest profit without exceeding the specified investment limit.

    Args:
        actions_data (pd.DataFrame): DataFrame containing stock data.
        max_investment (int, optional): The maximum amount to be invested. Defaults to 500.

    Returns:
        list: The best combination of actions as a list of dictionaries.
        float: The total profit corresponding to the best combination.
        float: The total invested cost corresponding to the best combination.
    """

    # Initialize variables
    best_profit = 0
    best_combination = []

    # Iterate through all possible combinations of actions
    for r in range(1, len(actions_data) + 1):
        for combination in itertools.combinations(actions_data.to_dict('records'), r):
            profit = calculate_profit(combination)  # Calculate profit of the current combination
            cost = calculate_cost(combination)  # Calculate cost of the current combination
            # Update best combination if this combination provides a higher profit without exceeding budget
            if cost <= max_investment and profit > best_profit:
                best_profit = profit
                best_combination = combination
                best_cost = cost

    return best_combination, best_profit, best_cost

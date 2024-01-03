
from utils import calculate_profit


def glouton(actions_data: 'pd.DataFrame', max_investment: int = 500) -> (list, float, float):
    """
    Optimizes action investments using a greedy approach.

    This function selects a combination of actions from the given dataset that maximizes profit 
    without exceeding the specified maximum investment limit. It uses a greedy approach to achieve this.

    Args:
        actions_data (pd.DataFrame): DataFrame containing action data.
        max_investment (int, optional): Maximum amount to invest. Defaults to 500.

    Returns:
        list: Selected actions as a list of dictionaries.
        float: Total estimated profit from the selected actions.
        float: Total cost of the selected actions.
    """

    # Filter out actions that are too expensive
    actions_data = actions_data[actions_data['price'] <= max_investment]

    # Calculate actual monetary profit for each action
    actions_data['actual_profit'] = actions_data['price'] * actions_data['profit']

    # Sort actions by profit percentage, then by actual profit, in descending order
    actions_data_sorted = actions_data.sort_values(by=['profit', 'actual_profit'], ascending=False)

    selected_actions = []
    total_cost = 0

    # Iterate over sorted actions, selecting actions as long as total cost is within budget
    for _, action in actions_data_sorted.iterrows():
        if total_cost + action['price'] <= max_investment:
            selected_actions.append(action)
            total_cost += action['price']

    # Calculate total profit from selected actions
    total_profit = calculate_profit(selected_actions)

    return selected_actions, total_profit, total_cost

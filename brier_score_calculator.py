def brier_score(forecasts, outcomes):
    """
    Calculate the Brier score.

    Parameters:
    - forecasts (list): A list of forecasted probabilities.
    - outcomes (list): A list of actual outcomes, where 1 represents True and 0 represents False.

    Returns:
    - float: The Brier score.
    """
    # Ensure input lists have the same length
    assert len(forecasts) == len(outcomes), "Input lists must have the same length"

    # Initialize a variable to keep track of the sum of squared differences
    sum_of_squared_differences = 0

    # Iterate over each forecast-outcome pair
    for forecast, outcome in zip(forecasts, outcomes):
        # Compute the squared difference for this pair
        squared_difference = (forecast - outcome) ** 2
        # Add the squared difference to the running total
        sum_of_squared_differences += squared_difference

    # Compute the mean squared difference
    brier_score_value = sum_of_squared_differences / len(forecasts)

    return brier_score_value

# Example usage:
forecasts = [0.1, 0.9, 0.8, 0.3]  # Forecasted probabilities for four questions
outcomes = [0, 1, 1, 0]  # Actual outcomes for the four questions

# Get the Brier score
score = brier_score(forecasts, outcomes)
print(f"Brier Score: {score}")

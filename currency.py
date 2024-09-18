def format_conversion_result(amount, from_currency, to_currency, rate, conversion_type):
    """Format the result to display in Streamlit app."""
    inverse_rate = 1 / rate
    if conversion_type == "latest":
        return (
            f"The latest conversion rate from {from_currency} to {to_currency} is {rate:.5f}. "
            f"So {amount} {from_currency} corresponds to {rate * amount:.2f} {to_currency}. "
            f"The inverse rate is {inverse_rate:.5f}."
        )
    else:
        return (
            f"The conversion rate on {conversion_type} from {from_currency} to {to_currency} was {rate:.5f}. "
            f"So {amount} in {from_currency} correspond to {rate * amount:.2f} in {to_currency}. "
            f"The inverse rate was {inverse_rate:.5f}."
        )

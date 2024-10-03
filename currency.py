def format_conversion(amount, rate, inverse_rate, from_currency, to_currency, date):
    converted_amount = amount * rate
    if date == 'today':
        date_str = 'today'
    else:
        date_str = date.strftime("%d/%m/%Y")  # Formatting the date as DD/MM/YYYY

    return (f"The conversion rate on {date_str} from {from_currency} to {to_currency} "
            f"is {rate:.5f}. So {amount:.2f} in {from_currency} correspond to {converted_amount:.2f} in {to_currency}. "
            f"The inverse rate was {inverse_rate:.5f}.")

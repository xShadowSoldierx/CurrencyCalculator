import eel
import requests

eel.init('web')

@eel.expose
def conv_currency(from_currency_short: str, to_currency_short: str, amount: float, currency=False):
    print(from_currency_short)
    print(to_currency_short)
    print(amount)
    from_short = from_currency_short.upper()
    to_short = to_currency_short.upper()
    response = requests.get(f'https://api.exchangerate.host/latest?base={from_short}')
    data  = response.json()
    new_amount = amount * data['rates'][to_short]
    if currency == True:
        return new_amount, to_short
    else:
        return new_amount

eel.start('index.html', size=(400,400))
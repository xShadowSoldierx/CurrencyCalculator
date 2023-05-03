'''
An application to convert one currency to another currency
Copyright (C) Ricardo Boock - 2023
'''


import json
import os
import requests

import terminal_output as tOut


def main():
    FILE = os.path.abspath(__file__)
    PATH = os.path.dirname(FILE)
    
    # Welcome
    tOut.print_logo()
    
    # Set available currencies
    currencies = set_currencies()
    
    # Fetch data from API and save to json files
    fetch_data(currencies=currencies, path=PATH)
    
    # Show available currencies
    print_currencies(currencies=currencies)
    
    # Get from currency
    from_currency = get_from_currency(currencies=currencies)
    
    # Get to currency
    to_currency = get_to_currency(currencies=currencies)
    
    # Get amount
    amount = get_amount(currencies=currencies, from_currency=from_currency)
    
    # Calculate and return the converted value
    calc_value(
        path=PATH,
        currencies=currencies,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount
    )
    
    # Rerun application
    rerun_app()


def set_currencies():
    allowed_currency = {
        'armenischer dram': 'AMD',
        'australischer dollar': 'AUD',
        'brasilianischer real': 'BRL',
        'bitcoin': 'BTC',
        'kanadischer dollar': 'CAD',
        'schweizer franken': 'CHF',
        'china yuan renminbi': 'CNY',
        'euro': 'EUR',
        'britisches pfund': 'GBP',
        'hongkong-dollar': 'HKD',
        'indische rupie': 'INR',
        'südkoreanischer won': 'KRW',
        'mexikanischer peso': 'MXN',
        'norwegische krone': 'NOK',
        'neuseeland-dollar': 'NZD',
        'russischer rubel': 'RUB',
        'schwedische krone': 'SEK',
        'singapur-dollar': 'SGD',
        'türkische lira': 'TRY',
        'us dollar': 'USD',
        'japanischer yen': 'JPY',
        'venezolanischer bolívar': 'VES',
        'südafrikanischer rand': 'ZAR'
    }
    
    return allowed_currency


def fetch_data(currencies, path):
    try:
        for i in currencies:
            file = currencies[i]
            
            response = requests.get(f'https://api.exchangerate.host/latest?base={file}')
            data = response.json()
            
            file_name = f'{path}/currency/currency_{file}.json'
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
        tOut.success_exchange_rates_updated()
    except Exception:
        tOut.error_api_connection_failed()


def print_currencies(currencies):
    content = f'''Here is a list of all available currencies:

    {'Currency':<25} | {'Short':<5}
    ---------------------------------
'''
    tOut.print_characters(content=content, speed=tOut.OUTPUT_SPEED)
    
    for currency, short in currencies.items():
        if currency == 'us dollar':
            currency = 'US Dollar'
        else:
            currency = currency.title()
        tOut.print_characters(content=f"    {currency:<25} |  {short:<5}\n", speed=tOut.OUTPUT_SPEED*0.5)


def get_from_currency(currencies):
    try:
        from_currency = input('\n💶 Choose the first currency: ').lower()
        
        if len(from_currency) == 3:
            from_currency = list(currencies.keys())[list(currencies.values()).index(from_currency.upper())]
        
        if from_currency not in currencies:
            raise Exception
    except Exception:
        tOut.error_try_again()
        return get_from_currency(currencies)
    
    return from_currency


def get_to_currency(currencies):
    try:
        to_currency = input('\n💴 Choose the second currency: ').lower()
        
        if len(to_currency) == 3:
            to_currency = list(currencies.keys())[list(currencies.values()).index(to_currency.upper())]
        
        if to_currency not in currencies:
            raise Exception
    except Exception:
        tOut.error_try_again()
        return get_to_currency(currencies)
    
    return to_currency


def get_amount(currencies, from_currency):
    try:
        amount = float(input(f'\n💰 Enter the amount of {currencies[from_currency]}: '))
    except Exception:
        tOut.error_try_again()
        return get_amount(currencies, from_currency)
    
    return amount


def calc_value(path, currencies, from_currency, to_currency, amount):
    from_short = currencies[from_currency]
    to_short = currencies[to_currency]

    with open(f'{path}/currency/currency_{from_short}.json', 'r') as f:
        data = json.load(f)

    new_amount = round(amount * data['rates'][to_short], 2)

    print(f'\n\033[1;32m💵 {amount:.2f} {from_short} are converted {new_amount:.2f} {to_short}!\033[0m\n')


def rerun_app():
    rerun = input("Do you want to restart the program (y/n)? ")
    if rerun == "y":
        main()
    elif rerun == "n":
        print("Exiting program...")
    else:
        tOut.error_try_again()
        rerun_app()


if __name__ == '__main__':
    main()

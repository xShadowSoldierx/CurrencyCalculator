# An application to convert one currency to another currency
# Copyright (C) Ricardo Boock - 2023


import json
import os
import sys
import requests

import terminal_output as tOut


def main():
    FILE = os.path.abspath(__file__)
    PATH = os.path.dirname(FILE)
    
    # Welcome
    tOut.print_logo()
    
    # Set available currencies
    currencies = set_currencies()
    
    # Fetch data from api
    fetch_data(currencies=currencies, path=PATH)
    
    # Show available currencies
    print_currencies(currencies=currencies)
    
    # Get from currency
    from_currency = get_from_currency(currencies=currencies)
    
    # Get to currency
    to_currency = get_to_currency(currencies=currencies)
    
    # Get amount
    amount = get_amount(currencies=currencies, from_currency=from_currency)
    
    # Calculate value
    calc_value(
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
    except:
        tOut.error_api_connection_failed()


def print_currencies(currencies):
    print('\nHere is a list of all available currencies:\n')
    
    print(f"{'Currency':<25} | {'Short':<5}")
    print("---------------------------------")
    for currency, short in currencies.items():
        if currency == 'us dollar':
            currency = 'US Dollar'
        else:
            currency = currency.title()
        print(f"{currency:<25} |  {short:<5}")


def get_from_currency(currencies, from_currency=None):
    try:
        from_currency = input('\nChoose the first currency: ').lower()
        
        if len(from_currency) == 3:
            from_currency = list(currencies.keys())[list(currencies.values()).index(from_currency.upper())]
        
        if from_currency not in currencies:
            raise ValueError
    except KeyboardInterrupt:
        tOut.error_keyboard_interrupt()
        sys.exit()
    except:
        tOut.error_try_again()
        return get_from_currency(from_currency)
    
    return from_currency


def get_to_currency(currencies, to_currency=None):
    try:
        to_currency = input('\nChoose the second currency: ').lower()
        
        if len(to_currency) == 3:
            to_currency = list(currencies.keys())[list(currencies.values()).index(to_currency.upper())]
        
        if to_currency not in currencies:
            raise ValueError
    except KeyboardInterrupt:
        tOut.error_keyboard_interrupt()
        sys.exit()
    except:
        tOut.error_try_again()
        return get_to_currency(to_currency)
    
    return to_currency


def get_amount(currencies, from_currency, amount=None):
    try:
        amount = float(input(f'\nEnter the amount of {currencies[from_currency]}: '))
    except KeyboardInterrupt:
        tOut.error_keyboard_interrupt()
        sys.exit()
    except:
        tOut.error_try_again()
        return get_amount(amount)
    
    return amount


def calc_value(currencies, from_currency, to_currency, amount):
    from_short = currencies[from_currency]
    to_short = currencies[to_currency]

    with open(f'currency/currency_{from_short}.json', 'r') as f:
        data = json.load(f)

    new_amount = round(amount * data['rates'][to_short], 2)

    print(f'{amount:.2f} {from_short} are converted {new_amount:.2f} {to_short}!')


def rerun_app():
    pass


if __name__ == '__main__':
    main()
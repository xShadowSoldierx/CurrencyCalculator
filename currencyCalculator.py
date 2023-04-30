# An application to convert one currency to another currency
# Copyright (C) Ricardo Boock - 2023


import json
import os
import requests


def main():
    # Set available currencies
    currencies = set_currencies()
    
    # Fetch data from api
    fetch_data(currencies=currencies)
    
    # Show available currencies
    print_currencies()
    
    # Get from currency
    get_from_currency()
    
    # Get to currency
    get_to_currency()
    
    # Get amount
    get_amount()
    
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


def fetch_data(currencies):
    try:
        for i in currencies:
            file = currencies[i]
            
            response = requests.get(f'https://api.exchangerate.host/latest?base={file}')
            data = response.json()
            
            file_name = f'currency/currency_{file}.json'
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        print('''**********************************************************************
    * No connection to the API-server. The data might not be the latest. *
    **********************************************************************''')


def print_currencies():
    pass


def get_from_currency():
    pass


def get_to_currency():
    pass


def get_amount():
    pass


def rerun_app():
    pass


if __name__ == '__main__':
    main()
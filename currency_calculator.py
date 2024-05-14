"""
An application to convert one currency to another currency
Copyright (C) Ricardo Boock - 2023
"""

from typing import Dict
import concurrent.futures
import json
import os
import requests

import terminal_output as tOut


def main() -> None:
    """
    This function serves as the entry point of the program.

    It initializes the file path, prints the logo, sets available currencies,
    and fetches data from an API.
    """

    FILE: str = os.path.abspath(__file__)
    PATH: str = os.path.dirname(FILE)

    # Welcome
    tOut.print_logo()

    # Set available currencies
    currencies: Dict[str, str] = set_currencies()

    # Fetch data from API and save to json files
    fetch_data(currencies=currencies, path=PATH)

    # Show available currencies
    print_currencies(currencies=currencies)

    # Get from currency
    from_currency: str = get_from_currency(currencies=currencies)

    # Get to currency
    to_currency: str = get_to_currency(currencies=currencies)

    # Get amount
    amount: float = get_amount(currencies=currencies, from_currency=from_currency)

    # Calculate and return the converted value
    calc_value(
        path=PATH,
        currencies=currencies,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
    )

    # Rerun application
    rerun_app()


def set_currencies() -> Dict[str, str]:
    """
    Sets the available currencies and returns a dictionary mapping long currency names
    to their short codes.

    Returns:
        Dict[str, str]: A dictionary mapping long currency names to their short codes.
    """

    allowed_currency: Dict[str, str] = {
        "armenischer dram": "AMD",
        "australischer dollar": "AUD",
        "brasilianischer real": "BRL",
        "bitcoin": "BTC",
        "kanadischer dollar": "CAD",
        "schweizer franken": "CHF",
        "china yuan renminbi": "CNY",
        "euro": "EUR",
        "britisches pfund": "GBP",
        "hongkong-dollar": "HKD",
        "indische rupie": "INR",
        "südkoreanischer won": "KRW",
        "mexikanischer peso": "MXN",
        "norwegische krone": "NOK",
        "neuseeland-dollar": "NZD",
        "russischer rubel": "RUB",
        "schwedische krone": "SEK",
        "singapur-dollar": "SGD",
        "türkische lira": "TRY",
        "us dollar": "USD",
        "japanischer yen": "JPY",
        "venezolanischer bolívar": "VES",
        "südafrikanischer rand": "ZAR",
    }

    return allowed_currency


def fetch_data(currencies: Dict[str, str], path: str) -> None:
    """
    Fetches data from an API based on the provided currencies and saves it to JSON files.

    Parameters:
    - currencies (Dict[str, str]): A dictionary mapping currency names to their short codes.
    - path (str): The path where the JSON files will be saved.

    Returns:
    None
    """

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = {
                executor.submit(
                    requests.get,
                    f"https://api.exchangerate.host/latest?base={file}",
                    timeout=10,
                ): file
                for file in currencies
            }

            for future in concurrent.futures.as_completed(futures):
                file_name: str = f"{path}/currency/currency_{futures[future]}.json"
                os.makedirs(os.path.dirname(file_name), exist_ok=True)

                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(future.result().json(), f, ensure_ascii=False, indent=4)

        tOut.success_exchange_rates_updated()
    except requests.exceptions.RequestException:
        tOut.error_api_connection_failed()


def print_currencies(currencies: Dict[str, str]) -> None:
    """
    A function to print a list of all available currencies with their corresponding short codes.

    Parameters:
        currencies (Dict[str, str]): A dictionary mapping long currency names to their short codes.

    Returns:
        None
    """

    content: str = f"""Here is a list of all available currencies:

    {'Currency':<25} | {'Short':<5}
    ---------------------------------
"""
    tOut.print_characters(content=content, speed=tOut.OUTPUT_SPEED)

    for currency, short in currencies.items():
        if currency == "us dollar":
            currency = "US Dollar"
        else:
            currency = currency.title()
        tOut.print_characters(
            content=f"    {currency:<25} |  {short:<5}\n", speed=tOut.OUTPUT_SPEED * 0.5
        )


def get_from_currency(currencies: Dict[str, str]) -> str:
    """
    A function to get the user's input for the first currency choice.

    Parameters:
        currencies (Dict[str, str]): A dictionary mapping currency names to their short codes.

    Returns:
        str: The selected currency code.
    """

    while True:
        from_currency = input("\n💶 Choose the first currency: ").lower()

        if from_currency in currencies:
            return from_currency

        if len(from_currency) == 3:
            from_currency = list(currencies.keys())[
                list(currencies.values()).index(from_currency.upper())
            ]

        if from_currency in currencies:
            return from_currency

        tOut.error_try_again()


def get_to_currency(currencies: Dict[str, str]) -> str:
    """
    A function to get the user's input for the second currency choice.

    Parameters:
        currencies (Dict[str, str]): A dictionary mapping currency names to their short codes.

    Returns:
        str: The selected currency code.
    """

    to_currency: str = input("\n💴 Choose the second currency: ").lower()

    if len(to_currency) == 3:
        to_currency = list(currencies.keys())[
            list(currencies.values()).index(to_currency.upper())
        ]
    elif to_currency not in currencies:
        tOut.error_try_again()
        return get_to_currency(currencies)

    return to_currency


def get_amount(currencies: Dict[str, str], from_currency: str) -> float:
    """
    A function to get the user's input for the amount of a specific currency.

    Parameters:
        currencies (Dict[str, str]): A dictionary mapping currency names to their short codes.
        from_currency (str): The currency code for which the amount is being entered.

    Returns:
        float: The amount entered by the user.
    """

    while True:
        try:
            return float(
                input(f"\n💰 Enter the amount of {currencies[from_currency]}: ")
            )
        except ValueError:
            tOut.error_try_again()


def calc_value(
    path: str,
    currencies: Dict[str, str],
    from_currency: str,
    to_currency: str,
    amount: float,
) -> None:
    """
    A function to calculate the converted amount from one currency to another based on the
    provided currency rates.

    Parameters:
        path (str): The path to the currency data files.
        currencies (Dict[str, str]): A dictionary mapping currency names to their short codes.
        from_currency (str): The code of the currency to convert from.
        to_currency (str): The code of the currency to convert to.
        amount (float): The amount of the currency to convert.

    Returns:
        None
    """

    from_short: str = currencies[from_currency]
    to_short: str = currencies[to_currency]

    with open(
        f"{path}/currency/currency_{from_short}.json", "r", encoding="utf-8"
    ) as f:
        data: dict = json.load(f)["rates"]

    new_amount: float = round(amount * data[to_short], 2)

    print(
        f"\n\033[1;32m💵 {amount:.2f} {from_short} are converted "
        f"{new_amount:.2f} {to_short}!\033[0m\n"
    )


def rerun_app() -> None:
    """
    A function to rerun the application based on user input.

    Parameters:
        None

    Returns:
        None
    """

    while True:
        rerun = input("Do you want to restart the program (y/n)? ")[0].lower()
        if rerun == "y":
            main()
            break
        elif rerun == "n":
            print("Exiting program...")
            break
        else:
            tOut.error_try_again()


if __name__ == "__main__":
    main()

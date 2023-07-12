import time

# Lower value -> faster output

OUTPUT_SPEED = 0.0025


def print_characters(content, speed):
    for char in content:
        if char == '\n':
            print()
        else:
            print(char, end='', flush=True)
            time.sleep(speed)    


def error_api_connection_failed(speed=OUTPUT_SPEED):
    content = '''\033[1;31m***************************************************************************\033[0m
\033[1;31m* ❗ No connection to the API-server. The data might not be the latest.❗ *\033[0m
\033[1;31m***************************************************************************\033[0m\n\n'''

    print_characters(content, speed)


def error_keyboard_interrupt(speed=OUTPUT_SPEED):
    content = '\n\n❗ Script execution stopped by user.\n\n'
    
    print_characters(content, speed)


def error_try_again(speed=OUTPUT_SPEED):
    content = '\n\033[1;31m❌ Invalid input. Please try again.\033[0m\n'
    
    print_characters(content, speed)


def success_exchange_rates_updated(speed=OUTPUT_SPEED):
    content = '\033[1;32m✅ Exchange rates updated.\033[0m\n\n'
    
    print_characters(content, speed)


def print_logo(speed=OUTPUT_SPEED):
    content = '''
\033[34m╔═╗┬ ┬┬─┐┬─┐┌─┐┌┐┌┌─┐┬ ┬  ╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐
║  │ │├┬┘├┬┘├┤ ││││  └┬┘  ║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘
╚═╝└─┘┴└─┴└─└─┘┘└┘└─┘ ┴   ╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─\033[0m\n\n'''

    print_characters(content, speed)
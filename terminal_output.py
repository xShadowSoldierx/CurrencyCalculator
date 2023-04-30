import time

# Lower value -> faster output

OUTPUT_SPEED = 0.0025


def error_api_connection_failed(speed=OUTPUT_SPEED):
    content = '''
\033[1;31m***************************************************************************\033[0m
\033[1;31m* ❗ No connection to the API-server. The data might not be the latest.❗ *\033[0m
\033[1;31m***************************************************************************\n\033[0m
'''

    for char in content:
        if char == '\n':
            print()
        else:
            print(char, end='', flush=True)
            time.sleep(speed)    


def error_keyboard_interrupt(speed=OUTPUT_SPEED):
    content = '\n\n❗ Script execution stopped by user.'
    
    for char in content:
        print(char, end='', flush=True)
        time.sleep(speed)


def error_try_again(speed=OUTPUT_SPEED):
    content = '\033[1;31m\n❌ Invalid input. Please try again.\n\033[0m'
    
    for char in content:
        print(char, end='', flush=True)
        time.sleep(speed)


def success_exchange_rates_updated(speed=OUTPUT_SPEED):
    content = '\033[1;32m✅ Exchange rates updated.\n\033[0m'
    
    for char in content:
        print(char, end='', flush=True)
        time.sleep(speed) 


def print_logo(speed=OUTPUT_SPEED):
    logo = '''\033[34m╔═╗┬ ┬┬─┐┬─┐┌─┐┌┐┌┌─┐┬ ┬  ╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐
║  │ │├┬┘├┬┘├┤ ││││  └┬┘  ║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘
╚═╝└─┘┴└─┴└─└─┘┘└┘└─┘ ┴   ╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─
\033[0m
'''

    for char in logo:
        if char == '\n':
            print()
        else:
            print(char, end='', flush=True)
            time.sleep(speed)

def print_batman(speed=OUTPUT_SPEED):
    batman = '''
⠀⠀⠀⢀⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡀⠀⠀⠀
⠀⠀⠀⣼⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⡀⠀⠀
⠀⠀⢠⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣇⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⡀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⡟⠋⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⢿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣿⣿⣿⣿⡇
⠸⣿⣿⣿⣿⣷⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣠⣴⣿⣿⣿⣿⡇
⠀⢿⣿⣿⡟⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⢻⣿⣿⣿⠁
⠀⠘⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⠀
⠀⠀⠀⠙⠧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠓⠢⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠴⠒⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠒⠙⠿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⡿⠟⠓⠢⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠉⣉⠁⠀⠀⠈⢉⠉⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠀⠀
⠀⣄⠀⡴⠁⠀⠀⠀⡆⠀⠀⠀\033[33m⠾⠿⣶⣾⣷⣶⡿⠷\033[0m⠀⠀⠀⢀⠇⠀⠀⠀⠳⡀⠀⠀⠀
⢰⣿⡿⣱⣦⣄⡀⣠⣷⠀⠀⠀⠀⠀⠀\033[33m⠈⠃\033[0m⠀⠀⠀⠀⠀⠀⢸⣄⡀⠀⣀⣤⣜⣶⣃⠀
⢳⣿⣱⣿⣿⣿⣿⣿⣿⣆⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣿⣿⣿⣿⣿⣿⣿⡞⣯⠆
⢀⣇⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⠀⠉⡏⣟⣿⡏⠏⠉⢹⠉⠈⣿⣿⣿⣿⣿⣿⣿⣿⢡⠀
⠸⣜⡿⣿⣿⢹⣿⣿⡿⠛⠻⠿⣿⣿⣿⣶⣶⣾⣷⣿⡿⠟⠛⢿⣿⣿⣿⡫⣿⣿⢿⣫⠀
⠀⠈⣽⣶⣾⣿⣿⡿⠁⠀⠀⠀⠀⠙⢿⣿⣿⣟⠋⠁⠀⠀⠀⠀⠻⣿⣿⣿⣮⣷⡏⠁⠀
⠀⢠⣿⣿⣿⣿⡿⢁⣀⣄⡀⠀⠀⢀⣾⣿⣿⣿⣧⠀⠀⠀⣀⣀⡀⢹⣿⣿⣿⣿⣿⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣼⣿⣿⣿⣿⣿⣤⣶⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠀⠀
⠀⢸⠟⠉⠈⢙⣿⣿⣿⣿⣿⣿⣿⣿⠙⠻⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⠛⠉⠙⢿⡆⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠁⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠛⠉⠉⠉⠁
'''

    for char in batman:
        if char == '\n':
            print()
        else:
            print(char, end='', flush=True)
            time.sleep(speed)


if __name__ == '__main__':
    error_api_connection_failed()
    error_keyboard_interrupt()
    error_try_again()
    print_logo()
    print_batman()
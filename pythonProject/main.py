import random

MAX_LINES = 6
MIN_BET = 1
MAX_BET = 100

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def get_deposit():
    while True:
        amount = input("How much would you like to deposit? EUR: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!")

    return amount

def get_lines():
    while True:
        amount = input(f"How many lines would you like to bet? (1 - {MAX_LINES}): ")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_LINES:
                break
            else:
                print(f"Amount must be inbetween 1 and {MAX_LINES}")
        else:
            print("Please enter a number!")

    return amount

def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be inbetween ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a number!")

    return amount

def spin(lines, bet):
    print(f"Your spin is ${bet} on {lines} lines for a total of ${lines * bet}")

def main():
    balance = get_deposit()
    #lines = 1
    while True:
        print(f"Balance: ${balance}")
        print("----------------")
        print("1 - Make another deposit")
        print("2 - Set lines")
        print("3 - Set Bet")
        print("4 - Spin!")
        print("0 - Exit")
        print("----------------")
        while True:
            try:
                option = int(input("What would you like to do? "))
                break
            except ValueError:
                print("Please enter a valid option!")

        #menu
        if option == 1:
            balance += get_deposit()
        elif option == 2:
            lines = get_lines()
        elif option == 3:
            try:
                while True:
                    bet = get_bet()
                    if balance > bet * lines: break
                    else:
                        print(f"Bet(${bet * lines}) must be lower than your balance(${balance})!")
            except NameError:
                print("Set the number of lines first!")
        elif option == 4:
            try:
                spin(lines, bet)
            except NameError:
                print("Please set the number of lines and bet amount first!")
        elif option == 0:
            break
        else:
            print("Please enter a valid option!")

main()
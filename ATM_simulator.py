
# ATM SIMULATOR PROGRAM

attempts_left = 3


def create_pin():
    x = input("Create your code: ")

    if len(x) == 4 and x.isdigit():
        print("Your code has been created")
        return x
    else:
        print("Invalid code")
        return None


# Common PIN verification function
def authenticate(correct_pin):
    global attempts_left

    while attempts_left > 0:
        input_pin = input("Enter your pin: ")

        if input_pin == correct_pin:
            print("Permission granted")
            return True
        else:
            attempts_left -= 1
            print("Incorrect PIN")
            print("Attempts remaining:", attempts_left)

    print("ATM BLOCKED")
    return False


def check_balance(correct_pin, balance):

    if authenticate(correct_pin):
        return balance

    return None


def deposit(correct_pin, amount, balance):

    if authenticate(correct_pin):
        if amount <= 0:
            print("Invalid amount")
            return None

        balance = balance + amount
        print("Successfully deposited")
        return balance

    return None


def withdraw(correct_pin, amount, balance):

    if authenticate(correct_pin):
        if amount <= 0:
            print("Invalid amount")
            return None

        if amount > balance:
            print("You cannot withdraw more than your balance")
            return None

        balance = balance - amount
        print("Successfully withdrawn")
        return balance

    return None


def change_pin(correct_pin):

    if authenticate(correct_pin):

        new_pin = input("Enter your new PIN: ")

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must contain exactly 4 digits")
            return correct_pin

        again = input("Confirm your new PIN: ")

        if new_pin == again:
            print("PIN successfully changed")
            return new_pin
        else:
            print("PINs do not match")
            return correct_pin

    return correct_pin


def main():

    pin = create_pin()

    if pin is None:
        print("Cannot start ATM without a valid PIN")
        return

    balance = 0

    while True:

        if attempts_left == 0:
            print("ATM access terminated")
            break

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        print("==============================")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:

            result = check_balance(pin, balance)

            if result is not None:
                print("Your balance is:", result)

        elif choice == 2:

            try:
                amount = int(input("Enter deposit amount: "))
                result = deposit(pin, amount, balance)

                if result is not None:
                    balance = result

            except ValueError:
                print("Enter a valid numeric amount")

        elif choice == 3:

            try:
                amount = int(input("Enter withdrawal amount: "))
                result = withdraw(pin, amount, balance)

                if result is not None:
                    balance = result
                    print("Remaining balance:", balance)

            except ValueError:
                print("Enter a valid numeric amount")

        elif choice == 4:

            result = change_pin(pin)

            if result is not None:
                pin = result

        elif choice == 5:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Select between 1 and 5.")


# Run ATM
main()

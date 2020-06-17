class BankAccount:
    def __init__(self, bal: float) -> None:
        self.__balance = bal

    def deposit(self, amount: float) -> None:
        self.__balance += amount
    
    def withdraw(self, amount:float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self) -> float:
        return self.__balance


def main():
    # Get the starting balance.
    start_bal = float(input('Enter your starting balance: '))
    # Create a BankAccount object.
    savings = BankAccount(start_bal)
    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)
    # Display the balance.
    print('Your account balance is $', \
    format(savings.get_balance(), ',.2f'),
    sep='')
    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)
    # Display the balance.
    print('Your account balance is $', \
    format(savings.get_balance(), ',.2f'),
    sep='')

# Call the main function.
main()
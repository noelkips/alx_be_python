import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command line banking operations.
    
    Usage:
        python main-0.py <command>:<amount>
        python main-0.py display
    
    Commands:
        deposit:<amount> - Deposit money into the account
        withdraw:<amount> - Withdraw money from the account
        display - Show current balance
    """
    # Create account with example starting balance of $100
    account = BankAccount(100)
    
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and parameters
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    
    # Extract amount if provided
    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Error: Amount must be a valid number")
            sys.exit(1)

    # Execute the appropriate command
    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
            
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
                
        elif command == "display":
            account.display_balance()
            
        else:
            print("Invalid command.")
            print("Usage: python main-0.py <command>:<amount>")
            print("Commands: deposit:<amount>, withdraw:<amount>, display")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
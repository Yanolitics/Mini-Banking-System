author = "Yanolitics"

print(f"""
┌────────────────────────────────┐
│       MINI BANKING SYSTEM      │
│        by {author:<12}         │
└────────────────────────────────┘
""")

# Part 1: Database Simulation
accounts = []


# -------------------------------------------------------------------
# Helper Function: Find Account
# -------------------------------------------------------------------
def find_account(name: str):
    """Finds an account by name (case-insensitive) in the simulated database."""
    for account in accounts:
        if account["name"].lower() == name.lower():
            return account
    return None


# Part 2: Account Creation Function
def create_account(name: str, initial_balance: float) -> dict:
    """Creates a new bank account after validating initial balance and checking for duplicate names."""
    if find_account(name):
        raise ValueError(f"An account with the name '{name}' already exists.")
    if initial_balance < 0.0:
        raise ValueError("Invalid Balance.")

    new_account = {
        "name": name,
        "balance": initial_balance,
        "transactions": [],
    }
    accounts.append(new_account)
    print(f"Account '{name}' created with initial balance: ${initial_balance:.2f}")
    return new_account

# Part 3: Deposit Function
def deposit(name: str, amount: float) -> float:
    """Deposits funds into an account and records the transaction."""
    if amount <= 0.0:
        raise ValueError("Amount is Invalid")

    account = find_account(name)
    if not account:
        raise ValueError(f"Account '{name}' not found.")

    account["balance"] += amount
    account["transactions"].append({"type": "Deposit", "amount": amount})
    return account["balance"]


# Part 4: Withdraw Function
def withdraw(name: str, amount: float) -> float:
    """Withdraws funds from an existing account after validating available balance."""
    if amount <= 0.0:
        raise ValueError("Amount is Invalid")

    account = find_account(name)
    if not account:
        raise ValueError(f"Account '{name}' not found.")

    if amount > account["balance"]:
        raise ValueError("Insufficient Balance")

    account["balance"] -= amount
    account["transactions"].append({"type": "Withdrawal", "amount": amount})
    return account["balance"]


# Part 5: Show Account Summary
def show_account(name: str) -> None:
    """Displays the account details, balance, and transaction history."""
    account = find_account(name)
    if not account:
        raise ValueError(f"Account '{name}' not found.")

    print(f"\n--- Account Summary: {account['name']} ---")
    print(f"Current Balance: ${account['balance']:.2f}")
    print("Transactions:")
    if not account["transactions"]:
        print("  No transactions recorded.")
    else:
        for transaction in account["transactions"]:
            print(f"  - {transaction['type']}: ${transaction['amount']:.2f}")
    print("-----------------------------------\n")


# Part 6: Testing Section
if __name__ == "__main__":
    print("--- 1. Creating Account ---")
    create_account("Alice", 1000.00)

    print("\n--- 2. Performing Multiple Deposits ---")
    print(f"Balance: ${deposit('Alice', 500.00):.2f}")
    print(f"Balance: ${deposit('Alice', 250.00):.2f}")

    print("\n--- 3. Performing Multiple Withdrawals ---")
    print(f"Balance: ${withdraw('Alice', 300.00):.2f}")
    print(f"Balance: ${withdraw('Alice', 100.00):.2f}")

    print("\n--- 4. Testing Duplicate Account Guardrail ---")
    try:
        create_account("Alice", 500.00)
    except ValueError as e:
        print("Caught expected error:", e)

    print("\n--- 5. Testing Overdraft Guardrail ---")
    try:
        withdraw("Alice", 5000.00)
    except ValueError as e:
        print("Caught expected error:", e)

    print("\n--- 6. Displaying Account Summary ---")
    show_account("Alice")

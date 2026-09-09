# 🏦 Mini Banking System (Python)

---

Welcome to my Mini Banking System project! This repository contains a pure **Python 3** script designed to simulate core banking operations, including account creation, deposits, withdrawals, real-time balance tracking, and formatted transaction histories.

As a self-taught aspiring data practitioner operating under the moniker **Yanolitics**, I built this project to demonstrate how to manage in-memory data states, enforce business logic guardrails, abstract repetitive searches using helper functions, and handle exceptions cleanly.

---

## 🗺️ How It Works

The script follows a structured banking flow:  
**Database Simulation → Account Lookup Helper → Ledger Transactions (Deposit/Withdraw) → Exception Guardrails → Formatted Account Summary**.

---

## 🛠️ Step-by-Step Breakdown

### 1. Database Simulation & Helper Abstraction
* **Database Schema:** Stores all accounts in a global `accounts` list. Each account is represented as a dictionary containing `"name"` (`str`), `"balance"` (`float`), and `"transactions"` (`list`).
* **Lookup Helper (`find_account`):** Abstracts search logic across all functions. It performs a case-insensitive lookup (e.g., matching `"alice"` to `"Alice"`) and returns either the account dictionary or `None`.

### 2. Account Creation (`create_account`)
* **Purpose:** Initializes a new account with a starting balance.
* **Guardrails:** Validates that the initial balance is non-negative (`>= 0.0`) and checks `find_account()` to prevent duplicate account names.
* **Return:** Appends the record to the database and returns the created dictionary structure.

### 3. Deposits & Withdrawals (`deposit` / `withdraw`)
* **Purpose:** Mutates account balances and appends real-time transaction records.
* **Validation & Security:**
  * Ensures transaction amounts are strictly positive (`amount > 0.0`).
  * Verifies the target account exists using the helper function.
  * Checks available balance before performing withdrawals to prevent overdrafts.
* **Transaction Logging:** Appends structured records (`{"type": "Deposit"/"Withdrawal", "amount": amount}`) directly to the account's transaction history list.

### 4. Account Summary (`show_account`)
* **Purpose:** Generates a human-readable ledger summary for any registered account.
* **Formatting:** Displays the account holder's name, formats balances as monetary values with two decimal places (`$1000.00`), and iterates through transaction logs with fallback handling if no transactions exist.

### 5. Automated Guardrail Testing
* **Purpose:** Verifies system stability inside an `if __name__ == "__main__":` execution block.
* **Test Coverage:** Runs valid deposits and withdrawals, then uses isolated `try/except` blocks to deliberately test duplicate name creation, overdraft attempts, and invalid transaction amounts without crashing the program.

---

### OUTPUT
<img width="513" height="546" alt="Screenshot 2026-09-09 160526" src="https://github.com/user-attachments/assets/f6f9511e-ce3e-4e08-9c37-34bedb3dc13b" />


---

## ⚡ Tech Stack & Core Concepts Demonstrated

* **Language:** Python 3
* **Core Paradigms:** Functional Programming, Modular Architecture, DRY (Don't Repeat Yourself) Design, Defensive Programming.
* **Data Engineering Concepts:** In-Memory State Management, Input Sanitization & Normalization, Schema Standardization, Custom Helper Abstraction, and Exception Handling (`raise ValueError`).
* **Data Structures:** Nested Dictionaries, Dynamic List Collections, and Type-Annotated Functions (`str`, `float`, `dict`, `None`).

---

## 👨‍💻 About the Developer

I’m Timothy, a former banking documentation analyst who spent three years managing rigid data compliance and structure. I chose to pivot into the tech sector because I love building systems, wrestling with technical tools, and mastering business intelligence.

I am entirely self-taught through dedicated, project-driven bootcamps and courses. While I am still navigating the earlier stages of my career, I bring a high tolerance for debugging, a sharp eye for detail from my banking days, and a commitment to writing clean, reliable code.

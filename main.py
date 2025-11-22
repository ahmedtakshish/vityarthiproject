# budget_tracker.py
"""
Personal Budget Tracker
A simple command-line application to track income and expenses
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class BudgetTracker:
    def __init__(self, data_file="budget_data.json"):
        self.data_file = data_file
        self.transactions = self.load_data()
    
    def load_data(self) -> List[Dict]:
        """Load transactions from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Note: Starting with empty transaction history")
                return []
        return []
    
    def save_data(self):
        """Save transactions to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.transactions, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save data - {e}")
    
    def add_transaction(self, amount: float, category: str, transaction_type: str, description: str = ""):
        """Add a new transaction (income or expense)"""
        if amount <= 0:
            print("Error: Amount must be positive")
            return False
            
        transaction = {
            'id': len(self.transactions) + 1,
            'amount': amount,
            'category': category.strip(),
            'type': transaction_type.lower(),
            'description': description.strip(),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.transactions.append(transaction)
        self.save_data()
        print(f"Success: {transaction_type} of ${amount:.2f} added to {category}")
        return True
    
    def calculate_balance(self) -> float:
        """Calculate current balance"""
        balance = 0.0
        for transaction in self.transactions:
            if transaction['type'] == 'income':
                balance += transaction['amount']
            else:
                balance -= transaction['amount']
        return balance
    
    def show_summary(self):
        """Show transaction summary"""
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = self.calculate_balance()
        
        print("\n" + "="*50)
        print("BUDGET SUMMARY")
        print("="*50)
        print(f"Total Income:    ${total_income:.2f}")
        print(f"Total Expenses:  ${total_expenses:.2f}")
        print(f"Current Balance: ${balance:.2f}")
        
        if balance > 0:
            print("Status: Positive balance")
        elif balance < 0:
            print("Status: Negative balance")
        else:
            print("Status: Break-even")
        print("="*50)
        
        # Show expenses by category
        expense_categories = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                category = transaction['category']
                expense_categories[category] = expense_categories.get(category, 0) + transaction['amount']
        
        if expense_categories:
            print("\nExpenses by Category:")
            for category, amount in expense_categories.items():
                percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
                print(f"  {category}: ${amount:.2f} ({percentage:.1f}%)")
    
    def show_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("No transactions to display.")
            return
        
        print("\n" + "="*70)
        print("ALL TRANSACTIONS")
        print("="*70)
        
        for transaction in self.transactions:
            type_indicator = "[INCOME] " if transaction['type'] == 'income' else "[EXPENSE]"
            amount_display = f"+${transaction['amount']:.2f}" if transaction['type'] == 'income' else f"-${transaction['amount']:.2f}"
            
            print(f"#{transaction['id']} | {transaction['date']}")
            print(f"  {type_indicator} {amount_display} - {transaction['category']}")
            if transaction['description']:
                print(f"  Note: {transaction['description']}")
            print("-" * 50)
    
    def delete_transaction(self, transaction_id: int):
        """Delete a transaction by ID"""
        for i, transaction in enumerate(self.transactions):
            if transaction['id'] == transaction_id:
                # Update IDs for remaining transactions
                for j in range(i + 1, len(self.transactions)):
                    self.transactions[j]['id'] -= 1
                
                deleted_amount = transaction['amount']
                deleted_type = transaction['type']
                del self.transactions[i]
                self.save_data()
                print(f"Transaction #{transaction_id} deleted ({deleted_type} of ${deleted_amount:.2f})")
                return True
        
        print(f"Error: Transaction #{transaction_id} not found")
        return False

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("PERSONAL BUDGET TRACKER")
    print("="*40)
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Summary")
    print("4. View All Transactions")
    print("5. Delete Transaction")
    print("6. Exit Program")
    print("-" * 40)

def get_float_input(prompt: str) -> float:
    """Safely get float input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt: str) -> int:
    """Safely get integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    tracker = BudgetTracker()
    
    print("Welcome to the Personal Budget Tracker")
    print("This program helps you track your income and expenses.")
    
    while True:
        display_menu()
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            print("\n-- Record New Income --")
            amount = get_float_input("Enter income amount: $")
            category = input("Enter category (e.g., Salary, Bonus, Gift): ").strip()
            if not category:
                category = "Uncategorized"
            description = input("Enter description (optional): ").strip()
            tracker.add_transaction(amount, category, 'income', description)
        
        elif choice == '2':
            print("\n-- Record New Expense --")
            amount = get_float_input("Enter expense amount: $")
            category = input("Enter category (e.g., Food, Rent, Transport): ").strip()
            if not category:
                category = "Uncategorized"
            description = input("Enter description (optional): ").strip()
            tracker.add_transaction(amount, category, 'expense', description)
        
        elif choice == '3':
            tracker.show_summary()
        
        elif choice == '4':
            tracker.show_transactions()
        
        elif choice == '5':
            print("\n-- Delete Transaction --")
            transaction_id = get_int_input("Enter transaction ID to delete: ")
            tracker.delete_transaction(transaction_id)
        
        elif choice == '6':
            print("Thank you for using the Budget Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
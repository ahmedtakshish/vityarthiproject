# Personal Budget Tracker

A simple command-line application for tracking personal income and expenses. Built with Python, this tool helps you maintain a clear overview of your financial situation by recording transactions and generating useful summaries.

## Features

- **Record Income and Expenses**: Easily add new transactions with categories and descriptions
- **View Financial Summary**: See your total income, expenses, and current balance at a glance
- **Transaction History**: Browse all recorded transactions with full details
- **Category Analysis**: View spending breakdown by category with percentages
- **Data Persistence**: All data is automatically saved to a JSON file
- **Delete Transactions**: Remove incorrect or duplicate entries

## Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation
1. Download `budget_tracker.py` to your computer
2. Open terminal/command prompt in the download directory
3. Run: `python budget_tracker.py`

## How to Use

### Basic Commands
When you run the program, you'll see this menu:

PERSONAL BUDGET TRACKER
========================================

Record Income

Record Expense

View Summary

View All Transactions

Delete Transaction

Exit Program


### Adding Transactions
**To add income:**
- Choose option 1
- Enter amount (e.g., `1500`)
- Enter category (e.g., `Salary`)
- Add description if needed (e.g., `Monthly paycheck`)

**To add expenses:**
- Choose option 2
- Enter amount (e.g., `45.50`)
- Enter category (e.g., `Groceries`)
- Add description if needed (e.g., `Weekly shopping`)

### Viewing Your Finances
**Summary (Option 3)** shows:
- Total income and expenses
- Current balance
- Spending by category with percentages

**All Transactions (Option 4)** shows:
- Complete history with dates and descriptions
- Income marked with `[INCOME]` and expenses with `[EXPENSE]`

### Managing Transactions
**Delete (Option 5)** lets you remove transactions by their ID number (shown in the transactions list).

## Example Session
PERSONAL BUDGET TRACKER
========================================
Choose an option (1-6): 1

-- Record New Income --
Enter income amount: $2000
Enter category (e.g., Salary, Bonus, Gift): Salary
Enter description (optional): April salary
Success: income of $2000.00 added to Salary

Choose an option (1-6): 2

-- Record New Expense --
Enter expense amount: $85
Enter category (e.g., Food, Rent, Transport): Food
Enter description (optional): Groceries
Success: expense of $85.00 added to Food

Choose an option (1-6): 3

==================================================
BUDGET SUMMARY
==================================================
Total Income: $2000.00
Total Expenses: $85.00
Current Balance: $1915.00
Status: Positive balance
==================================================

Expenses by Category:
Food: $85.00 (100.0%)


## Data Storage

Your transactions are automatically saved to `budget_data.json` in the same folder as the program. This file is created when you add your first transaction.

### Backup Your Data
To backup your financial records, simply make a copy of the `budget_data.json` file.

## Troubleshooting

### Common Issues

**"Python not found" error**
- Make sure Python is installed
- On Windows, try `python3 budget_tracker.py` instead
- On Mac/Linux, you might need to use `python3 budget_tracker.py`

**File permission errors**
- Run the program from a folder where you have write permissions
- Avoid system-protected directories like Program Files

**Corrupted data file**
- If the program won't start, delete `budget_data.json` and start fresh
- Your existing data will be lost, but the program will work again

**Invalid input errors**
- For amounts, only enter numbers (e.g., `50` or `29.99`)
- Don't include currency symbols in the amount field

## Tips for Effective Use

1. **Be consistent with categories** - Use the same category names for similar expenses
2. **Add descriptions** - Helpful for remembering what transactions were for
3. **Regular updates** - Enter transactions soon after they happen for accuracy
4. **Review weekly** - Use the summary feature to check your spending patterns

## Customization

You can modify the categories to fit your needs. Common categories include:
- **Income**: Salary, Freelance, Investments, Gifts
- **Expenses**: Rent, Food, Transport, Utilities, Entertainment, Healthcare

## Support

This is a simple local application. Your data never leaves your computer.

If you encounter bugs or have suggestions:
1. Check that you're using a supported Python version
2. Ensure the `budget_data.json` file isn't corrupted
3. Try running the program from a different directory

## Privacy & Security

- All data stored locally on your computer
- No internet connection required
- No personal information collected
- You control all your financial data

---

**Remember**: This is a basic tool for personal use. For complex financial needs, consider consulting a financial advisor or using professional accounting software.

**File**: `budget_tracker.py`  
**Version**: 1.0  

### Basic Commands
When you run the program, you'll see this menu:

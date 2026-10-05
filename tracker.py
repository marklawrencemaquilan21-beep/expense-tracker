# Module 1 - Laboratory 3: The Tracker Does Math
# Author: MARK LAWRENCE N. MAQUILAN
# A simple expense tracker that accepts a user-defined number of expenses.

author = "MARK LAWRENCE N. MAQUILAN"

print("=" * 40)
print("\t EXPENSE TRACKER")
print("\tYour wallet buddy.")
print("=" * 40)

print("MAIN MENU")
print(f"\t[1] {'Add an expense':<20} (coming soon)")
print(f"\t[2] {'View all expenses':<20} (coming soon)")
print(f"\t[3] {'Show total spent':<20} (coming soon)")
print(f"\t[4] {'Exit':<20} (coming soon)")


name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log your expenses.\n")

# Number of expenses to enter
num_expenses = int(input("How many expenses will you enter? "))

items = []
amounts = []

# Loop for collecting each expense
for i in range(1, num_expenses + 1):
    item = input(f"\nWhat is your expense no. {i}? ")
    amount = float(input("Amount? "))
    items.append(item)
    amounts.append(amount)

total = sum(amounts)
average = total / num_expenses if num_expenses > 0 else 0


print("\n" + "-" * 40)
print("SUMMARY")
for item, amount in zip(items, amounts):
    print(f" - {item:<10}: Php{amount}")
print(f"\nTotal spent   : Php {total}")
print(f"Average       : Php {average}")
print("-" * 40)
print(f"Made by: {author} | Installment 3")
print("=" * 40)

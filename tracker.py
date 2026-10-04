# Module 1 - Laboratory 2: Talking to the User
# Author: MARK LAWRENCE N. MAQUILAN
# A simple expense tracker that accepts two expenses.

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
print(f"Welcome, {name}! Let's log your two expenses.\n")

item1 = input("What's your first expense? ")
amount1 = float(input("Amount? "))

item2 = input("\nWhat's your second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print ("")
print("-" * 40)
print("SUMMARY")
print(f"  - {item1:<10}: Php {amount1}")
print(f"  - {item2:<10}: Php {amount2}")
print(f"\nTotal spent   : Php {total}")
print(f"Average       : Php {average}")
print("-" * 40)
print(f"Made by: {author} | Installment 2")
print("=" * 40)

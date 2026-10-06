# Module 1 - Laboratory 3: The Tracker Does Math
# Author: MARK LAWRENCE N. MAQUILAN
# A simple expense tracker that calculates, subtotal, average, tax, and budget.

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

subtotal = 0

item1 = input("What's your first expense? ")
amount1 = float(input(f"Amount of your {item1}? "))
subtotal += amount1

item2 = input("\nWhat's your second expense? ")
amount2 = float(input(f"Amount of your {item2}? "))
subtotal += amount2

average = subtotal / 2

tax_rate = float(input("\nTax rate in %? "))
tax = subtotal * (tax_rate / 100)

total = subtotal + tax

budget = float(input("How much is your budget? "))
budget_limit = total > budget

left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f"\t- {item1:<20}: Php {amount1}")
print(f"\t- {item2:<20}: Php {amount2}\n")
print(f"\tSubtotal\t\t: Php {subtotal:.2f}")
print(f"\tAverage\t\t\t: {average:.2f}")
print(f"\tTax ({tax_rate}%)\t\t: Php{tax:.2f}")
print(f"\tTotal Amount\t\t: Php {total:.2f}")
print(f"\tam I over-budget?\t: {budget_limit}")
print(f"\tTotal budget left\t: Php {left:.2f}")

print("-" * 40)
print(f"Made by: {author} | Installment 3")
print("=" * 40)

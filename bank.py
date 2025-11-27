# Read values from input file
with open("balance_input.txt", "r") as file:
    lines = file.readlines()
    initial_balance = float(lines[0].strip())
    deposit_amount = float(lines[1].strip())

# Calculate updated balance
updated_balance = initial_balance + deposit_amount

# Display result
print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
print("Updated Balance:", updated_balance)

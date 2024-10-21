balance = 1000
while balance > 0:
    print("Current balance: {balance}")
    withdrawal = int(input("Enter the amount to withdraw (or 0 to exit): "))

    if withdrawal == 0:
        print("Transaction cancelled. Exiting...")
        break
    elif withdrawal > balance:
        print("Insufficient balance. Try a smaller amount.")
    else:
        balance -= withdrawal
        print(f"Withdrawal successful. Remaining balance: {balance}")
if balance == 0:
    print("No balance left. Exiting...")

colors = ["Red", "Blue", "Green"]
sizes = ["Small", "Medium", "Large"]
print("Available product variants:")
for color in colors:
    for size in sizes:
        print(f"Color: {color}, Size: {size}")

while True:
    print("Welcome to the tip calculator.")

    total_bill = float(input("What was the total Bill? "))
    tip_percentage = int(input("What percentage tipo would you like to give? 10, 12, or 15? "))
    people_split = int(input("How many people to split the bill? "))

    result_tip = round((tip_percentage / 100) * total_bill)
    bill_plus_tip = round((result_tip + total_bill) / people_split, 2)

    print(f"Each person should pay: ${bill_plus_tip}")

    check = input("\nWould you like to do it again? Y/N: ")
    if check.upper() == 'Y':
        continue
    break
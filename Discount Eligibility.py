total_bill = int(input("Enter Total bill: "))

is_member = str(input("Are you a Member? Yes/No: "))

        if total_bill >= 1000 and is_member == "Yes"
            print("10% off")

        elif total_bill >= 1000 and is_member == "no":
            print("5% off")

        else:
            print("No discount")

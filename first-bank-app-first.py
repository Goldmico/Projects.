print("SFAE Bank | John Doe")

first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"

print("Customer's full name:", full_name)

balance = 1000000
account_number = 725829303827
account_type = "Cheque"
cards = 2

print("Bank Balance:", balance)
print("Account Number:", account_number)
print("Account Type:", account_type)
print("Cards:", cards)


gold_member = False
diamond_member = True

deposit_amount = 0
withdraw_amount = 0
fees = 0
overdraft_limit = 0
member_overdraft_limit = 0

if gold_member == True:
    deposit_amount = 30000
    withdraw_amount = 10000
    fees = 1000
    overdraft_limit = 1000
    print("Gold Member:", gold_member)
    print("Max Deposit amount:", deposit_amount)
    print("Max Withdraw amount:", withdraw_amount)
    print("Fees to be paid to bank:", fees)
    print("Overdraft limit:", overdraft_limit)

if diamond_member == True:
    deposit_amount = 300000
    withdraw_amount = 100000
    fees = 3000
    overdraft_limit = 500
    print("Diamond Member:", diamond_member)
    print("Max Deposit amount:", deposit_amount)
    print("Max Withdraw amount:", withdraw_amount)
    print("Fees to be paid to bank:", fees)
    print("Overdraft limit:", overdraft_limit)


loan_agreement = False
loan_amount = 100000
interest_rate = "N/A"
credit_score = 700
can_apply = False

if credit_score == 700:
    interest_rate = 5.0

if loan_agreement == True:
    print("You have a valid loan agreement.")
else:
    print("You do not have a valid loan agreement. Please apply.")

if credit_score >= 580:
    can_apply = True
    print("Credit score:", credit_score, "|", "You are able to apply for a loan")

is_member = True
membership_type = "N/A"
bonus_points = 0

if is_member == True:
    membership_type = "Student"
else:
    print("You do not have a valid membership.")

if membership_type == "Food":
    bonus_points = 50
    print("Your membership type is", membership_type)
    print("Bonus points:", bonus_points)
elif membership_type == "Student":
    bonus_points = 200
    print("Your membership type is", membership_type)
    print("Bonus points:", bonus_points)

pin_code = 7718
pin_input = 7718
failed_attempt_until_lock = 5
failed_attempts = 2
account_status = "N/A"

if pin_input != 7718 and failed_attempts == 5:
    print("Account locked, please contact bank for more info.")
else:
    print("Account Not Locked")

if failed_attempts >= 2:
    account_status = "Active"
else:
    account_status = "Locked, contact bank for more info"

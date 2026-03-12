# other veriables i added late (mbbb)
# also made by d1prezz dont steal you cheeky arse

#MEMBERSHIP VERIABLES
membership_active = False

print("Welcome to SFAE Bank | Version 2 | Developed by d1prezz")
print("Register Now!")

full_name = input("Please input your full name:")
print("Welcome,", full_name)

# ----------------------------------------------------------------------------------------------
# d
account_number = input("Please input a unique account number:")
account_number_confirmation = input("To confirm, please put in your account number again:")

if account_number_confirmation == account_number:
    print("Thank you! Your official account number is:", account_number)
else:
    print("The account number does not match, please retry again!")
    account_number_confirmation = input("To confirm, please put in your account number again:")
    if account_number_confirmation != account_number:
        sys.exit("Account number does not match, please restart session.")

    if account_number_confirmation == account_number:
        print("Thank you! Your official account number is:", account_number)

# ----------------------------------------------------------------------------------------------------
# Pin area thingy
pin = input("Please input your Unique Pin. Make sure it is not a common number:")
pin_confirmation = input("To confirm, please put in your Pin again:")

if pin_confirmation == pin:
    print("Thank you! Your official PIN is:", pin)
else:
    print("The PIN does not match, please retry again!")
    pin_confirmation = input("To confirm, please put in your PIN again:")
    if pin_confirmation != pin:
            sys.exit("Pin still does not match. Please restart session.")

    if pin_confirmation == pin:
        print("Thank you! Your official PIN is:", pin) # 1

# ------------------------------------------------------------------------------------------------------

account_type = input("Account Types | Eco | Deluxe | Which account type will you be purchasing?")
account_types = ("Eco", "Deluxe")

# p

if account_type in account_types:
    print("Thank you! Your official account type is:", account_type)
else:
    print("The account type does not match, please retry again!")

cards = 1
balance = 0

# r

print("Your account is activating...")
print("Your account is officially activated!")

print("------------------------------------------")
print("Full Name:", full_name)
print("Account Number:", account_number)
print("PIN:", pin)
print("Account Type:", account_type)
print("Cards:", cards)
print("Balance:", balance)
print("Membership:", membership_active)

# e

print("------------------------------------------")
# ---------------------------------------------------------------------------------------------------

options = "Deposit", "Withdraw", "Cashsend"

if options == "Deposit":
    balance = input("Please input the amount to deposit:")
    account_number_application = input("Please put in your unique account number:")
    pin_application = input("Please put in your card pin for safety reasons:")
    if account_number_application and pin_application:
        print("Thank you! Your updated balance is:", "R",balance)
        print("Your updated info:")
        print("------------------------------------------")
        print("Full Name:", full_name)
        print("Account Number:", account_number)
        print("PIN:", pin)
        print("Account Type:", account_type)
        print("Cards:", cards)
        print("Balance:", balance)
        print("Membership:", membership_active)

        print("------------------------------------------")
    else: #z
        print("Please retry again! Ether your PIN or Account number is invalid")
        account_number_application = input("Please put in your unique account number:")
        pin_application = input("Please put in your card pin for safety reasons:")
        if account_number_application and pin_application:
            print("Thank you! Your updated balance is:", "R", balance)
            print("Your updated info:")
            print("------------------------------------------")
            print("Full Name:", full_name)
            print("Account Number:", account_number)
            print("PIN:", pin)
            print("Account Type:", account_type)
            print("Cards:", cards)
            print("Balance:", balance)
            print("Membership:", membership_active)

            print("------------------------------------------")
            if options != "Deposit":
                sys.exit("Account number does not match, please redo session.")
# ---------------------------------------------------------------------------------------------------

if options == "Withdraw": # z
    withdraw_input = float(input("Please input the amount to withdraw:"))
    balance = balance - withdraw_input
    account_number_application = input("Please put in your unique account number:")
    pin_application = input("Please put in your card pin for safety reasons:")
    if account_number_application and pin_application:
        print("Thank you! Your updated balance is:", "R", balance)
        print("------------------------------------------")
        print("Your updated info:")
        print("Full Name:", full_name)
        print("Account Number:", account_number)
        print("PIN:", pin)
        print("Account Type:", account_type)
        print("Cards:", cards)
        print("Balance:", balance)
        print("Membership:", membership_active)

print("------------------------------------------")
if options != "Withdraw":
    print("No such option. Please redo session.")
# ------------------------------------------------------------------------------------------------------------------------------
basic_payment = 2000
deluxe_payment = 5000
# ------------------------------------------------------------------------------------------------------------------------------
if membership_active == False:
    register_membership = input("Please register your membership! (Continue by saying YES" )
    if register_membership != "YES":
        sys.exit("Not a valid answer. Please restart session.")
    if register_membership == "YES":
        membership_types = input("Two membership types: Basic (15% off Loan repayments) Deluxe (50% Off Loan Repayments) Choose by saying Deluxe or Basic (Basic is R2000 and Deluxe is R5000")
        if register_membership != "Basic": # start here for deluxe
            sys.exit("Not a valid answer. Please restart session.")
        if membership_types == "Basic":
            buy_basic = input("To confirm, Please put in your Unique Account number: ")
            if buy_basic != account_number:
                sys.exit("Not a valid answer. Please restart session.")
            if buy_basic == account_number:
                pin_basic = input("Please put in your card pin for safety reasons:")
                if buy_basic != pin:
                    sys.exit("Not a valid answer. Please restart session.")
                if pin_basic == pin:
                    balance = balance - basic_payment
                    membership_active = True
                    membership_type = "Basic"
                    print("------------------------------------------")
                    print("Your updated info:")
                    print("Full Name:", full_name)
                    print("Account Number:", account_number)
                    print("PIN:", pin)
                    print("Account Type:", account_type)
                    print("Cards:", cards)
                    print("Balance: R",balance)
                    print("Membership:", membership_active)
                    print("membership_type:", membership_type)
                print("------------------------------------------")
            elif registration_deluxe != "Deluxe":
                sys.exit("Not a valid answer. Please restart session.")
                if membership_types == "Deluxe":
                    buy_deluxe = input("To confirm, Please put in your Unique Account number: ")
                    if buy_deluxe != account_number:
                        sys.exit("Not a valid answer. Please restart session.")
                        if buy_deluxe == account_number:
                            pin_basic = input("Please put in your card pin for safety reasons:")
                            if buy_deluxe != pin_basic:
                                sys.exit("Not a valid answer. Please restart session.")
                                if pin_basic == pin:
                                    balance = balance - deluxe_payment
                                    membership_active = True
                                    membership_type = "Deluxe"
                                    print("------------------------------------------")
                                    print("Your updated info:")
                                    print("Full Name:", full_name)
                                    print("Account Number:", account_number)
                                    print("PIN:", pin)
                                    print("Account Type:", account_type)
                                    print("Cards:", cards)
                                    print("Balance: R", balance)
                                    print("Membership:", membership_active)
                                    print("membership_type:", membership_type)
                                print("------------------------------------------")

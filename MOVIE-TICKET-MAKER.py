# MOVIE WEBSITE BOOKING
import sys

print("SQmovies")

import random

# LOGIN VERIABLES

username = ""
password = ""
logged_in = False
registered = False
payment = False

user_2_name = "Name here"
user_1_name = "Name Here"

user_1_coming_smallman = "Not Coming"
user_2_coming_smallman = "Not Coming"


smallman_booking = False

print("")
print("Register")
username_input = input("Please register by creating a username: ")
if username_input != username:
    username = username_input
    password_input = input("Please register by creating a password: ")
    if password_input != password:
        password = password_input
        print("Account created!")
        registered = True

print("")

if registered == True:
    print("Login:")
    username_login_input = input("Please login by inputting your username: ")
    if username_login_input == username:
        password_login_input = input("Please input your Password: ")
        if password_login_input == password:
            logged_in = True
            print("Logged In! Welcome,", username)

print("")
print("Options:")
print("View Movies")
print("Make Bookings")
print("View Bookings")
print("Cancel Bookings")

options = input("Please input your option by word (Example, Movies): ").lower()
print("")

while options:
    if options == "movies":
        print("Movies")
        print("Smallman")
        print("Finding The Python")
        movie_movie_option_option = input("Please input the movie you would are interested in: ").lower()
        if movie_movie_option_option == "smallman":
            print("Smallman")
            print("Trailer: https://www.youtube.com/watch?v=Ox8ZLF6cGM0&pp=ygUQc3VwZXJtYW4gdHJhaWxlcg%3D%3D")
            print("Times: 11:00 | 12:00")
            print("Days: Monday(11:00), Wednesday(12:00)")
            print("Age Group: PG-13")
            print("")


    elif options == "bookings":
        print("Make Bookings")
        movie_booking_input = input("What movie are you interested in? (Please say 1 movie)").lower()
        if movie_booking_input == "smallman":
            print("Smallman")
            print("Smallman has a capacity of only 2 people per booking due to its high stakes.")
            user_1_input_smallman = input("Is Person 1 coming?: (Say Y) ").lower()
            if user_1_input_smallman == "y":
                user_1_coming_smallman = "Coming"
            else:
                user_1_coming_smallman = "Not Coming"
            user_2_input_smallman = input("Is Person 2 coming?: (Say Y) ").lower()
            if user_2_input_smallman == "y":
                user_2_coming_smallman = "Coming"
            else:
                user_2_coming_smallman = "Not Coming"

            if user_1_coming_smallman or user_2_coming_smallman != "Not Coming":
                print("Smallman is rated 13+.")
                user_1_input_age_smallman = input("How old is person 1? (Please say age by number").lower()
                if user_1_input_age_smallman >= "13":
                    print("User 1 is eligible for the following movie: (Smallman)")
                else:
                    print("User 1 is not eligible for movie. Cancelling their booking.")
                    user_1_coming_smallman = "Not Coming (Reason underage for movie)"
                user_2_input_age_smallman = input("How old is person 2? (Please say age by number").lower()
                if user_2_input_age_smallman >= "13":
                    print("User 2 is eligible for the following movie: (Smallman)")
                else:
                    print("User 2 is not eligible for movie. Cancelling their booking.")
                    user_1_coming_smallman = "Not Coming (Reason underage for movie)"

                if user_1_coming_smallman != "Not Coming":
                    user_1_payment = 20
                else:
                    user_1_payment = 0

                if user_2_coming_smallman != "Not Coming":
                    user_2_payment = 20
                else:
                    user_2_payment = 0

                if user_1_coming_smallman != "Not Coming":
                    user_1_name = input("What is the name for user 1?")
                    if user_1_name != "":
                        print("User 1 name is:", user_1_name)
                    if user_2_coming_smallman != "Not Coming":
                        user_2_name = input("What is the name for user 2?")
                        if user_2_name != "":
                            print("User 2 name is:", user_2_name)

                print("Smallman costs: 20$ per person")
                full_payment = user_1_payment + user_2_payment
                print("Total is:", full_payment, "Please pay now! by saying (PAY):")
                pay = input("Pay here: ")
                if pay == "PAY":
                    print("Booking completed")
                    smallman_booking = True
                    payment = True

                if payment == True:
                    person_1_id = random.randint(10_000_000_000, 99_999_999_999)
                    person_2_id = random.randint(10_000_000_000, 99_999_999_999)
                    if user_1_coming_smallman or user_2_coming_smallman != "Not Coming":
                        print(user_1_name, "Unique ID is:", person_1_id,
                              "Please use this to register yourself at the theatre!")
                        print(user_2_name, "Unique ID is:", person_2_id, "Please use this to register yourself at the theatre!")
                    else:
                        print("Booking cancelled.")

    elif options == "view":
        print("View Bookings:")
        if smallman_booking:
            print("There is a booking for Smallman")

            if user_1_coming_smallman != "Not Coming":
                print(user_1_name, user_1_coming_smallman, "| " "Age:", user_1_input_age_smallman, "| ", "Unique ID:", person_1_id)
            else:
                print("Person 1 Not coming")

            if user_2_coming_smallman != "Not Coming":
                print(user_2_name, user_2_coming_smallman, "| " "Age:", user_2_input_age_smallman, "| ", "Unique ID:", person_2_id)
            else:
                print("Person 2 Not coming")
        else:
            print("No Bookings at the moment!")

    elif options == "cancel":
        print("Cancel Bookings:")
        if smallman_booking == True:
            print("There is a booking for Smallman")
            confirmation = input("Would you like to cancel this booking?: ").lower()
            if confirmation == "yes":
                print("Booking cancelled. Refunded.")
                user_1_coming_smallman = "Not Coming"
                user_2_coming_smallman = "Not Coming"
                smallman_booking = False
                payment = False
                person_1_id = None
                person_2_id = None
            else:
                print("No bookings to be cancelled!")

    elif options == "exit":
        print("Thanks for visiting! SK Movies. Hope you book again!")
        break

    options = input("Please input your option by word (Example, Movies): ").lower()

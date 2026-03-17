from operator import truediv
import sys

# MADE BY D1PREZZ
# FINISHED ON 17/03/2026
# DO NOT STEAL!



print("Better Impaq Learning Portal (BILP)")

# Account:

user_id = "95197"
user_password = "1307235475082"
name = "Mulweli Madzhie"

assignment_1_submitted_english = 'Not Submitted'
assignment_1_submitted_ns = 'Not Submitted'
assignment_2_submitted_english = 'Not Submitted'
assignment_2_submitted_ns = 'Not Submitted'
assignment_3_submitted_english = 'Not Submitted'
assignment_3_submitted_ns = 'Not Submitted'
assignment_4_submitted_english = 'Not Submitted'
assignment_4_submitted_ns = 'Not Submitted'






english_submissions = ("Assignment 1:",assignment_1_submitted_english,"| Assignment 2:",assignment_2_submitted_english,"| Assignment 3:",assignment_3_submitted_english,"| Assignment 4:",assignment_4_submitted_english)
ns_submissions = ("Assignment 1:",assignment_1_submitted_ns,"| Assignment 2:",assignment_2_submitted_ns,"| Assignment 3:",assignment_3_submitted_ns,"| Assignment 4:",assignment_4_submitted_ns)


english = "Assignment 1 (Task) | Assignment 2 (Test) | Assignment 3 (Test) | Assignment 4 (Task) | TERM 1 |"
notice = "Please note: Assignment list will update after the term."

natural = "Assignment 1 (Exam) | Assignment 2 (Test) | Assignment 3 (Test) | TERM 1 |"
notice = "Please note: Assignment list will update after the term."

logged_in = False

print("Login Page | Better Impaq Learning Portal")
login_id = input("Please input your school ID: ")
if login_id == user_id:
    login_pass = input("Please input your password: ")
    if login_pass != user_password:
        print("Please restart session. Reason: Invalid password")
        sys.exit("Login failed.")
    if login_pass == user_password:
        print("Login successful.")
        logged_in = True
        if login_pass != user_password:
            sys.exit("Login failed.")
            logged_in = False

    print("You are now officialy logged in!")
    print("Better Impaq Learning Portal (BILP)")
    print("")
    print("")
    print("Options:"
          "View Assignments (1) "
          "View my submissions (2) "
          "Submit Assignments (3) "
          "Helpful Videos (4) "
          "Exit (5) ")
    print("")
    print("")

# ==================================================================================================


while logged_in:
    print("=========================================================================")
    option_input = input("Please input your option by the number: ")
    print("")
    print("")

    if option_input == "1": # subject page
        print("=========================================================================")
        subject_choice = input("Please input your Subject (English, Natural Sciences): ").lower()

        if subject_choice == "english":
            print("=========================================================================")
            print("")
            print("")
            print(english)
            print(notice)
            print("")
            print("")


        elif subject_choice == "natural sciences":
            print("=========================================================================")
            print("")
            print("")
            print(natural)
            print(notice)
            print("")
            print("")


    # ==================================================================================================

    elif option_input == "2": # the submissions page
        print("=========================================================================")
        print("")
        print("")
        subject_choice = input("Please input your Subject (English, Natural Sciences) ").lower()
        print("")
        print("")


        if subject_choice == "english":
            print("==========================================================================")
            print("")
            print("")
            print(english_submissions)
            print(notice)
            print("")
            print("")


        elif subject_choice == "natural sciences":
            print("=========================================================================")
            print("")
            print("")
            print(ns_submissions)
            print(notice)
            print("")
            print("")

    # =========================================================================================================

    elif option_input == "3": # the submission page
        print("==========================================================================")
        print("")
        print("")
        subject_choice = input("Please input your subject (English, Natural Sciences) ").lower()
        print("")
        print("")


        if subject_choice == "english":
            print("")
            print("")
            eng_submit = input("Please input your PDF Document for submission.")
            print("")
            print("")

            if "tinyurl" in eng_submit:
                print("")
                print("")
                eng_update_task = input("Please choose the task number your submitting to. Example: assignment 3").lower()
                print("")
                print("")


                if eng_update_task == "assignment 1":
                    assignment_1_submitted_english = 'Submitted'
                    english_submissions = ("Assignment 1:",assignment_1_submitted_english,
                           "| Assignment 2:",assignment_2_submitted_english,
                           "| Assignment 3:",assignment_3_submitted_english,
                           "| Assignment 4:",assignment_4_submitted_english)
                    print("Assignment 1 submitted")


                elif eng_update_task == "assignment 2":
                    print("")
                    print("")
                    assignment_2_submitted_english = 'Submitted'
                    english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                           "| Assignment 2:", assignment_2_submitted_english,
                                           "| Assignment 3:", assignment_3_submitted_english,
                                           "| Assignment 4:", assignment_4_submitted_english)
                    print("Assignment 2 submitted")



                elif eng_update_task == "assignment 3":
                    print("")
                    print("")
                    assignment_3_submitted_english = 'Submitted'
                    english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                           "| Assignment 2:", assignment_2_submitted_english,
                                           "| Assignment 3:", assignment_3_submitted_english,
                                           "| Assignment 4:", assignment_4_submitted_english)
                    print("Assignment 3 submitted")



                    if "tinyurl" in eng_submit:
                        print("")
                        print("")
                        eng_update_task = input(
                            "Please choose the task number your submitting to. Example: assignment 3").lower()

                        if eng_update_task == "assignment 1":
                            assignment_1_submitted_english = 'Submitted'
                            english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                                   "| Assignment 2:", assignment_2_submitted_english,
                                                   "| Assignment 3:", assignment_3_submitted_english,
                                                   "| Assignment 4:", assignment_4_submitted_english)
                            print("")
                            print("")
                            print("Assignment 1 submitted")



                        elif eng_update_task == "assignment 2":
                            print("")
                            print("")
                            assignment_2_submitted_english = 'Submitted'
                            english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                                   "| Assignment 2:", assignment_2_submitted_english,
                                                   "| Assignment 3:", assignment_3_submitted_english,
                                                   "| Assignment 4:", assignment_4_submitted_english)

                            print("Assignment 2 submitted")



                        elif eng_update_task == "assignment 3":
                            assignment_3_submitted_english = 'Submitted'
                            english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                                   "| Assignment 2:", assignment_2_submitted_english,
                                                   "| Assignment 3:", assignment_3_submitted_english,
                                                   "| Assignment 4:", assignment_4_submitted_english)
                            print("Assignment 3 submitted")



                elif eng_update_task == "assignment 4":
                    assignment_4_submitted_english = 'Submitted'
                    english_submissions = ("Assignment 1:", assignment_1_submitted_english,
                                           "| Assignment 2:", assignment_2_submitted_english,
                                           "| Assignment 3:", assignment_3_submitted_english,
                                           "| Assignment 4:", assignment_4_submitted_english)
                    print("Assignment 4 submitted")



# =========================================================================================================
    if subject_choice == "natural sciences":
        print("")
        print("")
        ns_submit = input("Please input your PDF Document for submission.")
        print("")
        print("")

        if "tinyurl" in ns_submit:
            print("")
            print("")
            ns_update_task = input("Please choose the task number your submitting to. Example: assignment 3").lower()
            print("")
            print("")
            if ns_update_task == "assignment 1":
                assignment_1_submitted_ns = 'Submitted'
                ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                       "| Assignment 2:", assignment_2_submitted_ns,
                                       "| Assignment 3:", assignment_3_submitted_ns,
                                       "| Assignment 4:", assignment_4_submitted_ns)
                print("Assignment 1 submitted")

            elif ns_update_task == "assignment 2":
                print("")
                print("")
                assignment_2_submitted_ns = 'Submitted'
                ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                       "| Assignment 2:", assignment_2_submitted_ns,
                                       "| Assignment 3:", assignment_3_submitted_ns,
                                       "| Assignment 4:", assignment_4_submitted_ns)
                print("Assignment 2 submitted")

            elif ns_update_task == "assignment 3":
                print("")
                print("")
                assignment_3_submitted_ns = 'Submitted'
                ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                       "| Assignment 2:", assignment_2_submitted_ns,
                                       "| Assignment 3:", assignment_3_submitted_ns,
                                       "| Assignment 4:", assignment_4_submitted_ns)
                print("Assignment 3 submitted")

                if "tinyurl" in ns_submit:
                    print("")
                    print("")
                    ns_update_task = input(
                        "Please choose the task number your submitting to. Example: assignment 3").lower()

                    if ns_update_task == "assignment 1":
                        assignment_1_submitted_ns = 'Submitted'
                        ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                               "| Assignment 2:", assignment_2_submitted_ns,
                                               "| Assignment 3:", assignment_3_submitted_ns,
                                               "| Assignment 4:", assignment_4_submitted_ns)
                        print("")
                        print("")
                        print("Assignment 1 submitted")

                    elif ns_update_task == "assignment 2":
                        print("")
                        print("")
                        assignment_2_submitted_ns = 'Submitted'
                        ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                               "| Assignment 2:", assignment_2_submitted_ns,
                                               "| Assignment 3:", assignment_3_submitted_ns,
                                               "| Assignment 4:", assignment_4_submitted_ns)

                        print("Assignment 2 submitted")

                    elif ns_update_task == "assignment 3":
                        assignment_3_submitted_ns = 'Submitted'
                        ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                               "| Assignment 2:", assignment_2_submitted_ns,
                                               "| Assignment 3:", assignment_3_submitted_ns,
                                               "| Assignment 4:", assignment_4_submitted_ns)
                        print("Assignment 3 submitted")

            elif ns_update_task == "assignment 4":
                assignment_4_submitted_ns = 'Submitted'
                ns_submissions = ("Assignment 1:", assignment_1_submitted_ns,
                                       "| Assignment 2:", assignment_2_submitted_ns,
                                       "| Assignment 3:", assignment_3_submitted_ns,
                                       "| Assignment 4:", assignment_4_submitted_ns)
                print("Assignment 4 submitted")





    elif option_input == "4":
        print("==========================================================================")
        subject_choice = input("Please input your subject (English, Natural Sciences) ").lower()
        if subject_choice == "english":
            print("English Youtube Videos For Prep")
            print("| Assignment 1: https://youtu.be/vHoTJuf4aqA?si=Uo_uDDTSl4G9c5VJ")
            print("| Assignment 2: https://youtu.be/gES-AewCOAI?si=dqlKWRlyQmP2VW9C")
            print("| Assignment 3: https://youtu.be/AQNFJVdmklA?si=hy172fs3wNbgktYU")
            print("| Assignment 4: https://youtu.be/mg6nVDx2ePQ?si=i5OiRsDaBrazJblu")

        elif subject_choice == "natural sciences":
            print("Not Ready.")


    elif option_input == "5":
        break

# D1PREZZ GAME

import time
import random

username = ""
password = ""
logged_in = False

house_1 = False
house_2 = False
has_houses = True


victories = 0
loss = 0

level = "0"


options = ""

# THE AVAILABLE BOSSES

# LEVEL 1
boss_1_jarastic_hp = 10
boss_1 = "Jamin"
# LEVEL 1

# LEVEL 2
boss_2_FAHHH_hp = 20
boss_2 = "FAHH OF SKELETONS"
# LEVEL 2

# CLEAR UNDEFINEDS
boss_name = ""
boss_hp = ""
boss_damage = ""



# LEVEL 3
boss_3_MIKES_FIRE_BALL_hp = 40
boss_3_THE_COLLECTION_OF_BEASTS_hp = 40
boss_3_HEALTH_RECOLLECTION_health = 30
# LEVEL 3

# LEVEL 4
boss_4_GRILL_MY_ENEMIES = 60
boss_4_TRUGIC_OF_BREAD_health = 30
# LEVEL 4


# THE AVAILABLE GIANTS
gabril_ability_fire_hp = 10
gabril_ability_fire_hp_2 = 30
CLASH_ability_DRASH = 40
CLASH_ability_UBUNTU = 60
AZUR_ability_STEALTH = 50
AZUR_ability_TRYHARD_health = 40


have_gabril = True
have_Clash = False
have_Azur = False

if have_Azur == True:
    level = "3"
elif have_Clash == True:
    level = "2"
else:
    level = "1"

if victories == str(5):
    have_Clash = True
elif victories == str(15):
    have_Azur = True



player_won = ""
tutorial_input = ""

print("Game")
print("Register")


register_username = input("Please input your new username: ")
if register_username != "":
    username = register_username
    print("Your username is: ", username)
    register_password = input("Please input your new password: ")
    if register_password != "":
        print("Account created!")
        password = register_password

print("")
print("Login")
login_username = input("Please input your username: ")
if login_username == username:
    login_password = input("Please input your password: ")
    if login_password == password:
        print("Logged in!")
        logged_in = True

if logged_in == True:
    print("")
    print("Welcome to the game!")
    print("")
    print("In this game, you can fight bosses, create houses and much more!")
    tutorial_input = input("Would you like a tutorial? (Yes or No)")
    if tutorial_input == "Yes":
        print("")
        print("Welcome to the tutorial!")
        print("You will use your first Giant. His name is Gabril")
        print("Gabril will help you fight for you!")
        print("His abilities are as follows:")
        print("")
        print("1: Fire | Deals 10 HP | Magha Fist | Deals 30 HP")
        print("")
        print("")
        print("To do abilities, just say their name! for example, Fire, or FIRE, or fire. Lets test this out.")
        print("We will fight a boss! He is Jamin!")

        import time

        player_1_hp = 100
        boss_hp = 100

        # Ability damage
        gabril_ability_fire_hp = 20
        gabril_ability_fire_hp_2 = 35

        # Cooldowns in seconds
        fire_cooldown = 10
        magha_cooldown = 30

        drash_cooldown = 5
        ubuntu_cooldown = 10

        stealth_cooldown = 10
        tryhard_health_cooldown = 20

        # Last time abilities were used
        last_fire = 0
        last_magha = 0

        print("Fight him on! Remember, your abilities are: FIRE | MAGHA FIST")

        while boss_hp > 0 and player_1_hp > 0:
            print(f"\nPlayer HP: {player_1_hp} | Boss HP: {boss_hp}")
            action = input("1: FIRE | 2: MAGHA FIST: ")
            current_time = time.time()

            # FIRE ability
            if action == "1":
                if current_time - last_fire < fire_cooldown:
                    print("🔥 FIRE is on cooldown! Please use a different ability.")
                    continue

                print("FIGHTING...")
                time.sleep(2)
                boss_hp -= gabril_ability_fire_hp
                print(f"EPIC HIT 🔥 | Boss HP is now {boss_hp}")
                last_fire = current_time  # update cooldown

            # MAGHA FIST ability
            elif action == "2":
                if current_time - last_magha < magha_cooldown:
                    print("💥 MAGHA FIST is on cooldown! Please use a different ability.")
                    continue

                print("FIGHTING...")
                time.sleep(2)
                boss_hp -= gabril_ability_fire_hp_2
                print(f"BIG HIT 💥 | Boss HP is now {boss_hp}")
                last_magha = current_time  # update cooldown

            else:
                print("Invalid input!")
                continue

            # Boss turn (simple attack)
            if boss_hp > 0:
                print("Boss attacks!")
                time.sleep(3)
                player_1_hp -= 10
                print(f"You got hit! Player HP is now {player_1_hp}")

        # End of fight
        if player_1_hp <= 0:
            print("💀 YOU LOST!")
            player_won = False
        elif boss_hp <= 0:
            print("🏆 YOU WON!")
            player_won = True

options_print_tutorial_won = [
    "You Won! Here are the following options:",
    "Houses",
    "PLAY NOW",
    "Gacha",
    "EXIT"
]

options_print_tutorial_loss = [
    "Even though you lost, you have completed the tutorial! | Here are the following options:",
    "Houses",
    "PLAY NOW",
    "Gacha",
    "EXIT"
]

options_print = [
    "Here are the following options:",
    "Houses",
    "PLAY NOW",
    "Gacha",
    "EXIT",
    "Victories"
]

if tutorial_input == "Yes":
    if player_won == True:
        print("")
        print(options_print_tutorial_won)
    else:
        print("")
        print(options_print_tutorial_loss)

elif tutorial_input == "No":
    print("")
    print(options_print)

# ALWAYS ask for option after

options = input("\nPlease enter your option: ").lower()

while options:

    if house_1 or house_2 == True:
        has_houses = True

        if victories >= 5:
            has_houses = True
            house_1 = True
        elif victories >= 15:
            has_houses = True
            house_1 = True
            house_2 = True
        else:
            has_houses = False


    if victories >= 5:
        have_Clash = True
    if victories >= 15:
        have_Azur = True
    if options == "houses":
        print("Houses")
        print("")
        print("In houses, you can view your Giant collection! You can also view your amount of money!")
        if has_houses == True:
            print("You have houses!")
        else:
            print("You have no houses! Get 5 wins to get your first house!")
        if has_houses and house_1 == True:
            print("\nYou have 1 House!")
            if have_gabril == True:
                    print("\n🔥 GIANT INFO: Gabril 🔥")
                    print("Gabril is your first Giant. He is strong with fire-based abilities and close combat skills.")
                    print("\nABILITIES:")
                    print("1️⃣ FIRE")
                    print("   - Deals 20 HP damage to enemies")
                    print("   - Can burn enemies over time")
                    print("   - Cooldown: 10 seconds")
                    print("2️⃣ MAGHA FIST")
                    print("   - Deals 35 HP damage")
                    print("   - A powerful punch that crushes foes")
                    print("   - Cooldown: 30 seconds")
                    print("\nTIP: Use FIRE for frequent attacks and MAGHA FIST for big bursts of damage!")
        if has_houses and house_1 == True:
                print("\n🛡 GIANT INFO: Clash 🛡")
                print("Clash is a defensive and powerful Giant specializing in heavy attacks and crowd control.")
                print("\nABILITIES:")
                print("1️⃣ DRASH")
                print("   - Deals 40 HP damage")
                print("   - A strong smash attack")
                print("   - Cooldown: 5 seconds")
                print("2️⃣ UBUNTU")
                print("   - Deals 60 HP damage")
                print("   - Ultimate attack to deal massive damage")
                print("   - Cooldown: 10 seconds")
                print("\nTIP: Use DRASH frequently and save UBUNTU for critical moments!")
                if have_Clash == True:
                    print("You have Clash!")
                else:
                    print("You can unlock Clash! (5 wins required)")


                print("\n🌙 GIANT INFO: Azur 🌙")
                print("Azur is a stealthy and tactical Giant, perfect for sneaky attacks and quick recovery.")
                print("\nABILITIES:")
                print("1️⃣ STEALTH")
                print("   - Deals 50 HP damage")
                print("   - Can dodge enemy attacks while striking")
                print("   - Cooldown: 10 seconds")
                print("2️⃣ TRYHARD")
                print("   - Restores 40 HP to Azur")
                print("   - A recovery move for tough fights")
                print("   - Cooldown: 20 seconds")
                print("\nTIP: Use STEALTH to strike safely and TRYHARD to stay alive longer!")
        if have_Azur == True:
            print("You have Azur!")
        else:
            print("You can unlock Azur! (15 wins required)")

    elif options == "play now":
        print("")
        print("PLAY NOW")
        if str(level) == "1":
            print("You are Level 1! Therefore you have Gabril!")
            print("Gabril's abilities: FIRE: Burn your enemies and make them suffer! | MAGHA FIST | PUNCH LIKE A PIECE OF MAGHA")
            print("You are playing.. ")
            time.sleep(2)
            print("")
            print("JAMIN!")
            play_now = input("PLAY NOW?").lower()
            if play_now == "yes":

                player_1_hp = 100
                boss_hp = 100

                # Ability damage
                gabril_ability_fire_hp = 20
                gabril_ability_fire_hp_2 = 35

                # Cooldowns in seconds
                fire_cooldown = 10
                magha_cooldown = 30

                drash_cooldown = 5
                ubuntu_cooldown = 10

                stealth_cooldown = 10
                tryhard_health_cooldown = 20

                # Last time abilities were used
                last_fire = 0
                last_magha = 0

                while boss_hp > 0 and player_1_hp > 0:
                    print(f"\nPlayer HP: {player_1_hp} | Boss HP: {boss_hp}")
                    action = input("1: FIRE | 2: MAGHA FIST: ")
                    current_time = time.time()

                    # FIRE ability
                    if action == "1":
                        if current_time - last_fire < fire_cooldown:
                            print("🔥 FIRE is on cooldown! Please use a different ability.")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp
                        print(f"EPIC HIT 🔥 | Boss HP is now {boss_hp}")
                        last_fire = current_time  # update cooldown

                    # MAGHA FIST ability
                    elif action == "2":
                        if current_time - last_magha < magha_cooldown:
                            print("💥 MAGHA FIST is on cooldown! Please use a different ability.")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp_2
                        print(f"BIG HIT 💥 | Boss HP is now {boss_hp}")
                        last_magha = current_time  # update cooldown

                    else:
                        print("Invalid input!")
                        continue

                    # Boss turn (simple attack)
                    if boss_hp > 0:
                        print("Boss attacks!")
                        time.sleep(3)
                        player_1_hp -= 10
                        print(f"You got hit! Player HP is now {player_1_hp}")

                # End of fight
                if player_1_hp <= 0:
                    print("💀 YOU LOST!")
                    player_won = False
                    loss = loss + 1
                elif boss_hp <= 0:
                    print("🏆 YOU WON!")
                    player_won = True
                    victories = victories + 1

        # LEVEL 2 BOSS FIGHT
        elif str(level) == "2":
            print("You are Level 2! Therefore you have Gabril AND CLASH!")

            print("Choosing boss...")
            time.sleep(2)

            randomized = random.randint(1, 2)

            if randomized == 1:
                boss_name = boss_2
                boss_hp = boss_2_FAHHH_hp
                boss_damage = 20
            elif randomized == 2:
                boss_name = "CLASH SHADOW"
                boss_hp = 25
                boss_damage = 15

            print(f"You are fighting: {boss_name}")

            play_now = input("PLAY NOW?").lower()
            if play_now == "yes":

                player_1_hp = 100

                # Ability damage
                gabril_ability_fire_hp = 20
                gabril_ability_fire_hp_2 = 35

                # Cooldowns
                fire_cooldown = 10
                magha_cooldown = 30

                last_fire = 0
                last_magha = 0

                while boss_hp > 0 and player_1_hp > 0:
                    print(f"\nPlayer HP: {player_1_hp} | Boss HP: {boss_hp}")
                    action = input("1: FIRE | 2: MAGHA FIST: ")
                    current_time = time.time()

                    if action == "1":
                        if current_time - last_fire < fire_cooldown:
                            print("🔥 FIRE is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp
                        print(f"EPIC HIT 🔥 | Boss HP is now {boss_hp}")
                        last_fire = current_time

                    elif action == "2":
                        if current_time - last_magha < magha_cooldown:
                            print("💥 MAGHA FIST is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp_2
                        print(f"BIG HIT 💥 | Boss HP is now {boss_hp}")
                        last_magha = current_time

                    else:
                        print("Invalid input!")
                        continue

                    # Boss turn
                    if boss_hp > 0:
                        special = random.randint(1, 4)

                        if boss_name == boss_2 and special == 1:
                            print("💀 FAHHH RAGE ATTACK!")
                            player_1_hp -= boss_damage + 10
                        else:
                            print(f"{boss_name} attacks!")
                            player_1_hp -= boss_damage

                        print(f"Player HP is now {player_1_hp}")

                if player_1_hp <= 0:
                    print("💀 YOU LOST!")
                    player_won = False
                    loss += 1
                else:
                    print("🏆 YOU WON!")
                    player_won = True
                    victories += 1


        # LEVEL 3 BOSS FIGHT
        elif str(level) == "3":
            print("You are Level 3! Therefore you have Gabril, CLASH AND AZUR!")

            print("Choosing boss...")
            time.sleep(2)

            randomized = random.randint(1, 3)

            if randomized == 1:
                boss_name = "MIKES FIRE BALL"
                boss_hp = boss_3_MIKES_FIRE_BALL_hp
                boss_damage = 25

            elif randomized == 2:
                boss_name = "THE COLLECTION OF BEASTS"
                boss_hp = boss_3_THE_COLLECTION_OF_BEASTS_hp
                boss_damage = 20

            elif randomized == 3:
                boss_name = "HEALTH RECOLLECTION"
                boss_hp = boss_3_HEALTH_RECOLLECTION_health
                boss_damage = 15

            print(f"You are fighting: {boss_name}")

            play_now = input("PLAY NOW?").lower()
            if play_now == "yes":

                player_1_hp = 120

                # Ability damage
                gabril_ability_fire_hp = 20
                gabril_ability_fire_hp_2 = 35

                # Cooldowns
                fire_cooldown = 10
                magha_cooldown = 30

                last_fire = 0
                last_magha = 0

                while boss_hp > 0 and player_1_hp > 0:
                    print(f"\nPlayer HP: {player_1_hp} | Boss HP: {boss_hp}")
                    action = input("1: FIRE | 2: MAGHA FIST: ")
                    current_time = time.time()

                    if action == "1":
                        if current_time - last_fire < fire_cooldown:
                            print("🔥 FIRE is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp
                        print(f"EPIC HIT 🔥 | Boss HP is now {boss_hp}")
                        last_fire = current_time

                    elif action == "2":
                        if current_time - last_magha < magha_cooldown:
                            print("💥 MAGHA FIST is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(2)
                        boss_hp -= gabril_ability_fire_hp_2
                        print(f"BIG HIT 💥 | Boss HP is now {boss_hp}")
                        last_magha = current_time

                    else:
                        print("Invalid input!")
                        continue

                    # Boss turn
                    if boss_hp > 0:
                        special = random.randint(1, 4)

                        if boss_name == "HEALTH RECOLLECTION" and special == 1:
                            boss_hp += 10
                            print(f"🧠 {boss_name} healed! Boss HP is now {boss_hp}")
                        else:
                            print(f"{boss_name} attacks!")
                            player_1_hp -= boss_damage

                        print(f"Player HP is now {player_1_hp}")

                if player_1_hp <= 0:
                    print("💀 YOU LOST!")
                    player_won = False
                    loss += 1
                else:
                    print("🏆 YOU WON!")
                    player_won = True
                    victories += 1

        # LEVEL 4 BOSS FIGHT
        elif str(level) == "4":
            print("🔥 LEVEL 4 🔥")
            print("You now face the strongest bosses so far...")

            print("Choosing boss...")
            time.sleep(2)

            randomized = random.randint(1, 2)

            if randomized == 1:
                boss_name = "GRILL MY ENEMIES"
                boss_hp = boss_4_GRILL_MY_ENEMIES
                boss_damage = 30

            elif randomized == 2:
                boss_name = "TRUGIC OF BREAD"
                boss_hp = boss_4_TRUGIC_OF_BREAD_health
                boss_damage = 20

            print(f"You are fighting: {boss_name}")

            play_now = input("PLAY NOW?").lower()
            if play_now == "yes":

                player_1_hp = 140  # stronger player

                # Ability damage
                gabril_ability_fire_hp = 25
                gabril_ability_fire_hp_2 = 45

                # Cooldowns (slightly faster gameplay)
                fire_cooldown = 8
                magha_cooldown = 25

                last_fire = 0
                last_magha = 0

                while boss_hp > 0 and player_1_hp > 0:
                    print(f"\nPlayer HP: {player_1_hp} | Boss HP: {boss_hp}")
                    action = input("1: FIRE | 2: MAGHA FIST: ")
                    current_time = time.time()

                    if action == "1":
                        if current_time - last_fire < fire_cooldown:
                            print("🔥 FIRE is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(1.5)
                        boss_hp -= gabril_ability_fire_hp
                        print(f"EPIC HIT 🔥 | Boss HP is now {boss_hp}")
                        last_fire = current_time

                    elif action == "2":
                        if current_time - last_magha < magha_cooldown:
                            print("💥 MAGHA FIST is on cooldown!")
                            continue

                        print("FIGHTING...")
                        time.sleep(1.5)
                        boss_hp -= gabril_ability_fire_hp_2
                        print(f"BIG HIT 💥 | Boss HP is now {boss_hp}")
                        last_magha = current_time

                    else:
                        print("Invalid input!")
                        continue

                    # 🔥 Boss turn (ADVANCED)
                    if boss_hp > 0:
                        special = random.randint(1, 3)

                        if boss_name == "GRILL MY ENEMIES" and special == 1:
                            print("🔥 ULTIMATE: GRILL EVERYTHING!!!")
                            player_1_hp -= boss_damage + 20

                        elif boss_name == "TRUGIC OF BREAD" and special == 1:
                            boss_hp += 15
                            print(f"🍞 {boss_name} healed! Boss HP is now {boss_hp}")

                        else:
                            print(f"{boss_name} attacks!")
                            player_1_hp -= boss_damage

                        print(f"Player HP is now {player_1_hp}")

                # End
                if player_1_hp <= 0:
                    print("💀 YOU LOST LEVEL 4!")
                    player_won = False
                    loss += 1
                else:
                    print("🏆 YOU WON LEVEL 4!")
                    player_won = True
                    victories += 1

    elif options == "victories":
        print("Victories")
        print("Wins: ", str(victories))
        print("Losses: ", str(loss))
        print("Play and WIN in order to get new giants and Houses!")

    elif options == "gacha":
        print("Gacha")
        print("WIP | Please come back later!")

    elif options == "exit":
        print("See you next time!")
        break

    options = input("\nPlease enter your option: ").lower()

# MADE BY D1PREZZ
# NOT OPEN SOURCE

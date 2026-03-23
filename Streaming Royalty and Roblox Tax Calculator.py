# STREAMING ROYALTY / ROBLOX / AMOUNT CALCULATOR!
# DO NOT STEAL
# MADE BY D1PREZZ | ALL RIGHTS RESERVED

print("Calculate the amount you can get from roblox transactions and Spotify Stream payments!")

options = input("Please input Spotify, Roblox, Apple Music, Youtube Music, Soundcloud OR Deezer (Say FAQ to open the FAQ): ")

while options:
    if options == "Spotify":
        pps = float(input("Please input your Pay Per Stream (Default for spotify is 0.0040): "))
        if pps != "":
            print("Your Pay Per Stream is: ",pps)
            arp = float(input("Please input your artist royalty precentage: "))
            if arp != "":
                print("Your result is:", arp)
                streams = float(input("Please input your Spotify Stream amount: "))
                if streams != "":
                    print("Your Spotify Stream amount is:", streams)
                    result = pps * streams * (arp / 100)
                    print("Your Spotify Stream amount is:", "$",result)

    elif options == "Roblox":
        roblox_tax = 0.70
        print("Roblox Tax Rate is currently: 70%", "So you will get 70% of the initial payment")
        roblox_amount = int(input("Please input your amount: "))
        if roblox_amount != "":
            total = roblox_amount * roblox_tax
            print("Your payment shall be:", total)


    elif options == "Apple Music":
        pps = float(input("Please input your PPS (Pay Per Stream) Default for Apple Music is 0.0080: "))
        if pps != "":
            print("Your Pay Per Stream is:", pps)
            arp = float(input("Please input your artist royalty precentage: "))
            if arp != "":
                print("Your result is:", arp)
                streams = float(input("Please input your Apple Music Stream amount: "))
                if streams != "":
                    print("Your Apple Music Stream amount is:", streams)
                    result = pps * streams * (arp / 100)
                    print("Your Apple Music amount is:", "$",result)

    elif options == "Youtube Music":
        pps = float(input("Please input your Pay Per Stream Default for Youtube Music is 0.0070: "))
        if pps != "":
            print("Your Pay Per Stream is:", pps)
            arp = float(input("Please input your artist royalty precentage: "))
            if arp != "":
                print("Your result is:", arp)
                streams = float(input("Please input your Youtube Music Stream amount: "))
                if streams != "":
                    print("Your Youtube Music amount is:", streams)
                    result = pps * streams * (arp / 100)
                    print("Your Youtube Music amount is:", "$",result)


    elif options == "Soundcloud":
        pps = float(input("Please input your Pay Per Stream Default for SoundCloud is 0.0030: "))
        if pps != "":
            print("Your Pay Per Stream is:", pps)
            arp = float(input("Please input your artist royalty precentage: "))
            if arp != "":
                print("Your result is:", arp)
                streams = float(input("Please input your SoundCloud Stream amount: "))
                if streams != "":
                    print("Your SoundCloud Stream amount is:", streams)
                    result = pps * streams * (arp / 100)
                    print("Your SoundCloud Stream amount is:", "$",result)


    elif options == "Deezer":
        pps = float(input("Please input your Pay Per Stream Default for Deezer is 0.0060: "))
        if pps != "":
            print("Your Pay Per Stream is:", pps)
            arp = float(input("Please input your artist royalty precentage: "))
            if arp != "":
                print("Your result is:", arp)
                streams = float(input("Please input your Deezer Stream amount: "))
                if streams != "":
                    print("Your Deezer Stream amount is:", streams)
                    result = pps * streams * (arp / 100)
                    print("Your Deezer Stream amount is:", "$",result)

    elif options == "FAQ":
        print("Which streaming service earns more money?")
        print("The streaming service that earns the msot money is actually Apple Music. Which earns 0.0080 per view. ")
        print("Which streaming service earns the least money?")
        print("The streaming service that earns the least is Spotify! Which earns 0.0040 per view. ")








    options = input("Please input Spotify, Roblox, Apple Music, Youtube Music, Soundcloud OR Deezer (Say FAQ to open the FAQ) ")



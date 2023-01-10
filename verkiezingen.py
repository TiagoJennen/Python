while True:
    print("Vul hier uw nieuwe premier in : ")
    namen = input()
    import sys
    while True:
        print("Type stop als de verkiezing voorbij is")
        klaar = input()
        if klaar == 'stop':
            sys.exit()
        print(namen)
# Info over gebruiker
naam = input("Wat is je naam + je achternaam? ")
leeftijd = input("Hoe oud ben je? ")
geboorteplaats = input("Waar ben je geboren? ")
woonplaats = input("Waar woon je? ")
hobbys = input("Wat zijn je hobby's? ")
wachtwoord = input("Wat is je wachtwoord? ")
pincode = input("Wat is je pincode? ")
print("Hallo " + naam + "! Je bent " + leeftijd + " jaar oud. Je bent geboren in " + geboorteplaats + ". Je woont nu in " + woonplaats + ". Je hobby's zijn " + hobbys + ". Je wachtwoord is " + wachtwoord + ". Je pincode is " + pincode) 

# E-mail van gebruiker vragen
def main():
    print("Welkom bij de e-mail")
    print("")
    emailinput = input("Vul hier je e-mail in: ")
    (emailinput) = emailinput.split("@")
    print(emailinput)
main()

# Raad het woord
geheimwoord = "woord"
raad = ""
while raad != geheimwoord:
    raad = input("Raad het WOORD: ")
print("Goed geraden!")
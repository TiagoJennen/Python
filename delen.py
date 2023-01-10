def divide(x, y, z):
    return x / y / z
while True:
    num1 = float(input("Voer eerste getal in: "))
    num2 = float(input("Voer tweede getal in: "))
    num3 = float(input("Voer derde getal in: "))
    print(num1, "/", num2, "/", num3,  "=", divide(num1, num2, num3))
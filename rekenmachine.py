def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Selecteer optie.")
print("1.Plus")
print("2.Min")
print("3.Keer")
print("4.Delen")
while True:
    choice = input("Selecteer optie.(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Voer eerste getal in: "))
        num2 = float(input("Voer tweede getal in: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        if choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        if choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        if choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
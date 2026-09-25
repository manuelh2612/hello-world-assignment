def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2


def calculate_tax(money, tax):
    return money + (money * tax)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


radius = float(input("Enter the radius: "))
area = circle_area(radius)
print(f"Circle area: {area:.2f}")

money = float(input("Enter the money: "))
tax = float(input("Enter the tax rate as a decimal: "))
total = calculate_tax(money, tax)
print(f"Total due: {total:.2f}")

fahrenheit = float(input("Enter the Fahrenheit temperature: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Celsius: {celsius:.5f}")

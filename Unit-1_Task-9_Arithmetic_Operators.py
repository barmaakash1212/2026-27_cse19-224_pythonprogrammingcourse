num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
exponentiation = num1 ** num2
if num2 != 0:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
else:
    division = "Undefined (Cannot divide by zero)"
    floor_division = "Undefined (Cannot divide by zero)"
    modulus = "Undefined (Cannot divide by zero)"
print("\n--- Results ---")
print(f"Addition ({num1} + {num2})          = {addition}")
print(f"Subtraction ({num1} - {num2})       = {subtraction}")
print(f"Multiplication ({num1} * {num2})    = {multiplication}")
print(f"Exponentiation ({num1} ** {num2})    = {exponentiation}")
print(f"Division ({num1} / {num2})          = {division}")
print(f"Floor Division ({num1} // {num2})    = {floor_division}")
print(f"Modulus ({num1} % {num2})           = {modulus}")
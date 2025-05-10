print( """⣶⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣶
⣿⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⣿
⣿⠀⢸⡟⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⠀⠀⣿
⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⣿⠀⠘⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⠀⠀⣿
⣿⠀⠀⣀⣀⣀⣀⠀⠀⣀⣀⣀⣀⠀⠀⣀⣀⣀⣀⠀⠀⣿
⣿⠀⠀⣿⠉⠉⣿⠀⠀⣿⠉⠉⣿⠀⠀⣿⠉⠉⣿⠀⠀⣿
⣿⠀⠀⠙⠛⠛⠋⠀⠀⠙⠛⠛⠋⠀⠀⠙⠛⠛⠋⠀⠀⣿
⣿⠀⠀⣶⠶⠶⣶⠀⠀⣶⠶⠶⣶⠀⠀⣶⠶⠶⣶⠀⠀⣿
⣿⠀⠀⠿⠶⠶⠿⠀⠀⠿⠶⠶⠿⠀⠀⠿⠶⠶⠿⠀⠀⣿
⣿⠀⠀⣀⣀⣀⣀⠀⠀⣀⣀⣀⣀⠀⠀⣀⣀⣀⣀⠀⠀⣿
⣿⠀⠀⣿⣉⣉⣿⠀⠀⣿⣉⣉⣿⠀⠀⣿⣉⣉⣿⠀⠀⣿
⣿⠀⠀⠉⠉⠉⠉⠀⠀⠉⠉⠉⠉⠀⠀⠉⠉⠉⠉⠀⠀⣿
⢿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠿""")
print("Welcome to the calculator!")
print("Please enter the first number:")
a=float(input())
print("Please enter the second number:")
b=float(input())
print("Please enter the operator:")
o=input()
match o:
    case "+":
        print(f"{a} + {b} = {a+b}")
    case "-":
        print(f"{a} - {b} = {a-b}")
    case "*":
        print(f"{a} * {b} = {a*b}")
    case "/":
        print(f"{a} / {b} = {a/b}")
    case "%":
        print(f"{a} % {b} = {a%b}")
    case "**":
        print(f"{a} ** {b} = {a**b}")
 
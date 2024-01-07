"""
HW3
Savchenko Kirill
"""
# 1
try:
    print("1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday")
    user_select = int(input("choose number between 1-7: "))
    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            raise Exception("Enter number between 1-7")
except ValueError as e:
    print("Enter only integer numbers between 1-7")
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# 2

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if first_number == second_number:
        print("congratulations, numbers are equal")
    elif first_number != second_number:
        if first_number <= second_number:
            print(first_number, second_number)
        elif first_number >= second_number:
            print(second_number, first_number)
        else:
            print("Error")
    else:
        print("Error")

except ValueError as e:
    print("Enter only integer numbers")
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# 3

try:
    a = float(input('write first number: '))
    b = float(input('write second number: '))
    operation = input('what to do? (+, -, *, /): ')
    match operation:
        case '+':
            print(a + b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            print(a / b)

except ValueError as e:
    print("Enter only integer numbers")
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print("you can't divide by 0")
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

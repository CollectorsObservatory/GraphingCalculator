import datetime
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# basically a program with two modes basic and graphical calculator
# graphical calculator calculates derivatives , integrals and plots a graphic


class Calculator:
    """Basic functions of calculator"""
    def __init__(self, num_1, num_2, operation, ans=0):
        self.num_1 = num_1
        self.num_2 = num_2
        self.ans = ans
        self.operation = operation

    def addition(self):
        return self.num_1 + self.num_2

    def subs(self):
        return self.num_1 - self.num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def division(self):
        try:
            return self.num_1 / self.num_2
        except ZeroDivisionError:
            return "Can't Divide by Zero!"

    def power(self):
        return self.num_1 ** self.num_2

    def modulo(self):
        try:
            if self.num_1 % self.num_2 == 0:
                return f"{self.num_1} can be divided by {self.num_2}"

            else:
                return "No full division possible!"
        except ZeroDivisionError:
            return "Can't Divide by Zero!"


# start of the program by giving the user choices to choose from
print("   ***Welcome to Apollo Calculator***   ")    # Print a welcome message
print(f"  Current time is {current_time}")
print(" ")
print("   Here are the available modes:")
print("   Press 1- **Basic Calculator**")
print("   Press 2- **Graphical Calculator**")
print("   Press 3- **Graphics only mode**")
print("   Press 4- **Equation Solver**")
print(" ")
while True:
    try:
        mode_choice = int(input("-Please choose the mode: "))
        if mode_choice == 1:
            ans_list = []  # used later to store the last result to be used again
            # Define a list of valid operators
            operator_list = ["-", "+", "*", "**", "/", "%"]

            # Define the output format
            print(f"-Possible operations are {operator_list}")
            print("            -% for Modulo")
            print("            -** for Power")
            print("-If you want to use your old result , type ans in the terminal ")

            # Start an infinite loop to keep the calculator running
            while True:
                try:
                    # Get the user's input for the first number
                    number_1 = float(input("-Please enter the first number: "))
                    # Get the user's input for the second number
                    number_2 = float(input("Please enter the second number: "))
                    # Get the user's choice of operation
                    operator = str(input("-Choose the operation: "))
                    print(" ")

                    # Check if the operator is valid, if not, prompt the user to try again
                    if operator not in operator_list:
                        print("Please try again!")

                    # Create a Calculator instance with user inputs
                    calculation = Calculator(num_1=number_1, num_2=number_2, operation=operator)


                    def calculator_suite(calc, op):
                        """Created this function simply to be able to use the ans list variable"""
                        op = operator
                        if operator == "+":
                            print(calculation.addition())
                            ans_list.append(calculation.addition())

                        elif operator == "-":
                            print(calculation.subs())
                            ans_list.append(calculation.subs())

                        elif operator == "**":
                            print(calculation.power())
                            ans_list.append(calculation.power())

                        elif operator == "*":
                            print(calculation.multiply())
                            ans_list.append(calculation.multiply())

                        elif operator == "/":
                            print(calculation.division())
                            ans_list.append(calculation.division())

                        elif operator == "%":
                            print(calculation.modulo())
                            ans_list.append(calculation.modulo())
                        return ""


                    print(calculator_suite(calculation, operator))
                    ans = ans_list[0]

                    choice = input("-Type ans to use old result, Press Enter to Continue, Type exit to quit: ")

                    if choice.lower() == "ans":
                        while True:
                            new_number_2 = float(input("-Enter second number: "))
                            new_operator = str(input("-Enter operator: "))
                            calculation = Calculator(num_1=ans, num_2=new_number_2, operation=operator)
                            print(calculator_suite(calculation, new_operator))
                            ans_list.append(calculation.modulo())
                            ans = ans_list[1]
                            print(ans)

                    elif choice.lower() == "":
                        continue  # Continue to the next iteration of the loop

                    elif choice.lower() == "exit":
                        print("**Closing Basic Calculator, see you soon !**")
                        break  # Exit the loop if the user wants to exit

                except ValueError:
                    print("*Wrong input, Please try again!*")  # Handle invalid inputs
        if mode_choice == 2:
            # now switching to graphical calculator , a class here is useless
            print("** x is by default the symbol of the variable **")
            print("** WE HANDLE SIN FUNCTIONS **")
            while True:

                function = input("-Enter function using x: ")

                x = sp.symbols("x")   # x is the variable symbol by default as stated to the user

                derivative_function = sp.diff(function, x)  # calculate derivative

                integrate_function = sp.integrate(function, x)  # calculate integral

                f_func = sp.lambdify(x, function, 'numpy')  # this line and below are used for plotting purposes

                f_derivative_func = sp.lambdify(x, derivative_function, 'numpy')

                f_integrate_func = sp.lambdify(x, integrate_function, 'numpy')

                x_values = np.linspace(-15, 15, 400)

                y_values = [f_func(x_val) for x_val in x_values]

                y_derivative_values = [f_derivative_func(x_val) for x_val in x_values]

                y_integrate_values = [f_integrate_func(x_val) for x_val in x_values]

                action_input = str(input("-Type D for derivative, I for integration or B for both: "))
                if action_input.lower == "d":
                    print(derivative_function)

                elif action_input.lower() == "i":
                    print(integrate_function)

                elif action_input.lower() == "b":
                    print(f"**Derivative is {derivative_function}  **")
                    print(f"**Integral is {integrate_function} + C **")

                view_input = str(input("-Do you want to view the plot of the function? (Y for yes , N for no, "
                                       "E to exit program): "))

                if view_input.lower() == "y":
                    # will open a window to display the function
                    plt.figure(figsize=(10, 8))
                    plt.plot(x_values, y_values, label=function)
                    plt.plot(x_values, y_derivative_values, label='Derivative', linestyle='--')
                    plt.plot(x_values, y_integrate_values, label='Integral', linestyle='--')
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.legend()
                    plt.title('Function, Its Derivative and Integral')
                    plt.grid(True)
                    plt.show()
                elif view_input.lower() == "n":
                    print("**Reseting Graphical Calculator**")
                    print(" ")
                    continue
                else:
                    print("**Closing Graphing Calculator, see you soon !**")
                    break
        if mode_choice == 3:
            print("**Welcome to Graphical only mode**")
            while True:
                function = input("-Enter function using x: ")
                try:
                    x = sp.symbols("x")  # x is the variable symbol by default as stated to the user
                    f_func = sp.lambdify(x, function, 'numpy')
                    x_values = np.linspace(-15, 15, 400)
                    y_values = [f_func(x_val) for x_val in x_values]
                    plt.figure(figsize=(10, 8))
                    plt.plot(x_values, y_values, label=function)
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.legend()
                    plt.title(f'Plot of the function:{function}')
                    plt.grid(True)
                    plt.show()
                    mode_3 = str(input("Do you wish to continue using this mode?(y or n): "))
                    try:
                        if mode_3.lower() == "y":
                            continue
                        elif mode_3.lower() == "n":
                            print("**Closing Graphics only mode, see you soon !**")
                            break
                    except ValueError:
                        print("Wrong input, Reset the program and try again")
                except ValueError:
                    print("Wrong input, Reset the program and try again")

        if mode_choice == 4:
            print("**Welcome to equation solver**")
            print("** x is by default the symbol of the variable **")
            while True:
                x = sp.symbols('x')
                enter_basic_calculation = input("Enter your equation: ")
                try:
                    solution = sp.solve(enter_basic_calculation, x)
                    print(f"solution is: {solution}")
                    mode_4 = str(input("Do you wish to continue using this mode?(y or n): "))
                    try:
                        if mode_4.lower() == "y":
                            continue
                        elif mode_4.lower() == "n":
                            print("**Closing Graphics only mode, see you soon !**")
                            break
                    except ValueError:
                        print("Wrong input, Reset the program and try again")

                except ValueError:
                    print("Wrong input , please try again !")

    except ValueError:
        print("**Wrong input, Please try again!**")  # Handle invalid inputs

    finally:
        print("**Developed by CollectorsObservatory**")


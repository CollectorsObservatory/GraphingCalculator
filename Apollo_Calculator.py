# author Fares Majdoub
import datetime
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
x = sp.symbols("x")


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
        """Adds 2 numbers"""
        return self.num_1 + self.num_2

    def subs(self):
        """Substratcs 2 numbers"""
        return self.num_1 - self.num_2

    def multiply(self):
        """Multiplies 2 numbers"""
        return self.num_1 * self.num_2

    def division(self):
        """Divides two numbers"""
        try:
            return self.num_1 / self.num_2
        except ZeroDivisionError:
            return "Can't Divide by Zero!"

    def power(self):
        """Return one number to the power of the second number"""
        return self.num_1 ** self.num_2

    def modulo(self):
        """Checks if one number can be divided by another"""
        try:
            if self.num_1 % self.num_2 == 0:
                return f"{self.num_1} can be divided by {self.num_2}"
            else:
                return "No full division possible!"
        except ZeroDivisionError:
            return "Can't Divide by Zero!"

    def calculator_suite(self):
        """This function checks the operation input by the user and assigns the right method to it"""
        if self.operation == "+":
            return self.addition()
        elif self.operation == "-":
            return self.subs()
        elif self.operation == "**":
            return self.power()
        elif self.operation == "*":
            return self.multiply()
        elif self.operation == "/":
            return self.division()
        elif self.operation == "%":
            return self.modulo()


class Function:
    """Serves to see the first integral and derivative to a function and to plot it"""

    def __init__(self, function):
        self.function = sp.simplify(function)

    def derivative(self):
        """Retuns the derivative"""
        return sp.diff(self.function, x)

    def integrate(self):
        """Returns the integral"""
        return sp.integrate(self.function, x)

    def plot(self):
        """Plots the graph of the function"""
        f_func = sp.lambdify(x, self.function, 'numpy')
        f_derivative_func = sp.lambdify(x, self.derivative(), 'numpy')
        f_integrate_func = sp.lambdify(x, self.integrate(), 'numpy')
        x_values = np.linspace(-15, 15, 400)
        y_values = [f_func(x_val) for x_val in x_values]
        y_derivative_values = [f_derivative_func(x_val) for x_val in x_values]
        y_integrate_values = [f_integrate_func(x_val) for x_val in x_values]
        plt.figure(figsize=(10, 8))
        plt.plot(x_values, y_values, label=self.function)
        plt.plot(x_values, y_derivative_values, label='Derivative', linestyle='--')
        plt.plot(x_values, y_integrate_values, label='Integral', linestyle='--')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.title('Function, Its Derivative and Integral')
        plt.grid(True)
        plt.show()


# start of the program by giving the user choices to choose from
print("   ***Welcome to Apollo Calculator***   ")  # Print a welcome message
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

                    result = calculation.calculator_suite()
                    ans_list.append(result)

                    print(result)
                    ans = ans_list[0]

                    choice = input("-Type ans to use old result, Press Enter to Continue, Type exit to quit: ")

                    if choice.lower() == "ans":
                        while True:
                            new_number_2 = float(input("-Enter second number: "))
                            new_operator = str(input("-Enter operator: "))
                            calculation = Calculator(num_1=ans, num_2=new_number_2, operation=operator)
                            print(calculation.calculator_suite())

                    elif choice.lower() == " ":
                        continue  # Continue the loop

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
                new_function = input("-Enter function using x: ")
                new_function = Function(function=new_function)

                action_input = str(input("-Type D for derivative, I for integration or B for both: "))
                try:
                    if action_input.lower == "d":
                        print(new_function.derivative())

                    elif action_input.lower() == "i":
                        print(new_function.integrate())

                    elif action_input.lower() == "b":
                        print(f"**Derivative is {new_function.derivative()}  **")
                        print(f"**Integral is {new_function.integrate()} + C **")
                except ValueError:
                    print("Wrong input, Please Enter D for derivative, I for integration or B for both")

                view_input = str(input("-Do you want to view the plot of the function? (Y for yes , N for no, "
                                       "E to exit program): "))
                if view_input.lower() == "y":
                    new_function.plot()

                elif view_input.lower() == "n":
                    print("**Reseting Graphical Calculator**")
                    print(" ")

                elif view_input.lower() == "e":
                    print("**Closing Graphing Calculator, see you soon !**")
                    print(" ")
                else:
                    print("Wrong input, Try again!")

        if mode_choice == 3:
            print("**Welcome to Graphical only mode**")
            while True:

                function_mode3 = input("-Enter function using x: ")
                function_mode3 = Function(function=function_mode3)  # Linking with the function class

                try:
                    function_mode3.plot()
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

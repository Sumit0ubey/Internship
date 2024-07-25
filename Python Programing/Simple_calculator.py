class Calculator:
    
    def __init__(self):
        self.on = True
        self.main()
        
    def calculation(self):
        try:
            self.first_number = float(input("Enter the First Number: "))
            self.second_number = float(input("Enter the Second Number: "))
            self.choice = int(input("Enter your Choice: \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Exit \n ---> "))
            
            if self.choice == 1:
                result = self.first_number + self.second_number
                print(f'Addition of {self.first_number} and {self.second_number} is {result}')
            elif self.choice == 2:
                result = self.first_number - self.second_number
                print(f'Subtraction of {self.first_number} and {self.second_number} is {result}')
            elif self.choice == 3:
                result = self.first_number * self.second_number
                print(f'Multiplication of {self.first_number} and {self.second_number} is {result}')
            elif self.choice == 4:
                if self.second_number != 0:
                    result = self.first_number / self.second_number
                    print(f'Division of {self.first_number} and {self.second_number} is {result}')
                else:
                    print("Error: Division by zero is not allowed.")
            elif self.choice == 5:
                self.on = False
            else:
                print("Wrong Input. \n retry..")
        except ValueError:
            print("Invalid input. Please enter numbers only for the calculations and valid choices for the operation.")
        except Exception as e:
            print(f"There was a Problem: {e}")

    def main(self):
        while self.on:
            self.calculation()
        
if __name__ == "__main__":
    calculator = Calculator()

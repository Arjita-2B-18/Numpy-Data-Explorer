import numpy as np

import matplotlib.pyplot as plt


class IntArray:

    def __init__(self, int_array):
        if not isinstance(int_array, np.ndarray):
            raise ValueError("Input must be a NumPy array")

        self.int_array = int_array

    def display(self):
        print("\nEmployee production data:")
        print(self.int_array)

    def salary(self):
        money_per_product = 7
        salaries = self.int_array * money_per_product
        print("\nSalaries of employees:")
        print(salaries)

    def show_data(self):
        x = np.arange(len(self.int_array))
        plt.plot(x, self.int_array, marker='o')
        plt.title("Productivity of Employees")
        plt.xlabel("Employee Rank")
        plt.ylabel("Products per Month")
        plt.grid(True)
        plt.show()
data = np.genfromtxt("company_cleaned.txt", delimiter=",")
obj = IntArray(data)
obj.display()
obj.salary()
obj.show_data()
import numpy as np
import matplotlib.pyplot as plt
from operationclass import IntArray

file_path = "company.txt"

def read_file():
    data = []
    with open(file_path, "r") as file:
        for line in file:
            numbers = line.strip().split(",")
            numbers = [int(x) for x in numbers]
            data.append(numbers)
    return np.array(data)

def company_total(index, data):
    return np.sum(data[index])

def best_company(data):
    best = 1
    highest = 0
    for i in range(len(data)):
        total = company_total(i, data)
        if total > highest:
            highest = total
            best = i + 1
    print("\nBest company:", best, "with", highest, "products")

def worst_company(data):
    worst = 1
    lowest = company_total(0, data)
    for i in range(len(data)):
        total = company_total(i, data)
        if total < lowest:
            lowest = total
            worst = i + 1
    print("Worst company:", worst, "with", lowest, "products")

def show_averages(data):
    for i in range(len(data)):
        print("Average of company", i + 1, ":", np.mean(data[i]))

    total_sum = 0
    count = 0
    for row in data:
        for val in row:
            total_sum += val
            count += 1
    print("Overall average:", total_sum / count)

def main():
    print("\nProgram started\n")

    data = read_file()
    print("Company Data:\n", data)

    first_company = IntArray(data[0])
    first_company.display()
    first_company.salary()
    first_company.show_data()

    best_company(data)
    worst_company(data)
    show_averages(data)

    print("\nProgram finished")

if __name__=="_main_":

 main()
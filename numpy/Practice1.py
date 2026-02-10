import numpy as np

salaries = np.array([50, 23, 60, 26, 19, 43, 26, 64, 60, 45, 26, 57, 54])

mean_salary = np.mean(salaries)
print(f"Average salary: {mean_salary}K$")

max_salary = np.max(salaries)
min_salary = np.min(salaries)

print(f"Max salary: {max_salary}K$")
print(f"Min salary: {min_salary}K$")

std_salary = np.std(salaries)
print(f"Standard deviation salary: {std_salary}")

above_mean = salaries[salaries > mean_salary]
print(f"Salaries Above Mean: {above_mean}")
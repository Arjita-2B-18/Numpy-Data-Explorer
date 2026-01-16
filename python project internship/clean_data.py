import numpy as np

rows = []

with open("company.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split(",")))
        rows.append(numbers)

# Find the maximum row length
max_len = max(len(r) for r in rows)

# Make all rows the same length
cleaned_data = []
for r in rows:
    r = r + [np.nan] * (max_len - len(r))
    cleaned_data.append(r)

data = np.array(cleaned_data, dtype=float)

# Save cleaned file
np.savetxt("company_cleaned.txt", data, delimiter=",", fmt="%.1f")

print("✅ Data cleaned successfully and saved as company_cleaned.txt")
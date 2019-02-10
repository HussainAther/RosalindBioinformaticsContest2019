import numpy as np
import sys

"""
Alex starts to grow a bee population. Since he cannot account for all the bees, he decides to count
the amount of the bees in kilograms! Each day the population of bees evolves. Initially, on the first
day, there were 𝑛1 kilograms of the bees. Suppose that at the i-th day the amount of bees is n_i kilograms
then on the next day the number of bees can be calculated by the following rule:

n_i = a*n - b*n^2
"""

def next_day_bees(a, b, n):
    if abs((a * n) - (b * (n**2)) - n) > 1e+150:
        return("inf")
    return ((a * n) - (b * (n**2)))

# Calculate the number of bees according to Alex's rule
# a and b are constraints. n is the current size.
def total_bees(a, b, n):
    for j in range(1,int(1e+6)):
        if next_day_bees(a, b, n) == "inf":
            return(-1)
        if next_day_bees(a, b, n) <= 0:
            if abs(next_day_bees(a, b, n) - n) <= .00001:
                return(round(n,4))
            return(0)
        if abs(next_day_bees(a, b, n) - n) <= .00001:
            return(round(n,4))
        n = next_day_bees(a, b, n)
    return(-1)

count = 0

n = []
a = []
b = []

# Read the input of n, a, and b
with open("/Users/syedather/Downloads/qual1input.txt", "r") as file:
    for line in file:
        if count > 0:
            n.append(float(line.split(" ")[0]))
            a.append(float(line.split(" ")[1]))
            b.append(float(line.split(" ")[2]))
        count += 1

output = []

for i in range(len(n)):
    output.append(total_bees(a[i], b[i], n[i]))

with open("/Users/syedather/Downloads/qual1output.txt", "w") as file:
    for sol in output:
        file.write(str(sol))
        file.write("\n")


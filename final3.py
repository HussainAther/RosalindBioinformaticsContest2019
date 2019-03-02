

"""
In this problem your task is to arrange bacterial communities in the order of the "evolutionary age".

To simulate the evolution process we generate bacterial communities one by one. Each bacterial community
represents a generation that was constructed from the previous generation using the rules described below.
Bacteria in each generation are represented as strings consisting of 20 nucleotides that can vary from one
generation to another.

Input in this problem is a sequence of generations 𝑆=𝑔0,𝑔1,…,𝑔|𝑆|−1. Elements of 𝑆 is a subset of all generations
created by an evolutionary process. Generations in 𝑆 are arranged in some random unknown order. Each 𝑔𝑖 is described
in the input by a set of strings representing some bacteria randomly taken from the generation 𝑔𝑖. As a result you
should provide an order in which bacterial communities from 𝑆 were generated.
"""
results = []
subresults = []

with open("input.txt", "r") as file
    for line in file:
        line = line.replace("\n", ""))
        if len(line) > 1 and subresults != []:
            results.append(subresults)
            subresults = []
            first = line.split(" ")[0]
            second = line.split(" ")[1]
            count = 0
            for i in range(len(first):
                if first[i] != second[i]
                count += 1
            subresults.append(count)

for subresult in results:
    for i in subresult:
        print(i),

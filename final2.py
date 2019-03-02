import numpy as np

"""
While having a constant nucleotide sequence DNA molecules in a cell can be chemically modified in a number of different
ways. For example, the DNA bases can be methylated, or histone proteins, around which DNA is wrapped, can be supplied
with chemical tags such as acetylation. It is thought that such modifications (or marks) define cell specialization
or a cell state when a certain combination of marks regulate how genes are expressed.

In this problem, you are given genomic tracks describing a presence or an absence of several epigenomic marks.
Your task is to split the genomic positions into a number of states so that each state corresponds to a particular
combination of marks.

Input format:
Each input file consists of multiple lines. The first line contains 𝑘, the number of states you can use. Remaining
𝑀 lines in the input file contain sequences of 0 and 1, describing the epigenomic marks. All sequences have the same length 𝐿.

Output format:
Your output file should contain only one line with 𝐿 numbers, ranging from 0 to 𝑘−1.
The 𝑖-th number should be equal to the state assigned to the 𝑖-th nucleotide.
"""

lists = []
count = 0
with open("input.txt", "r") as file:
    for line in input:
        if count > 0:
            sublist = []
            for state in line.replace("\n", ""):
                sublist.append(state)
            lists.append(sublist)
        count += 1

for i in range(len(lists)):
    

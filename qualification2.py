import sympy

"""
There is a circular genome of length 𝐿. You have a sequencing machine which reads a consecutive
subsequence of length exactly 𝑛 of this genome starting from a position chosen uniformly at random.
However, there is a problem: the machine makes errors -- each nucleotide is replaced with an incorrect
one with probability 𝑝.

You have a budget for 𝑘 reads. After the sequencing is done you count nucleotides read from each
genome position. After that for each genome position you decide which nucleotide is located at this
position in the genome by the following rules:

+ The desired nucleotide is the one with the largest number of occurrences at this position;
+ If there are several suitable nucleotides you choose one of them uniformly at randomly.

In particular, if a position has never been covered by a read, then every nucleotide occurred 0 times
at this position and a nucleotide is chosen uniformly at random.

You are given several tests. Each test is represented by the length of the genome 𝐿, the length of a
read 𝑛, the probability of an error 𝑝 and the total number of reads 𝑘. Find the expected number of
positions with incorrect nucleotides.
"""

count = 0
L = []
n = []
p = []
k = []


def product(l): # calculate the product of a list of numbers
    out = float(1)
    for a in l:
        out*=a
    return out

def prob_reads(L, n, p, k, i): # i is the number of reads overlapping the base
    p1 = (1 - p) * (n * k / L) # probability of knowing only a single base with one read overlapping that position.
    total_prob = 0
    for j in range(1, k+1): # for each proabability of knowing i number of bases with j reads overlapping
        x, y = sympy.symbols("x y")
        formula = (x + y) ** j
        total_prob += (p1**j)* formula.expand().replace("x", 1).replace("y", 1)/4 # the binomial expansion around that number of reads overlapping the number of bases
    return total_prob

def prob(L, n, p, k):
    probability = 0
    if n * k > L:
        upperlimit = L # upperlimit is the max number of bases we can know. It should equal the total coverage by the reads but not more than the length of the genome.
    else:
        upperlimit = n * k
    lowerlimit = n # lowerlimit is the least number of bases we can know. In this problem, it would be n because that implies each read covers the same positions in the genome.
    for i in range(lowerlimit, upperlimit+1): # test the probabilty of knowing each number of correct bases
        mistakes = (L - i) * (1 - p) # expected number of mistakes for i bases
        prob_base = prob_reads(L, n, p, k, i) # probability of knowing i number of bases
        probability += mistakes * prob_base
    return(probability)

# Read the input of n, a, and b
with open("/Users/syedather/Downloads/qual2input.txt", "r") as file:
    for line in file:
        if count > 0:
            L.append(int(line.split(" ")[0]))
            n.append(int(line.split(" ")[1]))
            p.append(float(line.split(" ")[2]))
            k.append(int(line.split(" ")[3]))
        count += 1

output = []

for i in range(len(n)):
    output.append(prob(L[i], n[i], p[i], k[i]))

for sol in output:
    print(sol)


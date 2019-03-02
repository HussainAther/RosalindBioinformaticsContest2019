

"""
You are given a list of proteins. Each protein is represented as a sequence of amino acids. You have to
find as short DNA sequence as possible from which all the proteins can be translated.

Input Generation
We artificially generated a linear DNA genome. Then a number of proteins were translated from that genome,
both from forward and reverse-complement strands. More precise description of input generation depends on
the version of the problem and is given in the corresponding tab.

Input Format:
The first line of the input contains 𝑛 − the number of proteins. Each of the next 𝑛 lines contains a protein
represented as a string of amino acids with the naming corresponding to standard genetic code −
https://en.wikipedia.org/wiki/Genetic_code.  Each protein starts with the start codon (M) and ends with the
stop codon ($). Stop codon can appear only at the end of the protein.

Output Format:
The first line of the output should contain the string of nucleotides (ACGT) which represents the genome
string from which all the provided proteins can be translated. The next 𝑛 lines should contain the
positions starting from which the corresponding protein can be translated and the direction of the translation.
Each position is specified with a 1-indexed coordinate on forward strand. The direction can either be forward ('+') or reverse ('-").
"""

aabank = {
    "F":"TTT",
    "F":"TTC",
    "L":"TTA",
    "L":"TTG",
    "S":"TCT",
    "S":"TCC",
    "S":"TCA",
    "S":"TCG",
    "T":"TAT",
    "T":"TAC",
    "$":"TAA",
    "$":"TAG",
    "C":"TGT",
    "C":"TGC",
    "$":"TGA",
    "W":"TGG",
    "L":"CTT",
    "L":"CTC",
    "L":"CTA",
    "L":"CTG",
    "P":"CCT",
    "P":"CCC",
    "P":"CCA",
    "P":"CCG",
    "H":"CAT",
    "H":"CAC",
    "Q":"CAA",
    "Q":"CAG",
    "R":"CGT",
    "R":"CGC",
    "R":"CGA",
    "R":"CGG",
    "I":"ATT",
    "I":"ATC",
    "I":"ATA",
    "M":"ATG",
    "T":"ACT",
    "T":"ACC",
    "T":"ACA",
    "T":"ACG",
    "N":"AAT",
    "N":"AAC",
    "K":"AAA",
    "K":"AAG",
    "S":"AGT",
    "S":"AGC",
    "R":"AGA",
    "R":"AGG",
    "V":"GTT",
    "V":"GTC",
    "V":"GTA",
    "V":"GTG",
    "A":"GCT",
    "A":"GCC",
    "A":"GCA",
    "A":"GCG",
    "D":"GAT",
    "D":"GAC",
    "E":"GAA",
    "E":"GAG",
    "G":"GGT",
    "G":"GGC",
    "G":"GGA",
    "G":"GGG"
}

proteins = []

with open("input.txt", "r") as file:
    count = 0
    for line in file:
        if count += 0:
            proteins.append(line.replace("\n", ""))
        count += 1

proteins = reverse(sorted(proteins, key=len))

dna = ""
reversedna = dna[::-1]

results = {}

for protein in proteins:
    aastring = ""
    for base in protein:
        aastring += aabank[base]
    if aastring.replace("$","") not in dna and aastring.replace("$", "") not in reversedna:
        


print(dna)
for result in results:
    print(str(results) + " " + str(results[result]))

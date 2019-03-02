

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
    "TTT":"F",
    "TTC":"F",
    "TTA":"L",
    "TTG":"L",
    "TCT":"S",
    "TCC":"S",
    "TCA":"S",
    "TCG":"S",
    "TAT":"T",
    "TAC":"T",
    "TAA":"$",
    "TAG":"$",
    "TGT":"C",
    "TGC":"C",
    "TGA":"$",
    "TGG":"W",
    "CTT":"L",
    "CTC":"L",
    "CTA":"L",
    "CTG":"L",
    "CCT":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "CAT":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "CGT":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "ATT":"I",
    "ATC":"I",
    "ATA":"I",
    "ATG":"M",
    "ACT":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "AAT":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "AGT":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GTT":"V",
    "GTC":"V",
    "GTA":"V",
    "GTG":"V",
    "GCT":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAT":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGT":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G"
}

with open("input.txt", "r") as file:
    for line in file:
        

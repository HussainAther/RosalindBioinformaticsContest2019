

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

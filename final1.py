import networkx as nx

"""
Cancer progression can be viewed as an accumulation of somatic mutations over the life of the cell, starting with a single cell with a
healthy reference genome, and ultimately resulting in a cancerous tumor, where genome structure is severely altered. For the sake of
simplicity, we can assume that the only changes that happen to the genome during cancer progression are large scale structural variations,
and we will omit the facts that tumors can be heterogeneous, and that the genomes in questions are not haploid. With this simplified
model in mind, we can try to solve the problem of reconstructing the sequential structure of derived chromosomes in cancer genomes.


We can not measure actual chromosomes directly, but given that mutated chromosomes in cancer genomes are derived from a known reference,
we are guaranteed that every derived chromosome basically determines a novel path/cycle of segments of the reference chromosomes.
There exist several methods that can provide the information of how often a given segment of the healthy reference is present in the observed
cancer genome, as well as what are the possible adjacencies between segments extremities as they appear along the derived chromosomes in question.

More formally, if we assume that a reference genome is comprised of 𝑚 segments that were rearranged throughout the somatic evolutionary process,
the derived cancer genome can be represented as a graph on 𝑛=2⋅𝑚 vertices (i.e., segments extremities), with 𝑚 undirected segment edges that do
not share common vertices (i.e., determine a perfect matching on the vertices), and 𝑘 undirected adjacency edges, that correspond to transitions
between segments extremities in the observed derived genome. Every edge also has a non-negative integer multiplicity, corresponding to the number
of times the respective segment/adjacency is present in the cancer genome in question. In this problem, we only consider graphs where a segment
edge cannot coincide (i.e., be parallel) with the adjacency edge.


You need to decompose edges of the graph into the set of paths and cycles, not necessarily simple, so that segment and adjacency edges in each path
or cycle alternate, and each path begins and ends with the segment edge. Each such path/cycle corresponds to a derived cancer genome chromosome,
and a decomposition determines the sequentialized chromosomal structure of the cancer genome in question. For each edge, the number of its occurrences
in paths and cycles should be equal to its multiplicity.

Easy version: You should output any decomposition.

Hard version: You should minimize the number of paths and cycles in your decomposition.

The test for both versions is the same. You can download it here: https://stepik.org/media/attachments/lesson/207045/tests.zip.
"""

# Adjacency matrix

count = 0
graph = {}
with open("input.txt","r") as file:
    for line in file:
        if count > 0:
            graph[(line.split(" ")[0])] = line.split(" ")[1] + " " + line.split(" ")[2]
        count += 1

new_graph = nx.Graph()
for source, targets in graph.iteritems():
    for inner_dict in targets:
        assert len(inner_dict) == 1
        new_graph.add_edge(int(source) - 1, int(inner_dict.keys()[0]) - 1,
                           weight=inner_dict.values()[0])
adjacency_matrix = nx.adjacency_matrix(new_graph)

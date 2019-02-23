
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


"""

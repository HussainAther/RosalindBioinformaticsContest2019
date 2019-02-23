"""
Somewhere in the middle of Russia there is a zoo with the last indivuduals of the E. sphaerica species: 𝑛 males and 𝑛 females.
The zookeepers try to preserve the species from extinction. They genotyped the last individuals and now want to match the males
and females to mate to get as genetically diverse offspring as possible. The E. sphaerica species are very monogamous animals,
so that one male animal can only mate with one female animal and vice versa. Your task is to help the zookepers.

You are given 2𝑛 phased genotypes (𝑛 males and 𝑛 females). E. sphaerica are diploid with maximum two different alleles represented
as 0 or 1 at each genomic position. Thus, the genotypes at a position may be 0/0, 0/1, 1/0 or 1/1 with the number before the slash
representing allele on the first chromosome in a pair of homologous chromosomes, and the number after the slash representing the
allele on the second chromosome in the pair. The genetic diversity is measured as a number of hetorozygous positions
(with 0/1 or 1/0 genotypes) in all the offspring individuals.The genetics of E. sphaerica perfectly obey the Haldane's recombination
model with recombination rate of 1 centimorgan per 1 million nucleotides. That means, that the recombination between two positions
on the same chromosome happens with probability 12(1−𝑒−2𝑑⋅10−8), where 𝑑 is the distance between the positions measured in nucleotides.
"""

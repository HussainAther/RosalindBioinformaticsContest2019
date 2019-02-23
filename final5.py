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

Input Format:
The first line of the input contains numbers 𝑘 and 𝑝 -- the number of chromosomes in the species and the number of polymorphic sites.

The next 𝑝 lines describe polymorphic sites. The 𝑖-th line of this block contains two integer numbers 𝑐ℎ𝑟𝑜𝑚𝑖 (chromosomes are numbered from 1 to 𝑘) and 𝑝𝑜𝑠𝑖 (𝑝𝑜𝑠𝑖>0).

The polymorphic sites description is followed by the line with an integer 𝑛 -- the number of male genotypes, also equal to the number of female genotypes.

Next follow 2𝑛 blocks of 𝑝 lines separated by an empty line. The first 𝑛 blocks describe male genotypes, the second 𝑛 blocks describe female genotypes.

The 𝑖-th line of a genotype block contains genotype at site 𝑝𝑖. It could be one of the following: 0/0, 0/1, 1/0, 1/1.
"""

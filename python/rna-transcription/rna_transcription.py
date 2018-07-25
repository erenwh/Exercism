def to_rna(dna_strand):
    my_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    ret = ""
    for c in dna_strand:
        ret += my_dict.get(c)
    return ret

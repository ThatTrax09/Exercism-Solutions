def to_rna(dna_strand):
    if dna_strand == '':
        return dna_strand
    complement = {'C' : 'G', 'G' : 'C', 'A' : 'U', 'T' : 'A'}
    return ''.join([complement[nucleotide] for nucleotide in dna_strand])
        
    

import collections
from collections import Counter
from basic_data import * 


def validateSeq(dna_seq):
    """Validates a DNA sequence to ensure it contains only valid nucleotides."""
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq 


def countNucFreq1(seq1):
    """Counts the frequency of nucleotides in a sequence."""
    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq1:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
#OR
def countNucFreq2(seq2):
    """Counts the frequency of nucleotides in a sequence using collections.Counter."""
    return dict(collections.Counter(seq2))


def transcription(seq1):
    """Transcribes a DNA sequence into an RNA sequence by replacing T with U."""
    return seq1.replace("T","U")


def complement(seq1):
    """Returns the complement of a DNA sequence."""
    return ''.join([Complement[nuc] for nuc in seq1])


def revcomplement1(seq1):
    """Returns the reverse complement of a DNA sequence."""
    return ''.join([Complement[nuc] for nuc in seq1])[::-1]  # -1 reverses the string
#OR
def revcomplement2(seq2):
    """Returns the reverse complement of a DNA sequence using pythonic approach."""
    mapping = str.maketrans("ACGT", "TGCA")
    return seq2.translate(mapping)[::-1]  # Translate and reverse the string


def gc_content1(seq1):
    """Calculates the GC content of a DNA sequence."""
    gc_count = seq1.count('G') + seq1.count('C')
    return round((gc_count / len(seq1)) * 100 ) if len(seq1) > 0 else 0.0
#OR
def gc_content2(seq2): 
    """Calculates the GC content of a DNA sequence."""
    return round((seq2.count('G') + seq2.count('C')) / len(seq2) * 100)


def gc_subset(seq2, k=20):
    """Calculates the GC content of every k-length subset of a DNA sequence."""
    res = []
    for i in range(0, len(seq2) - k + 1, k):
        subseq = seq2[i:i + k]
        res.append(gc_content2(subseq))
    return res


def translate_seq(seq, in_pos=0):
    """Translates a DNA sequence into an amino acid sequence starting from a given position."""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(in_pos, len(seq)-2, 3)]


def codon_freq(seq, aminoacid):
    """Counts the frequency of a specific amino acid in a DNA sequence."""
    tmpList = []
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        if DNA_Codons[codon] == aminoacid:
             tmpList.append(codon)

    freqDict = dict(Counter(tmpList))
    totalcount = sum(freqDict.values())
    if totalcount == 0:
        return {}
    for codon in freqDict:
        freqDict[codon] = round(freqDict[codon] / totalcount, 2)
    return freqDict   
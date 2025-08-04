# DNA Toolkit

This is a simple Python-based DNA Toolkit that I built as part of my learning in bioinformatics and programming. It includes functions for validating DNA sequences, transcribing them to RNA, finding complements, calculating GC content, and translating DNA into proteins.

## Function Overview

### Validation & Frequency

- validateSeq(seq)  
  Validates a DNA sequence using defined nucleotides.

- countNucFreq1(seq)  
  Manual nucleotide count using a dictionary.

- countNucFreq2(seq)  
  Nucleotide frequency using collections.Counter.

---

### Transcription & Complements

- transcription(seq)  
  Converts DNA to RNA by replacing T with U.

- complement(seq)  
  Returns the complementary DNA strand.

- revcomplement1(seq)  
  Reverse complement using list comprehension.

- revcomplement2(seq)  
  Reverse complement using str.translate and slicing.

---

### GC Content

- gc_content1(seq)  
  Calculates GC content manually.

- gc_content2(seq)  
  Shorter version for GC content calculation.

- gc_subset(seq, k=20)  
  Calculates GC content in k-length windows across the sequence.

---

### Translation

- translate_seq(seq, in_pos=0)  
  Translates DNA sequence into amin

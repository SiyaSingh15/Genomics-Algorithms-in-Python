{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting nbimporter\n",
      "  Downloading nbimporter-0.3.4-py3-none-any.whl (4.9 kB)\n",
      "Installing collected packages: nbimporter\n",
      "Successfully installed nbimporter-0.3.4\n",
      "\u001b[33mWARNING: You are using pip version 21.2.4; however, version 24.0 is available.\n",
      "You should consider upgrading via the '/opt/conda/bin/python3 -m pip install --upgrade pip' command.\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!pip install nbimporter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nbimporter\n",
    "from basic_data import *\n",
    "import collections\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def validateSeq(dna_seq):\n",
    "    \"\"\"Validates a DNA sequence to ensure it contains only valid nucleotides.\"\"\"\n",
    "    tmpseq = dna_seq.upper()\n",
    "    for nuc in tmpseq:\n",
    "        if nuc not in Nucleotides:\n",
    "            return False\n",
    "    return tmpseq "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def countNucFreq1(seq1):\n",
    "    \"\"\"Counts the frequency of nucleotides in a sequence.\"\"\"\n",
    "    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}\n",
    "    for nuc in seq1:\n",
    "        tmpFreqDict[nuc] += 1\n",
    "    return tmpFreqDict\n",
    "#OR\n",
    "def countNucFreq2(seq2):\n",
    "    \"\"\"Counts the frequency of nucleotides in a sequence using collections.Counter.\"\"\"\n",
    "    return dict(collections.Counter(seq2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def transcription(seq1):\n",
    "    \"\"\"Transcribes a DNA sequence into an RNA sequence by replacing T with U.\"\"\"\n",
    "    return seq1.replace(\"T\",\"U\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def complement(seq1):\n",
    "    \"\"\"Returns the complement of a DNA sequence.\"\"\"\n",
    "    return ''.join([Complement[nuc] for nuc in seq1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def revcomplement1(seq1):\n",
    "    \"\"\"Returns the reverse complement of a DNA sequence.\"\"\"\n",
    "    return ''.join([Complement[nuc] for nuc in seq1])[::-1]  # -1 reverses the string\n",
    "#OR\n",
    "def revcomplement2(seq2):\n",
    "    \"\"\"Returns the reverse complement of a DNA sequence using pythonic approach.\"\"\"\n",
    "    mapping = str.maketrans(\"ACGT\", \"TGCA\")\n",
    "    return seq2.translate(mapping)[::-1]  # Translate and reverse the string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gc_content1(seq1):\n",
    "    \"\"\"Calculates the GC content of a DNA sequence.\"\"\"\n",
    "    gc_count = seq1.count('G') + seq1.count('C')\n",
    "    return round((gc_count / len(seq1)) * 100 ) if len(seq1) > 0 else 0.0\n",
    "#OR\n",
    "def gc_content2(seq2): \n",
    "    \"\"\"Calculates the GC content of a DNA sequence.\"\"\"\n",
    "    return round((seq2.count('G') + seq2.count('C')) / len(seq2) * 100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gc_subset(seq2, k=20):\n",
    "    \"\"\"Calculates the GC content of every k-length subset of a DNA sequence.\"\"\"\n",
    "    res = []\n",
    "    for i in range(0, len(seq2) - k + 1, k):\n",
    "        subseq = seq2[i:i + k]\n",
    "        res.append(gc_content2(subseq))\n",
    "    return res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "def translate_seq(seq, in_pos=0):\n",
    "    \"\"\"Translates a DNA sequence into an amino acid sequence starting from a given position.\"\"\"\n",
    "    return [DNA_Codons[seq[pos:pos+3]] for pos in range(in_pos, len(seq)-2, 3)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def codon_freq(seq, aminoacid):\n",
    "    \"\"\"Counts the frequency of a specific amino acid in a DNA sequence.\"\"\"\n",
    "    tmpList = []\n",
    "    for i in range(0, len(seq)-2, 3):\n",
    "        codon = seq[i:i+3]\n",
    "        if DNA_Codons[codon] == aminoacid:\n",
    "             tmpList.append(codon)\n",
    "\n",
    "    freqDict = dict(Counter(tmpList))\n",
    "    totalcount = sum(freqDict.values())\n",
    "    if totalcount == 0:\n",
    "        return {}\n",
    "    for codon in freqDict:\n",
    "        freqDict[codon] = round(freqDict[codon] / totalcount, 2)\n",
    "    return freqDict   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

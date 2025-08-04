def colored(seq):
    """Returns a colored representation of a DNA sequence."""
    bcolors = {
        'A': '\033[92m',  # Green 
        'C': '\033[94m',  # Blue 
        'G': '\033[93m',  # Yellow
        'T': '\033[91m',  # Red
        'U': '\033[91m',  # Red for RNA
        'reset': '\033[0;0m'  # Reset color 
    }
    tmpStr = "" 
    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc
    return tmpStr + '\033[0;0m'  # Reset color at the end


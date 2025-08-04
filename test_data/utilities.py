{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def colored(seq):\n",
    "    \"\"\"Returns a colored representation of a DNA sequence.\"\"\"\n",
    "    bcolors = {\n",
    "        'A': '\\033[92m',  # Green \n",
    "        'C': '\\033[94m',  # Blue \n",
    "        'G': '\\033[93m',  # Yellow\n",
    "        'T': '\\033[91m',  # Red\n",
    "        'U': '\\033[91m',  # Red for RNA\n",
    "        'reset': '\\033[0;0m'  # Reset color \n",
    "    }\n",
    "    tmpStr = \"\" \n",
    "    for nuc in seq:\n",
    "        if nuc in bcolors:\n",
    "            tmpStr += bcolors[nuc] + nuc\n",
    "        else:\n",
    "            tmpStr += bcolors['reset'] + nuc\n",
    "    return tmpStr + '\\033[0;0m'  # Reset color at the end"
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

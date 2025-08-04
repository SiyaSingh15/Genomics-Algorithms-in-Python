{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Nucleotides = [\"A\", \"C\", \"G\", \"T\"]\n",
    "Complement = {\"A\": \"T\", \"C\": \"G\", \"G\": \"C\", \"T\": \"A\"}\n",
    "\n",
    "DNA_Codons = {\n",
    "    # 'M' - START, '_' - STOP\n",
    "    \"GCT\": \"A\", \"GCC\": \"A\", \"GCA\": \"A\", \"GCG\": \"A\",\n",
    "    \"TGT\": \"C\", \"TGC\": \"C\",\n",
    "    \"GAT\": \"D\", \"GAC\": \"D\",\n",
    "    \"GAA\": \"E\", \"GAG\": \"E\",\n",
    "    \"TTT\": \"F\", \"TTC\": \"F\",\n",
    "    \"GGT\": \"G\", \"GGC\": \"G\", \"GGA\": \"G\", \"GGG\": \"G\",\n",
    "    \"CAT\": \"H\", \"CAC\": \"H\",\n",
    "    \"ATA\": \"I\", \"ATT\": \"I\", \"ATC\": \"I\",\n",
    "    \"AAA\": \"K\", \"AAG\": \"K\",\n",
    "    \"TTA\": \"L\", \"TTG\": \"L\", \"CTT\": \"L\", \"CTC\": \"L\", \"CTA\": \"L\", \"CTG\": \"L\",\n",
    "    \"ATG\": \"M\",\n",
    "    \"AAT\": \"N\", \"AAC\": \"N\",\n",
    "    \"CCT\": \"P\", \"CCC\": \"P\", \"CCA\": \"P\", \"CCG\": \"P\",\n",
    "    \"CAA\": \"Q\", \"CAG\": \"Q\",\n",
    "    \"CGT\": \"R\", \"CGC\": \"R\", \"CGA\": \"R\", \"CGG\": \"R\", \"AGA\": \"R\", \"AGG\": \"R\",\n",
    "    \"TCT\": \"S\", \"TCC\": \"S\", \"TCA\": \"S\", \"TCG\": \"S\", \"AGT\": \"S\", \"AGC\": \"S\",\n",
    "    \"ACT\": \"T\", \"ACC\": \"T\", \"ACA\": \"T\", \"ACG\": \"T\",\n",
    "    \"GTT\": \"V\", \"GTC\": \"V\", \"GTA\": \"V\", \"GTG\": \"V\",\n",
    "    \"TGG\": \"W\",\n",
    "    \"TAT\": \"Y\", \"TAC\": \"Y\",\n",
    "    \"TAA\": \"_\", \"TAG\": \"_\", \"TGA\": \"_\"\n",
    "}"
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

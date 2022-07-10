import random
import json

def parse_file(path):
  proteins = []
  with open(path) as f:
    lines = f.readlines()
  protein = ''
  info = ''
  for line in lines:
    if line.startswith('>'):
      if protein:
        proteins.append((info, protein))

      info = line.rstrip("\n").strip("")
      protein = ''
    else:
      protein += line.strip("")
  if protein:
    proteins.append((info, protein))
  return proteins

def save_data(path, data):
  with open(path, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)

def proteins2nucleotides(proteins):
  AA2NA = {
      "A": list("GCT,GCC,GCA,GCG".split(",")),
      "R": list("CGT,CGC,CGA,CGG,AGA,AGG".split(",")),
      "N": list("AAT,AAC".split(",")),
      "D": list("GAT,GAC".split(",")),
      "C": list("TGT,TGC".split(",")),
      "Q": list("CAA,CAG".split(",")),
      "E": list("GAA,GAG".split(",")),
      "G": list("GGT,GGC,GGA,GGG".split(",")),
      "H": list("CAT,CAC".split(",")),
      "I": list("ATT,ATC,ATA".split(",")),
      "L": list("TTA,TTG,CTT,CTC,CTA,CTG".split(",")),
      "K": list("AAA,AAG".split(",")),
      "M": list("ATG".split(",")),
      "F": list("TTT,TTC".split(",")),
      "P": list("CCT,CCC,CCA,CCG".split(",")),
      "S": list("TCT,TCC,TCA,TCG,AGT,AGC".split(",")),
      "T": list("ACT,ACC,ACA,ACG".split(",")),
      "W": list("TGG".split(",")),
      "Y": list("TAT,TAC".split(",")),
      "V": list("GTT,GTC,GTA,GTG".split(",")),
      "*": list("TAA,TGA,TAG".split(","))
}

  nucleotides = list(map(lambda protein: random.choice(AA2NA.get(protein, ["---"])), proteins))
  return nucleotides

def convert_data(proteins_blocks):
  nucleotides = {}

  for block in proteins_blocks:
    nucleotides[block[0]] = "".join(proteins2nucleotides(block[1]))
  return nucleotides

proteins_blocks = parse_file('sample.faa')
pattern_nucleotides = convert_data(proteins_blocks)
save_data('output.json', pattern_nucleotides)

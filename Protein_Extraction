import re
import json

def find_proteins(proteins, pat_combined):
  result = []
  counter = 0
  for protein in proteins:
    if re.search(pat_combined, protein):
      counter +=1
      result.append(protein)
      if counter == 5:
        break;
  return result

protein_file = 'swissprot_sample.fas'
pattern_file = 'prosite_sample.dat'
result_file = 'results.json'

proteins = []

with open(protein_file) as f:
  lines = f.readlines()
  protein = ''
  for line in lines:
    if line.startswith('>'):
      if protein:
        proteins.append(protein)
      protein = line.rstrip("\n").strip("")
    else:
      protein += line.rstrip("\n").strip("")

pattern_proteins = {}

with open(pattern_file) as f:
  lines = f.readlines()
  for line in lines:
    if not line.startswith('PA'):
      continue

    pattern = line.split(" ")[1].strip().replace('-', '').replace('.', ' ').strip()
    pat1 = re.compile(r"N[^P][ST][^P]")
    pat2 = re.compile(r"SG[A-Z]G")
    pat3 = re.compile(r"[RK]{2}[A-Z][ST]")
    pat4 = re.compile(r"[ST][A-Z][RK]")
    pat5 = re.compile(r"[ST][A-Z]{2}[DE]")
    pat6 = re.compile(r"[RK][A-Z]{2,3}[DE][A-Z]{2,3}Y")
    pat7 = re.compile(r"G[^EDRKHPFYW][A-Z]{2}[STAGCN][^P]")
    pat8 = re.compile(r"[A-Z]G[RK][RK]")
    pat9 = re.compile(r"C[A-Z][DN][A-Z]{4}[FY][A-Z]C[A-Z]C")
    pat10 = re.compile(r"[A-Z]{12}E[A-Z]{3}E[A-Z]C[A-Z]{6}[DEN][A-Z][LIVMFY][A-Z]{9}[FYW]")
    pat11 = re.compile(r"[DEQGSTALMKRH][LIVMFYSTAC][GNQ][LIVMFYAG][DNEKHS]S[LIVMST][^PCFY][STAGCPQLIVMF][LIVMATN][DENQGTAKRHLM][LIVMWSTA][LIVGSTACR][A-Z]{2}[LIVMFA]")
    
    pat_list = [pat1, pat2, pat3, pat4, pat5, pat6, pat7, pat8, pat9, pat10, pat11]

    for pat in pat_list:
      pattern_proteins[pat.pattern] = find_proteins(proteins, pat.pattern)

with open(result_file, 'w') as fp:
  json.dump(pattern_proteins, fp, sort_keys=True, indent=4)

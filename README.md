# Bioinformatics

1. With the swissprot_sample.fas file
[this Python program](./Protein_Extraction.py) extracts the proteins containing the input patterns in
the prosite_sample.dat file. For each pattern the program
prints out up to 5 proteins from the swissprot_sample.fas. Outputs are dumped in a .csv file.

2. [This Python program](./Proteins2Nucleotides.py) reads the sample.faa file and converts the amino
acid symbols into nucleotide symbols, I. e, Val to GTG. Results are dumped in a .csv file.

# Sample entry in swisprot.fas:

>108_LYCES (Q43495) Protein 108 precursor.
MASVKSSSSSSSSSFISLLLLILLVIVLQSQVIECQPQQSCTASLTGLNVCAPFLVPGSP
TASTECCNAVQSINHDCMCNTMRIAAQIPAQCNLPPLSCSAN
>10KD_VIGUN (P18646) 10 kDa protein precursor (Clone PSAS10).
MEKKSIAGLCFLFLVLFVAQEVVVQSEAKTCENLVDTYRGPCFTTGSCDDHCKNKEHLLS
GRCRDDVRCWCTRNC
>110K_PLAKN (P13813) 110 kDa antigen (PK110) (Fragment).
FNSNMLRGSVCEEDVSLMTSIDNMIEEIDFYEKEIYKGSHSGGVIKGMDYDLEDDENDED
EMTEQMVEEVADHITQDMIDEVAHHVLDNITHDMAHMEEIVHGLSGDVTQIKEIVQKVNV
AVEKVKHIVETEETQKTVEPEQIEETQNTVEPEQTEETQKTVEPEQTEETQNTVEPEQIE
ETQKTVEPEQTEEAQKTVEPEQTEETQKTVEPEQTEETQKTVEPEQTEETQKTVEPEQT
EETQKTVEPEQTEETQKTVEPEQTEETQKTVEPEQTEETQNTVEPEPTQETQNTVEP

# Sample entry in prosite.dat:

ID ASN_GLYCOSYLATION; PATTERN.
AC PS00001;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE N-glycosylation site.
PA N-{P}-[ST]-{P}.
CC /TAXO-RANGE=??E?V;
CC /SITE=1,carbohydrate;
CC /SKIP-FLAG=TRUE;
DO PDOC00001;
//
ID GLYCOSAMINOGLYCAN; RULE.
AC PS00002;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE Glycosaminoglycan attachment site.
PA S-G-x-G.
RU Additional rules:
RU There must be at least two acidic amino acids (Glu or Asp) from -2 to
RU -4 relative to the serine.
CC /TAXO-RANGE=??E??;
CC /SITE=1,glycosaminoglycan;
CC /SKIP-FLAG=TRUE;
DO PDOC00002;
//
ID SULFATION; RULE.
AC PS00003;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE Tyrosine sulfation site.
RU (1) Glu or Asp within two residues of the tyrosine (typically at -1).
RU (2) At least three acidic residues from -5 to +5.
RU (3) No more than 1 basic residue and 3 hydrophobic from -5 to +5
RU (4) At least one Pro or Gly from -7 to -2 and from +1 to +7 or at least
RU two or three Asp, Ser or Asn from -7 to +7.
RU (5) Absence of disulfide-bonded cysteine residues from -7 to +7.
RU (6) Absence of N-linked glycans near the tyrosine.
CC /TAXO-RANGE=??E??;
CC /SKIP-FLAG=TRUE;

DO PDOC00003;
//
ID CAMP_PHOSPHO_SITE; PATTERN.
AC PS00004;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE cAMP- and cGMP-dependent protein kinase phosphorylation site.
PA [RK](2)-x-[ST].
CC /TAXO-RANGE=??E?V;
CC /SITE=3,phosphorylation;
CC /SKIP-FLAG=TRUE;
DO PDOC00004;
//
ID PKC_PHOSPHO_SITE; PATTERN.
AC PS00005;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE Protein kinase C phosphorylation site.
PA [ST]-x-[RK].
CC /TAXO-RANGE=??E??;
CC /SITE=1,phosphorylation;
CC /SKIP-FLAG=TRUE;
DO PDOC00005;
//
ID CK2_PHOSPHO_SITE; PATTERN.
AC PS00006;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE Casein kinase II phosphorylation site.
PA [ST]-x(2)-[DE].
CC /TAXO-RANGE=??E??;
CC /SITE=1,phosphorylation;
CC /SKIP-FLAG=TRUE;
DO PDOC00006;
//
ID TYR_PHOSPHO_SITE; PATTERN.
AC PS00007;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE Tyrosine kinase phosphorylation site.
PA [RK]-x(2,3)-[DE]-x(2,3)-Y.

CC /TAXO-RANGE=??E?V;
CC /SITE=5,phosphorylation;
CC /SKIP-FLAG=TRUE;
DO PDOC00007;
//
ID MYRISTYL; PATTERN.
AC PS00008;
DT APR-1990 (CREATED); APR-1990 (DATA UPDATE); APR-1990 (INFO
UPDATE).
DE N-myristoylation site.
PA G-{EDRKHPFYW}-x(2)-[STAGCN]-{P}.
CC /TAXO-RANGE=??E?V;
CC /SITE=1,myristyl;
CC /SKIP-FLAG=TRUE;
DO PDOC00008;
//

NC_008702.gbk file
LOCUS NC_008702 4376040 bp DNA circular BCT
22-DEC-2006
DEFINITION Azoarcus sp. BH72, complete genome.
ACCESSION NC_008702
VERSION NC_008702.1 GI:119896292
KEYWORDS complete genome.
SOURCE Azoarcus sp. BH72
ORGANISM Azoarcus sp. BH72
Bacteria; Proteobacteria; Betaproteobacteria; Rhodocyclales;
Rhodocyclaceae; Azoarcus.
REFERENCE 1 (bases 1 to 4376040)
AUTHORS Krause,A., Ramakumar,A., Bartels,D., Battistoni,F., Bekel,T., Boch,J., Bohm,M., Friedrich,F., Hurek,T., Krause,L., Linke,B., McHardy,A.C., Sarkar,A., Schneiker,S., Syed,A.A., Thauer,R., Vorholter,F.J., Weidner,S., Puhler,A., Reinhold-Hurek,B., Kaiser,O. and Goesmann,A. TITLE Complete genome of the mutualistic, N2-fixing grass endophyte
Azoarcus sp. strain BH72
JOURNAL Nat. Biotechnol. 24 (11), 1385-1391 (2006)
PUBMED 17057704
REFERENCE 2 (bases 1 to 4376040)
CONSRTM NCBI Genome Project
TITLE Direct Submission
JOURNAL Submitted (22-DEC-2006) National Center for Biotechnology
Information, NIH, Bethesda, MD 20894, USA
REFERENCE 3 (bases 1 to 4376040)
AUTHORS Reinhold-Hurek,B. and Krause,A. TITLE Direct Submission
JOURNAL Submitted (19-SEP-2006) Reinhold-Hurek B., Krause A., University
of
Bremen, General Microbiology, PO. Box 33 04 40, D-28334 Bremen, GERMANY
COMMENT PROVISIONAL REFSEQ: This record has not yet been subject to
final NCBI review. The reference sequence was derived from AM406670. COMPLETENESS: full length.
FEATURES Location/Qualifiers
source 1..4376040
/organism="Azoarcus sp. BH72"

/mol_type="genomic DNA"
/strain="BH72"
/db_xref="taxon:62928"
gene 1..1443
/gene="dnaA"
/locus_tag="azo0001"
CDS 1..1443
/gene="dnaA"
/locus_tag="azo0001"
/function="ATPase involved in DNA replication initiation"
/note="Chromosomal replication initiator protein dnaA. Plays an important role in the initiation and regulation
of chromosomal replication. Binds to the origin of
replication; it binds specifically double-stranded DNA at
a 9 bp consensus (dnaA box): 5-TTATC(C/A)A(C/A)A-3. DnaA
binds to ATP and to acidic phospholipids (By similarity). InterPro: Bacterial chromosomal replication initiator
protein DnaA
High confidence in function and specificity"
/codon_start=1
/transl_table=11
/product="chromosomal replication initiator protein"
/protein_id="YP_931506.1"
/db_xref="GI:119896293"
/translation="MNQDFWPFCLARLEQELPQQQFNTWIKTLQAAESDADGAVALTL
TAPNRFVLQWVRERYMRRIGELGEEFHGQPIQLELQLPVAGAKSAPVAPARVRPAGAN
GGAAANSPMAPPVSEAAPPQIIVRPSEPEPVSANELAYDKTRLNADFTFDTLVTGRAN
DLARAAAMQVAQNPGTSYNPLFVYGGVGLGKTHLVHAIGNAVYRHNPRMVIRYVHVED
YYADVVRAYQQKSFDAFKRYYRSLDMLIIDDIQFFNNKNRTQEEFFHAFNALTEAKKQ
IVITCDTYPKDIQGLEDRLISRFDWGLTVQIEPPELEMRVAILQKKAEALRVSVDDDV
AFLIAKNLRSNVRELEGALNKVVAYARFHGRGISLEVAKEALKDLLHAHNRQLSIEHI QKTVADYYKIKVADMHSKKRTRVIARPRQVAMWLAKELTPMSLPAIGEAFGGRDHTTV
LHACRTITELRLGDHQLNHDVHVLTQVLRG"

gene 1502..2611
/gene="dnaN"
/locus_tag="azo0002"
CDS 1502..2611
/gene="dnaN"
/locus_tag="azo0002"
/EC_number="2.7.7.7"
/function="DNA polymerase sliding clamp subunit (PCNA
homolog)"
/note="DNA polymerase III beta chain (EC 2.7.7.7). DNA
polymerase III is a complex multichain enzyme responsible
for most of the replicative synthesis in bacteria. This
DNA polymerase also exhibits 3 to 5 exonuclease activity. The beta chain is required for initiation of replication
once it is clamped onto DNA It slides freely
(bidirectional and ATP- independent) along duplex DNA (By
similarity). InterPro: DNA polymerase III beta chain dnan:
DNA polymerase III beta subunit
High confidence in function and specificity"
/codon_start=1
/transl_table=11
/product="DNA-directed DNA polymerase"
/protein_id="YP_931507.1"
/db_xref="GI:119896294"
/translation="MLLLNTTRDALLAPLQSVAGIVEKRHTLPILSNVLIEKRGDQLT
LLATDIEIQIRTTTAGHIGGEDSSITVGARKLQDILRALSDSVDIVLTLEDKRLTVKA
GKSRFQLQTLPAADYPRMNLPDGDAVRFSVPQRAFKRQLAQVSYSMAQQDIRYYLNGL
LLIADGSELRMVATDGHRLAYAAGDLAVPVQARTEAILPRKTVLELARQLADTDDPLE
IILAGNQAVFRFGSIELVTKLIDGKFPDYERVIPQNHPRMVTFDRQPLLASLQRAAIL
TNEKFRGVRMVLGEGALKIISSNTEQEEAQEELEIDYHDTPLDIGFNVTYLLDVLNNL
SSEQVEWRFNDGNSSALVTLPGNDKFKYVVMPMRI"

NC_008702.ptt file
Azoarcus sp. BH72, complete genome - 1..4376040
3989 proteins
Location Strand Length PID Gene Synonym Code COG Product
1..1443 + 480 119896293 dnaA azo0001 - - chromosomal replication initiator protein
1502..2611 + 369 119896294 dnaN azo0002 - - DNA-directed DNA polymerase
2821..5310 + 829 119896295 gyrB azo0003 - -

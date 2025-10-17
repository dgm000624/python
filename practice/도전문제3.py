# dna = "ctacaatgtcagtatacccattgcattagccgg"

dna = input("염기 서열을 입력")

codon_list = []
codon_dict = {}
for i in range(0, len(dna), 3) :
    codon_list.append(dna[i:i+3])
print(codon_list)

for(offset, codon_dna) in enumerate(codon_list) :
    if (len(codon_list[offset])) != 3:
        continue
    else :
        codon_dict[codon_dna] = codon_list.count(codon_list[offset])

print(codon_dict)

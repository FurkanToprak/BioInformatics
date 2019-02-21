# Author: Furkan Toprak
# Center for Phage Technology
# Date: 2/17/2019
# TableClassifer.py Version 1.0

def write_down(l):
    ret = ""
    for a in l:
        ret += a.lstrip() + "\n"
    return ret


with open("OM_bugs.csv", "r", encoding='utf-8-sig') as bugs:
    bugs = bugs.read()
    bugs = bugs.split("\n")
    for i in range(0, len(bugs)):
        bugs[i] = ''.join(x for x in bugs[i] if x.isalpha())
    for i in reversed(range(0, len(bugs))):
        if bugs[i] == "":
            del bugs[i]
    with open('ncbi_phages.tsv', 'r') as bact:
        bact = bact.read().split("\n")
        pos_genus = []
        neg_genus = []
        for i in range(2, len(bact)):
            bact_genus = bact[i].split("\t")[0].split(" ")[0]
            if bact_genus in bugs:
                neg_genus.append(bact[i].split("\t")[0])
            else:
                pos_genus.append(bact[i].split("\t")[0])
        output = open("sorted_table.txt", "w")
        output.write("Gram +:\n\n")
        output.write(write_down(pos_genus))
        output.write("\n\n\nGram -:\n\n")
        output.write(write_down(neg_genus))
        output.close()

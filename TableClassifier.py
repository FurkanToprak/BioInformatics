# Author: Furkan Toprak
# Center for Phage Technology
# Date: 2/17/2019
# TableClassifer.py Version 1.0

def write_down(l):
    ret = ""
    for a in l:
        ret += a.lstrip() + "\n"
    return ret

data_file = open("Gram_stains.txt", "r")
data = data_file.read().split("\n")
pos_genus = data[data.index("Gram + Genera:") + 1: data.index("Gram + Species:")]
pos_species = data[data.index("Gram + Species:") + 1: data.index("Gram - Genera:")]
neg_genus = data[data.index("Gram - Genera:") + 1: data.index("Gram - Species:")]
neg_species = data[data.index("Gram - Species:") + 1:]
data_file.close()
pos_include_file = open("include_positive.txt", "r")
pos_include = pos_include_file.read().split("\n")
pos_include_file.close()
neg_include_file = open("include_negative.txt", "r")
neg_include = neg_include_file.read().split("\n")
neg_include_file.close()
phages_file = open("ncbi_phages.tsv", "r")
phage = phages_file.read().split("\n")[2:]
pos_bugs = []
neg_bugs = []
unknown_bugs = []
for i in phage:
    if i.split("\t")[0].split(" ")[0] in pos_genus or i.split("\t")[0].split(" ")[0] in pos_species or\
            i.split("\t")[0] in pos_include or i.split("\t")[0].split(" ")[0] in pos_include:
        pos_bugs.append(i.split("\t")[0])
    elif i.split("\t")[0].split(" ")[0] in neg_genus or i.split("\t")[0].split(" ")[0] in neg_species or\
            i.split("\t")[0] in neg_include or i.split("\t")[0].split(" ")[0] in neg_include:
        neg_bugs.append(i.split("\t")[0])
    else: unknown_bugs.append(i.split("\t")[0])
phages_file.close()
output_file = open("sorted_table.txt", "w")
output_file.write("Unknown:\n")
output_file.write(write_down(unknown_bugs))
output_file.write("\nGram +:\n")
output_file.write(write_down(pos_bugs))
output_file.write("\nGram -:\n")
output_file.write(write_down(neg_bugs))
output_file.close()
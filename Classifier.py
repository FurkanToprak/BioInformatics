# Author: Furkan Toprak
# Center for Phage Technology
# Date: 11/9/2018
# Classifer.py Version 1.0

with open('BacteriaList.txt', 'r') as bact:
    # The following is an inefficient way to classify Species of Bacteria by Gram stain.
    # Note to self: Genera lists are duplicate; 2 exist for formatting reasons.
    # Combine Taxonomic lists to form hierarchy.
    bact = bact.read()
    bact = bact.split("\n")
    phylum = []
    class_ = []
    order = []
    family = []
    genus = []
    genus_2 = []
    species = []
    embedded_s_g = []
    for i in range(0, len(bact)):
        periods = len(bact[i].split("."))
        if periods == 2:
            phylum.append(bact[i])
        elif periods == 3:
            class_.append(bact[i])
        elif periods == 4:
            order.append(bact[i])
        elif periods == 5:
            family.append(bact[i])
        elif periods == 6:
            genus.append(bact[i])
            temp = []
            temp.append(bact[i])
            genus_2.append(temp)
        elif periods == 7:
            species.append(bact[i])
            genus_2[-1].append(bact[i])

    def formatter(list_temp):
        list_temp2 = list_temp
        '''Removes numbers and special characters from strings in a list'''
        for i in range(0, len(list_temp)):
            list_temp2[i] = ''.join(j for j in list_temp2[i] if j.isalpha())
        return list_temp2

    for i in range(len(genus)):
        genus_2[i] = formatter(genus_2[i])
    #print(genus_2) # 0th index of each sublist is the genus. Following are species.
    species_num = 0
    for i in species:
        species_num += int(i.split("(")[1].split(")")[0])

    print("There are", species_num, "species.")
    # print("Phyla:", formatter(phylum))
    # print("Classes:", formatter(class_))
    # print("Orders:", formatter(order))
    # print("Families:", formatter(family))
    # print("Genera", formatter(genus))
    # print("Species:", formatter(species))

    with open("OM_bugs.csv", "r", encoding='utf-8-sig') as bugs:
        bugs = bugs.read()
        bugs = bugs.split("\n")
        for i in range(0, len(bugs)):
            bugs[i] = ''.join(x for x in bugs[i] if x.isalpha())
        for i in reversed(range(0, len(bugs))):
            if bugs[i] == "":
                del bugs[i]
        # print(bugs)

        with open("Gram_stains.txt", "w") as gram_file:
            pos_genus = []
            neg_genus = []
            for i in range(len(formatter(genus))):
                if genus[i] in bugs:
                    neg_genus.append(genus[i])
                else:
                    pos_genus.append(genus[i])
            gram_file.write("Gram + Genera:\n" + "\n".join(pos_genus) +
                            "\n***\n\n\nGram - Genera:\n" + "\n".join(neg_genus))

            pos_species = []
            neg_species = []
            # Analyzes Species
            for i in range(len(formatter(genus))):
                if genus_2[i][0] in pos_genus:
                    temp = genus_2[i][1:]
                    for q in temp:
                        pos_species.append(q)
                else:
                    temp = genus_2[i][1:]
                    for q in temp:
                        neg_species.append(q)
            gram_file.write("\n***\n\n\nGram + Species:\n" + "\n".join(pos_species) +
                            "\n***\n\n\nGram - Species:\n" + "\n".join(neg_species))


# %%
with open('chemistry.txt', 'r+') as chem:
    file = ''
    for line in chem:
        line = line.strip().replace('\t', '')
        line = "[" + line + "],\n"
        file += line
        print(line)
    chem.write(file)


def main():
   with open("dna.pdb","r") as f:
       with open("dna1.pdb","w") as g:
           for i in f.readlines():
               if "O2'" in i.split(" "):
                   i = ""
               elif "HO'2" in i.split(" "):
                   i = ""
               elif "U" in i.split(" "):
                   i = i.replace(" U  ","DT  ")
                   if "H6" in i.split(" "):
                       i = i.replace("H6","C7")
                  # g.write(i)
               if "C" in i.split(" "):
                   i = i.replace(" C  ","DC  ")
                  # g.write(i)
               if "G" in i.split(" "):
                   i = i.replace(" G  ","DG  ")
                  # g.write(i)
               if "A" in i.split(" "):
                   i = i.replace(" A  ","DA  ")
               g.write(i)

#gmx pdb2gmx -f dna_9.pdb -ignh
#gmx trjconv -s conf.gro -o dna_9_1.pdb -f conf.gro

if __name__ == '__main__':
   main()

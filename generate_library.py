import matplotlib.pyplot as plt
import forgi.visual.mplotlib as fvm
import forgi.graph.bulge_graph as fgb
import subprocess

# Run the command using the subprocess module
RNAinverse = "RNAinverse" # define the path to a RNAinverse file yourself
path_to_rosetta_bin = # define the path to a Rosetta bin folder 
yourself

cmds = []
rnas = []
db = pd.DataFrame(columns=["name","ps","ss","l","cmd"])
for n_stems in range(2,5):
   for length_stem in range(2,5):
       for length_loop in [3,5]:
           for length_mloop in range(2,5):
               length_tailstem = length_stem
               name = ".".join(map(str,[n_stems, length_stem, length_loop, length_mloop, length_tailstem]))
               stem = "("*length_stem+"."*length_loop+")"*length_stem
               ss = "("*length_tailstem+("."*length_mloop+stem)*n_stems+"."*length_mloop+")"*length_tailstem
               length = length_tailstem*2+(length_mloop*2+length_stem*2+length_loop)*n_stems
               # Run the command using the subprocess module
               process = subprocess.Popen(RNAinverse, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
               output, error = process.communicate(input=ss.encode())

               # Print the output of the command
               ps = output.decode().split(" ")[0].lower()


               #bg = fgb.BulgeGraph.from_dotbracket(ss)
               #fvm.plot_rna(bg, text_kwargs={"fontweight":"black"}, lighten=0.7,
               #             backbone_kwargs={"linewidth":3})
               #plt.show()
               name = [n_stems,length_stem,length_loop,length_mloop]
               filename = ".".join(map(str,name))
               print(filename,ps,ss,length)

               #plt.savefig(f"/home/akniga/RNA/{filename}.jpg")
               #plt.close()
               cmd = f"""f{path_to_rosetta_bin}/rna_denovo.static.linuxgccrelease -sequence "{ps}" -secstruct "{ss}" -nstruct 1 -out:f>
               cmds.append(cmd)
               db.append({"name":filename,"ps":ps,"ss":ss,"l":length,"cmd":cmd},ignore_index=True)
               rnas.append(name)

db.to_csv("db.csv")

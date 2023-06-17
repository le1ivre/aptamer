gmx pdb2gmx -f dna_prot.pdb -ignh -glu 1 -his 1 -merge interactive -ss
gmx editconf -f conf.gro -o boxed.gro -bt dodecahedron -d 1.5
gmx solvate -cp boxed.gro -cs spc216.gro -o solvated.gro -p topol.top

cp ../../2.4.5.3_46/*.mdp .
gmx grompp -f ions.mdp -c solvated.gro -p topol.top -o ions.tpr -maxwarn 5
 gmx genion -s ions.tpr -o solvated_ions.gro -p topol.top -pname NA -nname CL -neutral # 3
gmx make_ndx -f em.gro

gmx grompp -f minim.mdp -c solvated_ions.gro -p topol.top -o em.tpr -maxwarn 5
gmx mdrun -v -deffnm em

gmx grompp -f nvt.mdp -c em.gro -p topol.top -o nvt.tpr -maxwarn 5 -r em.gro -n index.ndx
gmx mdrun -v -deffnm nvt
gmx grompp -f npt.mdp -c nvt.gro -p topol.top -o npt.tpr -maxwarn 5 -r nvt.gro -n index.ndx
gmx mdrun -v -deffnm npt

gmx grompp -f md.mdp -c npt.gro -p topol.top -o md.tpr -maxwarn 5 -n index.ndx
gmx mdrun -v -deffnm md
gmx trjconv -s md.tpr -f md.xtc -o md_noPBC.xtc -pbc mol -center
gmx cluster -f md_noPBC.xtc -s md.tpr -method gromos -dt 100 -cutoff 0.3 -o -g -dist -ev -sz -tr -ntr -clid -cl

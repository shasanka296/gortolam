def grotolammps (nmol_file, gro_file, lamm_file):
    numberofato= numberofatom(nmol_file)
    totalbonds=0
    totalangles=0
    totaldihedrals=0
    totalimproperdihedrals=0
    for i,j in numberofato.iteams():
        totalbonds+=numberbonds(str(i))


def numberofatom(nmolfile):
    atom_number_dic={}
    with open(f"{nmolfile}", "r") as nmol:
        lines=nmol.readlines()
        for iteams in lines:
            if "[" and ";" and len(iteams)!=0:
                sub_mat=iteams.split()
                atom_number_dic[f"{sub_mat[0]}"]= int(sub_mat[1])
    return atom_number_dic


def numberbonds(name):
    with open(f"{name}")

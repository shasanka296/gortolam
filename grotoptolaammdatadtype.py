def grotolammps(nmol_file, gro_file, lamm_file):
    numberofato = numberofatom(nmol_file)
    totalbonds = 0
    totalangles = 0
    totaldihedrals = 0
    totalimproperdihedrals = 0
    for i, j in numberofato.iteams():
        tpe = "Solute1"
        if i == 0:
            tpe = "Solvent"
        totalbonds += numberbonds(str(i), tpe)
        totalangles += numberangles(str(i), tpe)


def numberofatom(nmolfile):
    atom_number_dic = {}
    with open(f"{nmolfile}", "r") as nmol:
        lines = nmol.readlines()
        for iteams in lines:
            if "[" and ";" and len(iteams) != 0:
                sub_mat = iteams.split()
                atom_number_dic[f"{sub_mat[0]}"] = int(sub_mat[1])
    return atom_number_dic


def numberbonds(name, tpe):
    with open(f"{name}_{tpe}.itp", "r") as itp:
        lines = itp.readlines()
        numberbond = 0
        start = False

        for line in lines:
            if "[ bonds ]" in line:
                start = True
            if start and '[angles]' not in line and ";" not in line:
                numberbond += 1
            if "[angles]" in line:
                return numberbond


def numberangles(name, tpe):
    with open(f"{name}_{tpe}.itp", "r") as itp:
        lines = itp.readlines()
        numberangels = 0
        start = False
        for line in lines:
            if "[angles]" in line:
                start = True
            if "[ dihedrals ]" in line:
                return numberangels
            if start and ";" not in line:
                numberangels += 1

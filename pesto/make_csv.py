import sys
import os
import glob

aa_3to1 = {
    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
    'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
    'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
    'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V',
    'SEC': 'U', 'PYL': 'O', 'ASX': 'B', 'GLX': 'Z', 'XLE': 'J', 'UNK': 'X'
}

output_dir = sys.argv[1]
csv_path = os.path.join(output_dir, "interface_residues.csv")

pdb_files = sorted(glob.glob(os.path.join(output_dir, "*_i0.pdb")))

if not pdb_files:
    print("No _i0.pdb files found.")
    sys.exit(1)

rows = []  # each entry will be one residue

for pdb_file in pdb_files:
    seen_residues = set()

    with open(pdb_file, 'r') as f:
        for line in f:
            if not line.startswith("ATOM"):
                continue
            try:
                chain    = line[21].strip()
                res_num  = line[22:26].strip()
                res_name = line[17:20].strip().upper()
                b_factor = float(line[60:66].strip())

                key = (chain, res_num)
                if key in seen_residues:
                    continue
                seen_residues.add(key)

                if b_factor >= 0.5:
                    code = 1
                elif b_factor <= 0.25:
                    code = 2
                elif b_factor < 0.5 and b_factor > 0.25:
                    code = 0

                aa1 = aa_3to1.get(res_name, 'X')
                rows.append((res_num, aa1, f"{b_factor:.2f}", code))

            except (ValueError, IndexError):
                continue

with open(csv_path, 'w') as f:
    f.write("res_num; res_name; b_factor; code\n")  # header
    for row in rows:
        f.write(";".join(str(x) for x in row) + "\n")

print(f"\nCSV generated: {csv_path}")       
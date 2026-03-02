import argparse
import numpy as np
from tmtools import tm_align
from tmtools.io import get_structure, get_residue_data

def main():
    parser = argparse.ArgumentParser(description="Executa o TM-align entre duas estruturas de proteínas")
    parser.add_argument("pdb1", help="Caminho para o primeiro ficheiro PDB")
    parser.add_argument("pdb2", help="Caminho para o segundo ficheiro PDB")
    args = parser.parse_args()

    # Carregar estruturas PDB
    s1 = get_structure(args.pdb1)
    s2 = get_structure(args.pdb2)

    # Obter coordenadas e sequências
    coords1, seq1 = get_residue_data(next(s1.get_chains()))
    coords2, seq2 = get_residue_data(next(s2.get_chains()))

    # Executar alinhamento
    res = tm_align(coords1, coords2, seq1, seq2)

    # Mostrar resultados
    print(f"Translation vector: {res.t}")
    print(f"Rotation matrix: \n{res.u}")
    print(f"TM-score (chain1): {res.tm_norm_chain1}")
    print(f"TM-score (chain2): {res.tm_norm_chain2}")
    print(f"RMSD: {res.rmsd}")

if __name__ == "__main__":
    main()

import argparse
import sys
from tmtools import tm_align
from tmtools.io import get_structure, get_residue_data

def main():
    parser = argparse.ArgumentParser(description="Execute TM-align and display structural alignment.")
    parser.add_argument("pdb1", help="Path to the first PDB file")
    parser.add_argument("pdb2", help="Path to the second PDB file")
    args = parser.parse_args()

    try:
        # 1. Load PDB structures
        s1 = get_structure(args.pdb1)
        s2 = get_structure(args.pdb2)

        # 2. Extract coordinates and sequences from the first chain of each
        coords1, seq1 = get_residue_data(next(s1.get_chains()))
        coords2, seq2 = get_residue_data(next(s2.get_chains()))

        # 3. Perform the structural alignment
        res = tm_align(coords1, coords2, seq1, seq2)

        # 4. Print Statistics
        print(f"Translation vector: {res.t}")
        print(f"Rotation matrix: \n{res.u}")
        print(f"TM-score (chain1): {res.tm_norm_chain1}")
        print(f"TM-score (chain2): {res.tm_norm_chain2}")
        print(f"RMSD: {res.rmsd}")

        # 5. Print the Alignment
        print("\nStructural Alignment:")
        print(f"PDB 1: {res.seqxA}")
        print(f"Links: {res.seqM}")
        print(f"PDB 2: {res.seqyA}")
        print("="*30 + "\n")

    except StopIteration:
        print("Error: Could not find chains in one of the PDB files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

import os
import sys
import argparse

os.chdir('/opt/ScanNet')

# Set paths
os.environ['MKL_NUM_THREADS'] = '4'
os.environ['NUMEXPR_NUM_THREADS'] = '4'
os.environ['OMP_NUM_THREADS'] = '4'
os.environ['OPENBLAS_NUM_THREADS'] = '4'
os.environ['VECLIB_MAXIMUM_THREADS'] = '4'
os.environ['NUMBA_DEFAULT_NUM_THREADS'] = '4'
os.environ['NUMBA_NUM_THREADS'] = '4'

import numpy as np

parser = argparse.ArgumentParser(description='ScanNet: Protein binding site prediction')
parser.add_argument('input', type=str, help='PDB ID, Uniprot ID, or path to PDB/CIF file (optionally with _chain suffix)')
parser.add_argument('--mode', default='interface', choices=['interface', 'epitope', 'idp'],
                    help='Prediction mode (default: interface)')
parser.add_argument('--noMSA', action='store_true', help='Predict without MSA (faster, less accurate)')
parser.add_argument('--assembly', action='store_true', help='Process chains together as assembly')
parser.add_argument('--predictions_folder', default='/data/output', help='Output directory (default: /data/output)')
parser.add_argument('--name', default='', help='Custom output name')

args = parser.parse_args()

print('Input:', args.input)
print('Mode:', args.mode)
print('Use MSA:', not args.noMSA)
print('Assembly:', args.assembly)
print('Output folder:', args.predictions_folder)
print('Name:', args.name if args.name else '(auto)')

# Add ScanNet source to path
sys.path.insert(0, '/opt/ScanNet')

from preprocessing import PDBio
from utilities.paths import structures_folder, MSA_folder, model_folder

# Override prediction output folder
os.environ['SCANNET_PREDICTIONS_FOLDER'] = args.predictions_folder

# Run prediction by importing and calling predict_bindingsites logic
if __name__ == '__main__':
    from predict_bindingsites import predict_interface_residues, pipeline_noMSA, pipeline_MSA
    from predict_bindingsites import (interface_model_folder, interface_model_MSA, interface_model_noMSA,
                                       interface_model_name_MSA, interface_model_name_noMSA,
                                       epitope_model_folder, epitope_model_MSA, epitope_model_noMSA,
                                       epitope_model_name_MSA, epitope_model_name_noMSA,
                                       idp_model_folder, idp_model_MSA, idp_model_noMSA,
                                       idp_model_name_MSA, idp_model_name_noMSA)

    input_str = args.input
    query_pdbs = []
    query_chain_ids = []
    if '.txt' in input_str:
        with open(input_str, 'r') as f:
            for line in f:
                pdb, chain_ids = PDBio.parse_str(line[:-1])
                query_pdbs.append(pdb)
                query_chain_ids.append(chain_ids)
    else:
        query_pdbs, query_chain_ids = PDBio.parse_str(input_str)

    if args.name != '':
        query_names = [args.name]
    else:
        query_names = None

    predictions_folder = args.predictions_folder
    if not os.path.isdir(predictions_folder):
        os.makedirs(predictions_folder)

    use_MSA = not args.noMSA

    if use_MSA:
        pipeline = pipeline_MSA
    else:
        pipeline = pipeline_noMSA

    if args.mode == 'interface':
        mfolder = interface_model_folder
        chimera_thresholds = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
        if use_MSA:
            model_name = interface_model_name_MSA
            model = interface_model_MSA
        else:
            model_name = interface_model_name_noMSA
            model = interface_model_noMSA
    elif args.mode == 'epitope':
        mfolder = epitope_model_folder
        chimera_thresholds = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
        if use_MSA:
            model_name = epitope_model_name_MSA
            model = epitope_model_MSA
        else:
            model_name = epitope_model_name_noMSA
            model = epitope_model_noMSA
    elif args.mode == 'idp':
        mfolder = idp_model_folder
        chimera_thresholds = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
        if use_MSA:
            model_name = idp_model_name_MSA
            model = idp_model_MSA
        else:
            model_name = idp_model_name_noMSA
            model = idp_model_noMSA
    else:
        raise ValueError('Mode %s not supported' % args.mode)

    predict_interface_residues(
        query_pdbs=query_pdbs,
        query_chain_ids=query_chain_ids,
        query_names=query_names,
        pipeline=pipeline,
        model=model,
        model_name=model_name,
        model_folder=mfolder,
        structures_folder=structures_folder,
        predictions_folder=predictions_folder,
        MSA_folder=MSA_folder,
        biounit=True,
        assembly=args.assembly,
        overwrite_MSA=False,
        permissive=True,
        use_MSA=use_MSA,
        chimera_thresholds=chimera_thresholds,
        layer=None
    )
    print('Done. Output written to', predictions_folder)

#!/usr/bin/python3

import os
import argparse

from Bio import Phylo

formats_list = ["newick", "nexus", "nexml", "phyloxml", "cdao"]

parser = argparse.ArgumentParser(description='Converts between different Phylogenetic Tree formats using the Phylo module.')

parser.add_argument('-i', '--input', help='input phylogenetic tree file', required=True)
parser.add_argument('-if', '--input-format', help='format of the input phylogenetic tree', required=True)
parser.add_argument('-o', '--output', help='output phylogenetic tree file', required=True)
parser.add_argument('-of', '--output-format', help='format of the output phylogenetic tree', required=True)

arg = parser.parse_args()

if not(arg.input_format in formats_list):
	print("The input format ({}) is not valid. It must be one of: {}.".format(arg.input_format, ", ".join(formats_list)))
	os._exit(1)
	
if not(arg.output_format in formats_list):
	print("The output format ({}) is not valid. It must be one of: {}.".format(arg.output_format, ", ".join(formats_list)))
	os._exit(1)

if arg.input_format == arg.output_format:
	print("The input and output formats must be different.")
	os._exit(1)	

Phylo.convert(arg.input, arg.input_format, arg.output, arg.output_format)

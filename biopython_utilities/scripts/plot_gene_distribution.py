#!/usr/bin/python3

import math
import sys
import argparse

from random import seed
from random import random

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation

colors_list = [colors.red, colors.blue, colors.yellow, colors.brown, colors.green, colors.darkmagenta, colors.greenyellow, colors.lavender, colors.purple, colors.navy, colors.orange, colors.paleturquoise, colors.powderblue, colors.rosybrown, colors.turquoise, colors.black]

parser = argparse.ArgumentParser(description='Create an image with the distribution of a list of genes. Lines in the input TSV file must have four columns: (1) the group to wich the gene belongs to (each group is drawn in a different color), (2) the name of the gene, (3) the start coordinate, and (4) the end coordinate.')

parser.add_argument('INPUT_FILE', help='input TSV file with gene names and coordinates')
parser.add_argument('-o', '--output', default='image', help='output image name (without file extension)')
parser.add_argument('-f', '--format', default='pdf', help='output image format: PS, PDF, SVG, JPG, BMP, GIF, PNG, TIFF or TIFF (default is PDF)')
parser.add_argument('-s', '--start', help='start coordinate to draw (if not provided, it is automatically determined from the input data)')
parser.add_argument('-e', '--end', help='end coordinate to draw (if not provided, it is automatically determined from the input data)')
parser.add_argument('-p','--preserve-strand', help='use this flag to preserve gene strands', action='store_true')
parser.add_argument('-b','--breaks', default='20', help='number of axis breaks to represent the scale')
parser.add_argument('-r','--random-seed', default='1', help='random seed for color generation')

arg = parser.parse_args()

fh = open(arg.INPUT_FILE)
lines = fh.readlines()

series_features = {}
series_indexes = {}

series_index = 0
for line in lines:
    if not ('#' in line):
        temp_line = line.upper().replace('\n', '')
        sp_line = temp_line.split(sep='\t')
        series = sp_line[0]
        gene_name = sp_line[1]

        if int(sp_line[2]) > int(sp_line[3]):
          start = int(sp_line[3])
          end = sp_line [2]
          if arg.preserve_strand:
            strand = -1
          else:
            strand = 1
        else:
          start = int(sp_line[2])
          end = int(sp_line[3])
          strand = 1

        if series in series_features:
          series_features[series].append((gene_name, strand, start, end))
        else:
          series_features[series] = [(gene_name, strand, start, end)]
          series_indexes[series] = series_index
          series_index = series_index + 1

start = sys.maxsize
end = -1

gdd = GenomeDiagram.Diagram("diagram", tracklines = False, y = 0.4)
gd_track_for_features = gdd.new_track(1, scale = True, height = 1, scale_smallticks = 0)
gds_features = gd_track_for_features.new_set()

seed(int(arg.random_seed))

for series in series_features.keys():
  if series_indexes[series] < len(colors_list):
    current_color = colors_list[series_indexes[series]]
  else:
    current_color = colors.Color(random(), random(), random())

  for i in range(0, len(series_features[series])):
    current_feature = series_features[series][i]
    feature = SeqFeature(FeatureLocation(int(current_feature[2]), int(current_feature[3])), strand=current_feature[1])
    gds_features.add_feature(feature, name="{}".format(current_feature[0]), label=True, color=current_color)

    if int(current_feature[2]) < start:
      start = int(current_feature[2])
    if int(current_feature[3]) > end:
      end = int(current_feature[3])


if not arg.start == None:
  start = int(arg.start)
else:
  start = start - 1000

if not arg.end == None:
  end = int(arg.end)
else:
  end = end + 1000

if start > end:
  sys.exit("start must be less than end")

gd_track_for_features.start = start
gd_track_for_features.end = end
gd_track_for_features.scale_largetick_interval = (end-start) / int(arg.breaks)

gdd.draw(format="linear", fragments=1, start=start, end=end)
gdd.write(arg.output+'.'+arg.format, arg.format)

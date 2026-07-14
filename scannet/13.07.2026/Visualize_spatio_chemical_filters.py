#!/usr/bin/env python
# coding: utf-8

# # Visualizing spatio-chemical filters with pythreejs
# 
# 
# ## Important: Cells must be executed one at time (rather than with Cell -> Run All)
# 
# 

# # Calculate filter specificities (precomputed)
# The first step is to calculate the filter specificities.
# For the atomic filters, we must simply extract the neighborhood embedding layer parameters from the keras model object.
# For the amino acid filters, since the amino-acid specificity of individual gaussian components is *non-linear*, we must first determine it on a set of test proteins. This is done as follows:
# 1. Calculate, for each gaussian component of each filter, the distribution of activities.
# 2. Identify the top-1/5\% activating residues.
# 3. Determine their amino acid type, secondary structure and accessible surface area.
# 4. Determine the mean activity across the top-activating residues.
# 
# For the trained networks, the specificities are precomputed. Otherwise, calculating the amino acid filter specificities takes about 1-2 hour on a laptop
# To avoid this step and visualize only the atom filters, specify only_atom=True
# 
# Then, for a given filter, display the gaussians with highest mean activity (threshold1 = 33\% of the maximum mean activity), and show attribute specificity as inset.
# 
# 

# In[1]:


from visualizations import show_3d_filters,weight_logo_3d
from utilities import dataset_utils
import numpy as np

mode = 'epitope' # Prediction mode: 'interface' (protein-protein binding sites), 'epitope' (B-cell epitopes), 'idp' (protein - intrinsically disordered proteins binding sites)
use_MSA = True # Whether to use evolutionary information or not.



if mode == 'interface':
    top_percent = 5
    if use_MSA:
        model_name = 'ScanNet_PPI'
    else:
        model_name = 'ScanNet_PPI_noMSA'
    dataset_name = 'PPBS_validation'
    list_origins = np.concatenate([dataset_utils.read_labels('datasets/PPBS/labels_%s.txt'%dataset)[0]
     for dataset in ['validation_70','validation_homology','validation_topology','validation_none']
        ])
    
elif mode == 'epitope':
    top_percent = 5
    if use_MSA:
        model_name = 'ScanNet_PAI_0'
    else:
        model_name = 'ScanNet_PAI_noMSA_0'
    dataset_name = 'BCE_fold1'
    list_origins = dataset_utils.read_labels('datasets/BCE/labels_fold1.txt')[0]
    
elif mode == 'idp':
    top_percent = 5
    if use_MSA:
        model_name = 'ScanNet_PIDPI_0'
    else:
        model_name = 'ScanNet_PIDPI_noMSA_0'
    dataset_name = 'PIDPBS_fold0'
    list_origins = None
#     list_origins = dataset_utils.read_labels('datasets/PIDP/labels_fold0.txt')[0]
        
    


filter_specificities = show_3d_filters.calculate_filter_specificities(
    model_name,
    dataset_name = dataset_name,
    dataset_origins = list_origins,
    biounit=False,
    ncores=4,
    only_atom=False,
    top_percent = top_percent,
    fresh = False,
    Lmax = 1024

)




# ## Instantiate sphere geometry
# This cell must be executed first

# In[2]:


sg = weight_logo_3d.make_sphere_geometry(30)

# # Interactive visualization of one amino acid filter

# In[26]:


renderer = show_3d_filters.plot_aminoacid_filter(filter_specificities,117,sg=sg);
display(renderer)

# # Interactive visualization of one atomic filter

# In[ ]:


renderer = show_3d_filters.plot_atomic_filter(filter_specificities,119,sg=sg,threshold1=0.33);
display(renderer)

# # Filter visualization with custom camera position

# In[ ]:


renderer = show_3d_filters.plot_atomic_filter(filter_specificities,30,sg=sg,
                                             camera_position=[-0.3, 0.6, 1.0]);

display(renderer)


# # Filter visualization with custom camera position, take screenshot

# In[ ]:


renderer = show_3d_filters.plot_atomic_filter(filter_specificities,119,sg=sg,
                                             camera_position=[-0.3, 0.6, 1.0]);
recorder=weight_logo_3d.make_screenshot(renderer,'screenshot_filter1.png')
display(renderer)
recorder

# # Visualize atomic neighborhood

# In[16]:


from visualizations import show_3d_neighborhoods
pdbid = '7jvb' # Spike protein RBD
modelid = 0
chainid = 'A'
residue = 493 # ACE2 binding site.
atom = 'N'

    
atom_positions,atom_types,atom_bonds = show_3d_neighborhoods.get_neighborhood(
        pdb = pdbid[:4],
        model = modelid,
        chain = chainid,
        resnumber = residue,
        atom = atom,
        assembly=False,
        biounit=False,
)

renderer = show_3d_neighborhoods.show_atoms(atom_positions,atom_types,atom_bonds,render=True,
                                               radius_scale = 0.15,show_frame=True,
                                            camera_position=[-0.3, 0.6, 1.0]);
recorder=weight_logo_3d.make_screenshot(renderer,'screenshot_atomicneighborhood1.png')
display(renderer)
recorder

# # Atomic neighborhood superimposed with filter

# In[14]:


from visualizations import show_3d_neighborhoods
pdbid = '7jvb' # Spike protein RBD
modelid = 0
chainid = 'A'
residue = 493 # ACE2 binding site.
atom = 'N'
filter_index =56

    
atom_positions,atom_types,atom_bonds = show_3d_neighborhoods.get_neighborhood(
        pdb = pdbid[:4],
        model = modelid,
        chain = chainid,
        resnumber = residue,
        atom = atom,
        assembly=False,
        biounit=False,
)


list_objects = show_3d_neighborhoods.show_atoms(atom_positions,atom_types,atom_bonds,render=False,
                                               radius_scale = 0.15)
renderer = show_3d_filters.plot_atomic_filter(filter_specificities,
                                                 filter_index,
                                                  y_offset = 0.25,
                                                 sg=sg,
                                                 list_additional_objects=list_objects,
                                                threshold1=0.33);

display(renderer)

# # Amino acid neighborhood

# In[28]:


from visualizations import show_3d_neighborhoods
pdbid = '7jvb' # Spike protein RBD
modelid = 0
chainid = 'A'
residue = 493 # ACE2 binding site.
MSA_file = '/Users/jerometubiana/Downloads/MSA_7jvb_A_0_A.fasta' # None

    
aa_positions,aa_types,aa_bonds = show_3d_neighborhoods.get_neighborhood_aa(
        pdb = pdbid[:4],
        model = modelid,
        chain = chainid,
        resnumber = residue,
        assembly=False,
        biounit=False,
        MSA_file=MSA_file
)

renderer = show_3d_neighborhoods.show_aminoacids(aa_positions,aa_types,aa_bonds,render=True,
                                                 sg=sg);
recorder=weight_logo_3d.make_screenshot(renderer,'screenshot_aminoacidneighborhood1.png')
display(renderer)
recorder

# # Amino acid neighborhood with filter superimposed

# In[27]:


from visualizations import show_3d_neighborhoods
pdbid = '7jvb' # Spike protein RBD
modelid = 0
chainid = 'A'
residue = 490 # ACE2 binding site.
MSA_file = '/Users/jerometubiana/Downloads/MSA_7jvb_A_0_A.fasta' # None

    
aa_positions,aa_types,aa_bonds = show_3d_neighborhoods.get_neighborhood_aa(
        pdb = pdbid[:4],
        model = modelid,
        chain = chainid,
        resnumber = residue,
        assembly=False,
        biounit=False,
        MSA_file=MSA_file
)

list_objects = show_3d_neighborhoods.show_aminoacids(aa_positions,aa_types,aa_bonds,sg=sg,render=False);

renderer = show_3d_filters.plot_aminoacid_filter(filter_specificities,
                                                 117,
                                                 sg=sg,
                                                 list_additional_objects=list_objects,
                                                 threshold1=0.33,scale=3.0);
display(renderer)

# In[31]:


importlib.reload(show_3d_neighborhoods)

# In[36]:


renderer = show_3d_filters.plot_aminoacid_filter(filter_specificities,112,sg=sg,scale=3.0,
                                                camera_position=[-0.3,1.0,1.0]);
recorder=weight_logo_3d.make_screenshot(renderer,'screenshot_aminoacidfilter2.png')
display(renderer)
recorder

# In[ ]:




# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PI-LZerD](https://kiharalab.org/proteindocking/pilzerd.php), a software for protein-protein docking.

# Using the PI-LZerD image in Linux

You should adapt and run the following command: `docker run --rm -v "/your/data/dir:/data" pegi3s/pilzerd bash -c "cd /opt/lzerddistribution && runlzerd.sh /data/PDB1.pdb /data/PDB2.pdb && cp ./*.pdb /data"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `PDB1.pdb` to the name of the PDB file 1 you want to use.
- `PDB2.pdb` to the name of the PDB file 2 you want to use.

# Test data

To test the previous commands, the PDB file 1 used is available [here](https://github.com/pegi3s/dockerfiles/tree/master/pilzerd/test_data/1PPE_r_b.pdb) and the PDB file 2 is available [here](https://github.com/pegi3s/dockerfiles/tree/master/pilzerd/test_data/1PPE_l_b.pdb).

Then, you should simply run: `docker run --rm -v "/your/data/dir:/data" pegi3s/pilzerd bash -c "cd /opt/lzerddistribution && runlzerd.sh /data/1PPE_r_b.pdb /data/1PPE_l_b.pdb && cp ./*.pdb /data"`

# Using the PI-LZerD image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/pilzerd bash -c "cd /opt/lzerddistribution && runlzerd.sh /data/PDB1.pdb /data/PDB2.pdb"`

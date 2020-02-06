# multifractal_hic
Python routines to compute the multifractal spectrum of a Hi--C map

This project contains two scripts.

The first script, "spectrum.py", numerically computes the partition function <img src="https://render.githubusercontent.com/render/math?math=Z(q,\epsilon)"> from a given Hi--C map. The syntax is

./spectrum.py <FILE>

The accepted file format for the input file is
<name> <x> <y> <count>
where <name> is ignored, <x> and <y> are the bin coordinate (in unit of the resolution), and <count> is the Hi-C count (after appropriate normalization).  The script generates an output file with extension .scaling . The three columns of this file are: value of <img src="https://render.githubusercontent.com/render/math?math=\epsilon"> (in units of the map resolution), value of <img src="https://render.githubusercontent.com/render/math?math=Z(q,\epsilon)">, value of q. In particular, q is varied between 0 and 5 in steps of 0.25. The coarse graining scale <img src="https://render.githubusercontent.com/render/math?math=\epsilon"> is varied between 1 and 300. 
  
The second script, "spectrum2.py", computes the multifractal spectrum from the partition function using least-square fitting. The syntax is

./spectrum2.py <FILE.scaling> <eps_min> <eps_max>

The script produces two output files. The file with extension .mfct contains the multifractal spectrum (with format q, K(q)). Files with extensions .fit contain information about the fit, in particular: fitted value of a, corresponding sum of residuals, name of the input file.

  
  
  

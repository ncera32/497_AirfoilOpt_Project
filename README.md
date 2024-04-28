Overview:

This Project aims to optimize the shape of an NACA 2415 airfoil under specified flight conditions to achieve desired aerodynamic performance while satisfying multiple constraints.
The two constraints that are applied include the lift coefficient and moment coefficient equaling 0.5 and 0.03, respectively. Three separate optimization algorithms are implemented to 
explore different optimization strategies. The programs utilize PyOptSparse's buit-in algorithms: SLSQP, IPOPT, and CONMIN. 

Files:

1. '497project_CONMIN.py': This file contains the implementation of the airfoil optimization using the CONMIN algorithm. 
2. '497project_IPOPT.py': This file contains the implementation of the airfoil optimization using the IPOPT algorithm. 
3. '497project_SLSQP.py': This file contains the implementation of the airfoil optimization using the SLSQP algorithm. 
4. 'naca2415.dat.rtf': This file contains the coordinates of an NACA 2415 airfoil profile used as the initial shape for the optimization. 

Instructions:

Ensure that all required libraries (listed below) and python 3.x or later are installed. Visit https://mdolab-cmplxfoil.readthedocs-hosted.com/en/latest/ for additional guidance with
installing and setting up all requirements for the python scripts. Run each optimization script separately ('497project_CONMIN.py', '497project_IPOPT.py', and '497project_SLSQP.py') to
perform the airfoil shape optimization using the specified algorithm. Each script will produce and output file, with the title following the structure, 
output_'algorithm name' (output_CONMIN, output_IPOPT, and output_SLSQP). Each output file will containt a .dat file for the geometric constraints across the 
optimization, the modified airfoil shape at each iteration, an opt.hst file showing the total history of the optimization, a PDF file containing the
final airfoil shape, pressure coefficient, and local skin friction coefficient compared to the initial, and an .out file that contains the history of the 
objective function values across the optimization. Within the PDF file, the colored lines represent the optimized results, and the grey lines represent the
initial conditions. 

Requirements:

- Python 3.x
- Necessary Libraries: CMPLXFOIL, Numpy, MPI4py, pyGeo, pyOptSparse, Multipoint


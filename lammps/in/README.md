# LAMMPS Input Files

This directory contains LAMMPS input scripts for molecular dynamics simulations.

## Required LAMMPS Executable

The LAMMPS executable (`lmp_mpi`) is required to run these simulations but is not included in this repository due to its large size (54MB).

### Installation Options:

1. **System Package Manager:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install lammps
   
   # CentOS/RHEL
   sudo yum install lammps
   ```

2. **Conda:**
   ```bash
   conda install -c conda-forge lammps
   ```

3. **Build from Source:**
   See the [LAMMPS documentation](https://docs.lammps.org/Build.html) for compilation instructions.

### Executable Location

The scripts expect `lmp_mpi` to be available in your PATH. If installed elsewhere, create a symlink or modify the `LAMMPS_EXE` variable in the run scripts.

## Input Files

- `compress_y.in` - Y-direction compression simulation
- `deformation.in` - General deformation protocol
- `minimization.in` - Energy minimization
- `relax.in` - Structural relaxation
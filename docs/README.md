# **QMatSim: Multiscale DFT + MD Simulation Framework**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MATLAB](https://img.shields.io/badge/MATLAB-R2020b+-orange.svg)](https://www.mathworks.com/products/matlab.html)
[![Mathematica](https://img.shields.io/badge/Mathematica-12+-red.svg)](https://www.wolfram.com/mathematica/)
[![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)]()
[![Coverage](https://img.shields.io/badge/Coverage-92%25-brightgreen.svg)]()

*A modular, cross-platform quantum materials simulation framework combining Density Functional Theory (DFT) and Molecular Dynamics (MD), with unified workflows across Python, MATLAB, and Mathematica.*

**Core simulation capabilities include:**

- SIESTA-based DFT for electronic structure calculations  
- LAMMPS-based MD for strain engineering and thermal transport  
- Cross-platform postprocessing (Python, MATLAB, Mathematica)  
- HPC-ready job submission (SLURM) and CLI automation  
- Supercell generation, strain pipelines, and energy tracking  

**Author**: Dr. Meshal Alawein ([meshal@berkeley.edu](mailto:meshal@berkeley.edu))  
**Institution**: University of California, Berkeley  
**License**: MIT © 2025 Dr. Meshal Alawein — All rights reserved

---

## Project Overview

**QMatSim** is a research-grade multiscale simulation toolkit designed to unify quantum and classical simulation workflows for 2D materials and nanostructures. Developed for HPC environments and academic workflows, it tightly integrates DFT (SIESTA) and MD (LAMMPS), and provides robust analysis tools in Python, MATLAB, and Mathematica.

### Key Features

🧮 **DFT + MD Integration**: Fully modular SIESTA and LAMMPS pipelines  
🧱 **Strain Templates**: Auto-generated lattice deformation and supercells  
⚙️ **Cluster Ready**: SLURM input deck generation for batch jobs  
📊 **Postprocessing**: LDOS, band flattening, stress-strain, and more  
🔧 **Cross-Platform**: Analysis tools in Python, MATLAB, Mathematica  
🧪 **CLI Interface**: All workflows accessible via the `qmatsim` command  

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/alaweimm90/QMatSim.git
cd QMatSim

# Install in development mode
pip install -e .
```

---

## Command-Line Examples

```bash
# ➤ DFT Relaxation (SIESTA)
qmatsim relax --material MoS2 --structure 1x10_rectangular

# ➤ MD Minimization (LAMMPS)
qmatsim minimize --structure ripple10 --mode compress
qmatsim minimize --structure ripple10 --mode all

# ➤ Postprocessing
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## Repository Structure

```
QMatSim/
├── qmatsim/           # Core CLI logic
├── scripts/           # Automation tools
├── siesta/            # Templates and pseudopotentials
├── lammps/            # Potentials and in.data files
├── analysis.py        # Python-based analysis
├── analysis.m         # MATLAB analysis functions
├── analysis.nb        # Mathematica postprocessing
├── tests/             # CLI test suite
└── setup.py, README.md
```

---

## Testing & Validation

```bash
pytest tests/
```

Includes CLI, regression, and functional testing.

---

## Citation

If you use QMatSim in your research, please cite:

```yaml
cff-version: 1.2.0
message: "If you use QMatSim, please cite this project as below."
authors:
  - family-names: Alawein
    given-names: Meshal
    affiliation: UC Berkeley
title: QMatSim: Modular Multiscale Framework for DFT and MD
version: 0.1.0
license: MIT
date-released: 2025-07-19
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright © 2025 Dr. Meshal Alawein — All rights reserved.**

## Connect & Collaborate

<div align="center">

<strong>Dr. Meshal Alawein</strong><br/>
<em>Computational Physicist & Research Scientist</em><br/>
University of California, Berkeley

---

📧 <a href="mailto:meshal@berkeley.edu" style="color:#003262;">meshal@berkeley.edu</a>

<a href="https://www.linkedin.com/in/meshal-alawein" title="LinkedIn">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn" height="32" />
</a>
<a href="https://github.com/alaweimm90" title="GitHub">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub" height="32" />
</a>
<a href="https://malawein.com" title="Website">
  <img src="https://img.shields.io/badge/Website-003262?style=flat&logo=googlechrome&logoColor=white" alt="Website" height="32" />
</a>
<a href="https://scholar.google.com/citations?user=IB_E6GQAAAAJ&hl=en" title="Google Scholar">
  <img src="https://img.shields.io/badge/Scholar-4285F4?style=flat&logo=googlescholar&logoColor=white" alt="Scholar" height="32" />
</a>
<a href="https://simcore.dev" title="SimCore">
  <img src="https://img.shields.io/badge/SimCore-FDB515?style=flat&logo=atom&logoColor=white" alt="SimCore" height="32" />
</a>

</div>

<p align="center"><em>
Made with love, and a deep respect for the struggle.<br/>
For those still learning—from someone who still is.<br/>
Science can be hard. This is my way of helping. ⚛️
</em></p>

---

*Crafted with love, 🐻 energy, and zero sleep.*

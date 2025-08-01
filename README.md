# QMatSim: Multiscale DFT + MD Simulation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-green.svg)](https://www.python.org/)
[![SIESTA](https://img.shields.io/badge/SIESTA-4.1+-blue.svg)](https://siesta-project.org/siesta/)
[![LAMMPS](https://img.shields.io/badge/LAMMPS-stable-red.svg)](https://www.lammps.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#testing--validation)

*A comprehensive multiscale quantum materials simulation framework combining Density Functional Theory (DFT) and Molecular Dynamics (MD) — engineered for 2D materials research with HPC cluster integration and automated strain engineering.*

**Core simulation capabilities (fully implemented):**

- **DFT Integration**: SIESTA-based electronic structure calculations with strain engineering
- **MD Integration**: LAMMPS-based molecular dynamics for thermal transport and deformation
- **Strain Engineering**: Automated supercell generation and systematic strain studies
- **HPC Workflows**: SLURM job submission and cluster-ready batch processing
- **Cross-Platform Analysis**: Python, MATLAB, and Mathematica postprocessing tools
- **CLI Automation**: Unified command-line interface for all simulation workflows

**Author**: Dr. Meshal Alawein ([meshal@berkeley.edu](mailto:meshal@berkeley.edu))  
**Institution**: University of California, Berkeley  
**License**: MIT License © 2025 Dr. Meshal Alawein — All rights reserved

---

## Project Overview

**QMatSim** is a research-grade multiscale simulation toolkit designed to unify quantum and classical simulation workflows for 2D materials and nanostructures. Developed for HPC environments and academic workflows, it tightly integrates DFT (SIESTA) and MD (LAMMPS), providing robust analysis tools and automated strain engineering capabilities.

### Key Features

🧮 **DFT + MD Integration**: Seamless SIESTA and LAMMPS workflow coupling  
🧱 **Automated Strain Engineering**: Systematic supercell generation and deformation studies  
⚙️ **HPC Ready**: SLURM job submission with optimized resource allocation  
📊 **Multi-Platform Analysis**: Python, MATLAB, and Mathematica postprocessing  
🔧 **Comprehensive CLI**: All workflows accessible via unified `qmatsim` command  
🧪 **Materials Database**: Extensive pseudopotential libraries (GGA, LDA, GGA-SOC)  

---

## Quick Start

### Prerequisites
- **Python 3.9+** with NumPy, Matplotlib
- **SIESTA 4.1+** for DFT calculations
- **LAMMPS** (stable) for MD simulations
- **SLURM** (optional) for HPC job submission

### Installation
```bash
# Clone the repository
git clone https://github.com/alaweimm90/QMatSim.git
cd QMatSim

# Install in development mode
pip install -e .

# Verify installation
qmatsim --help
```

### Basic Usage
```bash
# ➤ DFT Relaxation (SIESTA)
qmatsim relax --material MoS2 --structure 1x10_rectangular

# ➤ MD Simulation (LAMMPS)
qmatsim minimize --structure ripple10 --mode compress
qmatsim minimize --structure ripple10 --mode all

# ➤ Postprocessing Analysis
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## Scientific Modules

### Core Simulation Engine
- **SIESTA Integration**: Complete DFT workflow with pseudopotential management
- **LAMMPS Integration**: MD simulations with multiple potential support
- **Strain Engineering**: Automated lattice deformation and supercell generation

### Materials Database
- **Pseudopotentials**: Complete elemental coverage (GGA, LDA, GGA-SOC functionals)
- **Structure Templates**: Primitive and rectangular supercell configurations
- **Material Support**: MoS₂, MoSe₂, WS₂, WSe₂ transition metal dichalcogenides

### HPC Workflows
- **SLURM Integration**: Automated job submission and resource management
- **Batch Processing**: Parallel strain studies and parameter sweeps
- **Error Handling**: Robust failure recovery and job monitoring

### Analysis Tools
- **Electronic Structure**: Band structure, LDOS, and PDOS analysis
- **Mechanical Properties**: Stress-strain relationships and elastic constants
- **Cross-Platform**: Python/MATLAB/Mathematica analysis pipelines

---

## Command-Line Interface

### DFT Calculations
```bash
# Single-point relaxation
qmatsim relax --material MoS2 --structure 1x1_primitive

# Supercell calculations
qmatsim relax --material MoS2 --structure 1x10_rectangular
```

### MD Simulations
```bash
# Compression studies
qmatsim minimize --structure ripple10 --mode compress

# Full deformation protocol
qmatsim minimize --structure ripple10 --mode all
```

### Analysis Pipeline
```bash
# Complete postprocessing
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## Repository Structure

```
QMatSim/
├── qmatsim/                    # Core CLI framework
│   ├── __init__.py            # Package initialization
│   └── __main__.py            # CLI entry point
├── scripts/                    # Automation tools
│   ├── run-DFT.sh             # SIESTA workflow automation
│   ├── run-MD.sh              # LAMMPS simulation control
│   ├── run-postprocessing.sh  # Analysis pipeline
│   └── template-siesta.sh     # Input file generation
├── siesta/                     # DFT infrastructure
│   ├── io_templates/          # SIESTA input templates
│   ├── pseudopotentials/      # Elemental pseudopotentials
│   ├── materials/             # Structure-specific calculations
│   └── python-utilities/      # Analysis scripts
├── lammps/                     # MD infrastructure
│   ├── data/                  # Atomic structure files
│   ├── in/                    # LAMMPS input scripts
│   └── potentials/            # Interatomic potentials
├── tests/                      # Test suite
├── docs/                       # Documentation
├── setup.py                   # Package configuration
├── pyproject.toml             # Build system
└── README.md                  # This file
```

---

## Testing & Validation

```bash
# Run test suite
pytest tests/

# CLI functionality tests
pytest tests/test_cli_basic.py
pytest tests/test_qmatsim_cli.py

# Integration tests (requires SIESTA/LAMMPS)
python -m qmatsim --help
```

### Validation Examples
- **Electronic Structure**: Band structure calculations for MoS₂ monolayers
- **Strain Engineering**: Systematic deformation studies up to 20% strain
- **Thermal Transport**: MD-based thermal conductivity calculations
- **Interface Physics**: Heterostructure modeling and charge transfer

---

## Performance & Scalability

- **HPC Optimization**: SLURM integration with intelligent resource allocation
- **Parallel Computing**: Multi-node DFT and MD simulations
- **Memory Management**: Efficient handling of large supercell calculations
- **Batch Processing**: Automated parameter sweeps and convergence studies

---

## Citation

If you use QMatSim in your research, please cite:

```bibtex
@software{qmatsim2025,
  title={QMatSim: Multiscale DFT + MD Simulation Framework},
  author={Alawein, Dr. Meshal},
  year={2025},
  url={https://github.com/alaweimm90/QMatSim},
  version={0.1.0},
  institution={University of California, Berkeley}
}
```

---

## Development

### Contributing
We welcome contributions! Please see our development guidelines:

```bash
# Fork and clone
git clone https://github.com/your-username/QMatSim.git
cd QMatSim

# Install development dependencies
pip install -e .[dev]

# Run tests before submitting
pytest tests/

# Submit pull request
```

### Architecture
- **Modular Design**: Clear separation between DFT, MD, and analysis components
- **Template System**: Flexible input file generation with variable substitution
- **Error Handling**: Comprehensive validation and failure recovery
- **Cross-Platform**: Python CLI with bash script backends for maximum compatibility

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
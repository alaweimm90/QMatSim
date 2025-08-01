# QMatSim: Advanced Strain Engineering Framework for 2D Quantum Materials

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-green.svg)](https://www.python.org/)
[![SIESTA](https://img.shields.io/badge/SIESTA-4.1+-blue.svg)](https://siesta-project.org/siesta/)
[![LAMMPS](https://img.shields.io/badge/LAMMPS-stable-red.svg)](https://www.lammps.org/)
[![Physical Review Materials](https://img.shields.io/badge/Phys.Rev.Materials-2025-brightgreen.svg)](https://journals.aps.org/prmaterials/)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#testing--validation)

*A cutting-edge multiscale simulation framework for strain-induced quantum phenomena in 2D materials — implementing advanced DFT + MD workflows with automated strain engineering to discover flat bands, lateral heterostructures, and emergent electronic phases in transition metal dichalcogenides.*

**Core scientific capabilities (fully implemented):**

- **Strain-Induced Physics**: Flat band emergence, hole localization, and lateral heterostructure formation
- **Electronic Structure**: Advanced DFT calculations with spin-orbit coupling and strain-dependent band engineering
- **Mechanical Deformation**: LAMMPS-based rippling, compression, and systematic strain protocols
- **Quantum Materials**: TMDCs (MoS₂, MoSe₂, WS₂, WSe₂) with comprehensive pseudopotential libraries
- **Multiscale Integration**: Seamless DFT-to-MD workflows for strain-electronic property correlations
- **HPC-Ready Automation**: SLURM integration with intelligent resource allocation and batch processing
- **Advanced Analysis**: Band structure engineering, LDOS mapping, and strain-dependent phase transitions

**Author**: Dr. Meshal Alawein ([meshal@berkeley.edu](mailto:meshal@berkeley.edu))  
**Institution**: University of California, Berkeley  
**License**: MIT License © 2025 Dr. Meshal Alawein — All rights reserved

---

## Project Overview

**QMatSim** implements the computational framework from "Strain-induced lateral heterostructures: Hole localization and the emergence of flat bands in rippled MoS₂ monolayers" (Alawein et al., Physical Review Materials 2025). This research-grade multiscale toolkit enables the discovery of strain-induced quantum phenomena in 2D materials through systematic DFT + MD simulations, revealing how mechanical deformation drives electronic phase transitions and emergent flat band physics in transition metal dichalcogenides.

<p align="center">
  <img src="docs/images/qmatsim_overview.png" alt="QMatSim Strain Engineering Framework" width="800"/>
  <br/>
  <em>Strain-induced flat band emergence and lateral heterostructure formation in rippled MoS₂</em>
</p>

### Key Features

🔬 **Strain-Induced Quantum Physics**: Automated discovery of flat bands and lateral heterostructures  
⚛️ **Advanced Electronic Structure**: DFT calculations with SOC for accurate band engineering  
🌊 **Mechanical Deformation Protocols**: Systematic rippling and compression strain studies  
🧮 **Multiscale Integration**: Seamless DFT-MD coupling for strain-electronic correlations  
⚙️ **HPC-Optimized Workflows**: SLURM automation with intelligent resource management  
📊 **Publication-Ready Analysis**: Advanced band structure and LDOS visualization tools  
🧪 **TMDC Materials Focus**: Complete libraries for MoS₂, MoSe₂, WS₂, WSe₂ systems  

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
# ➤ Strain-Induced Electronic Structure (DFT)
qmatsim relax --material MoS2 --structure 1x10_rectangular

# ➤ Mechanical Deformation Studies (MD)
qmatsim minimize --structure ripple10 --mode compress
qmatsim minimize --structure ripple10 --mode all

# ➤ Flat Band Discovery & Analysis
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## Scientific Modules

### Strain Engineering Engine
- **QMatSim Core**: Advanced strain-dependent electronic structure calculations
- **Flat Band Discovery**: Automated detection of strain-induced flat band emergence
- **Lateral Heterostructures**: Systematic mapping of strain-driven phase boundaries

### Quantum Materials Database
- **TMDC Libraries**: Complete MoS₂, MoSe₂, WS₂, WSe₂ material parameters
- **Pseudopotentials**: GGA, LDA, and GGA-SOC functionals with spin-orbit coupling
- **Strain Templates**: Pre-configured ripple geometries and compression protocols

### Multiscale Physics Solvers
- **Electronic Structure**: SIESTA-based DFT with advanced k-point sampling
- **Mechanical Deformation**: LAMMPS MD with realistic interatomic potentials
- **Coupling Protocols**: Automated strain transfer from MD to DFT calculations

### Advanced Analysis Suite
- **Band Structure Engineering**: Strain-dependent dispersion and flat band tracking
- **Hole Localization**: Spatial distribution analysis of strain-induced states
- **Phase Transition Mapping**: Systematic characterization of electronic phase boundaries
- **Publication Tools**: Berkeley-themed visualization with publication-quality figures

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
- **Flat Band Physics**: Strain-induced flat band emergence in rippled MoS₂ (reproduces Phys. Rev. Materials 2025)
- **Lateral Heterostructures**: Hole localization and electronic phase transitions
- **Strain Engineering**: Systematic deformation studies with up to 20% applied strain
- **Spin-Orbit Effects**: SOC-dependent band structure modifications in TMDCs
- **Multiscale Coupling**: DFT-MD correlation studies for strain-electronic property relationships

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
@article{alawein2025strain,
  title={Strain-induced lateral heterostructures: Hole localization and the emergence of flat bands in rippled MoS 2 monolayers},
  author={Alawein, Meshal and Ager, Joel W and Javey, Ali and Chrzan, DC},
  journal={Physical Review Materials},
  volume={9},
  number={2},
  pages={L021002},
  year={2025},
  publisher={APS}
}

@software{qmatsim2025,
  title={QMatSim: Advanced Strain Engineering Framework for 2D Quantum Materials},
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
````markdown
# **QMatSim: Multiscale DFT + MD Simulation Framework**

**QMatSim** is a modular and extensible multiscale simulation toolkit that integrates **Density Functional Theory (DFT)** and **Molecular Dynamics (MD)**. It combines **SIESTA** and **LAMMPS** workflows, providing support for flexible supercell geometries, strain-driven pipelines, and unified postprocessing across **Python**, **MATLAB**, and **Mathematica**.

---

## 🚀 **Key Features**

- **Unified CLI**: Single entry point (`qmatsim`) for all simulation stages.
- **Modular Workflows**: SIESTA and LAMMPS workflows for customization.
- **Supercell & Strain Simulation**: Template-based for simplicity.
- **SLURM Job Integration**: Auto-generated input decks for easy cluster submission.
- **Unified Postprocessing**: Includes band flattening, LDOS, stress-strain analysis.
- **Cross-Platform Postprocessing**: Supports **MATLAB**, **Mathematica**, and **Python**.
- **Easy Installation**: Installable via Python package (`pip install .`).

---

## 📦 **Project Structure**

```plaintext
QMatSim/
├── qmatsim/           # Python package
│   ├── main.py        # CLI logic (entry point)
│   └── __init__.py    # Package marker
│
├── scripts/           # Bash automation for DFT, MD, postprocessing
├── siesta/            # Materials, pseudopotentials, templates
├── lammps/            # Data/in/potentials for LAMMPS
│
├── analysis.py        # Python-based postprocessing
├── analysis.m         # MATLAB postprocessing
├── analysis.nb        # Mathematica postprocessing
│
├── tests/             # Minimal CLI test scaffolding
│   └── test_cli.py
│
├── setup.py           # Install metadata
├── pyproject.toml     # Build system configuration
└── README.md          # This file
````

---

## 🛠️ **Installation**

Clone the repository and install the package in development mode:

```bash
# Clone the repository
git clone https://github.com/alaweimm90/QMatSim.git
cd QMatSim

# Install in development mode
pip install -e .
```

Once installed, the `qmatsim` command-line tool will be available globally.

---

## 🔧 **CLI Usage**

### **DFT Relaxation (SIESTA)**

```bash
# Relaxation with SIESTA for MoS2 material
qmatsim relax --material MoS2 --structure 1x10_rectangular
```

### **MD Simulation**

```bash
# Compress-only MD simulation
qmatsim minimize --structure ripple10 --mode compress

# Full sequence MD simulation
qmatsim minimize --structure ripple10 --mode all
```

### **Postprocessing**

```bash
# Analyze MoS2 material
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## ✅ **Testing**

Run tests with **pytest**:

```bash
pytest tests/
```

---

## 📜 **License**

This project is distributed under the **MIT License**. See the `LICENSE` file for more details.

---

## 🧑‍💻 **Citation**

If you use **QMatSim** in your research, please cite it as follows:

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

## 🧪 **Example Test: `tests/test_cli.py`**

```python
import subprocess

def test_help_runs():
    """Ensure the CLI help command runs successfully."""
    result = subprocess.run(["python", "-m", "qmatsim", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "QMatSim CLI" in result.stdout
```

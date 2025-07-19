```markdown
# QMatSim: Multiscale DFT + MD Simulation Framework

**QMatSim** is a modular and extensible multiscale simulation toolkit for integrating Density Functional Theory (DFT) and Molecular Dynamics (MD), combining **SIESTA** and **LAMMPS** workflows. It supports flexible supercell geometries, strain-driven pipelines, and unified postprocessing across Python, MATLAB, and Mathematica.

---

## 🚀 Features

- ✅ Unified CLI entry point (`qmatsim`) for all simulation stages
- ✅ Modular SIESTA and LAMMPS workflows
- ✅ Template-based supercell and strain simulation
- ✅ SLURM job integration with auto-generated input decks
- ✅ Unified postprocessing: band flattening, LDOS, stress–strain
- ✅ MATLAB / Mathematica / Python postprocessing supported
- ✅ Installable Python package (`pip install .`)

---

## 📦 Project Structure

```

QMatSim/
├── qmatsim/           # Python package
│   ├── **main**.py    # CLI logic (entry point)
│   └── **init**.py    # Package marker
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
│   └── test\_cli.py
│
├── setup.py           # Install metadata
├── pyproject.toml     # Build system configuration
└── README.md          # This file

````

---

## 🛠️ Installation

```bash
# Clone and install in development mode
git clone https://github.com/alaweimm90/QMatSim.git
cd QMatSim
pip install -e .
````

You now have the `qmatsim` command-line tool available globally.

---

## 🔧 CLI Usage

```bash
# DFT relaxation (SIESTA)
qmatsim relax --material MoS2 --structure 1x10_rectangular

# MD simulation (compress-only or full sequence)
qmatsim minimize --structure ripple10 --mode compress
qmatsim minimize --structure ripple10 --mode all

# Postprocessing
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## ✅ Testing

```bash
pytest tests/
```

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` file.

---

## 🧑‍💻 Citation

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

## 🧪 Example Test: `tests/test_cli.py`

```python
import subprocess

def test_help_runs():
    """Ensure the CLI help command runs successfully."""
    result = subprocess.run(["python", "-m", "qmatsim", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "QMatSim CLI" in result.stdout
```

# **QMatSim: Multiscale DFT + MD Simulation Framework**

**QMatSim** is a modular simulation toolkit that integrates **Density Functional Theory (DFT)** and **Molecular Dynamics (MD)** using **SIESTA** and **LAMMPS**. It supports customizable supercells, strain-driven pipelines, SLURM integration, and unified postprocessing across **Python**, **MATLAB**, and **Mathematica**.

---

## 🚀 Features

- **Unified CLI** — Single command-line tool: `qmatsim`
- **Modular Workflows** — Customizable DFT (SIESTA) and MD (LAMMPS) pipelines
- **Supercell + Strain Templates** — Auto-configured lattice deformation setups
- **Cluster-Ready** — Auto-generates SLURM input decks
- **Cross-Platform Postprocessing** — MATLAB, Python, and Mathematica supported
- **Unified Analysis** — LDOS, band flattening, stress-strain, and energy tracking
- **Easy Installation** — `pip install .`

---

## 🧱 Project Structure

```plaintext
QMatSim/
├── qmatsim/           # Core Python CLI
│   ├── main.py
│   └── __init__.py
├── scripts/           # Automation scripts
├── siesta/            # Templates, materials, pseudopotentials
├── lammps/            # Potentials, data/in files
├── analysis.py        # Python postprocessing
├── analysis.m         # MATLAB postprocessing
├── analysis.nb        # Mathematica postprocessing
├── tests/             # CLI testing
│   └── test_cli.py
├── setup.py
├── pyproject.toml
└── README.md
```

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/alaweimm90/QMatSim.git
cd QMatSim

# Install in development mode
pip install -e .
```

After installation, the `qmatsim` CLI will be globally available.

---

## 🔧 Command-Line Usage

### ➤ DFT Relaxation (SIESTA)

```bash
qmatsim relax --material MoS2 --structure 1x10_rectangular
```

### ➤ MD Minimization

```bash
qmatsim minimize --structure ripple10 --mode compress     # Compress-only
qmatsim minimize --structure ripple10 --mode all          # Full sequence
```

### ➤ Postprocessing

```bash
qmatsim analyze --material MoS2 --structure 1x10_rectangular
```

---

## ✅ Testing

Run test suite with:

```bash
pytest tests/
```

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 🔖 Citation

Please cite **QMatSim** using the following `CITATION.cff`:

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

## 🧪 Example Test (`tests/test_cli.py`)

```python
import subprocess

def test_help_runs():
    """Check if `qmatsim --help` executes successfully."""
    result = subprocess.run(["python", "-m", "qmatsim", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "QMatSim CLI" in result.stdout
```

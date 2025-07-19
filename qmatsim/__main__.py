#!/usr/bin/env python3
# __main__.py — Main CLI entry point for QMatSim framework

import argparse
import subprocess
import sys
from pathlib import Path

# ---- DFT ----
def run_dft(args):
    subprocess.run(["bash", "scripts/run-DFT.sh", args.material, args.structure], check=True)

# ---- MD ----
def run_md(args):
    structure = args.structure
    mode = args.mode
    data_file = Path(f"lammps/data/{structure}.data")

    if not data_file.exists():
        print(f"❌ Missing data file: {data_file}")
        sys.exit(1)

    if mode == "compress":
        input_file = Path("lammps/in/compress_y.in")
        if not input_file.exists():
            print(f"❌ Missing input script: {input_file}")
            sys.exit(1)
        subprocess.run(["bash", "scripts/compress-MD.sh", structure], check=True)

    elif mode == "all":
        missing = []
        for fname in ["compress_y.in", "deformation.in", "minimization.in"]:
            if not Path(f"lammps/in/{fname}").exists():
                missing.append(fname)
        if missing:
            print(f"❌ Missing LAMMPS input files: {', '.join(missing)}")
            sys.exit(1)
        subprocess.run(["bash", "scripts/run-MD.sh", structure], check=True)
    else:
        print("⚠️ Unknown or unsupported mode. Use '--mode compress' or '--mode all'.")
        sys.exit(1)

# ---- Postprocessing ----
def run_post(args):
    subprocess.run(["bash", "scripts/run-postprocessing.sh", args.material, args.structure], check=True)

# ---- CLI Entrypoint ----
def main():
    parser = argparse.ArgumentParser(description="QMatSim CLI — Multiscale DFT + MD toolkit")
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # DFT
    p_dft = subparsers.add_parser("relax", help="Run SIESTA DFT simulation")
    p_dft.add_argument("--material", required=True, help="Material name (e.g. MoS2)")
    p_dft.add_argument("--structure", required=True, help="Structure (e.g. 1x10_rectangular)")
    p_dft.set_defaults(func=run_dft)

    # MD
    p_md = subparsers.add_parser("minimize", help="Run LAMMPS MD simulation")
    p_md.add_argument("--structure", required=True, help="Structure name (e.g. ripple10)")
    p_md.add_argument("--mode", choices=["compress", "all"], default="all", help="MD mode [default: all]")
    p_md.set_defaults(func=run_md)

    # Postprocessing
    p_post = subparsers.add_parser("analyze", help="Run DFT postprocessing")
    p_post.add_argument("--material", required=True)
    p_post.add_argument("--structure", required=True)
    p_post.set_defaults(func=run_post)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)

if __name__ == "__main__":
    main()

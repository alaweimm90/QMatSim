#!/bin/bash
# === compress-MD.sh ===
# Usage: ./compress-MD.sh <structure>

structure="$1"
LAMMPS_EXE="lmp_mpi"

if ! command -v "$LAMMPS_EXE" >/dev/null 2>&1; then
    echo "Error: $LAMMPS_EXE not found in PATH" >&2
    exit 1
fi

if [ -z "$structure" ]; then
    echo "Usage: ./compress-MD.sh <structure>"
    exit 1
fi

if [ -f compress_y.in ]; then
    "$LAMMPS_EXE" -in compress_y.in > compress_y.out 2>&1
    echo "Compression simulation complete for $structure"
else
    echo "compress_y.in not found. Nothing to run."
    exit 1
fi

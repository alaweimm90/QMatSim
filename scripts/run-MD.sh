# === run-MD.sh ===
# Usage: ./run-MD.sh <structure>

structure="$1"
LAMMPS_EXE="lmp_mpi"

if ! command -v "$LAMMPS_EXE" >/dev/null 2>&1; then
    echo "Error: $LAMMPS_EXE not found in PATH" >&2
    exit 1
fi

if [ -z "$structure" ]; then
    echo "Usage: ./run-MD.sh <structure>"
    exit 1
fi

found_any_input=false
for mode in compress-y.in deformation.in minimization.in; do
    if [ -f "$mode" ]; then
        found_any_input=true
        "$LAMMPS_EXE" -in "$mode" > "${mode%.in}.out" 2>&1
    fi
done

if [ "$found_any_input" = false ]; then
    echo "No LAMMPS input files found. Skipping simulation."
    exit 0
fi

echo "SIMULATION DONE" > completed.output

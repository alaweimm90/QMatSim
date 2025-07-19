#!/bin/bash
# === run-DFT.sh ===
# Usage: ./run-DFT.sh <material> <structure>

material="$1"
structure="$2"

supercell="$structure"
type="Monolayer"
functional="GGA"
SOC="F"
RELAXED="F"
RelaxRun="T"
StaticRun="T"
BandsRun="T"
LDOSRun="T"
partition="2"
strains=("0")

targetDir="siesta/materials/$material/$type/$structure/$supercell"
template_io="siesta/io_templates"
pseudopath="siesta/pseudopotentials"

copy_material_files() {
    local mat="$1"; local func="$2"; local soc="$3"
    case $mat in
        MoS2) ext1="Mo"; ext2="S";;
        MoSe2) ext1="Mo"; ext2="Se";;
        WS2) ext1="W"; ext2="S";;
        WSe2) ext1="W"; ext2="Se";;
        *) echo "Unknown material $mat"; exit 1;;
    esac

    if [ "$soc" = "T" ]; then
        cp $pseudopath/${func}-SOC/$ext1.psf .
        cp $pseudopath/${func}-SOC/$ext2.psf .
    else
        cp $pseudopath/${func}/$ext1.psf .
        cp $pseudopath/${func}/$ext2.psf .
    fi
}

set_partition_variables() {
    accountVAR="co_msedcc"
    paritionVAR="savio2_bigmem"
    QoSVAR="savio_lowprio"
    nodesVAR="1"
    cpusVAR="24"
}

copy_material_files "$material" "$functional" "$SOC"
mkdir -p "$targetDir/0"

for strain in "${strains[@]}"; do
    simulation="Relaxation"
    ./scripts/generate-input.sh "$material" "$type" "$structure" "$supercell" "$simulation" "$functional" "$strain" "$SOC"
    mv input.fdf 1-Relaxation.tmp
    cat 1-Relaxation.tmp $template_io/Relaxation-io.fdf > 1-Relaxation.fdf

    simulation="Static"
    ./scripts/generate-input.sh "$material" "$type" "$structure" "$supercell" "$simulation" "$functional" "$strain" "$SOC"
    mv input.fdf 2-Static.tmp
    cat 2-Static.tmp $template_io/Static-io.fdf > 2-Static.fdf

    simulation="Bands"
    ./scripts/generate-input.sh "$material" "$type" "$structure" "$supercell" "$simulation" "$functional" "$strain" "$SOC"
    mv input.fdf 3-Bands.tmp
    cat 3-Bands.tmp $template_io/Bands-io.fdf > 3-Bands.fdf

    simulation="LDOS"
    ./scripts/generate-input.sh "$material" "$type" "$structure" "$supercell" "$simulation" "$functional" "$strain" "$SOC"
    mv input.fdf LDOS.tmp
    cat LDOS.tmp $template_io/Static-io.fdf > LDOS.fdf

    rm *.tmp

    cp scripts/template-siesta.sh job.sh
    set_partition_variables "$partition"

    sed -i "s/typeVAR/$type/g; s/materialVAR/$material/g; s/functionalVAR/$functional/g; s/structureVAR/$structure/g; s/supercellVAR/$supercell/g; s/strainVAR/$strain/g; s/socVAR/$SOC/g; s/accountVAR/$accountVAR/g; s/paritionVAR/$paritionVAR/g; s/QoSVAR/$QoSVAR/g; s/nodesVAR/$nodesVAR/g; s/cpusVAR/$cpusVAR/g; s/RelaxVAR/$RelaxRun/g; s/StaticVAR/$StaticRun/g; s/BandsVAR/$BandsRun/g; s/LDOSVAR/$LDOSRun/g" job.sh

    mv *.fdf *.sh *.psf "$targetDir/0/"
    cp "$targetDir/Structure/$material.STRUCT_IN" "$targetDir/0/$material.STRUCT_IN"

    cd "$targetDir/0"
    sbatch -o job.out -e job.err job.sh
    cd -
done

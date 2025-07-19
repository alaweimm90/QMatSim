#!/bin/bash
cp ~/SIESTA/referenceFiles/findsym_sample-copy1.in findsym_sample.in

# Material

material="MoS2"
titleVAR="Symmetrized coordinates"
latticeTolVAR="0.00001"
positionsTolVAR="0.00001"
occupationTolVAR="0.00001"
#centeringVAR="P"

# Read the lattice parameters from MoS2.STRUCT_OUT
a1=$(awk 'NR==1 {printf "%s %s %s", $1, $2, $3}' MoS2.STRUCT_OUT)
a2=$(awk 'NR==2 {printf "%s %s %s", $1, $2, $3}' MoS2.STRUCT_OUT)
a3=$(awk 'NR==3 {printf "%s %s %s", $1, $2, $3}' MoS2.STRUCT_OUT)
NatomsVAR=$(awk 'NR==4 {print $1}' MoS2.STRUCT_OUT)
atomTypesVAR=$(awk 'NR>=5 {printf "%s ", $1}' MoS2.STRUCT_OUT)
atomsPositionsVAR=$(awk 'NR>=5 {print $3, $4, $5}' MoS2.STRUCT_OUT)

# Replace latticeVAR in findsym_sample.in
sed -i "s|titleVAR|${titleVAR}|" findsym_sample.in
sed -i "s|latticeTolVAR|${latticeTolVAR}|" findsym_sample.in
sed -i "s|positionsTolVAR|${positionsTolVAR}|" findsym_sample.in
sed -i "s|occupationTolVAR|${occupationTolVAR}|" findsym_sample.in
sed -i "s|latticeVAR|${a1}\n${a2}\n${a3}|" findsym_sample.in
#sed -i "s|centeringVAR|${centeringVAR}|" findsym_sample.in
sed -i "s|NatomsVAR|${NatomsVAR}|" findsym_sample.in
sed -i "s|atomTypesVAR|${atomTypesVAR}|" findsym_sample.in
awk -v var="$atomsPositionsVAR" '{gsub("atomsPositionsVAR", var)}1' findsym_sample.in > temp && mv temp findsym_sample.in

~/bin/findsym findsym_sample.in > MoS2-symmetrized.cif

awk '/_atom_site_fract_symmform/{flag=1; next} flag{print $2, $5, $6, $7}' MoS2-symmetrized.cif > MoS2.tmp
awk '{ if ($1 == 2) { $1 = "2 16" } else if ($1 == 1) { $1 = "1 42" } print }' MoS2.tmp > MoS2.modified.tmp
head -n 4 MoS2.STRUCT_OUT > MoS2-symmetrized.STRUCT_IN && cat MoS2.modified.tmp >> MoS2-symmetrized.STRUCT_IN
sed -i '$d' MoS2-symmetrized.STRUCT_IN

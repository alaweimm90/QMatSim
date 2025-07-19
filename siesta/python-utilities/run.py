import os

# List of (a11, a22) values for strains 0 to 20
a_values = [
    (3.32635, 54.54500),
    (3.38700, 53.91000),
    (3.39605, 53.28400),
    (3.33982, 52.66700),
    (3.34259, 52.06600),
    (3.34156, 51.46300),
    (3.34128, 50.85700),
    (3.34286, 50.26000),
    (3.34284, 49.66300),
    (3.34298, 49.08600),
    (3.34476, 48.51100),
    (3.34436, 47.94600),
    (3.34539, 47.36800),
    (3.34561, 46.80100),
    (3.34560, 46.23300),
    (3.34571, 45.68300),
    (3.34705, 45.08600),
    (3.34782, 44.48800),
    (3.34746, 43.89900),
    (3.35479, 43.32900),
    (3.355093, 42.77900)
]

def transform_coordinates(old_a11, old_a22, new_a11, new_a22, old_a33, x, y, z):
    new_x = x * new_a11 / old_a11
    new_y = y * new_a22 / old_a22
    new_z = z  # Keep z unchanged
    return new_x, new_y, new_z

def process_file(file_path, new_a11, new_a22):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    try:
        # Extract lattice vectors and coordinates
        a11, a12, a13 = map(float, lines[0].split())
        a21, a22, a23 = map(float, lines[1].split())
        a31, a32, old_a33 = map(float, lines[2].split())
        num_atoms = int(lines[3].strip())

        # Prepare new lattice vectors (only a11 and a22 are changed)
        new_lattice_vectors = [
            f"{new_a11} {a12} {a13}\n",
            f"{a21} {new_a22} {a23}\n",
            f"{a31} {a32} {old_a33}\n"
        ]

        # Process the coordinates
        new_coordinates = []
        for i in range(4, 4 + num_atoms):
            elements = lines[i].split()
            if len(elements) != 5:
                print(f"Warning: Skipping malformed line {i+1} in {file_path}")
                continue

            atom_id = int(elements[0])
            atomic_number = int(elements[1])
            x, y, z = map(float, elements[2:])

            # Transform coordinates
            new_x, new_y, new_z = transform_coordinates(a11, a22, new_a11, new_a22, old_a33, x, y, z)
            new_coordinates.append(f"{atom_id} {atomic_number} {new_x:.8f} {new_y:.8f} {new_z:.8f}\n")

        # Write the modified content back to the original file
        with open(file_path, 'w') as f:
            f.writelines(new_lattice_vectors)
            f.write(str(num_atoms) + "\n")
            f.writelines(new_coordinates)

        print(f"Processed and updated {file_path}")

    except (ValueError, IndexError) as e:
        print(f"Error processing {file_path}: {e}")

def main():
    new_a33_value = 50.00000  # Set the desired a33 value (but it won't change)
    for strain in range(21):  # Loop from 0 to 20
        new_a11, new_a22 = a_values[strain]
        structure_path = f"{strain}/Structure/"
        
        for root, _, files in os.walk(structure_path):
            for file in files:
                if file.endswith(".STRUCT_IN") or file.endswith(".STRUCT_OUT"):
                    file_path = os.path.join(root, file)
                    process_file(file_path, new_a11, new_a22)

if __name__ == "__main__":
    main()

import os

def transform_coordinates(old_a33, new_a33, x, y, z):
    """
    Transform the z-coordinate based on the new lattice vector.
    """
    new_z = z * old_a33 / new_a33
    return x, y, new_z

def process_file(file_path, new_a33):
    """
    Process a .STRUCT_IN or .STRUCT_OUT file by updating the lattice vectors and transforming coordinates.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Extract lattice vectors and coordinates
    a11, a12, a13 = map(float, lines[0].split())
    a21, a22, a23 = map(float, lines[1].split())
    a31, a32, old_a33 = map(float, lines[2].split())
    num_atoms = int(lines[3].strip())

    # Prepare new lattice vectors
    new_lattice_vectors = [
        f"{a11} {a12} {a13}\n",
        f"{a21} {a22} {a23}\n",
        f"{a31} {a32} {new_a33}\n"
    ]

    # Process the coordinates
    new_coordinates = []
    for i in range(4, 4 + num_atoms):
        elements = lines[i].split()
        atom_id = int(elements[0])
        atomic_number = int(elements[1])
        x, y, z = map(float, elements[2:])

        # Transform coordinates
        new_x, new_y, new_z = transform_coordinates(old_a33, new_a33, x, y, z)
        new_coordinates.append(f"{atom_id} {atomic_number} {new_x:.8f} {new_y:.8f} {new_z:.8f}\n")

    # Write the modified content back to the original file
    with open(file_path, 'w') as f:
        f.writelines(new_lattice_vectors)
        f.write(str(num_atoms) + "\n")
        f.writelines(new_coordinates)

    print(f"Processed and updated {file_path}")

def main(new_a33):
    # Walk through all files in current directory and subdirectories
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".STRUCT_IN") or file.endswith(".STRUCT_OUT"):
                file_path = os.path.join(root, file)
                process_file(file_path, new_a33)

if __name__ == "__main__":
    # Set the new a33 value
    new_a33_value = 90.00000  # Replace with your desired a33 value
    main(new_a33_value)


    

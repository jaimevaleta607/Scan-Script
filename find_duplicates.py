import os
import hashlib

# Function to generate hash for a file
def generate_file_hash(file_path, chunk_size=1024):
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                sha256_hash.update(chunk)
    except FileNotFoundError:
        # Handle case where file is deleted or inaccessible
        return None
    return sha256_hash.hexdigest()

# Function to find duplicate files
def find_duplicates(root_directory):
    # Dictionary to store file hashes and their corresponding paths
    hash_map = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # Generate hash for the current file
            file_hash = generate_file_hash(file_path)
            
            if file_hash:
                # If the hash already exists in the map, it's a duplicate
                if file_hash in hash_map:
                    duplicates.append((file_path, hash_map[file_hash]))
                else:
                    # If not, add it to the map
                    hash_map[file_hash] = file_path

    return duplicates

# Main function to initiate the duplicate check
def main():
    root_directory = input("Enter the root directory to search for duplicates: ")
    
    duplicates = find_duplicates(root_directory)
    
    # Specify output file
    output_file = "duplicates_output.txt"
    
    # Open the file to write results
    with open(output_file, "w") as f:
        if duplicates:
            f.write("Duplicate files found:\n")
            for duplicate, original in duplicates:
                f.write(f"Duplicate: {duplicate}\nOriginal: {original}\n\n")
            print(f"Results written to {output_file}")
        else:
            f.write("No duplicate files found.\n")
            print(f"No duplicate files found. Results written to {output_file}")

if __name__ == "__main__":
    main()

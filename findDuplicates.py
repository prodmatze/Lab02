import os
import hashlib
import glob
def get_files(folder_path, file_extension):
    file_pattern = os.path.join(folder_path, file_extension)
    files = glob.glob(file_pattern)
    return files

folder_path = "/Users/mathieuwassmuth/dup_test"

file_extension = "*.png"
files = get_files(folder_path, file_extension)

# calculates the md5 hash of a file
def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        file_hash = hashlib.md5(file_data).hexdigest()
    return file_hash

def find_duplicates(files):
    file_hashes = {}
    duplicate_files = []

    for file in files:
        file_md5_hash = calculate_hash(file)

        if file_md5_hash in file_hashes:
            duplicate_files.append(file)
        else:
            file_hashes[file_md5_hash] = file

    return duplicate_files

duplicate_files = find_duplicates(files)
print("Duplicate files: ", duplicate_files)


def delete_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except OSError as e:
            print(f"Error deleting file {file}: {e}")

##the following line deletes all duplicates
#delete_files(duplicate_files)





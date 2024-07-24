import glob
import os

# Directory path
download_path = '/YOUR/DOWNLOAD/DIRECTORY/PATH'

# Get a list of all items in the specified directory
items = glob.glob(os.path.join(download_path, '*'))

# Filter the list to include only files
file_paths = [item for item in items if os.path.isfile(item)]

print('Number of files found: ' + str(len(file_paths)))

# Check if any files are found
if not file_paths:
    print('No files found.')
else:
    # Iterate over each file
    for file_path in file_paths:
        # Get the file extension without the leading dot
        file_ext = os.path.splitext(file_path)[1][1:]
        
        # If file has no extension, use 'NO_EXT'
        if not file_ext:
            file_ext = 'NO_EXT'
        
        # Define the target directory based on the file extension
        target_dir = os.path.join(download_path, file_ext.upper())
        
        # Create the target directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Move the file to the target directory
        file_name = os.path.basename(file_path)
        new_path = os.path.join(target_dir, file_name)
        os.rename(file_path, new_path)
        
        print(f'Item: {file_path} has been moved to {new_path}!')

print("Files have been organized.")

import os

def print_directory_structure(path, indent=0):
    """
    Prints the structure of the directory at the specified path.
    
    :param path: The path to the directory.
    :param indent: Indentation level for nested directories.
    """
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    # Check if the path is a directory
    if not os.path.isdir(path):
        print(f"The path '{path}' is not a directory.")
        return
    
    # Print the directory name
    print("  " * indent + f"Directory: {os.path.basename(path)}")

    # Loop through the contents of the directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # If it's a directory, recursively call the function to print its structure
            print_directory_structure(item_path, indent + 1)
        else:
            # If it's a file, just print the file name
            print("  " * (indent + 1) + f"File: {item}")

# Example usage
if __name__ == "__main__":
    # Path to the directory you want to print the structure of
    directory_path = input("Enter the directory path: ")
    print_directory_structure(directory_path)

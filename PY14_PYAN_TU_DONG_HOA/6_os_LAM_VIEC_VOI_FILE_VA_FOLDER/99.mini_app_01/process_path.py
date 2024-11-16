import sys

def get_path_length(path):
    return len(path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        path_length = get_path_length(folder_path)
        print(f"The length of the selected folder path is: {path_length}")
    else:
        print("No folder path provided.")
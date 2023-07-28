import os
import multiprocessing
import sys

def count_files(directory):
    """Count all files in a directory, including in its subdirectories."""
    count = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        count += len(filenames)
    return directory, count

def get_immediate_subdirectories(parent_dir):
    """Return a list of immediate subdirectories."""
    return [os.path.join(parent_dir, name) for name in os.listdir(parent_dir) 
            if os.path.isdir(os.path.join(parent_dir, name))]

def get_directories_files_counts(dirs):
    """Get counts of files in multiple directories using parallel processing."""
    with multiprocessing.Pool() as pool:
        dir_counts = pool.map(count_files, dirs)
    return dir_counts

if __name__ == "__main__":
    parent_directory = sys.argv[1]  # Get directory from command line argument

    directories = get_immediate_subdirectories(parent_directory)

    dir_file_counts = get_directories_files_counts(directories)

    for dir, count in dir_file_counts:
        print(f"{dir}: {count} files")

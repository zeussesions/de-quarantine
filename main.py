import os
import subprocess

def count_items(directory):
    num_files = 0
    num_dirs = 0
    
    for root, dirs, files in os.walk(directory):
        num_dirs += len(dirs)
        num_files += len(files)
    
    return num_dirs, num_files

def remove_attr(directory):
    print(count_items(directory)[0] + " items to de-quarantine")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            subprocess.run(["sudo", "xattr", "-rd", "com.apple.quarantine", file_path])

if __name__ == '__main__':
    os.system("clear")
    dir_path = input("Enter the directory where your plugins are stored: ").strip()
    os.system("clear")
    print("Running Script...")
    print("if this message is here it means the script is doing things in the background. Don't worry if nothing is happening!")
    
    remove_attr(dir_path)

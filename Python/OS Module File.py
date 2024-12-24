#os module file services
import os

def main() -> None:
    print("Current Working Directory:", os.getcwd())
    with open('example_file.txt', 'w') as f:
        f.write("This is an example file.")
    print("File exists:", os.path.exists('example_file.txt'))
    os.rename('example_file.txt', 'renamed_file.txt')
    print("Renamed the file to 'renamed_file.txt'")
    print("File exists after renaming:", os.path.exists('renamed_file.txt'))
    os.remove('renamed_file.txt')
    print("Removed the file 'renamed_file.txt'")
    print("File exists after removal:", os.path.exists('renamed_file.txt'))
    print("Files in the current directory:", os.listdir())

main()

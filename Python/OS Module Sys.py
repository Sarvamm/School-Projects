"""os module system services"""
import os

def main() -> None:
    print("Current Working Directory:", os.getcwd())
    os.chdir("C:/") 
    print("Changed Working Directory:", os.getcwd())
    print("Contents of the Directory:", os.listdir())
    print("Current Process ID:", os.getpid())
    print("Parent Process ID:", os.getppid())
    print("OS Name:", os.name)
    os.system("echo this is a text message")
    print("Number of CPUs:", os.cpu_count())

main()

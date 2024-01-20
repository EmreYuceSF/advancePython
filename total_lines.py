"""
Write a program that expects pathnames as 
arguments and creates a pool of workers to all at 
once count how many lines long each file is
"""

import subprocess
import concurrent.futures
import sys
import os



def get_path_names()->list:
    """
    function gets absolute pathname/s from the user.
    user can enter pathname as a command line argument or as an input variable.
    usage for multiple pathname user should enter pathnames separating by a single white space.
    """
    if len(sys.argv) == 1:
        return input("enter the path names you want to check: ").split(" ")
    else:
        return (sys.argv[1:])


def collect_files(paths:list) -> list:
    """
    Goes through the list of paths provided as arguments and collects the list of files in those paths.
    The function returns a list of file paths with the parent directory path as a prefix.
    """
    files_with_suffix = []
    for path in paths:
        # first we check if path is exist
        if (os.path.exists(path)): 
            # fuction allows directory as an argument
            # we check if is an directory
            if (os.path.isdir(path)):
                #since it is a directory we list every file and sub-directory and with split method we store them in a list variable 
                files = subprocess.run(f"ls -1 {path}" , shell=True, text=True, capture_output=True)
                files = files.stdout.split("\n") 
                for i in range(len(files)):   
                    files_with_suffix.append(f"{path}/{files[i]}")
            # if path goes to a file we directly append that to our list        
            elif(os.path.isfile(path)):
                files_with_suffix.append(path)
        # gives the warning if path is not exist
        else:
            print(f"'{path}' is not an exist path!")

    return files_with_suffix

def length_of_file(file):
    """
    function goes to file and gets the number of lines if file is readable text base file
    """
    # Exceptions are used to eliminate any unreadable files or permission or Directories  
    try:
        with open(file, 'r') as data:
            try:
                lines = data.readlines()
                return len(lines)
            except UnicodeDecodeError:
                pass
    except IsADirectoryError:
        pass
    except PermissionError:
            print(f"There is no permission for '{file}'.")



def main():
    # this is the part workers are being created for each file to check total line numbers 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        paths = collect_files(get_path_names())
        results = zip(executor.map(length_of_file, paths),paths) 

        #for a nicer output some formatting has been used
        print("\n\n{:15}{}{:30}{}".format("","---[PATH]---","","---[TOTAL LINE]---"))
        print("-"*100)                    
        for result, path in results:
            if result:
                print(f"{path:60} ----> {result}")


if __name__=="__main__":
    main()
    




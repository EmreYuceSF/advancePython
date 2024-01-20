import subprocess
import concurrent.futures
import sys
import os


def get_path_names(): 
    """
    Gets Only path name/s as a command line argument
    You can put path to directory or a file
    """
    if len(sys.argv) == 1:
         print("Usage: Please provide the path name/s as a command line argument.\n"
              "Example:\n"
              "$ python3 ./thisprogram.py /Students/Someone/DirectoryOrFile\n"
              "Note: You can specify one or more paths separated by spaces.")
         sys.exit(1)
    else:
        return (sys.argv[1:])
    
    
# From Instructor’s notes 
def check(file):
    try:
        open(file).read()
        return True
    except UnicodeDecodeError:
        return False
    except IsADirectoryError:
        return False
    except:
        return False    
    
#from earlier assignmet
def collect_files(paths:list) -> list:
    """
    Goes through the list of paths provided as argument and collects the list of files in those paths.
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
                    if check(uniPath:=(f"{path}/{files[i]}")):
                        # we append path if it is in UTF-8 format   
                        files_with_suffix.append(uniPath)      
            elif(os.path.isfile(path)):
                files_with_suffix.append(path)
        # gives the warning if path is not exist
        else:
            print(f"'{path}' is not an exist path!")
    return files_with_suffix





def unicode_point_to_byte(unicode_points):
    # This function change unicode point to byte 
    # unicode point is the presentations of chars in numbers in decimal(base-10).
    # Example "A" -> 0-1000001 (1 bit for itself) (7 bits for character) -> 1*2**6 + 0*2**5 + ...0*2**1 + 1*2**0 -> 65   
    if unicode_points < 2**7:  # 0_*******  = max = 127 (1+2+4+8+16+32+64)
        return 1;
    elif unicode_points < 2**11: # 110_***** 10_******  olny *'s can represent a new character rest of the binary digits is being used to identify itself 
        return 2;
    elif unicode_points < 2**16: # 1110_**** 10_****** 10_****** 
        return 3;
    elif unicode_points <2**21:  # 11110_*** 10_****** 10_****** 10_******  
        return 4;

    
# Function to calculate the mean byte for each character in a file
def get_mean_byte_of_file_for_each_character(file):
    
    byte_total = 0
    char_count = 0
    
    # for each character we are increasing the char_count by one and 
    # increarsing the byte_total by the byte of the character  
    with open(file, "r", encoding="utf-8") as data:
        document  = data.read()
        for char in document:
            char_count += 1;
            unicode_point = ord(char)
            byte_total += unicode_point_to_byte(unicode_point)
    # char_count != 0 part will handle the empty files
    return (byte_total / char_count) if char_count != 0 else 0
     

    
    
def main():
    a = ""
  
    with concurrent.futures.ThreadPoolExecutor() as executor:
        paths = collect_files(get_path_names()) 
        results = zip(executor.map(get_mean_byte_of_file_for_each_character, paths), paths)
        print(f"\n{a:5}*** PATH ***{a:27}*** Avg Byte Per Character ***")
        print("-"*75)
        for result in results:
             print(f".../{'/'.join((result[1].split('/'))[-2:]):50} {result[0]:.3f}")
        
     
    

if __name__ == "__main__":
    main()

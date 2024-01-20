import csv
import json
import sys


"""
    This program accepts a single command line argument, which should be the path to a file with a ".csv" extension.
    It reads the CSV file, translates each line into JSON format, and creates a list of dictionaries.
    Each dictionary corresponds to a row, with column names as keys and row data as values.
    
    Usage: Enter a path to a CSV file as a command line argument and run the program.
    
"""

def get_file():
    """
    get_file function takes the path from command line and checks if it is leading to the expected file format 
    and than just returns opened CSV object
    """
    # we make sure there is exactly one path passed as an argument
    if (len(sys.argv)!=2):
        print("Usage: Enter a path to csv file as an argument and run the program")
        sys.exit(1)
    # we make sure the format is CSV, we check the last four character to confirm that    
    elif sys.argv[1][-4:] != ".csv":
        print("Usage: Make sure you enter a path to csv file.")
        sys.exit(1)
    else:
        # we get opened CSV file and we make sure we get support the unicode characters
        file =  open(sys.argv[1], 'r', newline='', encoding='utf-8')
        return file


        
def set_data_to_true_form(data):
    """
    since reading from a file returns only string object I wanted to change it any other possible form 
    it becomes int object if possible or float object if possible and rest remains string 
    and most importantly function changes empty parts to None.
    """
    if data == '':
        return None;
    try:
        data = int(data)
    except:
        pass
    try:
        if isinstance(data, int):
            pass
        else:
            data = float(data)
    except:
        pass            
    return data
 
 
        
def create_list_of_dictionary(file):
    # Obtain the header, which contains the column names.
    header = next(csv_file:=csv.reader(file))
    # After extracting the column names from the generator, we convert the remaining data into a list of rows.
    data = list(csv_file)
    # I aim for the final result to be a list of rows,
    # where each row is represented in dictionary format. The dictionaries have column names as keys and the corresponding row data as values for the respective keys
    list_from_csv = [{header[col_i].strip():set_data_to_true_form(data[row_i][col_i]) for col_i in range(len(header))}  for row_i in range(len(data))]
    # file is closed and no data leaking
    file.close()
    return list_from_csv
    


def dict_to_json(alist):
    json_form =  json.dumps(alist, ensure_ascii=False)
    return json_form 
 
           
            
if __name__ == "__main__":      
    json_file = dict_to_json(create_list_of_dictionary(get_file()))
    print(json_file)
  
    

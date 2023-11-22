import pandas as pd
from matplotlib import pyplot as plt

#File Path Input
file_path=input("Enter the file Path: ")
final_file_path=file_path.replace("\\","/")
#File reading
try:
    file_read=pd.read_excel(final_file_path,header=0)
    print(file_read)
except FileNotFoundError:
    print(f"File is Not Found at {file_path}")
except Exception as e:
    print(f"An Error Occured {e}")


# Written by Matt Duggan 05/02/2024

import tkinter as tk
from tkinter import filedialog

def remove_black(text_file):
    lines = text_file.split('\n')
    removed_lines = [line for line in lines if 'BL' not in line]
    return '\n'.join(removed_lines)

# %% Envoke the program
# input: File Path
# output: New file in same path with black removed from a standard EDL 
def main():
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    EDL_path = filedialog.askopenfilename()
    
    with open(EDL_path, "r") as file:
        EDL_contents = file.read()
        cleaned_EDL = remove_black(EDL_contents)
    
    with open(EDL_path[:-4]+"_cleaned"+".edl", "w") as file_new:
        file_new.write(cleaned_EDL)

if __name__ == "__main__":
    main()



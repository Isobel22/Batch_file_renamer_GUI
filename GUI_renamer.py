from Tkinter import *
import glob, os


root = Tk()  # root (main) window
main = Frame(root)  # create frame
main.pack(side='top')  # pack frame in main window
text = Label(main, text=u'--------------BATCH RENAMER---------------', font=(20))  # Header
text.pack()
text = Label(main, text=u'''Script written by Misha.  

This script will batch rename all files of selected extension in selected directory.
New name will be in format 'New_name001', depending on user-defined name pattern and desired number of digits.
''')  # Description
text.pack()


path_label = Label(main)  # Set directory label
path_label.pack()
def_path_text = Label(path_label, width=20, anchor=W, text='Set source directory:')
def_path_text.pack(side='left')
def_path = StringVar() # variable to be attached to r_entry
def_path.set('C:\Data\Python\doc') # default value
def_path_entry = Entry(path_label, width=20, textvariable=def_path)
def_path_entry.pack(side='left', fill=X)

extension_label = Label(main)  # Set extension label
extension_label.pack()
def_extension_text = Label(extension_label, width=20, anchor=W, text='Set affected extension:')
def_extension_text.pack(side='left')
def_extension = StringVar() # variable to be attached to r_entry
def_extension.set('.JPG') # default value
def_extension_entry = Entry(extension_label, width=20, textvariable=def_extension)
def_extension_entry.pack(side='left', fill=X)

filename_label = Label(main)  # Set filename label
filename_label.pack()
def_filename_text = Label(filename_label, width=20, anchor=W, text='Set new file name pattern:')
def_filename_text.pack(side='left')
def_filename = StringVar() # variable to be attached to r_entry
def_filename.set('Renamed_file') # default value
def_filename_entry = Entry(filename_label, width=20, textvariable=def_filename)
def_filename_entry.pack(side='left')

digits_label = Label(main)  # Set number of digits label
digits_label.pack()
def_number_of_digits_text = Label(digits_label, width=20, anchor=W, text='Set number of digits:')
def_number_of_digits_text.pack(side='left')
def_number_of_digits = StringVar() # variable to be attached to r_entry
def_number_of_digits.set('2') # default value
def_number_of_digits_entry = Entry(digits_label, width=20, textvariable=def_number_of_digits)
def_number_of_digits_entry.pack(side='left')


def rename():  # Renaming function, gets attributes from Entries
    number = 1
    dir = r'%s'
    extension = r'*%s'
    titlePattern = r'%s%s%s'
    for pathAndFilename in glob.iglob(os.path.join(dir % (def_path.get()), extension % (def_extension.get()))):
        digitedNumber = str(number).zfill(int(def_number_of_digits.get()))
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(dir % (def_path.get()), titlePattern % (def_filename.get(), digitedNumber, ext)))
        number += 1
        

execute = Button(main, text=' EXECUTE ', foreground="red", command=rename)  # Execute button
execute.pack()

root.mainloop()
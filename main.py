import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pandas import read_csv

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getCSV():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = read_csv(import_file_path)


browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)


def convertToExcel():
    global read_file

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel(export_file_path, index=None, header=True)


saveAsButton_Excel = tk.Button(text='Convert CSV to Excel', command=convertToExcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()




#os.chdir(r'C:\Users\Aharon T\Desktop\sample files')
# print(os.listdir())
# print(os.getcwd())


# print(df["col2"])
# print(df["col2"].iloc[5])
# for x in range(8):
#    datapoint= f.readline()
#    try:
#        datapoint.index(",")
#    except ValueError:
#        print ("Not found!")
#     else:
#        print (datapoint.index(","))

#
#
# r = open("pokemon_data.csv", 'w')
#
# r.close()
#

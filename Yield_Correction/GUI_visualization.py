from Tkinter import *
from graphGenerator_helper import *
from livePlotting_helper import plotLive

def map_Generator(*args):
    try:
        showVisual(int(combine_Type.get()), combine_Name.get(), lat_Name.get(), long_Name.get(), massFlow_Name.get(), sample_Length.get(), num_Degree.get(), filename.get())
    
    except ValueError:
        pass

def plot(*args):
	plotLive(combine_Type.get(), combine_Name.get(), lat_Name.get(), long_Name.get(), massFlow_Name.get(), filename.get())


def init(mainframe):
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

def labels(maimframe):
	filename_label = Label(mainframe, text="Enter a file name").grid(column=1, row=1, sticky=W)
	combine_Name_label = Label(mainframe, text="Enter the column label for combine data.").grid(column=1, row=2, sticky=W)
	combine_Typw_label = Label(mainframe, text="If it exists, please enter combine number (acceptable input: integer, if NA or analyze all combine type 0").grid(column=1, row=3, sticky=W)
	lat_Name_label = Label(mainframe, text="Please enter the column label for latitude data").grid(column=1, row=4, sticky=W)
	long_Name_label = Label(mainframe, text="Please enter the column label for longitude data").grid(column=1, row=5, sticky=W)
	massFlow_label = Label(mainframe, text="Please enter the column label for mass flow data").grid(column=1, row=6, sticky=W)
	sample_Length_label = Label(mainframe, text="Please choose the length of the sample points (x<=40)").grid(column=1, row=7, sticky=W)
	num_Degree_label =  Label(mainframe, text="Please choose the number of degree for the polynomial function").grid(column=1, row=8, sticky=W)
	

# Creating window and window name    
root = Tk()
root.title("Mass Flow Visualization")
mainframe = Frame(root)
# Creating window and window name    
init(mainframe)

# User input for generating mass flow map
filename = StringVar()
combine_Type = IntVar()
combine_Name = StringVar()
lat_Name = StringVar()
long_Name = StringVar()
massFlow_Name = StringVar()
sample_Length = IntVar()
num_Degree = IntVar()

filename_entry = Entry(mainframe, width=15, textvariable=filename)
filename_entry.grid(column=2, row=1, sticky=(W, E))

combine_Name_entry = Entry(mainframe, width=15, textvariable=combine_Name)
combine_Name_entry.grid(column=2, row=2, sticky=(W,E))

combine_Type_entry = Entry(mainframe, width=15, textvariable=combine_Type)
combine_Type_entry.grid(column=2, row=3, sticky=(W,E))

lat_Name_entry = Entry(mainframe, width=15, textvariable=lat_Name)
lat_Name_entry.grid(column=2, row=4, sticky=(W,E))

long_Name_entry = Entry(mainframe, width=15, textvariable=long_Name)
long_Name_entry.grid(column=2, row=5, sticky=(W,E))

massFlow_Name_entry = Entry(mainframe, width=15, textvariable=massFlow_Name)
massFlow_Name_entry.grid(column=2, row=6, sticky=(W,E))

sample_Length_entry = Entry(mainframe, width=15, textvariable=sample_Length)
sample_Length_entry.grid(column=2, row=7, sticky=(W,E))

num_Degree_entry = Entry(mainframe, width=15, textvariable=num_Degree)
num_Degree_entry.grid(column=2, row=8, sticky=(W,E))

# adding label to the entries
labels(mainframe)

# Call function to generate maps and graphs 
submit_Btn = Button(mainframe, text="Submit", command=map_Generator).grid(column=3, row=9, sticky=W)
plotLive_Btn = Button(mainframe, text="Plot Live", command=plot).grid(column=2, row=9, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

filename_entry.focus()
combine_Name_entry.focus()
combine_Type_entry.focus()
lat_Name_entry.focus()
long_Name_entry.focus()
massFlow_Name_entry.focus()	
sample_Length_entry.focus()	
num_Degree_entry.focus()

root.bind('<Return>', map_Generator)
root.mainloop()

import geopandas as pd
from functools import partial
import tkinter as tk

print("What is the folder Path: ", end='')

file = open(input()+'/schools.txt', 'w')

schoolButtons=[]

colleges = pd.read_file('collegedata/CollegesUniversities.shp')

window = tk.Tk()
window.geometry("500x300")

searchBar = tk.Frame(master=window)
entryStr = tk.StringVar()
school = tk.Entry(master = searchBar, width = 50, textvariable=entryStr)
school.pack(side='left')

def addSchool(school):
    file.write(school+'\n')

def search():
    for i in schoolButtons:
        i.pack_forget()
    schoolButtons.clear()
    for i in colleges[colleges['NAME'].str.contains(entryStr.get())==1]['NAME']:
        schoolButtons.append(tk.Button(master=window, text=i, command=partial(addSchool, i)))
    for i in schoolButtons:
        i.pack()
        

searchButton = tk.Button(master = searchBar, text = 'Search', command=search)
searchButton.pack()
searchBar.pack()



window.mainloop()
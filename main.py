import geopandas as pd
from functools import partial
import tkinter as tk

#ask user for conference
print("What is the folder Path: ", end='')
path = input()

#load college data
colleges = pd.read_file('collegedata/CollegesUniversities.shp')

#create window
window = tk.Tk()
window.geometry("500x300")

#search frame
schools=set()
searchResults = []
def search():
    for i in searchResults:
        i.pack_forget()
    searchResults.clear()
    for i in colleges[colleges['NAME'].str.contains(entryStr.get().upper())==1]['NAME']:
        searchResults.append(tk.Button(master=searchFrame, text=i, command=partial(schools.add, i)))
    for i in searchResults:
        i.pack()

searchFrame = tk.Frame(master=window)
searchBar = tk.Frame(master=searchFrame)
entryStr = tk.StringVar()
searchText = tk.Entry(master=searchBar, textvariable=entryStr)
searchText.pack(side='left')
searchButton = tk.Button(master=searchBar, text='Search', command=search)
searchButton.pack(side='left')
searchBar.pack()


#view frame
viewFrame = tk.Frame(master=window)
viewedSchools = []

#choose frame
controlFrame = tk.Frame(master=window)

def switchToSearchFrame():
    searchFrame.pack_forget()
    viewFrame.pack_forget()
    searchFrame.pack()

searchFrameButton = tk.Button(text='Search View', master = controlFrame, command = switchToSearchFrame)

def removeSchool(school):
    schools.remove(school)
    switchToViewFrame()

def switchToViewFrame():
    viewFrame.pack_forget()
    searchFrame.pack_forget()
    for i in viewedSchools:
        i.pack_forget()
    viewedSchools.clear()
    for i in schools:
        temp = tk.Frame(master=viewFrame)
        tk.Label(text = i, master=temp).pack(side='left')
        tk.Button(text='remove', master=temp, command=partial(removeSchool, i)).pack(side='left')
        viewedSchools.append(temp)
    for i in viewedSchools:
        i.pack()
    viewFrame.pack()

viewFrameButton = tk.Button(text='Conference View', master = controlFrame, command = switchToViewFrame)
searchFrameButton.pack(side='left')
viewFrameButton.pack(side='left')
controlFrame.pack()
searchFrame.pack()

window.mainloop()
#create shapefile
colleges[colleges['NAME'].isin(schools)].to_file(path+'/map.shp')
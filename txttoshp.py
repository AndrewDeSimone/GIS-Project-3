import geopandas as pd

print("What is the folder Path: ", end='')

path = input()

schools = set(open(path+'/schools.txt', 'r').read().split('\n'))

if "" in schools:
    schools.remove("")

colleges = pd.read_file('collegedata/CollegesUniversities.shp')

colleges[colleges['NAME'].isin(schools)].to_file(path+'/map.shp')
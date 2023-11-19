import geopandas as pd

print("What is the folder Path: ", end='')

path = input()

schools = open(path+'/schools.txt', 'r').read().split('\n')

colleges = pd.read_file('collegedata/CollegesUniversities.shp')

colleges[colleges['NAME'].isin(schools)].to_file(path+'/map.shp')
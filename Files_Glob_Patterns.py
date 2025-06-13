from pathlib import Path
p = Path('/home/philip/fileHandler/TestingFiles/')
#print(p.glob('*'))
#print(list(p.glob('*'))) # make a list from the generator
print(list(p.glob('*.csv')))
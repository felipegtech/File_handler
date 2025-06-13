from pathlib import Path
import os 
print(Path.cwd())
# Is_absolute() return True if it represents a abslute path or relative
print(Path.cwd().is_absolute())
print(Path('/home/philip/delicious/walnut').is_absolute())
# get an absolute path from a relative path
print(Path('/home/philip/path'))
print(Path.cwd() / Path('delicious/path'))
print(os.path.abspath('.')) 

# Extracting each attribute from the file Path
p = Path('/home/philip/walnut')
print("This is the anchor of the file :" +" " + p.anchor)
print(p.parent)
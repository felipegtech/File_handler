from pathlib import Path
# checking path  existing
# p.exists() returns True if the path exist or False if it doesn't exist
# p.is_file() True if the path exists and is a file
# p.is_dir() True if the path exist and is directory.

UbuntuSystem = Path('/home/philip')
notExistDir = Path('/home//This/Folder/Does/Not/Exist')
print(UbuntuSystem.exists())
print(notExistDir.exists())
print(UbuntuSystem.is_dir())
print(notExistDir.is_dir())


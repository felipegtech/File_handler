import os
# gathering information about specific files and folders
#o.path module provides that
print(os.path.getsize('/home/philip/fileHandler/TestingFiles/eu-ets.csv'))
print(os.listdir('/home/philip/fileHandler/TestingFiles/'))

# looping over each filename.
totalSize = 0
for filename in os.listdir('/home/philip/fileHandler/TestingFiles/'):
  totalSize = totalSize + os.path.getsize(os.path.join('/home/philip/fileHandler/TestingFiles/', filename))

print(totalSize)



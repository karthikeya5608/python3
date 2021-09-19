import os
import shutil
source=input("enter source folder name:")
listoffiles=os.listdir(source)
for file in listoffiles:
  name,ext=os.path.splitext(file)
  ext=ext[1:]
  if ext=='':
    continue
  if os.path.exists(source+'/'+ext):
      shutil.move(source+'/'+file,source+'/'+ext+'/'+file)  
  else:
      os.makedirs(source+'/'+ext)
      shutil.move(source+'/'+file,source+'/'+ext+'/'+file)  
           
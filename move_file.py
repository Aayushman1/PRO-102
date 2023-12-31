import os
import shutil

from_dir="C:/Users/Aayushman & Ashish/Desktop/DevHandbuch"
to_dir="C:/Users/Aayushman & Ashish/Documents/Programming/Python"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    
    #print(name)
    #print(extension)
    
    if extension == '':
        continue
    if extension in ['.doc','.docx','.pdf','.txt']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Document_files'
        path3=to_dir+'/'+'Document_files'+'/'+file_name
        
        if os.path.exists(path2):
            print('Moving '+file_name+' ...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving '+file_name+' ...')
            shutil.move(path1,path3)
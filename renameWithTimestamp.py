import os
import glob
import time

#folder = r"x:\python\"
folder = input("input a directory:\n")

#creating a time
ti_c = os.path.getctime(folder)
c_ti = time.ctime(ti_c)

#format
t_obj = time.strptime(c_ti)

#timestamp yyy_mm_dd
T_stamp = time.strftime("%Y_%m_%d", t_obj)

#loop adding prefix created time yyy_mm_dd_
for _, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename   
    newname = folder + str(T_stamp) + "_" + filename + ".jpg"
    try:
        os.rename(oldname, newname)
    except FileExistsError:
        print("File already Exists")

#out
print("new file names: ", glob.glob(folder + "*"))
import os.path as osp
import os
import shutil
#from path import path
import sys

def copy_file(dir, dest, filetype="txt", counter=0):
    for pack in os.walk(dir):
        for f in pack[2]:
            if not f.endswith(filetype) and couter <= 0:
                break;
            fullpath = pack[0] + "/" + f
            #topath = dest+'/'+f
            shutil.copy(fullpath, dest)
            counter -= 1

#def copy_n_file(from_path, to_path, count = 0):
#    entries = os.listdir(from_path)   
#    for entry_itr in entries:
#        copy_file(entry_itr, to_path, filetype='jpg')
#        count -= 1
#        if count <= 0:
#            break
#

def transferIntoMark(from_path1, from_path2, to_path):
        copy_file(from_path1, to_path, counter=3000)
        copy_file(from_path2, to_path, counter=3000)
        
    
if __name__ == '__main__':
    from_path_1 ="/home/young/workspace/ml-project/datasets/cover/core_3000/Annotation"
    from_path_2 ="/home/young/workspace/ml-project/datasets/cover/coreless_3000/Annotation"
    to_path = "/home/young/workspace/ml-project/datasets/Anno_core_coreless_battery_sub_3000_3000/"
    transferIntoMark(from_path_1, from_path_2, to_path)

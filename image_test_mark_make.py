import os.path as osp
import os
import sys


def transferIntoMark(from_path, to_path):
    with open(to_path, "w", encoding='utf-8') as to_f:
        entries = os.listdir(from_path)   
        i = 0
        for entry_itr in entries:
            index = entry_itr.find(".jpg")
            to_f.write(entry_itr[:index]+"\n")
            i += 1
            print("debug")
            print(i)
            if i==500:
                print("debug")
                print(i)
                break

if __name__ == '__main__':
    from_path ="/home/young/workspace/ml-project/datasets/cut_Image_core_coreless_battery_sub_5000_500"
    to_path = "/home/young/workspace/ml-project/datasets/image_test_mark.txt"
    transferIntoMark(from_path, to_path)

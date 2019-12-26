import os.path as osp
import os
import sys


def transferIntoMark(from_path, to_path):
    with open(to_path, "w", encoding='utf-8') as to_f:
        entries = os.listdir(from_path)   
        for entry_itr in entries:
            index = entry_itr.find(".jpg")
            to_f.write(entry_itr[:index]+"\n")

if __name__ == '__main__':
    from_path ="F:/young/cut_Image_core_coreless_battery_sub_3000_3000"
    to_path = "F:/young/image_unbalance_mark.txt"
    transferIntoMark(from_path, to_path)


# -*- coding: utf-8 -*-
import os
import sys
import shutil

def copy_file(path,Target_area):#传入需要遍历的根目录和需要复制到的区域
	path_list=os.listdir(path)
	for new_path in path_list:
		new_path=os.path.join(path,new_path)

		if os.path.isdir(new_path):
			copy_file(new_path,Target_area)
		elif os.path.isfile(new_path):
			Suffix_name=os.path.splitext(new_path)[1]

		#if Suffix_name in [".bmp",".gif",".png",".jpg"]:#指定文件后缀名，从而指定文件格式
		if Suffix_name in [".xml"]:
			shutil.copy(new_path,Target_area)
			#删除文件
			os.unlink(new_path)
		#else:
			#print("there is sth wrong")


copy_file('/home/zj/center7tagged','/home/zj/xhz/new')


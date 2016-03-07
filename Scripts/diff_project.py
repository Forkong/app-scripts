#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import codecs
from Foundation import NSDictionary

project_path = "app-scripts.xcodeproj/project.pbxproj"

re_note = re.compile(r"(/\*){1}[\w\d\s.+-@x\"\']+(\*/){1}")

# 对应key值，此部分需要自行填写
app_main_key = '79EF930E1C8D6D1D0003B699'
app_main_Sources_key    = '79EF93081C8D6D1D0003B699'
app_main_Frameworks_key = '79EF93091C8D6D1D0003B699'
app_main_Resources_key  = '79EF930A1C8D6D1D0003B699'

app_test_key = '79A3722E1C8D6F2B002D4766'
app_test_Sources_key    = '79A3722F1C8D6F2B002D4766'
app_test_Frameworks_key = '79A372331C8D6F2B002D4766'
app_test_Resources_key  = '79A372341C8D6F2B002D4766'		

# 抽取id
def get_id_dict(path):
	lines = read_file(path)
	id_dict = {}
	for line in lines:
		if "=" in line:
			index = line.index("=")
			new_line = line[0:index].strip()
			result = re.search(r"(/\*){1}([\w\d\s.+-@x\"\']+)((\*/){1})", new_line)
			if result:
				note = result.group(2).strip()
				the_id = new_line[0:24]
				id_dict[the_id] = note
	return id_dict


# 对比
def compare(plist, id_dict):
	objects = plist["objects"]

	app_test_Sources    = objects[app_test_Sources_key]["files"]
	app_test_Frameworks = objects[app_test_Frameworks_key]["files"]
	app_test_Resources  = objects[app_test_Resources_key]["files"]

	app_main_Sources    = objects[app_main_Sources_key]["files"]
	app_main_Frameworks = objects[app_main_Frameworks_key]["files"]
	app_main_Resources  = objects[app_main_Resources_key]["files"]

	print "****************** Test中有，而Main中没有的是： ******************"
	print "===========================Sources:================================"
	compare_values(app_test_Sources, app_main_Sources, id_dict)
	print "==========================Frameworks:=============================="
	compare_values(app_test_Frameworks, app_main_Frameworks, id_dict)
	print "===========================Resource:==============================="
	compare_values(app_test_Resources, app_main_Resources, id_dict)
	print "****************** Main,而Test中没有的是： ******************"
	print "===========================Sources:================================"
	compare_values(app_main_Sources, app_test_Sources, id_dict)
	print "==========================Frameworks:=============================="
	compare_values(app_main_Frameworks, app_test_Frameworks, id_dict)
	print "===========================Resource:==============================="
	compare_values(app_main_Resources, app_test_Resources, id_dict)

# 对比
def compare_values(array_1, array_2, id_dict):
	for array_1_key in array_1:
		array_1_value = id_dict[array_1_key]

		is_in = False
		for array_2_key in array_2:
			array_2_value = id_dict[array_2_key]
			if array_1_value == array_2_value:
				is_in = True
				break
		if not is_in:
			print array_1_value
	pass


def read_plist(plist):
	# 此处plist文件格式非标准，plist库无法解析,即使我去除所有的注释,仍然没用
	# 所以调用objc的解析的方法
	return NSDictionary.dictionaryWithContentsOfFile_(plist)

def read_file(path):
	f = codecs.open(path, 'r')
	lines = f.readlines()
	f.close()
	return lines

def write_file(lines, file_name):
	f = codecs.open(file_name, 'w')
	for line in lines:
		# print line
		f.write(line)
		if not line.endswith("\n"):
			f.write("\n")
	f.close()
	pass

if __name__ == '__main__':
	plist = read_plist(project_path)
	id_dict = get_id_dict(project_path)
	compare(plist, id_dict)


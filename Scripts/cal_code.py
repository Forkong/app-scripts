#!/usr/bin/python
# -*- coding: utf-8 -*-
# 计算文件夹内所有支持类型的文件总行数（除部分文件夹之外）
import os
import sys

# 不参与统计的文件夹
without_dir = ["/Support", "/Vendor"]

# 统计的文件类型
support_version = [".m", ".h"]

# 是否打印所有文件行数
is_print_all = True

# 设定的大文件行数，大于此行数，将打印出来
# 在is_print_all=True时，不打印
large_line_count = 300

def walk_dir(path):
	total_line_count = 0
	total_valid_count = 0
	for d,fd,fl in os.walk(path):
		if not check_is_in(d):
			for f in fl:
				sufix = os.path.splitext(f)[1]
				if sufix in support_version:
					line_count, valid_count = calculate_file(f, d + '/' + f)
					total_line_count  = total_line_count + line_count
					total_valid_count = total_valid_count + valid_count
	print "==============================="
	print "总行数为:", total_line_count, "有效行数:", total_valid_count

def check_is_in(d):
	is_in = False
	for dir_name in without_dir:
		if dir_name in d:
			is_in = True
	return is_in

def calculate_file(file_name ,file_path):
	if os.path.exists(file_path):
		input = open(file_path)  
		lines = input.readlines()

		valid_count = len(lines)
		line_count  = len(lines)
		for line in lines:
			if line == '\n' or (len(line)>=2 and line[0:2] == '//'):
				valid_count = valid_count-1
			
		if is_print_all:
			#文件名称 总行数 非基本注释、空行之外的总行数
			print "文件名称:", file_name, "总行数:", line_count, "有效行数:",valid_count
		else:
			if line_count >= large_line_count:
				print "大文件名称:", file_name, "总行数:", line_count, "有效行数:",valid_count
		return line_count, valid_count

if __name__ == "__main__":
	print sys.argv
	if len(sys.argv) == 2:
		walk_dir(sys.argv[1])
	else:
		walk_dir(os.getcwd())

# 输入：
# python cal_code.py
# python cal_code.py ../app-scripts/
	

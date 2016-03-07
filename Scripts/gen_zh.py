#!/usr/bin/python
# -*- coding: utf-8 -*-
# 此脚本用于从英文strings中完整导出中文strings
import codecs

EnglishLocalizableStringsPath = "./app-scripts/en.lproj/Localizable.strings"
ChineseLocalizableStringsPath = "./app-scripts/zh-Hans.lproj/Localizable.strings"

#读取strings文件
def read_strings(stringsName):
	f = codecs.open(stringsName, 'r')
	lines = f.readlines()
	f.close()
	return lines

#获取key
def get_chinese_string(line):
	array = line.split("=")
	if len(array) == 2:
		return array[0]
	else:
		return line

#组合中文
def combine_string(chinese_string):
	if chinese_string.find("\"") == -1:
		return chinese_string
	else:
		return chinese_string + "= " + chinese_string.rstrip() + ";"

#写入文件
def write_to_file(lines, path):
	f = codecs.open(path, 'w')
	for line in lines:
		f.write(line)
		if not line.endswith("\n"):
			f.write("\n")
	f.close()

if __name__ == "__main__":
	chinese_string_array = []
	
	#中文
	lines = read_strings(EnglishLocalizableStringsPath)	
	for line in lines:
		chinese_string_array.append(combine_string(get_chinese_string(line)))

	write_to_file(chinese_string_array, ChineseLocalizableStringsPath)
	print "中文导出成功"
	
	
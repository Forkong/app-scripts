#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import dateutil

prog = re.compile(r"r(\d+) \| (.+) \| (\d+-\d+-\d+)")
# 统计的文件类型
fileVersion = re.compile(r"(Index: )+[a-zA-Z0-9./:_ ]*.[hm]$")
# 单个文件diff开始
singleDiffStart = re.compile(r"(Index: )+[a-zA-Z0-9./:_ ]*.[a-zA-Z]$")
# 不需要统计的文件路径
withoutDirs = ["Reveal.framework",
               "Scripts/",
               "Vendor/"]

# 比较最新的x个版本,必须>=1
compareVersionCount = 1

def getContribution(path, last, revision):
    additions = 0
    deletions = 0

    cmd = "cd "+path+" && "+ "svn diff -r" + last + ":" + revision
    # print cmd
    p = os.popen(cmd, "r")
    
    isNeedDiff = False
    for line in p:
        line = line.strip()
        if not isNeedDiff:
            isNeedDiff = checkDiff(line)
            continue
        else:
            if singleDiffStart.match(line):
                isNeedDiff = checkDiff(line)
                continue
            else:
                if len(line) > 0:
                    # 单个文件diff输出开始
                    if line[0] == "-":
                        if line[0:2] != "---":
                            deletions += 1
                    elif line[0] == "+":
                        if line[0:2] != "+++":
                            additions += 1

    p.close()
    print "版本:", revision ,"新增:", additions, "删除:", deletions
    return additions, deletions

def checkDiff(line):
    isIn = False
    isNeedDiff = False
    if fileVersion.match(line):
        for withoutDir in withoutDirs:
            isIn = False
            if withoutDir in line:
                isIn = True
            if not isIn:
                isNeedDiff = True
            else:
                isNeedDiff = False
    return isNeedDiff

def compare(path, versionCount):
    first = True
    author = ""
    last = ""
    revision = ""
    index = 0
    info = {}

    p = os.popen("cd "+path+" && "+ "svn log", "r")
    
    for line in p:
        result = prog.match(line)
        if result:
            if first:
                revision, author, date = result.groups(1)
                first = False
                index += 1
            else:
                if index <= versionCount:
                    last = result.groups(1)[0]
                    additions, deletions = getContribution(path, last, revision)

                    if author in info:
                        if date not in info[author]:
                            info[author][date] = {'commits': 1, 'additions': additions,'deletions': deletions}
                        else:
                            info[author][date]['commits'] += 1
                            info[author][date]['additions'] += additions
                            info[author][date]['deletions'] += deletions
                    else:
                        info[author] = {}
                        info[author][date] = {'commits': 1, 'additions': additions,'deletions': deletions}

                    revision, author, date = result.groups(1)
                    index += 1
                    
    p.close()
    return info

def printResult(info):
    print "\n"
    print "====================汇总===================="
    for author in info:
        dates = []
        commits = []
        additions = []
        deletions = []
        for date in sorted(info[author].iterkeys(), reverse=True):
            dates.append(date)
            commits.append(info[author][date]['commits'])
            additions.append(info[author][date]['additions'])
            deletions.append(info[author][date]['deletions'])
            print "作者:", author, "日期:", date, "提交次数:", info[author][date]['commits'],
            print "新增:", info[author][date]['additions'], "删除:", info[author][date]['deletions']
    pass

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) >= 3:
        printResult(compare(sys.argv[1], int(sys.argv[2])))
    elif len(sys.argv) == 2:
        printResult(compare(sys.argv[1], compareVersionCount))
    else:
        printResult(compare("./", compareVersionCount))


# 执行：
# python cal_svn_commit.py 路径(目录层) 对比最新的n个版本个数(>=1)
# python cal_svn_commit.py
# python cal_svn_commit.py ./ 2





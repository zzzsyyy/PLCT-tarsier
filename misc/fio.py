import re
import sys
import os

fin = open(sys.argv[1], encoding='UTF-8')
fout = open(os.path.splitext(os.path.split(sys.argv[1])[1])[0] + ".csv", 'w')
line = fin.readline()
startline = re.compile(r"job1: \(g=0\): rw=(\w*), bs=\(R\) ([\d.]*\w*B)-\2, \(W\) \2-\2, \(T\) \2-\2, ioengine=libaio, iodepth=10")
resline = re.compile(r"\s*(read|write): IOPS=([\d.]+[kK]?), BW=([\d.]+\w*B/s) \(([\d.]+\w*B/s)\)\(([\d.]+\w*B)/(\d+msec)\)")

fout.write("测试类型,块大小,测试结果\n")
while line:
    matchObj = startline.match(line)
    if matchObj:
        rw = matchObj.group(1)
        fout.writelines(["\n", rw, ",", matchObj.group(2), ","])
    matchObj = resline.match(line)
    if matchObj:
        fout.writelines(["[IOPS=", matchObj.group(2), "--",matchObj.group(1),"=", matchObj.group(3),"]"])
    line = fin.readline()

fin.close()
fout.close()

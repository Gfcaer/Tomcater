# coding:utf-8
# 遍历制定目录下的所有

import os

allFile = []
repertFiles = []

for root, dirs, files in os.walk("d:\\CSWork\\中软工作\\023.专项工程\\NF产品目录\\"):
    for fileItem in files:
        if fileItem not in allFile:
            allFile.append(fileItem)
        else:
            repertFiles.append(fileItem)
    print(root + os.sep + str(repertFiles))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import zipfile

from docx import Document
from win32com import client as wc


#读取指定目录下所有的docx文档
#输入参数： 给的包含docx文档的目录
#返回： 包含docx文件名的列表
def readFiles(dirName):
    #定义输出符合条件的文件名称
    outFiles = []
    # 读取指定目录下的所有文件
    dirs = os.listdir(dirName)
    # 循环读取路径下的文件并筛选输出
    for dir in dirs:
        # 筛选docx文件，忽略其他类型的文件
        if os.path.splitext(dir)[1] == ".docx":
            outFiles.append(dir)
    return outFiles


#提起docx文档中的嵌入式对象
#输入参数： inputDir - 需要处理的docx文档目录
#输入参数： extractDir - 存放提出出来的docx文档目录
def parseDocx(inputDir, extratDir):
    docsFilenames = readFiles(inputDir)
    for docxFilename in docsFilenames:
        print("正在处理文件[" + docxFilename + "], 请稍后......")
        #提取不包含扩展名的文件名
        fileNameNoExt = docxFilename[0:-5]
        #进行解压
        f = zipfile.ZipFile(inputDir + '\\' + docxFilename, 'r')
        #获取系统临时目录
        tmpDir = os.environ["TEMP"]
        #把docx文档中的嵌入式文档提取出来写道指定的目录下
        f.extractall(tmpDir)
        counter = 1
        for file in f.namelist():
            #print(file)
            if file.endswith(".docx"):
                print('发现docx: ' + tmpDir + '\\' + file)
                document = Document(tmpDir + '\\' + file)
                document.save(extratDir + fileNameNoExt + ' - ' +
                              str(counter) + '.docx')
                counter = counter + 1
            if file.endswith(".doc"):
                #save doc to docx
                print('发现doc: ' + tmpDir + '\\' + file)
                w = wc.Dispatch('Word.Application')
                # 或者使用下面的方法，使用启动独立的进程：
                # w = wc.DispatchEx('Word.Application')
                doc = w.Documents.Open(tmpDir + '\\' + file)
                #必须有参数16，否则会出错.
                #print(doc.fileNameNoExt)
                
                doc.SaveAs(
                    extratDir + fileNameNoExt + ' - ' + str(counter) + '.docx',
                    16)
                counter = counter + 1
                doc.Close()
                w.Quit()
            if file.endswith(".do"):
                #save doc to docx
                print('发现do: ' + tmpDir + '\\' + file)


# 主函数
if __name__ == '__main__':
    parseDocx('D:\\workspace\\PythonTester\\resources\\',
              'D:\\workspace\\PythonTester\\inputfiles\\')

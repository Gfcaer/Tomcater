#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import xlrd
import xlsxwriter


#读取指定目录下所有的xlsx文档
#输入参数： 给的包含xlsx文档的目录
#返回值： 包含dxlsx文件名的列表
def readFiles(dirName):
    #定义输出符合条件的文件名称
    outFiles = []
    # 读取指定目录下的所有文件
    dirs = os.listdir(dirName)
    # 循环读取路径下的文件并筛选输出
    for dir in dirs:
        # 筛选xlsx文件，忽略其他类型的文件
        if os.path.splitext(dir)[1] == ".xlsx":
            outFiles.append(dir)
    return outFiles


#合并xlsx
#输入参数： 包含xlsx文档的目录
#输入参数： 新生成的xlsx文档名称
#返回值： 无
def mergeXlsx(inXlsDir, outXls):
    # 读取数据
    xtData = []
    xlsFilenames = readFiles(inXlsDir)
    for xlsFilename in xlsFilenames:
        wb = xlrd.open_workbook(inXlsDir + xlsFilename)
        #TODO 通过名字获取Sheet，需要根据实际情况进行修改
        sheet = wb.sheet_by_name('S1')
        for rownum in range(sheet.nrows):
            xtData.append(sheet.row_values(rownum))

    # 写入数据
    workbook = xlsxwriter.Workbook(outXls)
    #TODO 命名新Excel的Sheet名字，建议和上面相同
    worksheet = workbook.add_worksheet('S1S1')
    for i in range(len(xtData)):
        for j in range(len(xtData[i])):
            worksheet.write(i, j, xtData[i][j])
    # 关闭文件流
    workbook.close()


# 主函数
if __name__ == '__main__':
    #存放待解析的Word文档目录名，i请根据实际情况修改
    inXlsDir = 'D:\\workspace\\PythonTester\\resources\\xlsdir\\'
    outXls = 'D:\\workspace\\PythonTester\\resources\\outout.xlsx'
    mergeXlsx(inXlsDir, outXls)

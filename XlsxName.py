#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import xlsxwriter


#根据数据字典，
def XlsxName(inXls1, inXls2, outXls):
    
    #存放相同的数据
    xtData = []
    #存放不同的数据
    btData = []
    wb1 = xlrd.open_workbook(inXls1)  #打开文件
    sheet1 = wb1.sheet_by_name('差异数据')  #通过xuhao获取表格
    wb2 = xlrd.open_workbook(inXls2)  #打开文件
    sheet2 = wb2.sheet_by_name('数据项清单')  #通过名字获取表格
    xtData.append(sheet1.row_values(0) + sheet2.row_values(1))
    for rownum1 in range(sheet1.nrows):
        isSearch = False
        for rownum2 in range(sheet2.nrows):
            if sheet1.cell(rownum1, 2).value == sheet2.cell(rownum2, 5).value:
                if len(sheet1.cell(rownum1, 2).value) != 0:
                    print('    >>> 找到名称为[' + sheet2.cell(rownum2, 5).value +
                          ']的记录，正在合并中......')
                    xtData.append(
                        sheet1.row_values(rownum1) +
                        sheet2.row_values(rownum2))
                    isSearch = True
        if not isSearch:
            print('    >>> 发现数据字典中没有的项，正在整理到新的Sheet')
            strValue = sheet1.row_values(rownum1)
            #忽略空行
            print('    >>> ' + str(strValue) + ' - ' + str(len(str(strValue))))
            if len(str(strValue)) != 44:
                btData.append(strValue)

    # 写入和数据字段匹配的数据
    workbook = xlsxwriter.Workbook(outXls)
    worksheet = workbook.add_worksheet('数据字典-IDName')
    font = workbook.add_format({"font_size": 10})
    for i in range(len(xtData)):
        for j in range(len(xtData[i])):
            worksheet.write(i, j, xtData[i][j], font)
    #写入和数据字典不匹配的文件
    worksheet = workbook.add_worksheet('差异数据')
    font = workbook.add_format({"font_size": 9})
    #TODO: 需要处理Excel中的空行
    for i in range(len(btData)):
        for j in range(len(btData[i])):
            worksheet.write(i, j, btData[i][j], font)
    # 关闭文件流
    workbook.close()


# 主函数
if __name__ == '__main__':
    #存放待解析的Word文档目录名
    rootDir = 'D:\\workspace\\PythonTester\\'
    xlsxDataDict = rootDir + 'inputfiles\\数据字典.xlsx'
    xlsxID = rootDir + 'outfiles\\界面要素（ID）.xlsx'
    xlsxIDName = rootDir + 'outfiles\\界面要素（IDName）.xlsx'
    print('正在根据数据字典文件' + xlsxDataDict + '生成最终的' + xlsxIDName + '文件, 请稍后......')
    XlsxName(xlsxID, xlsxDataDict, xlsxIDName)
    print('处理完成，谢谢！！！')

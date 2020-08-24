# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 读取excel文件内容
import xlrd

xl = xlrd.open_workbook("C:/Users/10283/Desktop/各学科调查表/产科专科情况调查表.xlsx")
print(xl.sheet_names())
data = xl.sheet_by_index(1)
print(data.row(2))


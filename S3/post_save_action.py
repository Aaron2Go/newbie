# 12 avril 2018

import datetime
import pandas as pd
from S2.models import *
import os.path
import re

def format_field_id(s):
    return (''.join(list(filter(str.isdigit, str(s)))))[-6:]


def format_field_percentage(s):
    if isinstance(s, str):
        return float(s.rstrip('%'))
    else:
        return s


def format_field_name(s):
    return s.replace(' ', '')


def format_field_status(s):
    if '正常' in s:
        return '正常'
    elif '停牌' in s:
        return '停牌'


def interpret_navfile(file_path, project, infodate):
    df = pd.read_excel(file_path, sheet_name=0)
    print(df)
    ptn1 = re.compile(r'估?值?日期:?：?\s*([0-9]{4}\S?[0-9]{2}\S?[0-9]{2})')
    # 单位净值
    ptn2 = re.compile(r'今?日?单位净值:?：?\s*([0-9]+.[0-9]+)')
    ptn3 = re.compile(r'[累计年初期昨修正调整]')
    str1 = ''
    for row in range(0, len(df)):
        for col in range(0, df.shape[1] - 1):
            tmpstr = str(df.iat[row, col]) + str(df.iat[row, col + 1])
            if re.search(ptn1, tmpstr) != None:
                str0 = re.search(ptn1, tmpstr).group(0)
                for i in range(0, len(str0)):
                    if str0[i].isdigit():
                        str1 += str0[i]
                        if len(str1) == 4:
                            str1 += '-'
                        elif len(str1) == 7:
                            str1 += '-'
                print('口径日期: ', str1)
            elif re.search(ptn2, tmpstr) != None and re.search(ptn3, tmpstr) == None:
                    str2 = re.search(ptn2, tmpstr).group(1)
                    print('单位净值: ', str2)
    NavJournal.objects.get_or_create(
        Project=Project.objects.get(ID=project),  # 项目
        InfoDate=str1,  # 口径日期
        NetValue=str2  # 净值
    )

    # 持股明细
    # df = pd.read_excel(file_path, sheet_name=0)
    field_row = 0
    target_field_id = '科目代码'
    valid_rows_list = []
    for field_row in range(0, len(df)):
        if df.iat[field_row, 0] == target_field_id:
            break
    field_row_repeat = 0
    while df.iat[field_row + field_row_repeat, 0] == target_field_id:
        field_row_repeat += 1
    target_field_state = '停牌信息'
    for field_column in range(0, df.shape[1]):
        if df.iat[field_row, field_column] == target_field_state:
            break
    for row in range(field_row + field_row_repeat, len(df)):
        if '正常' in str(df.iat[row, field_column]) or '停牌' in str(df.iat[row, field_column]):
            valid_rows_list.append(row)
    field_list_name = ['科目代码', '科目名称', '数量', '单位成本', '成本', '成本占比', '市价', '市值', '市值占比', '估值增值', '停牌信息']
    field_list_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for column in range(0, df.shape[1]):
        if '科目代码' in df.iat[field_row, column]:
            field_list_number[0] = column
        elif '科目名称' in df.iat[field_row, column]:
            field_list_number[1] = column
        elif '数量' in df.iat[field_row, column]:
            field_list_number[2] = column
        elif '单位成本' in df.iat[field_row, column]:
            field_list_number[3] = column
        elif '成本' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[4] = column
        elif '成本' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[5] = column
        elif '市价' in df.iat[field_row, column] or '行情' in df.iat[field_row, column]:
            field_list_number[6] = column
        elif '市值' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[7] = column
        elif '市值' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[8] = column
        elif '估值' in df.iat[field_row, column] or '增值' in df.iat[field_row, column]:
            field_list_number[9] = column
        elif '停牌' in df.iat[field_row, column] or '交易' in df.iat[field_row, column]:
            field_list_number[10] = column
    temp_list = []
    for i in valid_rows_list:
        for j in range(0, len(field_list_name)):
            if j == 0:
                temp_list.append(format_field_id(df.iat[i, field_list_number[j]]))
            elif j == 1:
                temp_list.append(format_field_name(df.iat[i, field_list_number[j]]))
            elif j == 10:
                temp_list.append(format_field_status(df.iat[i, field_list_number[j]]))
            elif j == 5 or j == 8:
                temp_list.append(format_field_percentage(df.iat[i, field_list_number[j]]))
            else:
                temp_list.append(df.iat[i, field_list_number[j]])
        StockJournal.objects.get_or_create(
            Project=Project.objects.get(ID=project),
            InfoDate=infodate,
            Code=temp_list[0],
            Name=temp_list[1],
            Holdings=temp_list[2],
            Purchase_Price=temp_list[3],
            Costs=temp_list[4],
            Cost_to_Nav=temp_list[5],
            Market_Price=temp_list[6],
            Market_Value=temp_list[7],
            Market_Value_to_Nav=temp_list[8],
            Valuation=temp_list[9],
            Status=temp_list[10]
        )
        print(temp_list)
        temp_list.clear()


def interpret_branchfile(file_path):
    df = pd.read_excel(file_path, sheet_name=0)
    print(df)
    for i in range(0, len(df)):
        Branch.objects.get_or_create(Name=df['Name'][i], Area=df['Area'][i])


def interpret_projectfile(file_path):
    df = pd.read_excel(file_path, sheet_name=0)
    print(df)
    for i in range(0, len(df)):
        b1 = Branch.objects.get(Name=df['经营机构'][i])
        print(b1)
        Project.objects.get_or_create(
            ID=df['项目编码'][i],
            Name=df['项目名称'][i],
            Branch=b1,
            Type=df['项目类型'][i],
            Approval_Form_Num=df['审批通知书编号'][i],
            Issue_Date=df['发行日期'][i],
            Amount=df['金额（万）'][i],
            Duration=df['期限（月）'][i],
            Leverage_Ratio=df['杠杆比例'][i]
        )

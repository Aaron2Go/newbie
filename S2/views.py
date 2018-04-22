from django.shortcuts import render
from django.http import HttpResponse
from S2.models import * # Project, Branch, Stock, TargetFields, ExcelFiles
import pandas as pd


def FormatDataframe(request):
    df = pd.read_excel(request.FILES.get('excel_file'), sheet_name = 0)
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
    df_new = pd.DataFrame(data = None, index = None, columns = field_list_name)
    temp_list = []
    for i in valid_rows_list:
        for j in range(0, len(field_list_name)):
            if j == 0:
                temp_list.append((''.join(list(filter(str.isdigit, str(df.iat[i, field_list_number[j]])))))[-6:])
            else:
                temp_list.append(df.iat[i, field_list_number[j]])
        df_new.loc[df_new.shape[0] + 1] = temp_list
        temp_list.clear()
    return df_new

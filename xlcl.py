import xlrd
import xlsxwriter


def read_excel(file_path):
    # 获取数据
    data = xlrd.open_workbook(file_path)
    # 获取所有sheet名字
    sheet_names = data.sheet_names()
    sheet = sheet_names[0]

    # 获取sheet
    table = data.sheet_by_name(sheet)
    # 获取总行数
    nrows = table.nrows  # 包括标题
    # 获取总列数
    ncols = table.ncols

    # 计算出合并的单元格有哪些
    # colspan = {}
    # if table.merged_cells:
    #     for item in table.merged_cells:
    #         for row in range(item[0], item[1]):
    #             for col in range(item[2], item[3]):
    #                 # 合并单元格的首格是有值的，所以在这里进行了去重
    #                 if (row, col) != (item[0], item[2]):
    #                     colspan.update({(row, col): (item[0], item[2])})
    # 读取每行数据

    write_excel = xlsxwriter.Workbook("/Users/turtle/Desktop/2.xlsx")
    write_excel_sheet = write_excel.add_worksheet()
    count = 1
    last = False
    last_num = 0
    last_index = 0
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(table.cell_value(i, j))
        # print(row)
        write_excel_sheet.write(i, 0, count)
        write_excel_sheet.write(i, 1, row[1])
        if row[0] == '' and row[1] == '':
            last = True
            continue

        if last:
            last = False
            write_excel_sheet.merge_range(last_index, 0, i - 1, 0, last_num)

        last_num = count
        count += 1
        last_index = i

    write_excel.close()

    # # 读取每列数据
    # for j in range(ncols):
    #     col = []
    #     for i in range(1, nrows):
    #         # 假如碰见合并的单元格坐标，取合并的首格的值即可
    #         if colspan.get((i, j)):
    #             col.append(table.cell_value(*colspan.get((i, j))))
    #         else:
    #             col.append(table.cell_value(i, j))
    #     print(col)


if __name__ == '__main__':

    # write_excel = xlsxwriter.Workbook("/Users/turtle/Desktop/222.xlsx")
    # write_excel_sheet = write_excel.add_worksheet()
    # write_excel_sheet.write(0, 0, 1)
    # write_excel_sheet.write(1, 0, 11)
    # write_excel_sheet.write(2, 0, 13)
    # write_excel_sheet.write(3, 0, 2)
    # write_excel_sheet.merge_range(1, 0, 2, 0, 12)
    # write_excel.close()

    read_excel("/Users/turtle/Desktop/1.xls")

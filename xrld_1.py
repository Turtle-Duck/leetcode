import xlrd
import xlsxwriter
import numpy as np


class rcd:
    def __init__(self, id, name, c, d, e, price_list, cpv_list, d_list):
        self.id = id
        self.name = name
        self.c = c
        self.d = d
        self.e = e
        self.price_list = price_list
        self.cpv_list = cpv_list
        self.d_list = d_list
        # print(id, price_list)
        # self.ave = np.mean(price_list)
        sum = 0
        count = 0
        for n in price_list:
            if not isinstance(n, str):
                sum += n
                count += 1
        if count == 0:
            self.ave = 0
        else:
            self.ave = sum / count


def get_value(ele):
    return ele.ave


def process_excel(path_in, path_out):

    data = xlrd.open_workbook(path_in)
    sheet_names = data.sheet_names()
    sheet = sheet_names[0]
    table = data.sheet_by_name(sheet)
    # 获取总行数
    nrows = table.nrows
    # 获取总列数
    ncols = table.ncols

    have_value = list()
    for i in range(nrows):
        # print(table.cell_value(i, 0), table.cell_value(i, 1),table.cell_value(i, 2), table.cell_value(i, 3))
        if table.cell_value(i, 1) == '':
            continue
        have_value.append(i)

    nrows_index = 0
    count = 0
    all_rcd = list()
    while nrows_index < nrows:
        id = table.cell_value(nrows_index, 0)
        name = table.cell_value(nrows_index, 1)
        c = table.cell_value(nrows_index, 2)
        d = table.cell_value(nrows_index, 3)
        e = table.cell_value(nrows_index, 4)
        price_list = [table.cell_value(nrows_index, 5)]
        cpv_list = [table.cell_value(nrows_index, 6)]
        d_list = [table.cell_value(nrows_index, 7)]
        nrows_index += 1

        while nrows_index < nrows and count + 1 < len(have_value) and nrows_index < have_value[count+1]:
            price_list.append(table.cell_value(nrows_index, 5))
            cpv_list.append(table.cell_value(nrows_index, 6))
            d_list.append(table.cell_value(nrows_index, 7))
            nrows_index += 1

        all_rcd.append(rcd(id, name, c, d, e, price_list, cpv_list, d_list))
        count += 1

    all_rcd.sort(reverse=True, key=get_value)

    write_excel = xlsxwriter.Workbook(path_out)
    write_excel_sheet = write_excel.add_worksheet()
    index = 0
    for i in range(len(all_rcd)):
        ll = len(all_rcd[i].price_list)
        for j in range(ll):
            write_excel_sheet.write(index, 0, all_rcd[i].id)
            write_excel_sheet.write(index, 1, all_rcd[i].name)
            write_excel_sheet.write(index, 2, all_rcd[i].c)
            write_excel_sheet.write(index, 3, all_rcd[i].d)
            write_excel_sheet.write(index, 4, all_rcd[i].e)
            write_excel_sheet.write(index, 5, all_rcd[i].price_list[j])
            write_excel_sheet.write(index, 6, all_rcd[i].cpv_list[j])
            write_excel_sheet.write(index, 7, all_rcd[i].d_list[j])
            write_excel_sheet.write(index, 8, all_rcd[i].ave)
            index += 1
        if ll > 1:
            write_excel_sheet.merge_range(index - ll, 0, index - 1, 0, all_rcd[i].id)
            write_excel_sheet.merge_range(index - ll, 1, index - 1, 1, all_rcd[i].name)
            write_excel_sheet.merge_range(index - ll, 2, index - 1, 2, all_rcd[i].c)
            write_excel_sheet.merge_range(index - ll, 3, index - 1, 3, all_rcd[i].d)
            write_excel_sheet.merge_range(index - ll, 4, index - 1, 4, all_rcd[i].e)
            write_excel_sheet.merge_range(index - ll, 8, index - 1, 8, all_rcd[i].ave)

    write_excel.close()


def process_excel_2(path_in, path_out):
    data = xlrd.open_workbook(path_in)
    sheet_names = data.sheet_names()
    sheet = sheet_names[0]
    table = data.sheet_by_name(sheet)
    # 获取总行数
    nrows = table.nrows
    # 获取总列数
    ncols = table.ncols

    have_value = list()
    old = -1
    for i in range(nrows):
        # print(table.cell_value(i, 0), table.cell_value(i, 1),table.cell_value(i, 2), table.cell_value(i, 3))
        if table.cell_value(i, 0) == old:
            continue
        have_value.append(i)
        old = table.cell_value(i, 0)

    write_excel = xlsxwriter.Workbook(path_out)
    write_excel_sheet = write_excel.add_worksheet()
    for i in range(len(have_value) - 1):
        index = have_value[i]
        while index < have_value[i+1]:
            write_excel_sheet.write(index, 0, i + 1)
            index += 1
        if have_value[i+1] - have_value[i] > 1:
            write_excel_sheet.merge_range(have_value[i], 0, have_value[i + 1] - 1, 0, i + 1)

    write_excel.close()


if __name__ == '__main__':

    # write_excel = xlsxwriter.Workbook("/Users/turtle/Desktop/222.xlsx")
    # write_excel_sheet = write_excel.add_worksheet()
    # write_excel_sheet.write(0, 0, 1)
    # write_excel_sheet.write(1, 0, 11)
    # write_excel_sheet.write(2, 0, 13)
    # write_excel_sheet.write(3, 0, 2)
    # write_excel_sheet.merge_range(1, 0, 2, 0, 12)
    # write_excel.close()

    process_excel_2("/Users/turtle/Desktop/1.xlsx", "/Users/turtle/Desktop/2.xlsx")
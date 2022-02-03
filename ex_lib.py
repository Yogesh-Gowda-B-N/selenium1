import xlrd

def read_locators(sheetname):
    workbook = xlrd.open_workbook(r"C:\Users\user\PycharmProjects\training1\drivers\object.xls")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    next(rows)
    locators ={row[0].value:(row[1].value,row[2].value) for row in rows}
    return locators
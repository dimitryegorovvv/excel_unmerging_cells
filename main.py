import openpyxl
excel = openpyxl.open('excel.xlsx', data_only=False, read_only=False)

for sheet in excel.worksheets:
    merged_cells = list(map(str, sheet.merged_cells.ranges))
    for cell in merged_cells:
        save_from_cell = sheet[cell.split(':')[0]].value
        first_letter_ord_from = ord((cell.split(':')[0])[0])
        first_letter_ord_to = ord((cell.split(':')[1])[0])
        sheet.unmerge_cells(cell)
        while first_letter_ord_from != first_letter_ord_to:
            first_letter_ord_from = first_letter_ord_from + 1
            new_cell_split = cell.split(':')[0]
            new_cell = new_cell_split[:0] + chr(first_letter_ord_from) + new_cell_split[1:]
            sheet[new_cell] = save_from_cell

excel.save('correct_schedule.xlsx')

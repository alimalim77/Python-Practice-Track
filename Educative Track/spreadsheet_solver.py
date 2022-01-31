def spreadsheet_encode_column(col_str):
    tot = len(col_str)
    po = tot-1
    num = 0
    
    for i in range(tot):
        num += 26**po * (ord(col_str[i]) - ord('A') +1)
        po -= 1
    return num

print(spreadsheet_encode_column("AD"))
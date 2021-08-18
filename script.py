import gspread
from number_checker import check
# from status_checker import check

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open_by_url('URL')
worksheet = sh.get_worksheet(1)

numbers = worksheet.col_values(3)
i = 0
for number in numbers:
    i += 1
    if i > 20:
        break
    try:
        if len(number) != 10:
            raise Exception
        phone = int(f"91{number}")
        res = check(phone)['result']
        print(phone, "\t", res)
        if res == "not exists":
            worksheet.update(f"I{i}", "No")
        else:
            worksheet.update(f"I{i}", "Yes")
        # res = check(phone)['status']
        # print(phone, "\t", res)
        # if res == "available":
        #     worksheet.update(f"K{i}", "Available")
        # else:
        #     worksheet.update(f"K{i}", "Not available")
    except:
        continue

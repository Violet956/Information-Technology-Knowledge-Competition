import time
import numpy as np
import pyperclip
import xlrd

resArray = []


class niubi():
    def lihai(self):
        while True:
            t = jianting().main()
            for i in range(len(resArray)):
                if t in resArray[i][0]:
                    print(resArray[i][1])


class jianting():
    def clipboard_get(self):
        data = pyperclip.paste()
        return data

    def main(self):
        recent_txt = self.clipboard_get()
        while True:
            txt = self.clipboard_get()
            if txt != recent_txt:
                recent_txt = txt
                return recent_txt
            time.sleep(0.2)


if __name__ == '__main__':
    data = xlrd.open_workbook("data.xls")
    table = data.sheet_by_index(0)
    for i in range(table.nrows):
        line = table.row_values(i)
        resArray.append(line)
    resArray = np.array(resArray)
    niubi().lihai()

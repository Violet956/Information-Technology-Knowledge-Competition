import base64
import time
import pyperclip


class niubi():
    def lihai(self):
        while True:
            t = jianting().main()
            res = base64.b64decode(t)
            res = str(res)
            i = 1
            for ch in res:
                if ch.isalpha():
                    print(str(i) + ':' + ch)
                    i = i + 1


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
    niubi().lihai()

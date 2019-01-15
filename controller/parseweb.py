from bs4 import BeautifulSoup
import requests
import json


# webサイトからのデータの取得、解析を行う
class ParseWeb:
    html = None
    url = "https://kabuoji3.com/stock/1780/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
    }

    # コンストラクタ
    def __init__(self):
        print("webParseコンストラクタ")
        self.html = requests.get(self.url, headers=self.headers)

    # webサイトデータ解析
    def date_parse(self):
        print("date_parseメソッド")
        soup = BeautifulSoup(self.html.content, 'html5lib')
        tr = soup.find_all("tr")
        cells = None
        for data_row in tr:
            for data_cell in data_row.find_all(["td", "th"]):
                cells = data_cell
                print(str(cells))
        return str(cells)

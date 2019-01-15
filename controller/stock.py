import quandl
from quandl.errors.quandl_error import NotFoundError


class Stock:
    def __init__(self):
        pass

    def get(self, stock):
        """
        :param stock: アクセスしたい情報のURL
        :return: date: 取得したテーブルデータ
        :return: values: アクセスしたURL先から戻されるテーブルデータ
        """
        authtoken = '-e6TysnfpwHM4mZw94PM'

        try:
            data = quandl.get("TSE/" + stock, authtoken=authtoken)
        except NotFoundError:
            print("株式コード：" + stock + "は存在しません")
            return
        date, values = self.shape_data(data)
        return date, values

    def shape_data(self, arg_data):
        date = arg_data.index.strftime('%Y-%m-%d')
        values = date
        return arg_data, values


# test = Stock()
# for i in range(1000, 1100):
#     stock = format(i, "04")
#     value = test.get(stock)




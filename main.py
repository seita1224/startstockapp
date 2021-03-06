from bottle import Bottle, route, run, template
# todo bottleの設定の一元管理構想設定クラス(作成中)
from config.config import Setting
import bottle
from controller.parseweb import ParseWeb

app = Bottle()

# todo bottleの設定の一元管理構想(作成中)
# app = Setting(bottle)
file_main_path = "/static/"
# 静的ファイルパス設定
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/html"]
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/css"]
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/js"]


@app.route('/', method='GET')
def defult():
    parse_web = ParseWeb()
    # todo webサイト解析処理
    return template(parse_web.date_parse())


if __name__ == "__main__":
    run(app=app, host="0.0.0.0", quiet=False, reloader=True)
else:
    application = app

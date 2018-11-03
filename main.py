from bottle import Bottle, route, run, template,default_app
# todo bottleの設定の一元管理構想設定クラス(作成中)
from config.config import Setting
import bottle


# todo bottleの設定の一元管理構想(作成中)
# app = Setting(bottle)
file_main_path = "/static/"
# 静的ファイルパス設定
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/html"]
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/css"]
bottle.TEMPLATE_PATH += ["./" + file_main_path + "/js"]


@route('/', method='GET')
def defult():

    return template("index")


if __name__ == "__main__":
    run(host="0.0.0.0", quiet=False, reloader=True)
else:
    application = default_app()

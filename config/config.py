class Setting:
    bottle = None

    def __init__(self, bottle):
        self.bottle = bottle
        self.setting_file_path(bottle)
        return bottle

    def setting_file_path(self, bottle):
        file_main_path = "/static/"
        # 静的ファイルパス設定
        self.bottle.TEMPLATE_PATH += ["./" + file_main_path + "/html"]
        self.bottle.TEMPLATE_PATH += ["./" + file_main_path + "/css"]
        self.bottle.TEMPLATE_PATH += ["./" + file_main_path + "/js"]

import codecs
import json

class CommandSettings(object):
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.Permission = "everyone"
            self.Info = ""
            self.Cooldown = 60
            self.Debug = False
            self.ScriptName = "International Hello"
            self.ScriptVersion = "1.0.0"

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def Save(self, settingsfile, parent=None, script_name=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except Exception as e:
            if parent:
                parent.Log(script_name, "Failed to save settings to file.: {}".format(e))
        return

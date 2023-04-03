import json
from telegram.ext import Updater, MessageHandler, Filters

stringReadFromFile = open("userdata.json", 'r').read()
jsonDict = json.loads(stringReadFromFile)

class userData:
    def __init__(self, data):
        self.id = data['id']
        self.userid = data['userid']
        self.name = data['name']
        self.username = data['username']
        self.points = data['points']
        self.subtype = data['subcription_type']

    def toList(self):
        return [self.id, self.userid, self.name, self.username, self.points, self.subtype]

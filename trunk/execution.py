import os

class execute():
    def __init__(self):
        #ORDER.append(self.__class__.__name__)
        pass
    def action(self):
        pass

class exitQQ(execute):
    def __init__(self):
        execute.__init__(self)
        pass

    def action(self):
        try:
            command = 'taskkill /F /IM QQ.exe'
            os.system(command)
        except os.error, e:
            print e

class exitSys(execute):
    def __init__(self):
        execute.__init__(self)
        pass

    def action(self):
        try:
            command = 'shutdown -s -t 30 -c -f'
            os.system(command)
        except os.error, e:
            print e

class exit3A(execute):
    def __init__(self):
        execute.__init__(self)
        pass

    def action(self):
        try:
            command = 'taskkill /F /IM AuthClient.exe'
            os.system(command)
        except os.error, e:
            print e

DICT_ORDER = {'exitQQ':exitQQ(), 'exitSys':exitSys(), 'exit3A':exit3A()}


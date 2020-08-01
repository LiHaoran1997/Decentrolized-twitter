from flask_babel import Babel

# Flask-Babel plugin
babel = Babel()
class Mode():
    onBlockchain=True

    def __init__(self,mode):
        self.onBlockchain=mode

    def setMode(self,mode):
        if mode == "blockchain":
            onBlockchain = True
        elif mode == "common":
            onBlockchain = False
        else:
            onBlockchain  =False
        return onBlockchain
    def getMode(self):
        return self.onBlockchain
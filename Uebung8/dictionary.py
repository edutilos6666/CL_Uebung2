print("Das Modul dictionary.py wurde aufgerufen.")
class dictionary:
    def __init__(self):
        self.logger = open("verlauf.txt", "w")
        self.container = {}

    def __del__(self):
        self.logger.close()


    def get_def(self, begriff):
        self.logger.write("get_def wurde aufgrefuen.\n")
        return self.container.get(begriff)

    def set_def(self, begriff, definitionen):
        self.logger.write("set_def wurde aufgerufen.\n")
        ret = self.container.get(begriff, [])
        ret.extend(definitionen)
        self.container[begriff] = ret

    def del_def(self, begriff, definitionen):
        self.logger.write("del_def wurde aufgerufen.\n")
        ret = self.container.get(begriff, [])
        for i, el in enumerate(definitionen):
            for j, el2 in enumerate(ret):
                if el == el2:
                    del ret[i]


        self.container[begriff] = ret



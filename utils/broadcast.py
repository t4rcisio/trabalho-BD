import os.path
import pickle


class Broadcast:


    def __init__(self):

        self.homePath = "./TEMP"

        if not os.path.exists(self.homePath):
            os.mkdir(self.homePath)

    def bdData(self, data=False):

        temp = self.__tempData("login.pickle", data)
        if temp == "":
            return False
        return temp

    def dataTransfer(self, data=False):

        temp = self.__tempData("dataTransfer.pickle", data)
        if temp == "":
            return False
        return temp

    def credentials(self, data=False):

        temp = self.__tempData("credentials.pickle", data)
        if temp == "":
            return False
        return temp


    def labelinfo(self, data=False):

        temp = self.__tempData("labelinfo.pickle", data)
        if temp == "":
            return False
        return temp


    def __tempData(self, path, data=False):


        if data != False:

            with open(self.homePath + "/" + path, "wb") as file:
                pickle.dump(data, file)
            file.close()

        else:
            try:
                with open(self.homePath + "/" + path, "rb") as file:
                    content = pickle.load(file)
                file.close()
                return content
            except:
                return ""

class BuildBatch:

    def __init__(self, path):
        objType = "\"feature\": {" if "feature" in path else "\"hierarchicalrequirement\": {"
        self.batch = """{"Batch":[{"Entry":{ "Path": """ + path + ", \"Method\": \"POST\", \"Body\": { " + objType
        self.batchCap = "}}}]}"

    def buildJson(self, values):

        retStr = self.batch
        specialObjects = []

        for i in values:

            if '{' in i or '[' in i:
                closure = '}' if '{' in i else ']' 
                specialObjects.append(i + closure + ',')
            else:
                retStr += i + ","

        for o in specialObjects:
            retStr += o

        retStr = retStr[:-1] + self.batchCap

        return retStr 
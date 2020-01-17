
class BuildBatch:

    def __init__(self, path, values):
        self.batch = """{"Batch":[{"Entry":{ "Path": """ + path
        self.type = "\"feature\": {" if "feature" in path else "\"hierarchicalrequirement\": {"
        self.values = values
        self.specialObjects = []

    def buildJson(self):

        self.batch += ", \"Method\": \"POST\", \"Body\": { " + self.type

        for i in self.values:

            if '{' in i or '[' in i:
                closure = '}' if '{' in i else ']' 
                self.specialObjects.append(i + closure + ',')
            else:
                self.batch += i + ","

        batchCap = ""
        
        for c in self.batch:

            if c == "{":
                batchCap = "}" + batchCap
            elif c =="[":
                batchCap = "]"+ batchCap
        
        for o in self.specialObjects:
            self.batch += o

        self.batch = self.batch[:-1]

        print self.batch + batchCap

        return ""        
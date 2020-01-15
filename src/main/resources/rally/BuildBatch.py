
class BuildBatch:
    
    funcDictionary = {"\"Description\":": "\"\"", "\"Notes\":": "\"\"", "\"c_AcceptanceCriteria\":":"\"\"","\"PlannedStartDate\":": "\"\""}

    def __init__(self, path):
        self.batch = """{"Batch":[{"Entry":{ "Path": """ + path
        self.type = "\"feature\": {" if "feature" in path else "\"hierarchicalrequirement\": {"

    def buildJson(self):

        self.batch += ", \"Method\": \"POST\", \"Body\": { " + self.type

        for i in BuildBatch.funcDictionary:
            
            self.batch += i + BuildBatch.funcDictionary.get(i) + ","

        batchCap = ""
        
        for c in self.batch:

            if c == "{":
                batchCap = "}" + batchCap
            elif c =="[":
                batchCap = "]"+ batchCap

        self.batch = self.batch[:-1]

        print self.batch + batchCap

        return ""

test = BuildBatch("\"/hierarchicalrequirement/\"")

test.buildJson()

        
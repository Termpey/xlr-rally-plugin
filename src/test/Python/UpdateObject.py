#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import ssl, httplib, urllib, json

class UpdateObject:

    baseURL = '/slm/webservice/v2.0/'

    def __init__(self, userAndPass):
        self.userAndPass = userAndPass

    #
    #   Feature Manipulation
    #
    def basicFeature(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context())
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20F20420)'

        conn.request('GET', curURL, "", headers)

        fQResp = conn.getresponse()

        fQJson = json.loads(fQResp.read())

        print("****Feature Query****\n")
        print(fQJson)
        print("\n\n")

        fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch": [{"Entry": {"Path": "/porfolioitem/feature/%s", "Method": "POST", "Body": {"feature": {"State": "On Hold", "Description": "Testing Plugin Script", "Notes": "Testing Plugin Script", "c_AcceptancCriteria": "Testing Plugin Script", "PlannedStartDate": "2020-01-30", "PlannedEndDate": "2020-12-30"}}}}]}"""%fRef

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request('POST', curURL, data, headers)

        request = conn.getresponse()

        print("****Feature Batch Update****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Set Mileston feature
    #
    def milestoneFeature(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20F20420)'

        conn.request('GET', curURL, "", headers)

        fQResp = conn.getresponse()

        fQJson = json.loads(fQResp.read())

        print("****Feature Query****\n")
        print(fQJson)
        print("\n\n")

        fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'milestone?fetch=Name&query=(Name%20%3D%20\"2020%20Thu%2010/1\")'

        conn.request('GET', curURL, "", headers)

        milReq = conn.getresponse()

        milJson = json.loads(milReq.read())

        print("****Milestone Query****\n")
        print(milJson)
        print("\n\n")

        milRef = milJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/portfolioitem/feature/%s", "Method": 'POST", "Body": {"feature": {"Milestones": {"Milestone": "%s"}}}}]}"""%(fRef, milRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****Feature Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Set Team to Tech Feature
    #
    def teamFeature(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20F20420)'

        conn.request('GET', curURL, "", headers)

        fQResp = conn.getresponse()

        fQJson = json.loads(fQResp.read())

        print("****Feature Query****\n")
        print(fQJson)
        print("\n\n")

        fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'project?fetch=Name&query=(Name%20%3D%20\"Tech\")'

        conn.request('GET', curURL, "", headers)

        teamReq = conn.getresponse()

        teamJson = json.loads(teamReq.read())

        print("****Project/Team Query****\n")
        print(teamJson)
        print("\n\n")

        teamRef = teamJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/portfolioitem/feature/%s", "Method": 'POST", "Body": {"feature": {"Project": "%s"}}}]}"""%(fRef, teamRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****Feature Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Set Owner on Feature
    #
    def ownerFeature(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20F20420)'

        conn.request('GET', curURL, "", headers)

        fQResp = conn.getresponse()

        fQJson = json.loads(fQResp.read())

        print("****Feature Query****\n")
        print(fQJson)
        print("\n\n")

        fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'user?fetch=Name&query=((FirstName%20%3D%20Connor)%20AND%20(LastName%20%3D%20Trempe))'

        conn.request('GET', curURL, "", headers)

        ownReq = conn.getresponse()

        ownJson = json.loads(ownReq.read())

        print("****User Query****\n")
        print(ownJson)
        print("\n\n")

        ownRef = ownJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/portfolioitem/feature/%s", "Method": 'POST", "Body": {"feature": {"Owner": {"_ref": "%s"}}}}]}"""%(fRef, ownRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****Feature Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   User Story Manipulation
    #
    def basicUserStoryManipulation(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"Description": "Plugin Script Testing", "Notes": "Plugin Script Testing", "c_AcceptanceCriteria": "Plugin Script Testing"}}}]}"""%usRef

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Searching for and Adding Iteration to User Story
    #
    def iterationUserStory(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'iteration?fetch=Name&query=((Project.Name%20%3D%20Tech)%20AND%20(Name%20%3D%20\"2020%20Sprint%201:%201/1%20-%201/14\"))'

        conn.request('GET', curURL, "", headers)

        iterReq = conn.getresponse()

        iterJson = json.loads(iterReq.read())

        print("****Iteration Query****\n")
        print(iterJson)
        print("\n\n")

        iterRef = iterJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"Iteration": "%s"}}}]}"""%(usRef, iterRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Add Mileston to User Story
    #
    def milestoneUserStory(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'milestone?fetch=Name&query=(Name%20%3D%20\"2020%20Thu%2010/1\")'

        conn.request('GET', curURL, "", headers)

        milReq = conn.getresponse()

        milJson = json.loads(milReq.read())

        print("****Milestone Query****\n")
        print(milJson)
        print("\n\n")

        milRef = milJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"Milestones": {"Milestone": "%s"}}}}]}"""%(usRef, milRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Adding Team By Title
    #
    def teamUserStory(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'project?fetch=Name&query=(Name%20%3D%20\"Release%20Management%20Team\")'

        conn.request('GET', curURL, "", headers)

        ownReq = conn.getresponse()

        ownJson = json.loads(ownReq.read())

        print("****Project/Team Query****\n")
        print(ownJson)
        print("\n\n")

        ownRef = ownJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"Project": "%s"}}}]}"""%(usRef, ownRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Add State by Project and Title
    #
    def stateUserStory(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'flowstate?fetch=Name&query=((Name%20%3D%20Accepted)%20AND%20(Project.name%20%3D%20\"Release%20Management%20Team\"))'

        conn.request('GET', curURL, "", headers)

        stsReq = conn.getresponse()

        stsJson = json.loads(stsReq.read())

        print("****State(Flow State) Query****\n")
        print(stsJson)
        print("\n\n")

        stsRef = stsJson.get('QueryResult').get('Results')[0].get('_ref')

        curURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"FlowState": {"_ref": "%s"}}}}]}"""%(usRef, stsRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""

    #
    #   Add Owner by Name User Story
    #
    def ownerUserStory(self):
        conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
        headers = {'Authorization' : 'Basic %s' % self.userAndPass}

        curURL = UpdateObject.baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

        conn.request('GET', curURL, "", headers)

        usQResp = conn.getresponse()

        usQJson = json.loads(usQResp.read())

        print("****User Story Query****\n")
        print(usQJson)
        print("\n\n")

        usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

        curUrl = UpdateObject.baseURL + 'user?fetch=FirstName,LastName&query=((FistName%20%3D%20Connor)%20AND%20(LastName%20%3D%20Trempe))'

        conn.request('GET', curURL, "", headers)

        ownReq = conn.getresponse()

        ownJson = json.loads(ownReq.read())

        print("****User Query****\n")
        print(ownJson)
        print("\n\n")

        ownRef = ownJson.get('QueryResult').get('Results')[0].get('_ref')

        cURL = UpdateObject.baseURL + 'batch'

        data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"User": {"_ref": "%s"}}}}]}"""%(usRef, ownRef)

        headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(self.userAndPass, 'API KEY')}

        conn.request("POST", curURL, data, headers)

        request = conn.getresponse()

        print("****User Story Manipulation****\n")
        print(request.read())
        print("\n\n")

        return ""
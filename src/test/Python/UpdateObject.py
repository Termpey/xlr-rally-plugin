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
from base64 import b64encode

baseURL = '/slm/webservice/v2.0/'

userAndPass = b64encode(b"%s:%s")%("username", "password")

#
#   Feature Manipulation
#

conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20F20420)'

conn.request('GET', curURL, "", headers)

fQResp = conn.getresponse()

fQJson = json.loads(fQResp.read())

print("****Feature Query****\n")
print(fQJson)
print("\n\n")

fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

curURL = baseURL + 'batch'

data = """{"Batch": [{"Entry": {"Path": "/porfolioitem/feature/%s", "Method": "POST", "Body": {"feature": {"State": "On Hold", "Description": "Testing Plugin Script", "Notes": "Testing Plugin Script", "c_AcceptancCriteria": "Testing Plugin Script", "PlannedStartDate": "2020-01-30", "PlannedEndDate": "2020-12-30"}}}}]}"""%fRef

headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s'%(userAndPass, 'API KEY')}

conn.request('POST', curURL, data, headers)

request = conn.getresponse()

print("****Feature Batch Update****\n")
print(request.read())
print("\n\n")

#
#   User Story Manipulation
#

conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context()) #Re-establis Connection after PUT/POST/DELETE
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FormattedID%20%3D%20US138725)'

conn.request('GET', curURL, "", headers)

usQResp = conn.getresponse()

usQJson = json.loads(usQResp.read())

print("****User Story Query****\n")
print(usQJson)
print("\n\n")

usRef = usQJson.get('QueryResult').get('Results')[0].get('_ref')

data = """{"Batch":["Entry":{"Path":"/hierarchicalrequirement/%s", "Method": 'POST", "Body": {"hierarchicalrequirement": {"Description": "Plugin Script Testing", "Notes": "Plugin Script Testing", "c_AcceptanceCriteria": "Plugin Script Testing"}}}]}"""%usRef

conn.request("POST", curURL, data, headers)

request = conn.getresponse()

print("****User Story Manipulation****\n")
print(request.read())
print("\n\n")
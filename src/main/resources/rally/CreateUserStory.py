#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import logging, ssl, httplib, urllib, json
from bin.main.rally.BuildCreate import BuildCreate
from bin.main.rally.FetchReference import FetchReference
from base64 import b64encode

baseURL = '/slm/webservice/v2.0/'
values = []

query = FetchReference(userAndPass, configuration.url)

logger = logging.getLogger(__name__)
logger.debug("In Create User Story")

userAndPass = b64encode(b"%s:%s")%(configuration.userName, configuration.password)

conn = httplib.HTTPSConnection(configuration.url,"443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20' + %featureID + ')'

conn.request('GET', curURL, "", headers)

fQResp = conn.getresponse()

fQJson = json.loads(fQResp.read())

print(fQJson)

fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

val = "\"Name\": \"%s\""%title
values.append(val)

val = "\"PortfolioItem\": \"/portfolioitem/feature/%s\""%fRef

val = "\"PlannedStartDate\": \"%s\""%startDate
values.append(val)

val = "\"PlannedEndDate\": \"%s\""%endDate
values.append(val)

val = "\"Description\": \"%s\""%desc
values.append(val)

val = "\"c_AcceptanceCriteria\": \"%s\""%accCriteria
values.append(val)

curURL = baseURL + 'user?fetch=DisplayName&query(DisplayName%20%3D%20\"' + owner.replace(" ", "%20") + '\")'
ownRef = query.getValue(curURL, userAndPass)
val = "\"Owner\": \"%s\""%ownRef

curURL = baseURL + 'project?fetch=Name&query=(Name%20%3D%20\"' + team.replace(" ", "%20") + '\")'
teamRef = query.getValue(curURL, userAndPass)
val = "\"Project\": \"%s\""%teamRef
values.append(val)

curURL = baseURL + 'flowstate?fetch=Name&query=((Project.Name%20%3D%20\"Tech\")%20AND%20(Name%20%3D%20\"' + state.replace(" ", "%20") + '\"))'
stateRef = query.getValue(curURL, userAndPass)
val = "\"FlowState\": {\"_ref\": \"%s\""%stateRef
values.append(val)

if notes != "":
    val = "\"Notes\": \"%s\""
    values.append(val)

if milestone != "":
    curURL = baseURL + 'milesont?fetch=Name&query=(Name%20%3D%20\"' + milestone.replace(" ","%20")+ '\")'
    milRef = query.getValue(curURL, userAndPass)
    val = "\"Milestones\":{ \"Milestone\": \"%s\""%milRef
    values.append(val)

if iteration != "":
    curUrl = baseURL + 'iteration?fetch=Name&query=((Project.Name%20%3D%20Tech)%20AND%20(Name%20%3D%20\"' + iteration.replace(" ", "%20") + '\"))'
    iterRef = query.getValue(curURL, userAndPass)
    val = "\"Iteration\": \"%s\""%iterRef
    values.append(val)

if release != "":
    curURL = baseURL + 'release?fetch=Name&query((Project.Name%20%3D%20Tech)%20AND%20(Name%20%3D%20\"' + release.replace(" ", "%20")'\"))'
    releaseRef = query.getValue(curURL, userAndPass)
    val = "\"Release\": \"%s\""%releaseRef
    values.append(val)

curURL = baseURL + 'security/authorize'

conn.request('GET', curURL, "", headers)

secResp = conn.getresponse()

secJson = json.loads(secResp.read())

TOK = secResp.get('OperationResult').get('SecurityToken')

headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s' %(userAndPass, configuration.apiKey)}

buildJson = BuildCreate("HierarchicalRequirement")

data = buildJson.buildCreate(values)

info = json.loads(data)

curURL = 'hierarchicalrequirement/create?key=%s'%TOK

conn.request('PUT', curURL, json.dumps(info, indent=4), headers)

usCResp = conn.getresponse()

print(usCResp.read())
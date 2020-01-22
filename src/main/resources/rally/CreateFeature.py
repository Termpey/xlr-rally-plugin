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
from base64 import b64encode

baseURL = '/slm/webservice/v2.0/'

values = []

logger = logging.getLogger(__name__)
logger.debug("In Create Feature")

userAndPass = b64encode(b"%s:%s")%(configuration.userName, configuration.password)

conn = httplib.HTTPSConnection(configuration.url,"443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + '/portfolioitem/epic?fetch=FormattedID$query=(FormattedID%20%3D%20' + epicID + ')'

conn.request('GET', curURL, "", headers)

epicQResp = conn.getresponse()

epicQJson = json.loads(epicQResp.read())

epicRef = epicQJson.get('QueryResult').get('Result')[0].get('_ref')

val = "\"Name\": \"%s\""%title
values.append(val)

val = "\"PortfolioItem\": \"%s\""%epicRef
values.append(val)

val = "\"PlannedStartDate\": \"%s\""%startDate
values.append(val)

val = "\"PlannedEndDate\": \"%s\""%endDate
values.append(val)

val = "\"Description\": \"%s\""%desc
values.append(val)

val = "\"c_AcceptanceCriteria\": \"%s\""%accCriteria
values.append(val)

val = "\"State\": \"%s\""%state
values.append(val)

curURL = baseURL + 'user?fetch=DisplayName&query=(DisplayName%20%3D%20\"' + owner.replace(" ","%20") + '\")'
ownRef = getValue(curURL, userAndPass)
val = "\"Owner\": \"%s\""%ownRef
values.append(val)

if notes != "":
    val = "\"Notes\": \"%s\""
    values.append(val)

if milestone != "":
    curURL = baseURL + 'milesont?fetch=Name&query=(Name%20%3D%20\"' + milestone.replace(" ","%20")+ '\")'
    milRef = getValue(curURL, userAndPass)
    val = "\"Milestones\":{ \"Milestone\": \"%s\""%milRef
    values.append(val)

if iteration != "":
    curUrl = baseURL + 'iteration?fetch=Name&query=((Project.Name%20%3D%20Tech)%20AND%20(Name%20%3D%20\"' + iteration.replace(" ", "%20") + '\"))'
    iterRef = getValue(curURL, userAndPass)
    val = "\"Iteration\": \"%s\""%iterRef
    values.append(val)

curURL = baseURL + '/security/authorize'

conn.request('GET', curURL, "", headers)

secResp = conn.getresponse()

secJson = json.loads(secResp.read())

TOK = secResp.get('OperationResult').get('SecurityToken')

headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s' %(userAndPass, configuration.apiKey)}

jsonBuild = BuildCreate("feature")

data = jsonBuild.buildCreate(values)

info = json.loads(data)

curUrl = baseURL + 'feature/create?key=' + TOK

conn.request('PUT', curURL, json.dumps(info, indent=4), headers=headers)

fresp = conn.getresponse()

print(fresp.read())

def getValue(url, userAndPass):

    conn = httplib.HTTPSConnection(configuration.url,"443",context=ssl._create_unverified_context())
    headers = {'Authorization' : 'Basic %s' %userAndPass}

    conn.request('GET', url, "", headers)

    request = conn.getresponse()

    responseJson = json.loads(request.read())

    if responseJson.get('QueryResult').get('TotalResultCount') == 0:
        ref = responseJson.get('QueryResult').get('Results')[0].get('_ref')

        return ref
    else:
        logger.debug("Query of " + url + " resulted in 0 or multiple results")

        return ""
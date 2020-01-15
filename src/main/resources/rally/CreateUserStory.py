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
from base64 import b64encode

baseURL = '/slm/webservice/v2.0/'

logger = logging.getLogger(__name__)
logger.debug("In Create User Story")

userAndPass = b64encode(b"%s:%s")%(configuration.userName, configuration.password)

conn = httplib.HTTPSConnection(configuration.url,"443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + 'portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20%s)'%featureID

conn.request('GET', curURL, "", headers)

fQResp = conn.getresponse()

fQJson = json.loads(fQResp.read())

print(fQJson)

fRef = fQJson.get('QueryResult').get('Results')[0].get('_ref')

curURL = baseURL + 'security/authorize'

conn.request('GET', curURL, "", headers)

secResp = conn.getresponse()

secJson = json.loads(secResp.read())

TOK = secResp.get('OperationResult').get('SecurityToken')

headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s' %(userAndPass, configuration.apiKey)}

data = """{"HierarchicalRequirement":{"Name": "%s", "PortfolioItem": "/portfolioitem/feature/%s"}}"""%(name,fRef)

info = json.loads(data)

curURL = 'hierarchicalrequirement/create?key=%s'%TOK

conn.request('PUT', curURL, json.dumps(info, indent=4), headers)

usCResp = conn.getresponse()

print(usCResp.read())
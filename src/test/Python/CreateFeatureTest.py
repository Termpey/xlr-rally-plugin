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
logger.debug("In Create Feature")

userAndPass = b64encode(b"%s:%s")%("username", "password")

conn = httplib.HTTPSConnection("rally1.rallydev.com","443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' % userAndPass}

curURL = baseURL + '/portfolioitem/epic?fetch=FormattedID$query=(FormattedID%20%3D%20E4261)'

conn.request('GET', curURL, "", headers)

epicQResp = conn.getresponse()

epicQJson = json.loads(epicQResp.read())

print("****Epic Query****\n")
print(epicQJson)
print("\n\n")

epicRef = epicQJson.get('QueryResult').get('Result')[0].get('_ref')

curURL = baseURL + '/security/authorize'

conn.request('GET', curURL, "", headers)

secResp = conn.getresponse()

secJson = json.loads(secResp.read())

print("****Security Authorization****\n")
print(secJson)
print("\n\n")

TOK = secResp.get('OperationResult').get('SecurityToken')

headers = {'Authorization' : 'Basic %s', 'ZSESSIONID' : '%s' %(userAndPass, "API Key")}

data = """{"Feature":{"Name":"%s","PortfolioItem":"%s"}}"""%("Sanity Test",epicRef)

info = json.loads(data)

curUrl = baseURL + 'feature/create?key=' + TOK

conn.request('PUT', curURL, json.dumps(info, indent=4), headers=headers)

fresp = conn.getresponse()

print("****Feature Creation****\n")
print(fresp.read())
print("\n\n")
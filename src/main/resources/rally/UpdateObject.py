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

logger = logging.getLogger(__name__)
logger.debug("In Update Object")

baseURL = '/slm/webservice/v2.0/'

isFeature = 'F' in formattedID

userAndPass = b64encode(b"%s:%s")%(configuration.userName, configuration.password)

values = []

conn = httplib.HTTPSConnection(configuration.url,"443",context=ssl._create_unverified_context())
headers = {'Authorization' : 'Basic %s' %userAndPass}

curURL =  baseURL + '/portfolioitem/feature?fetch=FormattedID&query=(FormattedID%20%3D%20%s)'%formattedID if isFeature else baseURL + 'hierarchicalrequirement?fetch=FormattedID&query=(FromattedID%20%3D%20%s)'%formattedID

conn.request('GET', curURL, "", headers)

request = conn.getresponse()

reqJson = json.loads(request.read())

objectRef = reqJson.get('QueryResult').get('Results')[0].get('_ref')

for i in fields:
    
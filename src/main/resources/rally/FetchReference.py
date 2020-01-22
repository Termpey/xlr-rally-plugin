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

class FetchReference:

    def __init__(self, userAndPass, url):
        self.userAndPass = userAndPass
        self.url = url

    def getValue(self, query, values):
        conn = httplib.HTTPSConnection(self.url,"443",context=ssl._create_unverified_context())
        headers = {'Authorization' : 'Basic %s' %self.userAndPass}

        conn.request('GET', query, "", headers)

        request = conn.getresponse()

        responseJson = json.loads(request.read())

        if responseJson.get('QueryResult').get('TotalResultCount') == 0:
            ref = responseJson.get('QueryResult').get('Results')[0].get('_ref')

            return ref
        else:
            logger.debug("Query of " + url + " resulted in 0 or multiple results")

            return ""
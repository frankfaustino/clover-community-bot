# pylint: disable=missing-docstring
# pylint: disable=wrong-import-position

import sys
sys.path.append("lib")

from requests_toolbelt.adapters import appengine
import webapp2

import daily_digest
import hottest
import overview

appengine.monkeypatch()


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

APP = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/daily_digest', daily_digest.DailyDigest),
    ('/hottest', hottest.Hottest),
    ('/overview', overview.Overview),
], debug=True)

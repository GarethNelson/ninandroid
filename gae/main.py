#!/usr/bin/env python
import wsgiref.handlers
import os
import content
from google.appengine.ext import webapp

class HomePageHandler(webapp.RequestHandler):
      def get(self):
          self.response.out.write(content.homepage % ('http://www.nin.com/photoblog/uploaded_images/photo-757886-757915.jpg',''))

class LoginHandler(webapp.RequestHandler):
      def get(self):
          pass

urls = (('/home',HomePageHandler),
        ('/login',LoginHandler))

application = webapp.WSGIApplication(urls,debug=True)
wsgiref.handlers.CGIHandler().run(application)

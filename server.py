"""Application module file"""
import falcon

from resources import SampleResource
from db import SQLAlchemySessionManager, Session

# falcon.API instances are callable WSGI apps
APP = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])

# set x-www-form-urlencoded to be available via req.params
APP.req_options.auto_parse_form_urlencoded = True

# Resources are represented by long-lived class instances
SAMPLE = SampleResource()

# Sample route creation
APP.add_route('/sample', SAMPLE)

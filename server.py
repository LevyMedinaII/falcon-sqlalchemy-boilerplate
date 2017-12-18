import json
import falcon
import requests

from resources import AppliancesResource,  SampleResource
from db import SQLAlchemySessionManager, Session, Sample

# falcon.API instances are callable WSGI apps
app = falcon.API()

# set x-www-form-urlencoded to be available via req.params
app.req_options.auto_parse_form_urlencoded = True

# Resources are represented by long-lived class instances
sample = SampleResource()
appliances = AppliancesResource()

# Routes
app.add_route('/sample', sample)
app.add_route('/appliances', appliances)
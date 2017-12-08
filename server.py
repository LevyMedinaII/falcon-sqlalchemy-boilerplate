import json
import falcon
import requests

class TestResource(object):
    def on_get(self, req, res):
        #Test route
        root = 'https://reqres.in'
        route = '/api/users?page=2'

        test_data = requests.get(root + route)
        res.status = falcon.HTTP_200  # This is the default status
        test_data = test_data.json()
        res.body = json.dumps(test_data)

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
test = TestResource()

# things will handle all requests to the '/things' URL path
app.add_route('/test', test)
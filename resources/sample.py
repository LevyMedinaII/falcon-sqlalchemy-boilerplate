import json
import falcon

from db import Sample

# Sample Resource
class SampleResource(object):
    def on_get(self, req, res):
        # Test route
        ### External API Call ###
        # root = 'https://reqres.in'
        # route = '/api/users?page=2'
        # test_data = requests.get(root + route)
        # res.status = falcon.HTTP_200  # This is the default status
        # test_data = test_data.json()
        # res.body = json.dumps(test_data)
        
        ### Database add to table ###
        # sample_test = Sample(name='sample', fullname='Sample Name', password='samplepass')
        # self.session.add(sample_test)
        # self.session.commit()

        res.body = json.dumps({ 'status': 'finished' })
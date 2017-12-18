import json
import falcon

# from db import Sample

class AppliancesResource(object):
    def on_get(self, req, res):
        json_data = { 'test': 'test' }
        res.body = json.dumps(json_data)
        res.status = falcon.HTTP_200
        
    def on_post(self, req, res):
        # x-www-form-urlencoded
        # requestBody = req.params
        # earthquakeData = req.get_param_as_list('earthquake_data')

        # raw/json
        # requestBody  = json.load(req.stream)
        # earthquakeData = requestBody.get('earthquake_data')
        
        json_data = { 'test': 'test' }
        
        res.body = json.dumps(json_data)
        res.status = falcon.HTTP_200
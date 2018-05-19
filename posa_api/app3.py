import json
import falcon


class ObjRequestClass:


    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        if 'name' in req.params and 'age' in req.params:
            output = {
                'name': req.params['name'], 
                'age': req.params['age'], 
            }
        else:
            resp.status = falcon.HTTP_404
            output = {
                'msg': 'sfdfds',
            }
        
        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/params', ObjRequestClass())

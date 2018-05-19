import json
import falcon


class ObjRequestClass:
    __json__content = {}

    def __validate__json__input(self, req):
        try:
            self.__json__content = json.loads(req.stream.read())
            print('Json from client is validated')
            return True

        except ValueError:
            self.__json__content = {}
            print('Json is not validated!')
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {
            'status': 200,
            'msg': None
        }
        validated = self.__validate__json__input(req)
        if(validated):
            if 'name' in self.__json__content:
                output['msg'] = 'Hello {0}'.format(
                    self.__json__content['name'])
            else:
                output['status'] = 404
                output['msg'] = 'No noame'
        else:
            output['status'] = 404
            output['msg'] = 'json input is not validated'

        resp.body = json.dumps(output)

    def on_post(self, req, resp):

        data = json.loads(req.stream.read())

        equal = int(data['x']) + int(data['y'])
        output = {
            'msg': 'A soma é {0}'.format(equal)
        }
        resp.status = falcon.HTTP_201
        resp.body = json.dumps(output)

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {
            'msg': 'Não feito ainda'
        }

        resp.body = json.dumps(output)

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {
            'msg': 'Não feito ainda'
        }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/demo', ObjRequestClass())


import falcon
import json


# class ObjRequestClass:
#     def on_get(self, req, resp):
#         resp.status = falcon.HTTP_200
#         data = json.loads(req.stream.read())
#         print(data)

#         content = {
#             'name': "Jordan",
#             'age': 22
#         }

#         output = {}
#         if('method' not in data):
#             resp.status = falcon.HTTP_501
#             output['value'] = 'Error: no method found - sorry'
#         else:
#             if(data["method"] == "get-name"):
#                 output['value'] = content['name']
#             else:
#                 resp.status = falcon.HTTP_404
#                 output['value'] = None
#             resp.body = json.dumps(output)


# api = falcon.API()
# api.add_route('/test', ObjRequestClass())

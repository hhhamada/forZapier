from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token, JWTManager
#from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import User

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'hama'
api = Api(app)

jwt = JWTManager(app)

items = []

class Auth(Resource):
    def post(self):
        data = request.get_json()
        auth_user = authenticate(data['username'], data['password'])
        if not auth_user:
            return {'message': 'Invalid user.'}, 401
        access_token = create_access_token(identity=auth_user.id)
        return {'access_token': access_token} , 200

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}
        
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}
    
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            itam = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    @jwt_required
    def get(self):
        return {'items': items}

api.add_resource(Auth, '/auth')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(debug=True)
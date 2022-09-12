from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token, JWTManager
#from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import User
from customer import Customer,Interview
import datetime
import json

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'hama'
api = Api(app)

jwt = JWTManager(app)


date11 = datetime.datetime(2021, 11, 4, 17, 37, 28)
date1 = date11.strftime("%y/%m/%d %H:%M:%S.000")

interviews = [
    [
        Interview(1, date1, 'sample_zoom_url', 'sample_box_url'),
        Interview(2, date1, 'sample_zoom_url', 'sample_box_url'),
        Interview(3, date1, 'sample_zoom_url', 'sample_box_url'),
    ],
    [
        Interview(1, date1, 'sample_zoom_url', 'sample_box_url'),
        Interview(2, date1, 'sample_zoom_url', 'sample_box_url'),
    ]
]

customers = [
    Customer(1, 'user1', 'sample@example.com', interviews[0]),
    Customer(2, 'user2', 'sample@example.com', interviews[1]),
]

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

class InterviewList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('start_time',
    type=str,
    required=True,
    help="This field cannot be left blank!"
    )
    parser.add_argument('zoom_url',
    type=str,
    required=True,
    help="This field cannot be left blank!"
    )
    parser.add_argument('box_url',
    type=str,
    required=True,
    help="This field cannot be left blank!"
    )

    #@jwt_required()
    def get(self, customer_id):
        #if next(filter(lambda x: x['name'] == name, items), None) is not None:
        if next(filter(lambda x: x.id == customer_id, customers), None) is not None:
            return [iv_list.__dict__ for iv_list in customers[customer_id-1].interviews]
        return {'message': 'invald customer id'}

    #@jwt_required()
    def post(self, customer_id):
        if next(filter(lambda x: x.id == customer_id, customers), None) is not None:
            data = InterviewList.parser.parse_args()
            interview = Interview(len(customers[customer_id - 1].interviews) + 1, data['start_time'], data['zoom_url'], data['box_url'])
            customers[customer_id - 1].interviews.append(interview)
            return interview.__dict__, 201
        return {'message': "An custmer with id '{}' is not exists.".format(customer_id)}, 400

class InterviewAPI(Resource):
    #@jwt_required()
    def get(self, customer_id, interview_id):
        return {'interview': None}
    



api.add_resource(Auth, '/auth')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(InterviewList, '/interviews/<int:customer_id>')
api.add_resource(InterviewAPI, '/interview/<int:customer_id>/<int:interview_id>')


if __name__ == '__main__':
    app.run(debug=True)
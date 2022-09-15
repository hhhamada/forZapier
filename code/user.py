class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

class Reserver(object):
    def __init__(self, reserver_id, reserver_name, reserver_mailaddress):
        self.id = reserver_id
        self.name = reserver_name
        self.mail_address = reserver_mailaddress

class Nurse(object):
    def __init__(self, nurse_id, name):
        self.id = nurse_id
        self.name = name
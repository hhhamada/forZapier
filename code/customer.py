class Interview(object):
    def __init__(self, _id, start_time, zoom_url, box_url):
        self.id = _id
        self.start_time = start_time
        self.zoom_url = zoom_url
        self.box_url = box_url

class Customer(object):
    def __init__(self, _id, customer_name,email_address, interviews):
        self.id = _id
        self.customer_name = customer_name
        self.email_address = email_address
        self.interviews = interviews
class Reserve(object):
    def __init__(self, reserve_id, nurse, reserver_name, reserver_mailaddress, start_time):
        self.id = reserve_id
        self.nurse = nurse
        self.name = reserver_name
        self.mail_address = reserver_mailaddress
        self.start_time = start_time

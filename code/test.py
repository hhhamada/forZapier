import datetime
import json,random

class Interview(object):
    def __init__(self, _id, start_time, zoom_url, box_url):
        self.id = _id
        self.start_time = start_time
        self.zoom_url = zoom_url
        self.box_url = box_url

class User(object):
    def __init__(self, _id, username, password, email_address, interviews):
        self.id = _id
        self.username = username
        self.password = password
        self.email_address = email_address
        self.interviews = interviews




if __name__ == '__main__':
    date11 = datetime.datetime(2021, 11, 4, 17, 37, 28)
    date22 = datetime.datetime(2021, 11, 5, 17, 37, 28)
    date3 = datetime.datetime(2021, 11, 6, 17, 37, 28).strftime("%y/%m/%d %H:%M:%S.000")

    date1 = date11.strftime("%y/%m/%d %H:%M:%S.000")
    date2 = date22.strftime("%y/%m/%d %H:%M:%S.000")

    interviews1 = [
        Interview(1, date1, 'sample_zoom_url', 'sample_box_url'),
        Interview(2, date2, 'sample_zoom_url', 'sample_box_url'),
        Interview(3, date3, 'sample_zoom_url', 'sample_box_url'),
    ]

    interviews2 = [
        Interview(1, date3, 'sample_zoom_url', 'sample_box_url'),
        Interview(2, date2, 'sample_zoom_url', 'sample_box_url'),
    ]

    users = [
        User(1, 'user1', 'abcxyz', 'sample@example.com', interviews1),
        User(2, 'user2', 'abcxyz', 'sample@example.com', interviews2),
    ]

    print(interviews1[1])
    print(interviews1[1].__dict__)
    print(interviews1[1].start_time)

    iv_list = [iv.__dict__ for iv in interviews2]
    obj_json = json.dumps(iv_list)
    print(obj_json)

    year = 2022
    month = 5#random.randint(1,12)
    day = random.randint(28,28 if month == 2 else 30 if month in [4,6,9,11] else 31)
    print(year)
    print(month)
    print(day)

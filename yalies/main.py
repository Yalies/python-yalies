import requests


class Student:
    def __init__(self, raw):
        self.raw = raw

        self.netid = raw.get('netid')
        self.upi = raw.get('upi')
        self.first_name = raw.get('first_name')
        self.last_name = raw.get('last_name')
        self.image_id = raw.get('image_id')
        self.image = raw.get('image')
        self.year = raw.get('year')
        self.college = raw.get('college')
        self.pronoun = raw.get('pronoun')
        self.email = raw.get('email')
        self.residence = raw.get('residence')
        self.building_code = raw.get('building_code')
        self.entryway = raw.get('entryway')
        self.floor = raw.get('floor')
        self.suite = raw.get('suite')
        self.room = raw.get('room')
        self.birthday = raw.get('birthday')
        self.major = raw.get('major')
        self.address = raw.get('address')
        self.phone = raw.get('phone')
        self.leave = raw.get('leave')
        self.eli_whitney = raw.get('eli_whitney')
        self.access_code = raw.get('access_code')


class API:
    _HOST = 'https://yalies.io'
    _API_ROOT = '/api/'

    def __init__(self, token: str):
        self.token = token

    def post(self, endpoint: str, body: dict = {}):
        """
        Make a POST request to the API.

        :param params: dictionary of custom params to add to request.
        """
        headers = {
            'Authorization': 'Bearer ' + self.token,
        }
        request = requests.post(self._HOST + self._API_ROOT + endpoint,
                                json=body,
                                headers=headers)
        if request.ok:
            return request.json()
        else:
            raise Exception('API request failed. Received:\n' + request.text)

    def students(self, query=None, filters=None, page=None, page_size=None):
        """
        Given search criteria, get a list of matching students.
        """
        body = {
            'query': query,
            'filters': filters,
            'page': page,
            'page_size': page_size,
        }
        body = {k: v for k, v in body.items() if v}
        return [
            Student(student) for student in
            self.post('students', body=body)
        ]

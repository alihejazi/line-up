import json

class User():
    # Deserialise the following values from the returned User from the 3rd party API.
    # If more fields are returned by the 3rd party, we only return the one listed below
    def __init__(self, json: dict):
        self.id = json['id']
        self.email = json['email']
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.avatar = json['avatar']

    def as_payload(dict):
        return User(dict)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

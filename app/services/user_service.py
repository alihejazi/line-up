import os, requests
from dotenv import load_dotenv
from models.user import User
from exceptions.service_unavailable_exception import ServiceUnavailableException

# Read the .env file
load_dotenv()
BASE_REQRES_URI = os.getenv('BASE_REQRES_URI')

class UserService():
    def get_user(user_id: int):
        response = requests.get('{}/users/{}'.format(BASE_REQRES_URI, user_id))

        if response.status_code == 200:
            # Deserialise the returned user data into a User object
            return User(response.json()['data'])

        elif response.status_code == 404:
            return None

        # If we get neither 200 nor 404 from the 3rd party, then it's likely it
        # has a problem, so whatever the status code, let's raise an exception
        # and return 503 from our side to our clients
        raise ServiceUnavailableException()

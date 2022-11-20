from fastapi import FastAPI, Response, Depends
import jsonpickle
from models.user import User
from models.error_response import ErrorResponse
from exceptions.service_unavailable_exception import ServiceUnavailableException
# from services.user_service import UserService
from dependencies import dependencies

# Run the app
app = FastAPI()

# Here we could, if needed, add middleware to make our API much more relaible, secure, and stable.
# For example CORS rules, rate limiting middleware, JWT authentication middleware, etc. Due to time
# time-limitations I have not been able to implement any middleware in this submission, but I am
# commenting here to demonstrate knowledge.
# app.add_middleware(...)

@app.get("/users/{user_id}")
def getUser(user_id: int, resp: Response, dependencies: dict = Depends(dependencies)):
    try:
        # user service loaded by dependency injection
        user_service = dependencies['UserService']
        user: User = user_service.get_user(user_id)

        if (user is None):
            # Return error response with status 404 (which is set in outer if)
            resp.status_code = 404
            return ErrorResponse('No user found with id {}'.format(user_id))

        # Do whatever business logic needed on User here...

        # On finishing any required business logic, return 200 and user obj
        resp.status_code = 200
        # Re-serialise on return
        return jsonpickle.decode(user.toJSON())


    except ServiceUnavailableException as e:
        # Catch ServiceUnavailableException and return 503 from our side
        # to our clients
        resp.status_code = 503
        return ErrorResponse(str(e))

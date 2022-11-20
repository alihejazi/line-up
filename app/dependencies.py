# Very simple way to demonstrate dependency injection
from services.user_service import UserService

async def dependencies():
    return {
        "UserService": UserService
    }

from ninja import NinjaAPI

from users.api.views import router as user_router
from barber.api.views import router as barber_router

api = NinjaAPI()
api.add_router('/users/', user_router, tags=['User'])
api.add_router('/barbers/', barber_router, tags=['Barber'])
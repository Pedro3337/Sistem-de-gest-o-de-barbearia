from ninja import NinjaAPI

from users.api.views import router as user_router
from barber.api.views import router as barber_router
from service.api.views import router as service_router
from appointments.api.views import router as appointment_router

api = NinjaAPI()
api.add_router('/users/', user_router, tags=['User'])
api.add_router('/barbers/', barber_router, tags=['Barber'])
api.add_router('/services/', service_router, tags=['Services'] )
api.add_router('/appointments/', appointment_router, tags=['Appointment'])
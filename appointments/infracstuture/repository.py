from uuid import UUID

import appointments
from appointments.domain.entities import AppointmentEntity
from appointments.domain.respositorie import IAppointmentRepositorie
from appointments.infracstuture.models import Appointment
from clients.infrasctuture.models import Client
from barber.infrasctuture.models import Barber
from service.infrasctuture.models import Service

from typing import List
from datetime import date

class AppointmentRepository(IAppointmentRepositorie):
    def save(self, entity: AppointmentEntity) -> AppointmentEntity:

        print("DATE:", entity.date_a)
        print("TIME:", entity.time_a)
        print("TIMEZONE:", entity.time_a.tzinfo)

        client = Client.objects.get(id=entity.client)
        barber = Barber.objects.get(id=entity.barber)
        service = Service.objects.get(id=entity.service)
        Appointment.objects.update_or_create(
            id=entity.id,
            defaults={
                'client': client,
                'barber': barber,
                'service': service,
                'date': entity.date_a,
                'time': entity.time_a,
                'status': entity.status,
                'observation': entity.observation
            }
        )

        return entity

    def find_by_id(self, id: UUID) -> AppointmentEntity:
        try:
            return self._to_model(Appointment.objects.get(id=id))
        except Appointment.DoesNotExist:
            return None

    def response_all_appointments(self) -> List[AppointmentEntity]:
        try:
            return [self._to_model(appointments) for appointments in Appointment.objects.all()]
        except Appointment.DoesNotExist:
            return None

    def response_appointments_where_barber_id(self, barber_UUID: UUID) -> List[AppointmentEntity]:
        try:
            return [
                self._to_model(appointments)
                for appointments in Appointment.objects.filter(barber=barber_UUID).all()
            ]
        except Appointment.DoesNotExist:
            return None

    def response_appointement_where_barber_id_and_date(self, id: UUID, date: date):
        try:
            return [
                self._to_model(appointment)
                for appointment in Appointment.objects.filter(barber=id, date=date)
            ]
        except Appointment.DoesNotExist:
            return None

    def response_appointment_where_client_id(self, id: UUID) -> List[AppointmentEntity]:
        try:
            return [self._to_model(appointment) for appointment in Appointment.objects.filter(client=id)]
        except Appointment.DoesNotExist:
            return None

    def _to_model(self, model: Appointment) -> AppointmentEntity:
        return AppointmentEntity(
            id=model.id,
            client=model.client.id,
            barber=model.barber.id,
            service=model.service.id,
            date_a=model.date,
            time_a=model.time,
            status=model.status,
            observation=model.observation
        )
from ariadne import convert_kwargs_to_snake_case
from doctors.models import Doctor
from django.db import transaction

class DoctorsMutations:
    """
    Mutation methods to perform creation updates and deletion in the Doctors model
    """

    def __init__(self):
        pass

    @staticmethod
    @convert_kwargs_to_snake_case
    def create(_, info, create_input):

        try:
            with transaction.atomic():

                return dict(
                status=True,
                object=Doctor.objects.create(**create_input)
                )
        except Exception as e:
            return dict(status=False, error=f'An error occurred {e}')

    @staticmethod
    @convert_kwargs_to_snake_case
    def update(_, info, update_input):

        try:
            with transaction.atomic():

                return dict(
                    status=True,
                    object=Doctor.objects.update(**update_input)
                )
        except Exception as e:
            return dict(status=False, error=f'An error occurred {e}')


    @staticmethod
    @convert_kwargs_to_snake_case
    def soft_delete(_, info, uid):

        try:
            with transaction.atomic():
                record = Doctor.objects.get(uid=uid)
                record.soft_delete()
                return dict(
                    status=True,
                    object=record
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error occurred: {e}'
            )
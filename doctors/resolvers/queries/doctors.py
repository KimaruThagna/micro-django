from typing import Any, Dict, Optional

from ariadne import convert_kwargs_to_snake_case

from doctors.models import Doctor
from django.db import transaction


class DoctorsQueries:
    """
    Methods used to retrieve Doctors data
    """

    @staticmethod
    def filter(queryset, filter_input):
        return queryset.filter(**filter_input)

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctor(_, info, uid):

        try:
            with transaction.atomic():
                return dict(
                    status=True,
                    object=Doctor.objects.filter(uid=uid).not_deleted()[0]
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error as occurred {e}'
            )

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctors(_, info, pagination_input,filter_input):

        try:
            return paginate (DoctorsQueries.filter(
                Doctor.objects.all().not_deleted(), filter_input=filter_input),
                            pagination_input=pagination_input)
        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")
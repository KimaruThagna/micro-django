from typing import Dict, Optional

from ariadne import convert_kwargs_to_snake_case
from doctors.models import Doctor

class DoctorsMutations:
    """
    Mutation methods to perform creation updates and deletion in the Doctors model
    """

    def __init__(self):
        pass

    @staticmethod
    @convert_kwargs_to_snake_case
    def create(_, info, create_input: Dict):

        try:


            return dict(
                status=True,
                object=Doctor.objects.create(create_input)
            )
        except Exception as e:
            return dict(status=False, error=f'An error occurred {e}')

    @staticmethod
    @convert_kwargs_to_snake_case
    def soft_delete(_, info, uid: str, deleted_by: Optional[str] = None):
        if deleted_by:
            return MutationUtils.soft_delete(
                info=info, model=Doctor, uid=uid, deleted_by=deleted_by
            )
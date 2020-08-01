from typing import Any, Dict, Optional

from ariadne import convert_kwargs_to_snake_case

from doctors.models import Doctor
from utils.queries import QueryUtils


class DoctorsQueries:
    """
    Methods used to retrieve Doctors data
    """

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctor(_, info, uid: str) -> Dict:

        return QueryUtils.get_single_object(info=info, model=Doctor, uid=uid)

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_doctors(_, info, pagination_input: Optional[Dict[Any, Any]] = None,
                       filter_input: Optional[Dict[Any, Any]] = None) -> Dict:

        return QueryUtils.get_multiple_objects(info=info, model=Doctor, filter_input=filter_input,
                                               pagination_input=pagination_input)

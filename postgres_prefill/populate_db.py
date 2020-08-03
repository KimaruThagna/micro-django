import pandas as pd

from doctors.models import Doctor

def prefill_doctors(filename):
    data = pd.read_csv(filename)
    # convert data to a list of dictionaries for easy data entry
    doctors_records = data.T.to_dict().values()
    try:
        for record in doctors_records:
            Doctor.objects.create(**record)
            print(f'added doctors record for {record["last_name"]} in the {record["specialization"]} department')
    except Exception as e:
        print(f"DB prefill process failed due to {e}")

prefill_doctors('doctor_list.csv')
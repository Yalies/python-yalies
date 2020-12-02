import yalies
import os

# Initialize API with token from YALIES_TOKEN environment variable or console
api = yalies.API(os.environ.get('YALIES_TOKEN') or input('Insert Yalies API token: '))

# Perform a test request to the API
eriks = api.students('erik')
for erik in eriks:
    print(f'{erik.name} - {erik.college} {erik.year}')

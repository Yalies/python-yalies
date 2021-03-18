import yalies
import os


def log(people):
    """
    Utility function for logging lists of people in this script.
    """
    for person in people:
        print(f'{person.last_name}, {person.first_name} - {person.college} {person.year}')


# Initialize API with token from YALIES_TOKEN environment variable or console
api = yalies.API(os.environ.get('YALIES_TOKEN') or input('Insert Yalies API token: '))

# Perform a test request to the API
johns = api.people(query='john')
log(johns)

erik = api.person(filters={'netid': 'ekb33'})
print(erik.first_name)

import time

# Perform a more sophisticated request with filters and page
hopper_2024 = api.people(filters={
                               'college': ['Grace Hopper'],
                               'year': [2024]
                           },
                           page=1)
log(hopper_2024)


# Get all people at once
all_people = api.people(filters={'school_code': 'YC'})
print(f'Found {len(all_people)} people affiliated with Yale.')


# Get people by page with a custom page size
third_five_people = api.people(page=3, page_size=5)
log(third_five_people)

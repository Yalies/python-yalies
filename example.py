import yalies
import os


def log(students):
    """
    Utility function for logging lists of students in this script.
    """
    for student in students:
        print(f'{student.last_name}, {student.first_name} - {student.college} {student.year}')


# Initialize API with token from YALIES_TOKEN environment variable or console
api = yalies.API(os.environ.get('YALIES_TOKEN') or input('Insert Yalies API token: '))

# Perform a test request to the API
johns = api.students(query='john')
log(johns)


import time

# Perform a more sophisticated request with filters and page
hopper_2024 = api.students(filters={
                               'college': ['Grace Hopper'],
                               'year': [2024]
                           },
                           page=1)
log(hopper_2024)


# Get all students at once
all_students = api.students()
print(f'There are {len(all_students)} undergraduate students at Yale.')


# Get students by page with a custom page size
third_five_students = api.students(page=3, page_size=5)
log(third_five_students)

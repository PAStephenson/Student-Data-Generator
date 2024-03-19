import csv
import random

from faker import Faker

def generate_sex():
    sex = ['male', 'female']
    return random.choice(sex)

def generate_attendance():
    total_school_days = 360
    authorised = random.randint(0, total_school_days)
    unauthorised = random.randint(authorised, total_school_days)
    days_in_school = total_school_days - (authorised + unauthorised) 

    attendance = (days_in_school / total_school_days) * 100

    return [authorised, unauthorised, attendance]

def generate_nationality():
    nationality = ['White British', 'Non White British']
    return random.choice(nationality)

def generate_ATL():
    return random.randint(-100, 100)

def generate_PP():
    pp = ['yes', 'no']
    return random.choice(pp)

def generate_in_care():
    in_care = ['yes', 'no']
    return random.choice(in_care)


if __name__ == '__main__':

    fake = Faker('en_UK')

    class_list = ['7A1', '7A2', '7A3', '7A4', '7A5',
                  '7B1', '7B2', '7B3', '7B4', '7B5',
                  '8A1', '8A2', '8A3', '8A4', '8A5',
                  '8B1', '8B2', '8B3', '8B4', '8B5',
                  '9A1', '9A2', '9A3', '9A4', '9A5',
                  '9B1', '9B2', '9B3', '9B4', '9B5',
                  '10A1', '10A2', '10A3', '10A4', '10A5',
                  '10B1', '10B2', '10B3', '10B4', '10B5',
                  '11A1', '11A2', '11A3', '11A4', '11A5',
                  '11B1', '11B2', '11B3', '11B4', '11B5',
                  ]

    header = ['Class',
              'First Name',
              'Last Name',
              'Full Name',
              'Birthday',
              'Address',
              'Phone Number',
              'Sex',
              'PP',
              'Attendance',
              'Authorised',
              'Unauthorised',
              'In Care',
              ]

    with open('data.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for cls in class_list:
            for i in range(32):

                first = fake.first_name()
                last = fake.last_name()
                full_name = f'{first} {last}'

                student = [cls,
                           first,
                           last,
                           full_name,
                           fake.birthdate(),
                           fake.address(),
                           fake.phone_number(),
                           generate_sex(),
                           generate_PP(),
                           generate_attendance()[2],
                           generate_attendance()[0],
                           generate_attendance()[1],
                           generate_in_care()
                           ]
                writer.writerow(student)

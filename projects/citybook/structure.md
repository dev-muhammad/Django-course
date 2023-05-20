# CityBook project

## apps:

- common
- users
- categories
- locations
- establishments

## Models:

Users:
    - User (abstactUser)
        - id (uuid)
        - username (string)
        - email (email)
        - first_name
        - last_name

Common:
    - BaseModel:
        - id (uuid)
        - create time (datetime)
        - update time (datetime)
        - is active (bool defaul=True)

Categories:
    - Category:
        - title (varchar 70)
        - parent category (fk category)
        - description (varchar 512)
Locations:
    - Country:
        - title (varchar 70)
        - description (varchar 512)
    - City:
        - title (varchar 70)
        - description (varchar 512)
        - country (fk country)
    - Gps location:
        - place (fk place)
        - lat (positive float)
        - lon (positive float)

Estableshments:
    - Place:
        - title (varchar 70)
        - description (varchar 1024)
        - category (fk category)
        - address (varchar 70)
        - city (fk city)
        - contacts (o2o contact)
        - photos (related field)
        - work hours (m2m working hours)
        - gps location (related Gps location)
    - Contact:
        - primary phone (varchar 12)
        - secondary phone (varchar 12)
        - email (email field 120)
        - website (url field 120)
    - Work hours:
        - place (fk place)
        - weekday (enum weekdays)
        - start time (datime)
        - end time (datime)
    - Photo:
        - place (fk place)
        - image (image field)
        - order (int)
    - Enum Weekdays:
        - 0: Monday
        - 1: Tuesday
        - 2: Wednesday
        - 3: Thursday
        - 4: Friday
        - 5: Saturday
        - 6: Sunday

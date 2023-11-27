from django.core.exceptions import ValidationError
import re


def validate_name(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex =  r'^[A-Z][a-z]*\s[A-Z]\.\s[A-Z][a-z]*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name': name})
    
def validate_student_email(student_email):
    error_message ='Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^[\w\.-]+@school\.com$'


    good_email = re.match(regex, student_email)

    if good_email:
        return student_email
    else:
        raise ValidationError(error_message, params={'student email': student_email})
    
def validate_locker_combination(locker_combination):
    error_message = 'Combination must be in the format "12-12-12"'

    regex = r'^\d{2}-\d{2}-\d{2}$'

    good_locker_combination = re.match(regex, locker_combination)

    if good_locker_combination:
        return locker_combination
    else:
        raise ValidationError(error_message, params={'locker combination':locker_combination})

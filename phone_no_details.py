import phonenumbers
from phonenumbers import timezone, geocoder, carrier

if __name__ == '__main__':
    number = input("Enter Your No with +__: ")
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone,"en")
    reg = geocoder.description_for_valid_number(phone,"en")
    print("{0}\n{1}\n{2}\n{3}".format(phone,time,car,reg))
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# Country code + Phone number
number = "+84 0971234567"
# Ex output: Vietnam Viettel

vi_number = phonenumbers.parse(number, "VI")
print(geocoder.description_for_number(vi_number, "en"))

service_number = phonenumbers.parse(number, "VI")
print(carrier.name_for_number(service_number, "en"))
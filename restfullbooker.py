# restfullbooker.py
import requests
from booking_generator import GenerateBooking

def _url(path):
    return 'https://restful-booker.herokuapp.com' + path

def get_bookings(firstname="", lastname="", checkin="", checkout=""):
    payload = {}
    if firstname:
        payload['firstname'] = firstname
    if lastname:
        payload['lastname'] = lastname
    if checkin:
        payload['checkin'] = checkin
    if checkout:
        payload['checkout'] = checkout

    if payload:
        return requests.get(_url('/booking/'), params=payload)
    else:
        return requests.get(_url('/booking/'))

def describe_booking(booking_id):
    return requests.get(_url('/booking/{:d}/'.format(booking_id)))

def add_random_booking():
    return add_booking(GenerateBooking())

def add_booking(booking):
    return requests.post(_url('/booking/'), json=booking)

def remove_booking(booking_id, auth_token):
    return requests.delete(_url('/booking/{:d}/'.format(booking_id)), cookies={
        "token" : auth_token
    })

def update_booking(booking_id, auth_token, firstname = 'Jim', lastname = 'Brown', totalprice = 111, depositpaid = True, checkin = '2018-01-01', checkout = '2019-01-01', additionalneeds = 'Breakfast'):
    return requests.put(_url('/booking/{:d}/'.format(booking_id)), json={
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : depositpaid,
        "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkin
        },
        "additionalneeds" : additionalneeds
    }, cookies={
        "token" : auth_token
    })

def get_authtoken(username = 'admin', password = 'password123'):
    url = _url('/auth')
    return requests.post(url, json={
        "username" : username,
        "password" : password
    }).json()['token']

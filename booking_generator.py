from random import choice


def GenerateBooking():
    firstname = choice(['Avinash', 'Amol', 'Ranjeet', 'Monty', 'Jhon', 'Rojy'])
    lastname = choice(['Chougule', 'Patil', 'Mehta', 'Shah'])
    totalprice = choice([455, 7866, 7766, 3452, 3345, 1254, 3255, 6795])
    depositpaid = choice([True, False])
    checkin = choice(['2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-10'])
    checkout = choice(['2023-02-5', '2023-03-05', '2023-04-05', '2023-05-05', '2023-06-20'])
    additionalneeds = choice(['Breakfast', 'Coller', 'Towels', 'Lunch'])

    return (
        {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
    )
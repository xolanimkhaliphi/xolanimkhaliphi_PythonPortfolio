# Hotel cost function

def hotel_cost(number_of_nights):
    return 450 * number_of_nights


# Plane cost Function - based on a city selection

def plane_cost(city):
    if city == 'Johannesburg':

        return 920

    elif city == 'Cape Town':

        return 1200

    elif city == 'East London':

        return 890

    elif city == 'Port Elizabeth':

        return 1000

    else:

        return 0


# Car Rental function - Based on the number of days selection

def car_rental(days):
    return 250 * days


#  The holiday cost function

def holiday_cost(number_of_nights, city, days):
    return hotel_cost(number_of_nights) + plane_cost(city) + car_rental(days)


# For the cost the user will state how many nights they're staying, the city and how long they need the car for
# Example: The user is staying for 2 nights in Cape Town and will need the car for 2 days

cost = holiday_cost(number_of_nights=2, city='Cape Town', days=2)
print(f"Total Holiday Cost is : {cost}")

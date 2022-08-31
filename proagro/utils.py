from math import pi, sin, cos, sqrt, atan2


def degrees_to_radians(degrees):
    return degrees * 3.14159 / 180


def distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = degrees_to_radians(lat2 - lat1)
    dLon = degrees_to_radians(lon2 - lon1)
    a = (sin(dLat / 2) * sin(dLat / 2) +
         cos(degrees_to_radians(lat1)) * cos(degrees_to_radians(lat2)) *
         sin(dLon / 2) * sin(dLon / 2))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c  # Distance in km
    print("------------------------" + str(d) + "----------------------")
    return d

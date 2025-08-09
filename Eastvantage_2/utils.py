# Distance calculation

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on Earth 
    using the Haversine formula.

    Args:
        lat1 (float): Latitude of point 1 in decimal degrees
        lon1 (float): Longitude of point 1 in decimal degrees
        lat2 (float): Latitude of point 2 in decimal degrees
        lon2 (float): Longitude of point 2 in decimal degrees

    Returns:
        float: Distance between the two points in kilometers
    """

    R = 6371  # Earth's radius in kilometers

    # Convert latitude/longitude differences from degrees to radians
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    # Apply Haversine formula components
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )

    # Angular distance in radians
    c = 2 * asin(sqrt(a))

    # Convert angular distance to kilometers
    return R * c


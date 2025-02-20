from math import radians, sin, cos, sqrt, asin

def simple_distance(loc1, loc2):
    lat1, lon1 = loc1
    lat2, lon2 = loc2
    return sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

my_location = (43.205579, 27.914808)  # Bulgaria
friend1_location = (42.733883, 25.485830)  # Bulgaria
friend2_location = (38.963745, 35.243320)  # Turkey
friend3_location = (27.664827, -81.515755)  # Florida

distance1 = simple_distance(my_location, friend1_location)
distance2 = simple_distance(my_location, friend2_location)
distance3 = simple_distance(my_location, friend3_location)

print(" Our Global Locations:")
print(f"Me (Bulgaria, Varna): {my_location}")
print(f"Friend 1 (Bulgaria): {friend1_location}")
print(f"Friend 2 (Turkey): {friend2_location}")
print(f"Friend 3 (Florida): {friend3_location}")

print("\n Distances from me:")
print(f"Friend 1: {distance1:.2f}km")
print(f"Friend 2: {distance2:.2f}km")
print(f"Friend 3: {distance3:.2f}km")

distances = {
    "Friend 1": distance1,
    "Friend 2": distance2,
    "Friend 3": distance3
}
furthest_friend = max(distances, key=distances.get)
print(f"\n {furthest_friend} is the furthest away!")

all_locations = (my_location, friend1_location, friend2_location, friend3_location)
print("\n All locations in one tuple:")
print(all_locations)
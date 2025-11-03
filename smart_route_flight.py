from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math
from object_detector import detect_object_position

# Connect to the drone
print("Connecting to vehicle...")
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)

    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off...")
    vehicle.simple_takeoff(target_altitude)

    while True:
        print(f"Altitude: {vehicle.location.global_relative_frame.alt:.2f}")
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Target altitude reached.")
            break
        time.sleep(1)

# Utility to move forward in current heading
def move_forward(lat, lon, heading_deg, distance_meters):
    earth_radius = 6378137.0  # in meters
    heading_rad = math.radians(heading_deg)

    d_lat = distance_meters * math.cos(heading_rad) / earth_radius
    d_lon = distance_meters * math.sin(heading_rad) / (earth_radius * math.cos(math.radians(lat)))

    new_lat = lat + math.degrees(d_lat)
    new_lon = lon + math.degrees(d_lon)

    return new_lat, new_lon

# Start flight
arm_and_takeoff(10)
print("Starting fist-based navigation...")

duration = 60  # Total flight time
start_time = time.time()

current_heading = 0  # 0° = North
step_distance = 3    # meters
yaw_change = 45      # degrees on each turn

while time.time() - start_time < duration:
    lat = vehicle.location.global_frame.lat
    lon = vehicle.location.global_frame.lon

    direction = detect_object_position()
    print(f"Detected: {direction}")

    if direction in ["center", "right"]:
        print("Fist in center or right → TURNING LEFT")
        current_heading -= yaw_change
    elif direction == "left":
        print("Fist in left → TURNING RIGHT")
        current_heading += yaw_change
    else:
        print("No fist detected → Continue forward")

    current_heading = current_heading % 360  # Keep in [0, 360)
    new_lat, new_lon = move_forward(lat, lon, current_heading, step_distance)

    vehicle.simple_goto(LocationGlobalRelative(new_lat, new_lon, 10), groundspeed=7)
    time.sleep(5)

# Landing
print("Landing now...")
vehicle.mode = VehicleMode("LAND")
vehicle.close()

'''
    @author: Simon Li // siutsin
    @Link: https://github.com/siutsin/DeepRacer
    @License: MIT
'''


def reward_function(params):
    # Read input parameters
    # all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    # Only need the absolute steering angle
    steering = abs(params['steering_angle'])

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        return float(1e-3)  # likely crashed/ close to off track

    if params['is_reversed'] == True:
        return float(1e-3)  # likely crashed/ close to off track

    # first corner - left turn
    if params['closest_waypoints'][0] == 8 and params['closest_waypoints'][1] == 9 and params[
        'is_left_of_center'] == False:
        reward = 5
    if params['closest_waypoints'][0] == 17 and params['closest_waypoints'][1] == 18 and params[
        'is_left_of_center'] == True:
        reward = 5
    if params['closest_waypoints'][0] == 26 and params['closest_waypoints'][
        1] == 27 and distance_from_center == marker_2:
        reward = 5
    # second corner - right turn
    if params['closest_waypoints'][0] == 33 and params['closest_waypoints'][1] == 34 and params[
        'is_left_of_center'] == False:
        reward = 5
    # third corner - left turn
    if params['closest_waypoints'][0] == 36 and params['closest_waypoints'][1] == 37 and params[
        'is_left_of_center'] == False:
        reward = 5
    if params['closest_waypoints'][0] == 40 and params['closest_waypoints'][1] == 41 and params[
        'is_left_of_center'] == True:
        reward = 5
    if params['closest_waypoints'][0] == 49 and params['closest_waypoints'][
        1] == 50 and distance_from_center == marker_2:
        reward = 5
    # third corner - left turn
    if params['closest_waypoints'][0] == 36 and params['closest_waypoints'][1] == 37 and params[
        'is_left_of_center'] == False:
        reward = 5
    if params['closest_waypoints'][0] == 40 and params['closest_waypoints'][1] == 41 and params[
        'is_left_of_center'] == True:
        reward = 5
    if params['closest_waypoints'][0] == 49 and params['closest_waypoints'][
        1] == 50 and distance_from_center == marker_2:
        reward = 5
    # fourth corner - left turn
    if params['closest_waypoints'][0] == 51 and params['closest_waypoints'][1] == 52 and params[
        'is_left_of_center'] == True:
        reward = 5
    if params['closest_waypoints'][0] == 54 and params['closest_waypoints'][
        1] == 55 and distance_from_center == marker_2:
        reward = 5
    # fifth corner - left turn
    if params['closest_waypoints'][0] == 59 and params['closest_waypoints'][1] == 60 and params[
        'is_left_of_center'] == False:
        reward = 5
    if params['closest_waypoints'][0] == 64 and params['closest_waypoints'][1] == 65 and params[
        'is_left_of_center'] == True:
        reward = 5
    if params['closest_waypoints'][0] == 68 and params['closest_waypoints'][
        1] == 69 and distance_from_center == marker_2:
        reward = 5

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 30

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:  # Only need the absolute steering angle
        reward *= 0.5

    # penalize reward for the car taking slow actions
    # speed is in m/s
    # the below assumes your action space has a maximum speed of 5 m/s and speed granularity of 3
    # we penalize any speed less than 2m/s
    SPEED_THRESHOLD = 4
    if params['speed'] < SPEED_THRESHOLD:
        reward *= 0.5

    return float(reward)

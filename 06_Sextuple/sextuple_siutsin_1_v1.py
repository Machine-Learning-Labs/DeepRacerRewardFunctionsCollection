'''
    @author: Simon Li // siutsin
    @Link: https://github.com/siutsin/DeepRacer
    @License: MIT
'''

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
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

    if params['is_reversed'] == True or all_wheels_on_track == False:
        return float(1e-3)  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 30

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:  # Only need the absolute steering angle
        reward *= 0.5

    # penalize reward for the car taking slow actions
    # speed is in m/s
    # the below assumes your action space has a maximum speed of 5 m/s and speed granularity of 3
    # we penalize any speed less than 2m/s
    SPEED_THRESHOLD = 4.5
    if params['speed'] < SPEED_THRESHOLD:
        reward *= 0.5

    return float(reward)

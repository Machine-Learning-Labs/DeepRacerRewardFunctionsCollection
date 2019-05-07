'''
    @author: Manuel Eusebio de Paz Carmona // Pelirrojo
    @Link: https://github.com/Pelirrojo/DeepRacerRewardFunctionsCollection
    @License: MIT

    Inspired on sextuple_tiboonn_v1.py
'''

def reward_function(params):

    # Read input parameters ##############################
    speed = params['speed']
    progress = params['progress']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering = abs(params['steering_angle'])
    is_left_of_center = params['is_left_of_center']

    # Constants #########################################

    ABS_STEERING_THRESHOLD = 15

    # Min / Max Reward
    REWARD_MIN = -100000.0
    REWARD_MAX = 100000.0

    # Calculate markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.15 * track_width
    marker_3 = 0.25 * track_width
    marker_4 = 0.5 * track_width

    # Set Base Reward
    reward = 1

    if not all_wheels_on_track:    # Fail them if off Track
        return float(REWARD_MIN)
    elif progress >= 99:
        return float(REWARD_MAX)
    elif progress >= 75:   # we want the vehicle to continue making progress
        reward = (REWARD_MAX/2) * (progress/100)
    elif progress >= 50:   # we want the vehicle to continue making progress
        reward = (REWARD_MAX/4) * (progress/100)
    elif progress >= 25:  # we want the vehicle to continue making progress
        reward = (REWARD_MAX/8) * (progress / 100)
    elif progress >= 1:  # we want the vehicle to continue making progress
        reward = (REWARD_MAX/10) * (progress / 100)

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 1.0 * speed
        if is_left_of_center:
            reward *= reward * 0.1
    elif distance_from_center <= marker_2:
        reward *= 0.8 * speed
        if is_left_of_center:
            reward *= reward + 0.1
    elif distance_from_center <= marker_3:
        reward *= 0.3 * speed
        if is_left_of_center:
            reward *= reward + 0.1
    elif distance_from_center <= marker_4:
        reward *= 0.1 * speed
        if is_left_of_center:
            reward = reward + 0.1
    else:
        return float(REWARD_MIN)  # likely crashed/ close to off track

    # penalize reward if the car is steering way too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # make sure reward value returned is within the prescribed value range.
    reward = max(reward, REWARD_MIN)
    reward = min(reward, REWARD_MAX)

    return float(reward)

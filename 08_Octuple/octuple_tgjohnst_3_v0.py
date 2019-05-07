'''
    @author: Timothy Johnstone // tgjohnst
    @Link: https://github.com/tgjohnst/DeepestRacer
    @License: N/D
'''

def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering,
                    track_width, waypoints, closest_waypoint):
    '''
    '''

    import math
    from statistics import mean

    ######################
    ##### Constants ######
    ######################

    GLOBAL_MIN = -1e5
    GLOBAL_MAX = 1e5

    ######################
    ##### Helper fns #####
    ######################

    ######################
    ##### Centering ######
    ######################

    # negative exponential penalty for distance from center
    reward = math.exp(-6 * distance_from_center)

    # giant penalty if vehicle is exiting track
    if not on_track:
        reward = GLOBAL_MIN
    elif progress == 1:
        reward = GLOBAL_MAX
    else:  # we want the vehicle to continue making progress
        reward = reward * progress

    ######################
    ###### Steering ######
    ######################

    # penalize reward if orientation of the vehicle deviates way too much when compared to ideal orientation
    next_waypoint_yaw = waypoints[min(closest_waypoint + 1, len(waypoints) - 1)][-1]
    if abs(car_orientation - next_waypoint_yaw) >= math.radians(10):
        reward *= 0.25

    # penalize reward if the car is steering too much
    ABS_STEERING_THRESHOLD = 0.85
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.75

    ######################
    ###### Throttle ######
    ######################

    # Gotta go fast
    # if throttle < 0.35:
    reward *= 0.5 + throttle

    # decrease throttle while steering to some extent
    if throttle > 1 - (0.4 * abs(steering)):
        reward *= 0.8

    # make sure reward value returned is within the prescribed value range.
    reward = max(reward, GLOBAL_MIN)
    reward = min(reward, GLOBAL_MAX)

    return float(reward)

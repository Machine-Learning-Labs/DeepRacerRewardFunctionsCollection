'''
    @author: Timothy Johnstone // tgjohnst
    @Link: https://github.com/tgjohnst/DeepestRacer
    @License: N/D
'''

# This model was my first and was able to complete a lap, but not consistently. it implements a few kinds of penalties

def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering,
                    track_width, waypoints, closest_waypoint):
    '''
    '''

    import math

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    ######################
    ##### Centering ######
    ######################

    # negative exponential penalty for distance from center
    reward = math.exp(-1 * distance_from_center)

    # giant penalty if vehicle is exiting track
    if not on_track:
        reward = -1
    elif progress == 1:
        reward = 1e3
    else:  # we want the vehicle to continue making progress
        reward = reward * progress

    ######################
    ###### Steering ######
    ######################

    # penalize reward if orientation of the vehicle deviates way too much when compared to ideal orientation
    waypoint_yaw = waypoints[closest_waypoint][-1]
    if abs(car_orientation - waypoint_yaw) >= math.radians(5):
        reward *= 0.5

    # penalize reward if the car is steering too much
    ABS_STEERING_THRESHOLD = 0.7
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.75

    ######################
    ###### Throttle ######
    ######################

    # Gotta go fast
    if throttle < 0.35:
        reward *= 1 - (0.5 * throttle)

    # decrease throttle while steering to some extent
    if throttle > 1 - (0.4 * abs(steering)):
        reward *= 0.8

    # make sure reward value returned is within the prescribed value range.
    reward = max(reward, 1e-5)
    reward = min(reward, 1e5)

    return float(reward)

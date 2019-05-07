'''
    @author: MichelangeloPagliarini
    @Link: https://github.com/MichelangeloPagliarini/DeepRacer
    @License: N/D
'''

def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering,
                    track_width, waypoints, closest_waypoint):
    import math

    marker_1 = 0.25 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width

    reward = 1e-3
    if distance_from_center >= 0.0 and distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.2
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    # add steering penalty
    if abs(steering) > 0.3:
        reward *= 0.8
    elif abs(steering) > 0.5:
        reward *= 0.6

    # add throttle penalty
    if throttle < 0.5:
        reward *= 0.7

    return float(reward)

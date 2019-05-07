'''
    @author: cnunezre
    @Link: https://github.com/cnunezre/deepRacerReinvent
    @License: N/D
'''

def reward_function (on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    reward = 1e-3

    if distance_from_center >= 0.0 and distance_from_center <= track_width/3:
        reward = 1.0

    # add steering penalty
    if abs(steering) > 0.5:
        reward *= 0.80

    # add throttle penalty
    if throttle < 0.5:
        reward *= 0.80

    return reward

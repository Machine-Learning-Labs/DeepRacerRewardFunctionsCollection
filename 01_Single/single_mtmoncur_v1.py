'''
    @author: mtmoncur
    @Link: https://github.com/mtmoncur/deepracer_env
    @License: MIT
'''


def reward_function(params):
    """
    Available option:
        all_wheels_on_track (bool)
            True if car is on track, False otherwise
        x (float)
            x coordinate in meters
        y (float)
            y coordinate in meters
        distance_from_center (float)
            distance from car center to track center in meters
        is_left_of_center (bool)
            True if car is left of track cener, False otherwise
        heading (float)
            range of [0,360), this is the angle in degrees between
            the car's direction and the x-axis
        progress (float)
            range of [0,100], this is the percentage of the track completed
        steps (int)
            number of steps taken in the environment. This resets every time
            a new episode begins, and currently the maximum episode length is 200
        speed (float)
            current speed of car in meters per second
        steering_angle (float)
            range of about [-30,30], this is the angle at which the wheels are
            turning
        track_width (float)
            the track width in meters
    """
    if params['all_wheels_on_track']:
        return 1.0
    else:
        return 0.0

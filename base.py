'''
    @author: <Name> // <username>
    @Link: https://github.com/<username>/<repo>
    @License: <LICENSE If any>
'''


def reward(params):
    # Read input parameters ##############################

    all_wheels_on_track = params["all_wheels_on_track"]
    x = params["x"]
    y = params["y"]
    distance_from_center = params["distance_from_center"]
    is_left_of_center = params["is_left_of_center"]
    heading = params["heading"]
    progress = params["progress"]
    steps = params["steps"]
    speed = params["speed"]
    streering_angle = params["streering_angle"]
    track_width = params["track_width"]
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]

    # Constants #########################################

    REWARD_MIN = -100000.0
    REWARD_MAX = 100000.0

    reward = 0

    return float(reward)

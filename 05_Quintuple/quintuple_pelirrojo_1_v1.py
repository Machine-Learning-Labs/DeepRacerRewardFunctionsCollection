'''
    @author: Manuel Eusebio de Paz Carmona // Pelirrojo
    @Link: https://github.com/Pelirrojo/DeepRacerRewardFunctionsCollection
    @License: MIT
'''

def reward_function(params):

    # Read input parameters ##############################

    all_wheels_on_track = params["all_wheels_on_track"]
    distance_from_center = abs(params['distance_from_center'])
    track_width = params['track_width']
    progress = params["progress"]
    speed = params["speed"]

    # Constants #########################################

    REWARD_MIN = -1e5
    REWARD_MAX = 1e5

    # Logic #########################################

    # Give a very low reward by default
    reward = 1e-3

    try:

        # Give a high reward if no wheels go off the track and
        # the vehicle is somewhere in between the track borders
        if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
            reward = 1.0

        # we want the vehicle to continue making progress
        if progress >= 99:
            return float(REWARD_MAX)
        elif progress >= 75:
            reward = (REWARD_MAX / 2) * (progress / 100)
        elif progress >= 50:
            reward = (REWARD_MAX / 4) * (progress / 100)
        elif progress >= 25:
            reward = (REWARD_MAX / 8) * (progress / 100)
        elif progress >= 10:
            reward = (REWARD_MAX / 16) * (progress / 100)
        else:
            reward *= (speed / 5)

        # we want the vehicle stay inside the track
        if not all_wheels_on_track:
            return float(REWARD_MIN)

    except:
        reward = 1e-3

    return float(reward)

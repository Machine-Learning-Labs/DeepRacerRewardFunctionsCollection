'''
    @author: AWS Samples
    @Link: https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html
    @License: Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''


def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two track borders
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = abs(params['distance_from_center'])
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the vehicle is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return reward

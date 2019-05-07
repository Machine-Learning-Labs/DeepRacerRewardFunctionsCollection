'''
    @author: AWS Samples
    @Link: https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html
    @License: Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''

def reward_function(params):
    '''
    Example of rewarding the agent to follow the track center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = abs(params['distance_from_center'])

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
        reward = 1e-3  # likely crashed/close to off-track

    return reward

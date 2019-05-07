# AWS Deep Racer Reward Functions Compilation

This repository includes a compilation of reward functions for the AWS Deep Racer service.
They have been collected from many other authors with the interest of conducting a comparative study.

All the files include a initial description with:

```python

'''
    @author: <Name> // <username>
    @Link: https://github.com/<username>/<repo>
    @License: <LICENSE If any>
'''

```

## Taxonomy

The classification system is based solely on the input variables used in the function.

* Void: None of input params 
* Single: One input var i.e. all_wheels_on_track
* Double: Two ...
* Tredecuple: All the input 

## Input Parameters

The ```params``` dictionary object contains the following key-value pairs:

```python
    params = {
        "all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
        "x": float,                        # vehicle's x-coordinate in meters
        "y": float,                        # vehicle's y-coordinate in meters
        "distance_from_center": float,     # distance in meters from the track center 
        "is_left_of_center": Boolean,      # Flag to indicate if the vehicle is on the left side to the track center or not. 
        "heading": float,                  # vehicle's yaw in degrees
        "progress": float,                 # percentage of track completed
        "steps": int,                      # number steps completed
        "speed": float,                    # vehicle's speed in meters per second (m/s)
        "steering_angle": float,           # vehicle's steering angle in degrees
        "track_width": float,              # width of the track
        "waypoints": [[float, float], ... ], # list of [x,y] as milestones along the track center
        "closest_waypoints": [int, int]    # indices of the two nearest waypoints.
    }

```

## FAQ

* __What means v0 & v1?__ v0 It's about the Deep Racer SDK, some examples uses a ```reward_function(param1, param2,...)``` version with params 
in a verbose way, but last version (v1) uses the dictionary defined before: ```reward_function(params)```.
* __Which license are you using?__ Each file includes its licence if available, rest of own work is under MIT license.

## References

* https://aws.amazon.com/deepracer/
* https://docs.aws.amazon.com/deepracer/latest/developerguide/

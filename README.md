# AWS Deep Racer Reward Functions Compilation

This repository includes a compilation of reward functions for the AWS Deep Racer service.
They have been collected from many other authors with the interest of conducting a comparative study.

## Taxonomy

The classification system is based solely on the input variables used in the function.

* Void: None of input params 
* Single: One input var i.e. all_wheels_on_track
* Double
* Triple 
* Quadruple
* Quintuple 
* Sextuple 
* Septuple 
* Octuple 
* Nonuple 
* Decuple 
* Undecuple 
* Duodecuple 
* Tredecuple: All the input 


## Input Parameters

The params dictionary object contains the following key-value pairs:

```json
    {
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
        "waypoints": [[float, float], … ], # list of [x,y] as milestones along the track center
        "closest_waypoints": [int, int]    # indices of the two nearest waypoints.
    }

```

## References

* https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html
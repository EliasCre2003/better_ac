import ac
import acsys

from .vectors import Vector3D
from .tyre import Tyre, TyreIdentifier
from .exceptions import raise_car_state_error
from .better_ac import log

class Car:
    """
    A class representing a car. It is used to access various properties of the car.
    All fields are read-only
    """

    def __init__(self, car_id: int = 0):
        """
        Initialize the Car object with a car ID.
        
        :param car_id: The ID of the car, default is 0 (the player's car).
        """
        self.car_id = car_id
        self.fr = Tyre(TyreIdentifier.FL, car_id)
        self.fl = Tyre(TyreIdentifier.FR, car_id)
        self.rr = Tyre(TyreIdentifier.RL, car_id)
        self.rl = Tyre(TyreIdentifier.RR, car_id)

    @property
    @raise_car_state_error
    def speed_ms(self) -> float:
        """
        The speed of the car in meters per second.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedMS)
    
    @property
    @raise_car_state_error
    def speed_mph(self) -> float:
        """
        Tthe speed of the car in miles per hour.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedMPH)

    @property
    @raise_car_state_error
    def speed_kmh(self) -> float:
        """
        The speed of the car in kilometers per hour.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedKMH)

    @property
    @raise_car_state_error
    def throttle(self) -> float:
        """
        The gas pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Gas)
    
    @property
    @raise_car_state_error
    def brake(self) -> float:
        """
        The brake pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Brake)
    
    @property
    @raise_car_state_error
    def clutch(self) -> float:
        """
        The clutch pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Clutch)
    
    @property
    @raise_car_state_error
    def gear(self) -> int:
        """
        The current gear of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.Gear)
    
    @property
    @raise_car_state_error
    def best_lap(self) -> float:
        """
        The best lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.BestLap)
    
    @property
    @raise_car_state_error
    def cg_height(self) -> float:
        """
        The height of the center of gravity of the car from the ground.
        """
        return ac.getCarState(self.car_id, acsys.CS.CGHeight)
    
    @property
    @raise_car_state_error
    def best_drift_lap(self) -> float:
        """
        The best lap points in drift mode.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftBestLap)
    
    @property
    @raise_car_state_error
    def last_drift_lap(self) -> float:
        """
        The last lap points in drift mode.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftLastLap)
    
    @property
    @raise_car_state_error
    def drift_points(self) -> float:
        """
        The drift points of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftPoints)
    
    @property
    @raise_car_state_error
    def drive_train_speed(self) -> float:
        """
        The speed of the drive train (speed delivered to the wheels).
        """
        return ac.getCarState(self.car_id, acsys.CS.DriveTrainSpeed)
    
    @property
    @raise_car_state_error
    def rpm(self) -> float:
        """
        The current RPM of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.RPM)
    
    @property
    @raise_car_state_error
    def drift_points(self) -> float:
        """
        The drift points of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.InstantDrift)
    
    @property
    @raise_car_state_error
    def is_drift_invalid(self) -> bool:
        """
        Check if the drift is invalid.
        """
        return ac.getCarState(self.car_id, acsys.CS.IsDriftInvalid) == 1
    
    @property
    @raise_car_state_error
    def is_engine_limiter_on(self) -> bool:
        """
        Check if the engine limiter is on.
        """
        return ac.getCarState(self.car_id, acsys.CS.IsEngineLimiterOn) == 1
    
    @property
    @raise_car_state_error
    def lap_count(self) -> int:
        """
        The lap count of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapCount)
    
    @property
    @raise_car_state_error
    def is_lap_invalidated(self) -> bool:
        """
        Check if the lap is invalidated.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapInvalidated) == 1
    
    @property
    @raise_car_state_error
    def lap_time(self) -> float:
        """
        The lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapTime)
    
    @property
    @raise_car_state_error
    def last_ff(self) -> float:
        """
        The last force feedback value.
        """
        return ac.getCarState(self.car_id, acsys.CS.LastFF)
    
    @property
    @raise_car_state_error
    def last_lap_time(self) -> float:
        """
        The last lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.LastLap)
    
    @property
    @raise_car_state_error
    def normalized_spline_position(self) -> float:
        """
        The normalized position of the car on the track.
        """
        return ac.getCarState(self.car_id, acsys.CS.NormalizedSplinePosition)
    
    @property
    @raise_car_state_error
    def performance_meter(self) -> float:
        """
        Projection of how many seconds is the current time far from
        the current best lap
        """
        return ac.getCarState(self.car_id, acsys.CS.PerformanceMeter)
    
    @property
    @raise_car_state_error
    def steer_rotation(self) -> float:
        """
        The radians of steer rotation.
        """
        return ac.getCarState(self.car_id, acsys.CS.Steer)
    
    @property
    @raise_car_state_error
    def turbo_boost(self) -> float:
        """
        The turbo gain on engine torque of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.TurboBoost)
    
    @property
    @raise_car_state_error
    def caster_angle(self) -> float:
        """
        The caster angle of the car in radians.
        """
        return ac.getCarState(self.car_id, acsys.CS.Caster)
    
    @property
    @raise_car_state_error
    def gravity_acceleration(self) -> Vector3D:
        """
        The gravity acceleration on the vehicles center of gravity.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.AccG))
    
    @property
    @raise_car_state_error
    def local_angular_velocity(self) -> Vector3D:
        """
        The angular velocity of the car, using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.LocalAngularVelocity))
    
    @property
    @raise_car_state_error
    def local_velocity(self) -> Vector3D:
        """
        The velocity using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.LocalVelocity))
    
    @property
    @raise_car_state_error
    def speed_total(self) -> Vector3D:
        """
        Get all the speed representation x = kmh, y = mph, z = ms
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.SpeedTotal))
    
    @property
    @raise_car_state_error
    def velocity(self) -> Vector3D:
        """
        The velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.Velocity))
    
    @property
    @raise_car_state_error
    def wheel_angular_speed(self) -> Vector3D:
        """
        The wheel angular velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.WheelAngularSpeed))

    @property
    @raise_car_state_error
    def world_position(self) -> Vector3D:
        """
        Current Car Coordinates on map.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.WorldPosition))

    @property
    @raise_car_state_error
    def driver_name(self) -> str:
        """
        The name of the driver.
        """
        return ac.getDriverName(self.car_id)
    
    @property
    @raise_car_state_error
    def track_name(self) -> str:
        """
        The name of the track.
        """
        return ac.getTrackName(self.car_id)
    
    @property
    @raise_car_state_error
    def track_configuration_name(self) -> str:
        """
        The location of the track.
        """
        return ac.getTrackConfiguration(self.car_id)
    
    @property
    @raise_car_state_error
    def name(self) -> str:
        """
        The name of the car.
        """
        return ac.getCarName(self.car_id)
    
    @property
    @raise_car_state_error
    def last_splits(self) -> list:
        """
        The last splits of the car.
        """
        return ac.getLastSplits(self.car_id)
    
    @property
    @raise_car_state_error
    def is_car_in_pitlane(self) -> bool:
        """
        Check if the car is in the pit lane.
        """
        return ac.isCarInPitline(self.car_id) == 1
    
    @property
    @raise_car_state_error
    def is_car_in_pit(self) -> bool:
        """
        Check if the car is in the pit.
        """
        return ac.isCarInPit(self.car_id) == 1
    
    @property
    @raise_car_state_error
    def is_connected(self) -> bool:
        """
        Check if the car is connected.
        """
        return ac.isConnected(self.car_id) == 1
    
    @property
    @raise_car_state_error
    def ballast(self) -> float:
        """
        The car ballast value.
        """
        return ac.getCarBallast(self.car_id)
    
    @property
    @raise_car_state_error
    def minimum_height(self) -> float:
        """
        The car minimum height.
        """
        return ac.getCarMinHeight(self.car_id)

    @property
    @raise_car_state_error
    def leaderboard_position(self) -> int:
        """
        The car leaderboard position.
        """
        return ac.getCarLeaderboardPosition(self.car_id)
    
    @property
    @raise_car_state_error
    def real_time_leaderboard_position(self) -> int:
        """
        The car real time leaderboard position.
        """
        return ac.getCarRealTimeLeaderboardPosition(self.car_id)
    
    
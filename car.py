import ac
import acsys

from .vectors import Vector3D
from .tyre import Tyre, TyreIdentifier
# from .exceptions import raise_car_state_error

class Car:
    def __init__(self, car_id: int = 0):
        self.car_id = car_id
        self.fr = Tyre(TyreIdentifier.FL, car_id)
        self.fl = Tyre(TyreIdentifier.FR, car_id)
        self.br = Tyre(TyreIdentifier.RL, car_id)
        self.bl = Tyre(TyreIdentifier.RR, car_id)

    #@raise_car_state_error
    def get_ms(self) -> float:
        """
        Get the speed of the car in meters per second.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedMS)
    
    #@raise_car_state_error
    def get_mph(self) -> float:
        """
        Get the speed of the car in miles per hour.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedMPH)

    #@raise_car_state_error
    def get_kmh(self) -> float:
        """
        Get the speed of the car in kilometers per hour.
        """
        return ac.getCarState(self.car_id, acsys.CS.SpeedKMH)
    
    #@raise_car_state_error
    def get_gas(self) -> float:
        """
        Get the gas pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Gas)
    
    #@raise_car_state_error
    def get_brake(self) -> float:
        """
        Get the brake pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Brake)
    
    #@raise_car_state_error
    def get_clutch(self) -> float:
        """
        Get the clutch pedal position.
        """
        return ac.getCarState(self.car_id, acsys.CS.Clutch)
    
    #@raise_car_state_error
    def get_gear(self) -> int:
        """
        Get the current gear of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.Gear)
    
    #@raise_car_state_error
    def get_best_lap(self) -> float:
        """
        Get the best lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.BestLap)
    
    #@raise_car_state_error
    def get_cg_height(self) -> float:
        """
        Get the height of the center of gravity of the car from the ground.
        """
        return ac.getCarState(self.car_id, acsys.CS.CGHeight)
    
    #@raise_car_state_error
    def get_best_drift_lap(self) -> float:
        """
        Get the best lap points in drift mode.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftBestLap)
    
    #@raise_car_state_error
    def get_last_drift_lap(self) -> float:
        """
        Get the last lap points in drift mode.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftLastLap)
    
    #@raise_car_state_error
    def get_drift_points(self) -> float:
        """
        Get the drift points of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.DriftPoints)
    
    #@raise_car_state_error
    def get_drive_train_speed(self) -> float:
        """
        Get the speed of the drive train (speed delivered to the wheels).
        """
        return ac.getCarState(self.car_id, acsys.CS.DriveTrainSpeed)
    
    #@raise_car_state_error
    def get_rpm(self) -> float:
        """
        Get the current RPM of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.RPM)
    
    #@raise_car_state_error
    def get_drift_points(self) -> float:
        """
        Get the drift points of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.InstantDrift)
    
    #@raise_car_state_error
    def is_drift_invalid(self) -> bool:
        """
        Check if the drift is invalid.
        """
        return ac.getCarState(self.car_id, acsys.CS.IsDriftInvalid) == 1
    
    #@raise_car_state_error
    def is_engine_limiter_on(self) -> bool:
        """
        Check if the engine limiter is on.
        """
        return ac.getCarState(self.car_id, acsys.CS.IsEngineLimiterOn) == 1
    
    #@raise_car_state_error
    def get_lap_count(self) -> int:
        """
        Get the lap count of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapCount)
    
    #@raise_car_state_error
    def is_lap_invalidated(self) -> bool:
        """
        Check if the lap is invalidated.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapInvalidated) == 1
    
    #@raise_car_state_error
    def get_lap_time(self) -> float:
        """
        Get the lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.LapTime)
    
    #@raise_car_state_error
    def get_last_ff(self) -> float:
        """
        Get the last force feedback value.
        """
        return ac.getCarState(self.car_id, acsys.CS.LastFF)
    
    #@raise_car_state_error
    def get_last_lap_time(self) -> float:
        """
        Get the last lap time of the car in milliseconds.
        """
        return ac.getCarState(self.car_id, acsys.CS.LastLap)
    
    #@raise_car_state_error
    def get_normalized_spline_position(self) -> float:
        """
        Get the normalized position of the car on the track.
        """
        return ac.getCarState(self.car_id, acsys.CS.NormalizedSplinePosition)
    
    #@raise_car_state_error
    def get_performance_meter(self) -> float:
        """
        Projection of how many seconds is the current time far from
        the current best lap
        """
        return ac.getCarState(self.car_id, acsys.CS.PerformanceMeter)
    
    #@raise_car_state_error
    def get_steer_rotation(self) -> float:
        """
        Get the radians of steer rotation.
        """
        return ac.getCarState(self.car_id, acsys.CS.Steer)
    
    #@raise_car_state_error
    def get_turbo_boost(self) -> float:
        """
        Get the turbo gain on engine torque of the car.
        """
        return ac.getCarState(self.car_id, acsys.CS.TurboBoost)
    
    #@raise_car_state_error
    def get_caster_angle(self) -> float:
        """
        Get the caster angle of the car in radians.
        """
        return ac.getCarState(self.car_id, acsys.CS.Caster)
    
    #@raise_car_state_error
    def get_gravity_acceleration(self) -> Vector3D:
        """
        Get the gravity acceleration on the vehicles center of gravity.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.AccG))
    
    #@raise_car_state_error
    def get_local_angular_velocity(self) -> Vector3D:
        """
        Get the angular velocity of the car, using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.LocalAngularVelocity))
    
    #@raise_car_state_error
    def get_local_velocity(self) -> Vector3D:
        """
        Get the velocity using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.LocalVelocity))
    
    #@raise_car_state_error
    def get_speed_total(self) -> Vector3D:
        """
        Get all the speed representation x = kmh, y = mph, z = ms
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.SpeedTotal))
    
    #@raise_car_state_error
    def get_velocity(self) -> Vector3D:
        """
        Get the velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.Velocity))
    
    #@raise_car_state_error
    def get_wheel_angular_speed(self) -> Vector3D:
        """
        Get the wheel angular velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.WheelAngularSpeed))

    #@raise_car_state_error
    def get_world_position(self) -> Vector3D:
        """
        Current Car Coordinates on map.
        """
        return Vector3D(structure=ac.getCarState(self.car_id, acsys.CS.WorldPosition))

    #@raise_car_state_error
    def get_driver_name(self) -> str:
        """
        Get the name of the driver.
        """
        return ac.getDriverName(self.car_id)
    
    #@raise_car_state_error
    def get_track_name(self) -> str:
        """
        Get the name of the track.
        """
        return ac.getTrackName(self.car_id)
    
    #@raise_car_state_error
    def get_track_configuration_name(self) -> str:
        """
        Get the location of the track.
        """
        return ac.getTrackConfiguration(self.car_id)
    
    #@raise_car_state_error
    def get_name(self) -> str:
        """
        Get the name of the car.
        """
        return ac.getCarName(self.car_id)
    
    #@raise_car_state_error
    def get_last_splits(self) -> list:
        """
        Get the last splits of the car.
        """
        return ac.getLastSplits(self.car_id)
    
    #@raise_car_state_error
    def is_car_in_pitlane(self) -> bool:
        """
        Check if the car is in the pit lane.
        """
        return ac.isCarInPitline(self.car_id) == 1
    
    #@raise_car_state_error
    def is_car_in_pit(self) -> bool:
        """
        Check if the car is in the pit.
        """
        return ac.isCarInPit(self.car_id) == 1
    
    #@raise_car_state_error
    def is_connected(self) -> bool:
        """
        Check if the car is connected.
        """
        return ac.isConnected(self.car_id) == 1
    
    #@raise_car_state_error
    def get_ballast(self) -> float:
        """
        Get the car ballast value.
        """
        return ac.getCarBallast(self.car_id)
    
    #@raise_car_state_error
    def get_minimum_height(self) -> float:
        """
        Get the car minimum height.
        """
        return ac.getCarMinHeight(self.car_id)

    #@raise_car_state_error
    def get_leaderboard_position(self) -> int:
        """
        Get the car leaderboard position.
        """
        return ac.getCarLeaderboardPosition(self.car_id)
    
    #@raise_car_state_error
    def get_real_time_leaderboard_position(self) -> int:
        """
        Get the car real time leaderboard position.
        """
        return ac.getCarRealTimeLeaderboardPosition(self.car_id)
    
    
import ac
import acsys

from .vectors import Vector3D
from .exceptions import ACCarStateError, raise_car_state_error
from .better_ac import log
from .sim_info import info

@raise_car_state_error
def car_state(*args):
    return ac.getCarState(*args)


###############################################
################Car Portion####################
###############################################
class Car:
    """
    A class representing a car. It is used to access various properties of the car.
    It can be any car in the session. All fields are read-only.
    """

    def __init__(self, car_id: int):
        """
        Initialize the Car object with a car ID.
        
        :param car_id: The ID of the car, 0 would refer to the player car.
        """
        self._car_id = car_id
        self.fl = Tyre(acsys.WHEELS.FL, car_id)
        self.fr = Tyre(acsys.WHEELS.FR, car_id)
        self.rl = Tyre(acsys.WHEELS.RL, car_id)
        self.rr = Tyre(acsys.WHEELS.RR, car_id)

    @staticmethod
    def _test(instance):
        for name in dir(__class__):
            try:
                attr = getattr(__class__, name)
                if isinstance(attr, property):
                    value = getattr(instance, name)
                    log("{name}: {value}".format(name=name, value=value))
            except Exception as e:
                log("FAIL {}: {}".format(name, e))

    @staticmethod
    def do_test():
        Car._test(Car(0))

    @property
    @raise_car_state_error
    def speed_ms(self) -> float:
        """
        The speed of the car in meters per second.
        """
        return ac.getCarState(self._car_id, acsys.CS.SpeedMS)
    
    @property
    @raise_car_state_error
    def speed_mph(self) -> float:
        """
        Tthe speed of the car in miles per hour.
        """
        return ac.getCarState(self._car_id, acsys.CS.SpeedMPH)

    @property
    @raise_car_state_error
    def speed_kmh(self) -> float:
        """
        The speed of the car in kilometers per hour.
        """
        return ac.getCarState(self._car_id, acsys.CS.SpeedKMH)

    @property
    @raise_car_state_error
    def throttle(self) -> float:
        """
        The gas pedal position.
        """
        return ac.getCarState(self._car_id, acsys.CS.Gas)
    
    @property
    @raise_car_state_error
    def brake(self) -> float:
        """
        The brake pedal position.
        """
        return ac.getCarState(self._car_id, acsys.CS.Brake)
    
    @property
    @raise_car_state_error
    def clutch(self) -> float:
        """
        The clutch pedal position.
        """
        return ac.getCarState(self._car_id, acsys.CS.Clutch)
    
    @property
    @raise_car_state_error
    def gear(self) -> int:
        """
        The current gear of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.Gear)
    
    @property
    @raise_car_state_error
    def best_lap(self) -> float:
        """
        The best lap time of the car in milliseconds.
        """
        return ac.getCarState(self._car_id, acsys.CS.BestLap)
    
    @property
    @raise_car_state_error
    def cg_height(self) -> float:
        """
        The height of the center of gravity of the car from the ground.
        """
        return ac.getCarState(self._car_id, acsys.CS.CGHeight)
    
    @property
    @raise_car_state_error
    def best_drift_lap(self) -> float:
        """
        The best lap points in drift mode.
        """
        return ac.getCarState(self._car_id, acsys.CS.DriftBestLap)
    
    @property
    @raise_car_state_error
    def last_drift_lap(self) -> float:
        """
        The last lap points in drift mode.
        """
        return ac.getCarState(self._car_id, acsys.CS.DriftLastLap)
    
    @property
    @raise_car_state_error
    def drift_points(self) -> float:
        """
        The drift points of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.DriftPoints)
    
    @property
    @raise_car_state_error
    def drive_train_speed(self) -> float:
        """
        The speed of the drive train (speed delivered to the wheels).
        """
        return ac.getCarState(self._car_id, acsys.CS.DriveTrainSpeed)
    
    @property
    @raise_car_state_error
    def rpm(self) -> float:
        """
        The current RPM of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.RPM)
    
    @property
    @raise_car_state_error
    def drift_points(self) -> float:
        """
        The drift points of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.InstantDrift)
    
    @property
    @raise_car_state_error
    def is_drift_invalid(self) -> bool:
        """
        Check if the drift is invalid.
        """
        return ac.getCarState(self._car_id, acsys.CS.IsDriftInvalid) == 1
    
    @property
    @raise_car_state_error
    def is_engine_limiter_on(self) -> bool:
        """
        Check if the engine limiter is on.
        """
        return ac.getCarState(self._car_id, acsys.CS.IsEngineLimiterOn) == 1
    
    @property
    @raise_car_state_error
    def lap_count(self) -> int:
        """
        The lap count of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.LapCount)
    
    @property
    @raise_car_state_error
    def is_lap_invalidated(self) -> bool:
        """
        Check if the lap is invalidated.
        """
        return ac.getCarState(self._car_id, acsys.CS.LapInvalidated) == 1
    
    @property
    @raise_car_state_error
    def lap_time(self) -> float:
        """
        The lap time of the car in milliseconds.
        """
        return ac.getCarState(self._car_id, acsys.CS.LapTime)
    
    @property
    @raise_car_state_error
    def last_lap_time(self) -> float:
        """
        The last lap time of the car in milliseconds.
        """
        return ac.getCarState(self._car_id, acsys.CS.LastLap)
    
    @property
    @raise_car_state_error
    def normalized_spline_position(self) -> float:
        """
        The normalized position of the car on the track.
        """
        return ac.getCarState(self._car_id, acsys.CS.NormalizedSplinePosition)
    
    @property
    @raise_car_state_error
    def performance_meter(self) -> float:
        """
        Projection of how many seconds is the current time far from
        the current best lap
        """
        return ac.getCarState(self._car_id, acsys.CS.PerformanceMeter)
    
    @property
    @raise_car_state_error
    def steer_rotation(self) -> float:
        """
        The radians of steer rotation.
        """
        return ac.getCarState(self._car_id, acsys.CS.Steer)
    
    @property
    @raise_car_state_error
    def turbo_boost(self) -> float:
        """
        The turbo gain on engine torque of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.TurboBoost)
    
    @property
    @raise_car_state_error
    def caster_angle(self) -> float:
        """
        The caster angle of the car in radians.
        """
        return ac.getCarState(self._car_id, acsys.CS.Caster)
    
    @property
    @raise_car_state_error
    def gravity_acceleration(self) -> Vector3D:
        """
        The gravity acceleration on the vehicles center of gravity.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.AccG))
    
    @property
    @raise_car_state_error
    def local_angular_velocity(self) -> Vector3D:
        """
        The angular velocity of the car, using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.LocalAngularVelocity))
    
    @property
    @raise_car_state_error
    def local_velocity(self) -> Vector3D:
        """
        The velocity using the car as origin.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.LocalVelocity))
    
    @property
    @raise_car_state_error
    def speed_total(self) -> 'tuple[float, float, float]':
        """
        The speed in all three units: km/h, mph, m/s.
        """
        return tuple(ac.getCarState(self._car_id, acsys.CS.SpeedTotal))
    
    @property
    @raise_car_state_error
    def velocity(self) -> Vector3D:
        """
        The velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.Velocity))
    
    @property
    @raise_car_state_error
    def wheel_angular_speed(self) -> Vector3D:
        """
        The wheel angular velocity of the car.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.WheelAngularSpeed))

    @property
    @raise_car_state_error
    def world_position(self) -> Vector3D:
        """
        Current Car Coordinates on map.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.WorldPosition))
    
    @property
    @raise_car_state_error
    def drs_available(self) -> bool:
        """
        Check if the DRS (Drag Reduction System) is available, 
        i.e. if the car is in a DRS zone.
        """
        return ac.getCarState(self._car_id, acsys.CS.DrsAvailable) == 1
    
    @property
    @raise_car_state_error
    def drs_enabled(self) -> bool:
        """
        Check if the DRS (Drag Reduction System) is enabled.
        """
        return ac.getCarState(self._car_id, acsys.CS.DrsEnabled) == 1
    
    @property
    @raise_car_state_error
    def spent_energy(self) -> float:
        """
        The spent energy of the car in Joule.
        """
        return ac.getCarState(self._car_id, acsys.CS.ERSCurrentKJ) * 1000.0
    
    @property
    @raise_car_state_error
    def ers_heat_charging_mode(self) -> int:
        """
        The ERS heat mode of the car.
        0 = Motor, 1 = Battery
        """
        return ac.getCarState(self._car_id, acsys.CS.ERSHeatCharging)
    
    @property
    @raise_car_state_error
    def max_ers_energy(self) -> float:
        """
        The maximum ERS energy of the car in Joule.
        """
        return ac.getCarState(self._car_id, acsys.CS.ERSMaxJ)
    
    @property
    @raise_car_state_error
    def ers_recovery_level(self) -> int:
        """
        The ERS recovery level of the car
        """
        return ac.getCarState(self._car_id, acsys.CS.ERSRecovery)
    
    @property
    @raise_car_state_error
    def engine_brake_setting(self) -> int:
        """
        The current engine brake setting of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.EngineBrake)
    
    @property
    @raise_car_state_error
    def battery_charge(self) -> float:
        """
        The KERS/ERS charge to the battery of the car. 0.0 to 1.0
        """
        return ac.getCarState(self._car_id, acsys.CS.KersCharge)
    
    @property
    @raise_car_state_error
    def engine_input(self) -> float:
        """
        The KERS/ERS input to the engine of the car. 0.0 to 1.0
        """
        return ac.getCarState(self._car_id, acsys.CS.KersInput)
    
    @property
    @raise_car_state_error
    def last_ffb(self) -> float:
        """
        The last force feedback value.
        """
        return ac.getCarState(self._car_id, acsys.CS.LastFF)
    
    @property
    @raise_car_state_error
    def finished_race(self) -> bool:
        """
        Check if the car has finished the race.
        """
        return ac.getCarState(self._car_id, acsys.CS.RaceFinished) == 1
    
    @property
    @raise_car_state_error
    def front_ride_height(self) -> float:
        """
        The front ride height of the car in meters.
        """
        return ac.getCarState(self._car_id, acsys.CS.RideHeight)[0]
    
    @property
    @raise_car_state_error
    def rear_ride_height(self) -> float:
        """
        The rear ride height of the car in meters.
        """
        return ac.getCarState(self._car_id, acsys.CS.RideHeight)[1]
    
    @property
    @raise_car_state_error
    def turbo_boost(self) -> float:
        """
        The turbo boost of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.TurboBoost)
    
    @property
    @raise_car_state_error
    def drag_coefficient(self):
        """
        The drag coefficient of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.Aero, 0)
    
    @property
    @raise_car_state_error
    def front_lift_coefficient(self):
        """
        The front lift coefficient of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.Aero, 1)
    
    @property
    @raise_car_state_error
    def rear_lift_coefficient(self):
        """
        The rear lift coefficient of the car.
        """
        return ac.getCarState(self._car_id, acsys.CS.Aero, 2)
    
    @property
    @raise_car_state_error
    def ers_delivery_mode(self) -> int:
        """
        The index of the ERS delivery mode.
        """
        return ac.getCarState(self._car_id, acsys.CS.ERSDelivery)
    
    @property
    @raise_car_state_error
    def p2p_status(self) -> int:
        """
        The status index of the P2P (Push to Pass) system.
        (I think it is: 0 = unavailable, 1 = cooldown, 2 = active, 3 = ready)
        """
        return ac.getCarState(self._car_id, acsys.CS.P2PStatus)
    
    @property
    @raise_car_state_error
    def p2p_remaining(self) -> bool:
        """
        How many P2P (Push to Pass) activations are remaining.
        """
        return ac.getCarState(self._car_id, acsys.CS.P2PActivations)

    @property
    def driver_name(self) -> str:
        """
        The name of the driver.
        """
        return ac.getDriverName(self._car_id)
    
    @property
    def track_name(self) -> str:
        """
        The name of the track.
        """
        return ac.getTrackName(self._car_id)
    
    @property
    def track_length(self) -> float:
        """
        The length of the track in meters.
        """
        return ac.getTrackLength(self._car_id)
    
    @property
    def track_configuration_name(self) -> str:
        """
        The location of the track.
        """
        return ac.getTrackConfiguration(self._car_id)
    
    @property
    def name(self) -> str:
        """
        The name of the car.
        """
        return ac.getCarName(self._car_id)
    
    @property
    def last_lap_sectors(self) -> 'tuple[float, float, float]':
        """
        The last splits of the car.
        """
        return tuple(ac.getLastSplits(self._car_id))
    
    @property
    def is_car_in_pitlane(self) -> bool:
        """
        Check if the car is in the pit lane.
        """
        return ac.isCarInPitlane(self._car_id) == 1
    
    @property
    def is_car_in_pit(self) -> bool:
        """
        Check if the car is in the pit.
        """
        return ac.isCarInPit(self._car_id) == 1
    
    @property
    def is_connected(self) -> bool:
        """
        Check if the car is connected.
        """
        return ac.isConnected(self._car_id) == 1
    
    @property
    def ballast(self) -> float:
        """
        The car ballast value.
        """
        return ac.getCarBallast(self._car_id)
    
    @property
    def minimum_height(self) -> float:
        """
        The car minimum height.
        """
        return ac.getCarMinHeight(self._car_id)

    @property
    def leaderboard_position(self) -> int:
        """
        The car leaderboard position.
        """
        return ac.getCarLeaderboardPosition(self._car_id)
    
    @property
    def real_time_leaderboard_position(self) -> int:
        """
        The car real time leaderboard position.
        """
        return ac.getCarRealTimeLeaderboardPosition(self._car_id)
    
    @property
    def skin_name(self) -> str:
        """
        The skin name of the car.
        """
        return ac.getCarSkin(self._car_id)
    
    @property
    def driver_nation_code(self) -> str:
        """
        The nation code of the driver.
        """
        return ac.getDriverNationCode(self._car_id)
    
    @property
    def current_lap_sectors(self) -> 'tuple[int, int, int]':
        """
        The current sectors of the car in milliseconds.
        """
        return tuple(ac.getCurrentSplits(self._car_id))
    
    @property
    def is_ai_controlled(self) -> bool:
        """
        Check if the car is controlled by AI.
        """
        return ac.isAIControlled(self._car_id) == 1
    
    @property
    def tyre_compound(self) -> str:
        """
        The tyre compound of the car.
        """
        return ac.getCarTyreCompound(self._car_id)
    
    
class PlayerCar(Car):
    """
    A class representing the player's car. It inherits from the Car class.
    The player car is always the car with ID 0. It provides access to more 
    specific properties using the shared memory interface of Assetto Corsa.
    """

    def __init__(self):
        """
        Initialize the PlayerCar object with car ID 0.
        """
        super().__init__(car_id=0)
        self.fl = PlayerTyre(acsys.WHEELS.FL)
        self.fr = PlayerTyre(acsys.WHEELS.FR)
        self.rl = PlayerTyre(acsys.WHEELS.RL)
        self.rr = PlayerTyre(acsys.WHEELS.RR)

    @staticmethod
    def do_test():
        PlayerCar._test(PlayerCar())


    @property
    def max_power(self) -> float:
        """
        The maximum power of the car in kilowatts.
        """
        return info.static.maxPower / 1000.0
    
    @property
    def max_torque(self) -> float:
        """
        The maximum torque of the car in Newton-meters.
        """
        return info.static.maxTorque
    
    @property
    def max_rpm(self) -> int:
        """
        The maximum RPM of the car.
        """
        return info.static.maxRpm
    
    @property
    def max_fuel(self) -> float:
        """
        The maximum fuel capacity of the car.
        """
        return info.static.maxFuel
    
    @property
    def max_turbo_boost(self) -> float:
        """
        The maximum turbo boost of the car in liters.
        """
        return info.static.maxTurboBoost
    
    @property
    def stability_control(self) -> float:
        """
        The stability aid of the car. 0.0 to 1.0, where 0.0 is off and 1.0 is maximum stability aid.
        """
        return info.static.aidStability
    
    @property
    def auto_clutch(self) -> bool:
        """
        Check if the car has auto clutch enabled.
        """
        return info.static.aidAutoClutch == 1
    
    @property
    def auto_blip(self) -> bool:
        """
        Check if the car has auto blip enabled.
        """
        return info.static.aidAutoBlip == 1
    
    @property
    def auto_shift(self) -> bool:
        """
        Check if the car has auto shift enabled.
        """
        return info.physics.autoShifterOn == 1
    
    @property
    def has_drs(self) -> bool:
        """
        Check if the car has DRS (Drag Reduction System).
        """
        return info.static.hasDRS == 1
    
    @property
    def has_ers(self) -> bool:
        """
        Check if the car has ERS (Energy Recovery System).
        """
        return info.static.hasERS == 1
    
    @property
    def has_kers(self) -> bool:
        """
        Check if the car has KERS (Kinetic Energy Recovery System).
        """
        return info.static.hasKERS == 1
    
    @property
    def max_kers_energy(self) -> float:
        """
        The maximum KERS energy of the car in Joule.
        """
        return info.static.kersMaxJ 
    
    @property
    def num_ers_power_controller_settings(self) -> int:
        """
        The number of ERS power controller settings available for the car.
        """
        return info.static.ersPowerControllerCount
    
    # @property
    # def drs_enabled(self) -> bool:
    #     """
    #     Check if the DRS (Drag Reduction System) is enabled.
    #     """
    #     return info.physics.drs == 1
    
    @property
    def traction_control(self) -> float:
        """
        The traction control slip ratio limit of the car.
        """
        return info.physics.tc

    @property
    def heading(self) -> float:
        """
        Heading of the car on world coordinates
        """
        return info.physics.heading
    
    @property
    def pitch(self) -> float:
        """
        Pitch of the car on world coordinates
        """
        return info.physics.pitch
    
    @property
    def roll(self) -> float:
        """
        Roll of the car on world coordinates
        """
        return info.physics.roll
    
    @property
    def damage(self) -> 'tuple[float]':
        """
        Level of damage of each of the 4 car sections.
        """
        return tuple(info.physics.carDamage[:4])
    
    @property
    def pit_limiter_enabled(self) -> bool:
        """
        Check if the pit limiter is enabled.
        """
        return info.physics.pitLimiterOn == 1
    
    @property
    def abs(self) -> float:
        """
        The slip ratio limit of the ABS (Anti-lock Braking System).
        """
        return info.physics.abs
    
    @property
    def ers_power_controller_setting(self) -> int:
        """
        The ERS power controller setting of the car.
        """
        return info.physics.ersPowerLevel
    
    @property
    def batter_chargin(self) -> bool:
        """
        Check if the battery is charging.
        """
        return info.physics.ersIsCharging == 1

    @property
    def brake_bias(self) -> float:
        """
        The brake bias of the car. 0.0 to 1.0, where 0.0 is rear and 1.0 is front.
        """
        return info.physics.brakeBias
    
    @property
    def race_position(self) -> int:
        """
        Current postion of the car in the race.
        """
        return info.graphics.position
    
    @property
    def sector_index(self) -> int:
        """
        The current sector of the car.
        """
        return info.graphics.currentSectorIndex
    
    @property
    def last_sector(self) -> int:
        """
        The last sector time of the car in milliseconds.
        """
        return info.graphics.lastSectorTime

    @property
    def penalty_time(self) -> float:
        """
        The penalty time of the car in seconds.
        """
        return info.graphics.penaltyTime
    
    @property
    def ideal_line_on(self) -> bool:
        """
        Check if the ideal line is on.
        """
        return info.graphics.idealLineOn == 1

    # @property
    # def ffb(self) -> float:
    #     """
    #     Get the car's force feedback value.
    #     """
    #     return ac.getCarFFB()
    
    # @ffb.setter
    # def ffb(self, value: float) -> None:
    #     """
    #     Set the car's force feedback value.
        
    #     :param value: The force feedback value to set.
    #     """
    #     ac.setCarFFB(value)
    
    @property
    def num_engine_brake_settings(self) -> int:
        """
        The number of engine brake settings available for the car.
        """
        return info.static.engineBrakeSettingsCount


###############################################
################Tyre Portion###################
###############################################

class Tyre:
    def __init__(self, identifier, car_id: int):
        self.identifier = identifier
        self._car_id = car_id

    @property
    @raise_car_state_error
    def camber_radians(self) -> float:
        """
        The camber angle of the tyre in radians.
        """
        return ac.getCarState(self._car_id, acsys.CS.CamberRad)[self.identifier]

    @property
    @raise_car_state_error
    def camber_degrees(self) -> float:
        """
        The camber angle of the tyre in degrees.
        """
        return ac.getCarState(self._car_id, acsys.CS.CamberDeg)[self.identifier]
    
    @property
    def slip_angle(self) -> float:
        """
        The slip angle of the tyre in degrees.
        """
        return ac.getCarState(self._car_id, acsys.CS.SlipAngle)[self.identifier]

    @property
    @raise_car_state_error
    def slip_ratio(self) -> float:
        """
        The slip ratio of the tyre.
        """
        return ac.getCarState(self._car_id, acsys.CS.SlipRatio)[self.identifier]

    @property
    @raise_car_state_error
    def self_aligning_torque(self) -> float:
        """
        The self-aligning torque of the tyre.
        """
        return ac.getCarState(self._car_id, acsys.CS.Mz)[self.identifier]

    @property
    @raise_car_state_error
    def load(self) -> float:
        """
        The load on the tyre in Newtons.
        """
        return ac.getCarState(self._car_id, acsys.CS.Load)[self.identifier]

    @property
    @raise_car_state_error
    def radius(self) -> float:
        """
        The radius of the tyre in meters.
        """
        return ac.getCarState(self._car_id, acsys.CS.TyreRadius)[self.identifier]

    @property
    @raise_car_state_error
    def nd_slip(self) -> float:
        """
        How far the tyre is from optimal slip angle.
        """
        return ac.getCarState(self._car_id, acsys.CS.NdSlip)[self.identifier]

    @property
    @raise_car_state_error
    def tyre_slip(self) -> float:
        """
        The tyre slip.
        """
        return ac.getCarState(self._car_id, acsys.CS.TyreSlip)[self.identifier]

    @property
    @raise_car_state_error
    def dy(self) -> float:
        """
        I honeslty don't know what this is.
        """
        return ac.getCarState(self._car_id, acsys.CS.DY)[self.identifier]

    @property
    @raise_car_state_error
    def core_temperature(self) -> float:
        """
        The core temperature of the tyre in degrees Celsius.
        """
        return ac.getCarState(self._car_id, acsys.CS.CurrentTyresCoreTemp)[self.identifier]

    # @property
    # @raise_car_state_error
    # def thermal_state(self) -> float:
    #     """
    #     The temperature of the tyre.
    #     """
    #     return ac.getCarState(self.car_id, acsys.CS.ThermalState)[self.identifier]

    @property
    @raise_car_state_error
    def dynamic_pressure(self) -> float:
        """
        The dynamic pressure of the tyre in PSI.
        """
        return ac.getCarState(self._car_id, acsys.CS.DynamicPressure)[self.identifier]

    @property
    @raise_car_state_error
    def loaded_radius(self) -> float:
        """
        The loaded radius of the tyre in meters.
        """
        return ac.getCarState(self._car_id, acsys.CS.TyreLoadedRadius)[self.identifier]

    @property
    @raise_car_state_error
    def suspension_travel(self) -> float:
        """
        The suspension travel of the tyre in meters.
        """
        return ac.getCarState(self._car_id, acsys.CS.SuspensionTravel)[self.identifier]

    @property
    @raise_car_state_error
    def dirt_level(self) -> float:
        """
        The dirt level of the tyre.
        """
        return ac.getCarState(self._car_id, acsys.CS.TyreDirtyLevel)[self.identifier]
    
    @property
    @raise_car_state_error
    def tyre_contact_point(self) -> Vector3D:
        """
        The tyre contact point of the tyre.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.TyreContactPoint, self.identifier))
    
    @property
    @raise_car_state_error
    def tyre_contact_normal(self) -> Vector3D:
        """
        The tyre contact normal of the tyre.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.TyreContactNormal, self.identifier))
    
    @property
    @raise_car_state_error
    def tyre_contact_heading(self) -> Vector3D:
        """
        The tyre contact heading of the tyre.
        """
        return Vector3D(structure=ac.getCarState(self._car_id, acsys.CS.TyreHeadingVector, self.identifier))
    
    @property
    @raise_car_state_error
    def toe(self) -> float:
        """
        The toe angle of the tyre in degrees.
        """
        return ac.getCarState(self._car_id, acsys.CS.ToeInDeg, self.identifier)
    
    @property
    @raise_car_state_error
    def last_tyres_temperature(self) -> 'tuple[float, float, float]':
        """
        I think this is supposed to do the same as tyre_temperature in the PlayerTyre class,
        but from testing I can't get any sensible values from it. So use at own risk I guess.
        """
        return tuple(ac.getCarState(self._car_id, acsys.CS.LastTyresTemp, self.identifier))
    
    @property
    @raise_car_state_error
    def slip_angle_contact_patch(self) -> float:
        """
        The slip angle of the tyre at the contact patch.
        """
        return ac.getCarState(self._car_id, acsys.CS.SlipAngleContactPatch)[self.identifier]
    

class PlayerTyre(Tyre):
    """
    Tyre class for the player car. Inherits from Tyre.
    Provides further methods specific to the player car.
    """
    def __init__(self, identifier: int):
        super().__init__(identifier, 0)

    @property
    def tyre_wear(self) -> float:
        """
        The tyre wear of the tyre.
        """
        return info.physics.tyreWear[self.identifier]
    
    @property
    def max_suspension_travel(self) -> float:
        """
        The maximum suspension travel of the tyre.
        """
        return info.static.suspensionMaxTravel[self.identifier]
    
    @property
    def brake_temperature(self) -> float:
        """
        The brake temperature of the tyre in degrees Celsius.
        """
        return info.physics.brakeTemp[self.identifier]
    
    @property
    def tyre_temperature(self) -> 'tuple[float, float, float]':
        """
        The tyre temperature of the tyre in degrees Celsius.
        Returns a tuple with the inner, middle and outer temperatures.
        """
        return (
            info.physics.tyreTempI[self.identifier],
            info.physics.tyreTempM[self.identifier],
            info.physics.tyreTempO[self.identifier]
        )
    

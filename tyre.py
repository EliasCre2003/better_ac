import ac
import acsys


class TyreIdentifier:
    FL = 0
    FR = 1
    RL = 2
    RR = 3



class Tyre:
    def __init__(self, identifier, car_id: int):
        self.identifier = identifier
        self.car_id = car_id

    def get_camber_radians(self) -> float:
        """
        Get the camber angle of the tyre in radians.
        """
        return ac.getCarState(self.car_id, acsys.TS.CamberRad)[self.identifier]
    
    def get_camber_degrees(self) -> float:
        """
        Get the camber angle of the tyre in degrees.
        """
        return ac.getCarState(self.car_id, acsys.TS.CamberDeg)[self.identifier]
    
    # def get_slip_angle(self) -> float:
    #     """
    #     Get the slip angle of the tyre in degrees.
    #     """
    #     return ac.getCarState(self.car_id, acsys.TS.SlipAngle)[self.identifier]
    
    def get_slip_ratio(self) -> float:
        """
        Get the slip ratio of the tyre.
        """
        return ac.getCarState(self.car_id, acsys.TS.SlipRatio)[self.identifier]
    
    def get_self_aligning_torque(self) -> float:
        """
        Get the self-aligning torque of the tyre.
        """
        return ac.getCarState(self.car_id, acsys.TS.SelfAligningTorque)[self.identifier]
    
    def get_load(self) -> float:
        """
        Get the load on the tyre in Newtons.
        """
        return ac.getCarState(self.car_id, acsys.TS.Load)[self.identifier]
    
    def get_radius(self) -> float:
        """
        Get the radius of the tyre in meters.
        """
        return ac.getCarState(self.car_id, acsys.TS.Radius)[self.identifier]
    
    def get_nd_slip(self) -> float:
        """
        How far the tyre is from optimal slip angle.
        """
        return ac.getCarState(self.car_id, acsys.TS.NdSlip)[self.identifier]
    
    def get_tyre_slip(self) -> float:
        """
        Get the tyre slip.
        """
        return ac.getCarState(self.car_id, acsys.TS.TyreSlip)[self.identifier]
    
    def get_dy(self) -> float:
        """
        I honeslty don't know what this is.
        """
        return ac.getCarState(self.car_id, acsys.TS.Dy)[self.identifier]
    
    def get_core_temperature(self) -> float:
        """
        Get the core temperature of the tyre in degrees Celsius.
        """
        return ac.getCarState(self.car_id, acsys.TS.CurrentTyresCoreTemp)[self.identifier]
    
    def get_thermal_state(self) -> float:
        """
        Get the temperature of the tyre.
        """
        return ac.getCarState(self.car_id, acsys.TS.ThermalState)[self.identifier]
    
    def get_dynamic_pressure(self) -> float:
        """
        Get the dynamic pressure of the tyre in PSI.
        """
        return ac.getCarState(self.car_id, acsys.TS.DynamicPressure)[self.identifier]
    
    def get_loaded_radius(self) -> float:
        """
        Get the loaded radius of the tyre in meters.
        """
        return ac.getCarState(self.car_id, acsys.TS.TyreLoadedRadius)[self.identifier]
    
    def get_suspension_travel(self) -> float:
        """
        Get the suspension travel of the tyre in meters.
        """
        return ac.getCarState(self.car_id, acsys.TS.SuspensionTravel)[self.identifier]
    
    def get_dirt_level(self) -> float:
        """
        Get the dirt level of the tyre.
        """
        return ac.getCarState(self.car_id, acsys.TS.TyreDirtyLevel)[self.identifier]
    

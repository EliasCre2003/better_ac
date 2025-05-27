from sim_info import info


class Session:
    """
    An enum-like class that stores all the session types.
    """
    def __init__(self, index: int):
        match index:
            case 0:
                self.name = "unknown"
            case 1:
                self.name = "practice"
            case 2:
                self.name = "qualifying"
            case 3:
                self.name = "race"
            case 4:
                self.name = "hotlap"
            case 5:
                self.name = "time attack"
            case 6:
                self.name = "drift"
            case 7:
                self.name = "drag"
            case _:
                raise ValueError("Invalid session index: {}".format(index))
        self.index = index           


Session.UNKNOWN = Session(0)
Session.PRACTICE = Session(1)
Session.QUALIFYING = Session(2)
Session.RACE = Session(3)
Session.HOTLAP = Session(4)
Session.TIME_ATTACK = Session(5)
Session.DRIFT = Session(6)
Session.DRAG = Session(7)


def current_session() -> Session:
    """
    Get the type of the current session.
    """
    return Session(info.static.session)


class Flag:
    """
    An enum-like class that stores all the flag types.
    """
    def __init__(self, index: int):
        match index:
            case 0:
                self.name = "no flag"
            case 1:
                self.name = "blue flag"
            case 2:
                self.name = "yellow flag"
            case 3:
                self.name = "black flag"
            case 4:
                self.name = "white flag"
            case 5:
                self.name = "checkered flag"
            case 6:
                self.name = "penalty flag"
            case _:
                raise ValueError("Invalid flag index: {}".format(index))
        self.index = index


Flag.NO_FLAG = Flag(0)
Flag.BLUE_FLAG = Flag(1)
Flag.YELLOW_FLAG = Flag(2)
Flag.BLACK_FLAG = Flag(3)
Flag.WHITE_FLAG = Flag(4)
Flag.CHECKERED_FLAG = Flag(5)
Flag.PENALTY_FLAG = Flag(6)


def current_flag() -> Flag:
    """
    Get the type of the flag that is curently being shown on the track.
    """
    try:
        return Flag(info.physics.flag)
    except ValueError:
        return None
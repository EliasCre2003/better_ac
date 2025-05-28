import ac

from .sim_info import info


_logging_enabled = True
_console_enabled = True

def do_logging(enable: bool) -> None:
    """
    Enable or disable logging.
    
    :param enable: If True, logging is enabled. If False, logging is disabled.
    """
    global _logging_enabled
    _logging_enabled = enable

def do_console(enable: bool) -> None:
    """
    Enable or disable console output.
    
    :param enable: If True, console output is enabled. If False, console output is disabled.
    """
    global _console_enabled
    _console_enabled = enable


def log(*args) -> None:
    """
    Print a message to the log file, if it is not turned off.
    """
    global _logging_enabled
    if not _logging_enabled: return
    string = ""
    for message in args:
        if isinstance(message, str):
            string += message + " "
        else:
            string += str(message) + " "
    ac.log(string.strip())

def console(*args) -> None:
    """
    Print a message to the console, if it is not turned off.
    """
    global _console_enabled
    if not _console_enabled: return
    string = ""
    for message in args:
        if isinstance(message, str):
            string += message + " "
        else:
            string += str(message) + " "
    ac.console(string.strip())



def get_server_name() -> str:
    """
    Get the name of the server.
    """
    return ac.getServerName()

def get_server_ip() -> str:
    """
    Get the IP address of the server.
    """
    return ac.getServerIP()

def get_server_port() -> int:
    """
    Get the port of the server.
    """
    return ac.getServerHttpPort()

def get_server_slot_count() -> int:
    """
    Get the number of slots in the server.
    """
    return ac.getServerSlotCount()

def get_max_cars_count() -> int:
    """
    Get the max number of cars in the session.
    """
    return ac.getCarsCount()

def get_ffb_gain() -> float:
    """
    Get the FFB gain of the player car.
    """
    return ac.getFFBGain()

def set_ffb_gain(value: float) -> None:
    """
    Set the FFB gain of the player car.
    """
    ac.setFFBGain(value)


def get_track_name() -> str:
    """
    Get the name of the track.
    """
    return info.static.track
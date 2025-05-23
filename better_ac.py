import ac

def log(message) -> None:
    """
    Print a message to the log file.
    """
    if isinstance(message, str):
        ac.log(message)
    else:
        ac.log(str(message))

def console(message) -> None:
    """
    Print a message to the console.
    """
    if isinstance(message, str):
        ac.console(message)
    else:
        ac.console(str(message))



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



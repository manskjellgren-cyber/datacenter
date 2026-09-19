class DCIMError(Exception):
    """ Vår basklass för alla datacenterfel. """
    pass

class InvalidSensorDataError(DCIMError):
    """ Kastas när en sensor levererar ogiltiga värden. """
    pass

class DeviceNotFoundError(DCIMError):
    """ Kastas när en sökt nätresurs inte hittas i systemet. """
    pass

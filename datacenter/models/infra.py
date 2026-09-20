from datacenter.core.exceptions import InvalidSensorDataError
from datacenter.models.base import Natresurs

class Kylaggregat(Natresurs):
    """Representerar ett kylaggregat i datacentret."""
    
    def __init__(self, enhet_id: str, fabrikat: str, temp: float):
        # Anropa super().__init__(...) med funktion="kyla"
        super().__init__(
            enhet_id = enhet_id, 
            fabrikat = fabrikat, 
            funktion = "kyla")
            
        # Sätt self.temp = temp
        self.temp = temp
    
    
    @property
    def temp(self) -> float:
        # Returnera self._temp
        return self._temp
    
    @temp.setter
    def temp(self, value: float) -> None:
        # Validera intervallet (-50 till 100) och kasta
        if -50.0 <= value <= 100.0:
            self._temp = value
        else:
            raise InvalidSensorDataError(
                f"{value}°C är utanför tillåtet intervall (-50 till 100).")
        # InvalidSensorDataError om ogiltigt
            
    def kor_diagnostik(self) -> str:
        # Returnera diagnostiksträngen
        return f"Kylanalys OK för {self.enhet_id}. Aktuell temp: {self.temp}°C."
       
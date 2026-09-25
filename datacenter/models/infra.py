from datacenter.core.exceptions import InvalidSensorDataError
from datacenter.models.base import Natresurs


class Kylaggregat(Natresurs):
    """Representerar ett kylaggregat i datacentret."""

    def __init__(self, enhet_id: str, fabrikat: str, temp: float, status: str = "OK"):
        # Anropa super().__init__(...) utan ogiltiga parametrar som funktion
        super().__init__(enhet_id=enhet_id, fabrikat=fabrikat, status=status)

        # Sätt temperatur via property-setter (vilket kör valideringen)
        self.temp = temp

    @property
    def temp(self) -> float:
        """Returnerar den inställda måltemperaturen."""
        return self._temp

    @temp.setter
    def temp(self, value: float) -> None:
        """Validerar att temperaturen ligger inom tillåtet intervall (-50 till 100°C)."""
        if -50.0 <= value <= 100.0:
            self._temp = float(value)
        else:
            raise InvalidSensorDataError(
                f"{value}°C är utanför tillåtet intervall (-50 till 100)."
            )

    def kor_diagnostik(self) -> str:
        """Kör diagnostik på kylaggregatet och returnerar statusrapport."""
        return f"Kylanalys OK för {self.enhet_id}. Aktuell temp: {self.temp}°C."
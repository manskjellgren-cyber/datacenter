from datacenter.models.base import Natresurs

class Switch(Natresurs):
    """Representerar en fysisk eller virtuell switch i datacentret."""

    def __init__(self, enhet_id: str, fabrikat: str, antal_portar: int, status: str = "OK"):
        super().__init__(enhet_id=enhet_id, fabrikat=fabrikat, status=status)
        self.antal_portar = antal_portar
    
    @property
    def antal_portar(self) -> int:
        return self._antal_portar
        
    @antal_portar.setter
    def antal_portar(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{value} är inte ett giltigt antal portar (måste vara ett positivt heltal).")
        self._antal_portar = value
                            
    def kor_diagnostik(self) -> str:
        # Returnera diagnostiksträngen
        return f"Switchdiagnostik OK för {self.enhet_id}. Alla {self.antal_portar} svarar."
       
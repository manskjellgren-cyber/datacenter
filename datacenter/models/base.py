from abc import ABC, abstractmethod


class Natresurs(ABC):
    """Abstrakt basklass för alla övervakade enheter i datacentret."""
    
    def __init__(self, enhet_id: str, fabrikat: str, funktion: str, status: str = "OK"):
        self.enhet_id = enhet_id
        self.fabrikat = fabrikat
        self.funktion = funktion
        self.status = status
            
    @abstractmethod
    def kor_diagnostik(self) -> None:
        """Tvingar underklasser att implementera sin egen diagnostik"""
        pass
    
from datacenter.core.logger import setup_logger
from datacenter.core.exceptions import DeviceNotFoundError
from datacenter.models.base import Natresurs

class DatacenterManager:
    """Hanterar och orkestrerar alla nätresurser i datacentret."""
    
    def __init__(self):
        self.logger = setup_logger()
        self.resurser: dict[str, Natresurs] = {}
        self.logger.info("DatacenterManager initierad.")
    
    def registrera_resurs(self, resurs: Natresurs) -> None:
        self.resurser[resurs.enhet_id] = resurs
        self.logger.info(f"Registrerade resurs: {resurs.enhet_id} ({resurs.fabrikat})")
        
    def hamta_resurs(self, enhet_id: str) -> Natresurs:
        if enhet_id in self.resurser:
            return self.resurser[enhet_id]
        else:
            raise DeviceNotFoundError(f"Resursen '{enhet_id}' hittades inte i datacentret.")
        
    def kor_systemdiagnostik(self) -> list[str]:
        rapporter = []
        for resurs in self.resurser.values():
            rapporter.append(resurs.kor_diagnostik())
        return rapporter
       
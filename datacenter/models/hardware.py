from datacenter.models.base import Natresurs

class Server(Natresurs):
    """Representerar en fysisk eller virtuell server i datacentret."""
    def __init__(self, enhet_id: str, fabrikat: str, ip_adress: str, natverk_typ: str = "INTRANAT"):
            
        super().__init__(enhet_id=enhet_id, fabrikat=fabrikat, funktion="Beräkning")
        
        self.ip_adress = ip_adress 
        self.natverk_typ = natverk_typ
        self.cpu_belastning = 0.0
        
    def kor_diagnostik(self) -> str:
        return f"Serverdiagnostik OK för {self.enhet_id} ({self.ip_adress}) på {self.natverk_typ}. CPU: {self.cpu_belastning}%."
        
            
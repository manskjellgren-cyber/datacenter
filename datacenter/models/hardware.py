from datacenter.models.base import Natresurs

class Server(Natresurs):
    """Representerar en fysisk eller virtuell server i datacentret."""
    def __init__(self, enhet_id: str, fabrikat: str, ip_adress: str, natverk_typ: str, status: str = "OK"):
        # Anropa basklassens __init__ med de parametrar den faktiskt förväntar sig:    
        super().__init__(enhet_id=enhet_id, fabrikat=fabrikat, status=status)
        self.ip_adress = ip_adress 
        self.natverk_typ = natverk_typ
                
    def kor_diagnostik(self) -> str:
        return f"Serverdiagnostik {self.status} för {self.enhet_id} ({self.ip_adress}) på {self.natverk_typ}."
        
            
from abc import ABC, abstractmethod


class Natresurs(ABC):
    """Abstrakt basklass för alla nätverks- och infrastrukturresurser i datacentret."""

    def __init__(self, enhet_id: str, fabrikat: str, status: str = "OK") -> None:
        """Initierar gemensamma egenskaper för en datacenterresurs."""
        self.enhet_id = enhet_id
        self.fabrikat = fabrikat
        self.status = status

    @abstractmethod
    def kor_diagnostik(self) -> str:
        """Kör enhetsspecifik diagnostik och returnerar en rapportsträng.
        Måste implementeras av alla underklasser.
        """
        pass

    def __str__(self) -> str:
        """Användarvänlig strängrepresentation av objektet (t.ex. vid print())."""
        return f"{self.__class__.__name__} [{self.enhet_id}] ({self.fabrikat}) - Status: {self.status}"

    def __repr__(self) -> str:
        """Teknisk och entydig strängrepresentation för felsökning och loggning."""
        return f"<{self.__class__.__name__}(enhet_id='{self.enhet_id}', fabrikat='{self.fabrikat}', status='{self.status}')>"
import json
from datacenter.core.logger import setup_logger
from datacenter.core.exceptions import DeviceNotFoundError
from datacenter.models.base import Natresurs
from datacenter.models.hardware import Server
from datacenter.models.connectivity import Switch
from datacenter.models.infra import Kylaggregat


class DatacenterManager:
    """Hanterar och orkestrerar alla nätresurser i datacentret."""

    def __init__(self):
        self.logger = setup_logger()
        self.resurser: dict[str, Natresurs] = {}
        self.logger.info("DatacenterManager initierad.")

    @property
    def enheter(self) -> list[Natresurs]:
        """Returnerar alla registrerade resurser som en lista (används i notebook och tester)."""
        return list(self.resurser.values())

    def registrera_resurs(self, resurs: Natresurs) -> None:
        """Registrerar en ny nätresurs i systemet och loggar händelsen."""
        self.resurser[resurs.enhet_id] = resurs
        self.logger.info(f"Registrerade resurs: {resurs.enhet_id} ({resurs.fabrikat})")

    def lagg_till_enhet(self, enhet: Natresurs) -> None:
        """Alias för registrera_resurs för bakåtkompatibilitet."""
        self.registrera_resurs(enhet)

    def hamta_resurs(self, enhet_id: str) -> Natresurs:
        """Hämtar en specifik resurs baserat på enhet_id."""
        if enhet_id in self.resurser:
            return self.resurser[enhet_id]
        else:
            raise DeviceNotFoundError(f"Resursen '{enhet_id}' hittades inte i datacentret.")

    def kor_systemdiagnostik(self) -> list[str]:
        """Kör diagnostik på alla registrerade resurser och returnerar en samlad rapport."""
        rapporter = []
        for resurs in self.resurser.values():
            rapporter.append(resurs.kor_diagnostik())
        return rapporter

    def ladda_fran_json(self, filvag: str) -> int:
        """Laddar enheter från en JSON-fil och lägger till dem i systemet."""

        # Steg 1: Öppna filen och läs in innehållet
        with open(filvag, "r", encoding="utf-8") as f:
            enhets_lista = json.load(f)

        inlasta_antal = 0

        # Steg 2: Gå igenom varje enhet (dictionary) i listan, en i taget
        for enhet in enhets_lista:
            enhetstyp = enhet["typ"]  # Hämtar "server", "kylaggregat" eller "switch"

            # Steg 3: Skapa rätt sorts objekt baserat på enhetstyp
            if enhetstyp == "server":
                ny_enhet = Server(
                    enhet_id=enhet["enhet_id"],
                    fabrikat=enhet["fabrikat"],
                    ip_adress=enhet["ip_adress"],
                    natverk_typ=enhet["natverk_typ"]
                )
                self.registrera_resurs(ny_enhet)
                inlasta_antal += 1

            elif enhetstyp == "kylaggregat":
                ny_enhet = Kylaggregat(
                    enhet_id=enhet["enhet_id"],
                    fabrikat=enhet["fabrikat"],
                    temp=enhet["temp"]
                )
                self.registrera_resurs(ny_enhet)
                inlasta_antal += 1

            elif enhetstyp == "switch":
                ny_enhet = Switch(
                    enhet_id=enhet["enhet_id"],
                    fabrikat=enhet["fabrikat"],
                    antal_portar=enhet["antal_portar"]
                )
                self.registrera_resurs(ny_enhet)
                inlasta_antal += 1

        # Returnera hur många enheter vi lyckades ladda in
        return inlasta_antal
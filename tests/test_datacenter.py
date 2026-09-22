import unittest

# TODO 1: Importera dina exceptions (DeviceNotFoundError, InvalidSensorDataError)
from datacenter.core.exceptions import (DeviceNotFoundError, InvalidSensorDataError)
# TODO 2: Importera DatacenterManager
from datacenter.manager.datacenter_manager import DatacenterManager
# TODO 3: Importera Kylaggregat och Server
from datacenter.models.infra import Kylaggregat
from datacenter.models.hardware import Server

class TestDCIMSystem(unittest.TestCase):
    """Enhetstester för DCIM-systemets kärnfunktionalitet."""

    def test_kylaggregat_skapande_och_diagnostik(self):
        # TODO: Skapa kylaggregat, asserta temp och diagnostiksträng
        kyl = Kylaggregat("COOL-01", "Rittal", 20.0)
        self.assertEqual(kyl.temp, 20.0)
        self.assertEqual(kyl.kor_diagnostik(), "Kylanalys OK för COOL-01. Aktuell temp: 20.0°C.")
        
                
    def test_kylaggregat_ogiltig_temp_kastar_fel(self):
        # TODO: Skapa kylaggregat och asserta att InvalidSensorDataError kastas vid temp = 150.0
        kyl2 = Kylaggregat("COOL-02", "Rittal", 20.0)
        with self.assertRaises(InvalidSensorDataError):
            kyl2.temp = 150.0
                      

    def test_manager_registrera_och_hamta(self):
        # TODO: Skapa manager och server, registrera och hämta samt asserta ID
        manager1 = DatacenterManager()
        server1 = Server(
            enhet_id="SRV-01",
            fabrikat="Dell",
            ip_adress="192.168.1.10",
            natverk_typ="INTRANÄT",
            )
        manager1.registrera_resurs(server1)
        hamtad_resurs = manager1.hamta_resurs("SRV-01")
        self.assertEqual(hamtad_resurs.enhet_id, "SRV-01")
        pass

    def test_manager_okand_resurs_kastar_fel(self):
        # TODO: Skapa manager och asserta att DeviceNotFoundError kastas vid okänt ID
        manager = DatacenterManager()
        with self.assertRaises(DeviceNotFoundError):
            manager.hamta_resurs("FINNS_INTE")
        
        pass

    def test_manager_kor_systemdiagnostik(self):
        """Verifierar att systemdiagnostik samlar in rapporter från alla enheter."""
        manager = DatacenterManager()
        server = Server("SRV-01", "Dell", "192.168.1.10", "INTRANÄT")
        kyl = Kylaggregat("COOL-01", "Rittal", 20.0)

        manager.registrera_resurs(server)
        manager.registrera_resurs(kyl)

        rapporter = manager.kor_systemdiagnostik()

        self.assertEqual(len(rapporter), 2)
        # Ändrad delsträng för att matcha Server.kor_diagnostik()
        self.assertIn("Serverdiagnostik OK för SRV-01", rapporter[0])
        self.assertIn("Kylanalys OK för COOL-01", rapporter[1])
        


if __name__ == "__main__":
    unittest.main()
import logging

def setup_logger(filename: str = "datacenter.log") -> logging.Logger:
    """Konfigurerar och returnerar en central logger för DCIM-systemet"""
    
    # Konfigurera logging.basicConfig(...)
    
    logging.basicConfig(
        filename=filename, # Filen där allt sparas
        encoding="utf-8", # Hanterar Å, Ä och Ö korrekt
        level=logging.INFO, # Logga INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s [%(levelname)s] %(message)s", # Hur rader ser ut
        datefmt="%Y-%m-%d %H:%M:%S", # datumformat
        force=True # Skriver över eventuella tidigare inställningar   
    )

    # Returnera logger instansen för "DCIM"
    
    return logging.getLogger("DCIM")
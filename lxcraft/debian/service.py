from dataclasses import dataclass


@dataclass
class SystemdService:
    """Directory to be created or removed"""

    service_name: str
    must_be_enabled: bool = True
    must_reread: bool = True
    must_update: bool = True

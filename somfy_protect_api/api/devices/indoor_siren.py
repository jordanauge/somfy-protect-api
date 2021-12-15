"""Security InDoor Siren"""
from typing import cast, Dict

from somfy_protect_api.api.devices.base import SomfyProtectDevice


class IndoorSiren(SomfyProtectDevice):
    """Class to represent an InDoor Siren."""

    def get_rlink_quality(self) -> float:
        """Link Quality in %

        Returns:
            float: Link Quality percentage
        """
        return cast(float, self.get_status("rlink_quality_percent"))

    def get_battery_level(self) -> float:
        """Battery Level

        Returns:
            float: Battery Level percentage
        """
        return cast(float, self.get_status("battery_level"))

    def sound(self, sound_ref: str) -> Dict:
        return self.api.device_sound(self.site.id, self.device.id, sound_ref)

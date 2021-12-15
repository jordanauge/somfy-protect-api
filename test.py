#!/usr/bin/env python3
"""Usage Example"""
import json
import os

from somfy_protect_api.api.devices.category import Category
from somfy_protect_api.api.devices.indoor_camera import IndoorCamera
from somfy_protect_api.api.devices.indoor_siren import IndoorSiren
from somfy_protect_api.api.somfy_protect_api import SomfyProtectApi

try:
    from . import private
except ImportError:
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
CACHE_PATH = "token.json"

def get_token():
    """Retrieve a token from a file
    """
    try:
        with open(CACHE_PATH, "r") as cache:
            return json.loads(cache.read())
    except IOError:
        pass

def set_token(token) -> None:
    """WWrite a toek into a file
    """
    with open(CACHE_PATH, "w") as cache:
        cache.write(json.dumps(token))

if __name__ == "__main__":

    api = SomfyProtectApi(
        username=USERNAME, password=PASSWORD, token=get_token(), token_updater=set_token
    )

    # Check if we already have a token
    if not os.path.isfile(CACHE_PATH):
        set_token(api.request_token())

    # List Sites
    sites = api.get_sites()

    for site in sites:
        if 'Pomponne' in site.label:
            continue
        # Retieve Alarm Status
        print(f"Alarm Status for {site.label} is {site.security_level}")

#        # Set Alarm Status
#        disarmed = api.update_security_level(site_id=site.id, security_level="disarmed")
#        print(f"Task: {disarmed}")

        # Get Data from a Device.
        #import pdb; pdb.set_trace()
        devices = api.get_devices(site_id=site.id, category=Category.INDOOR_CAMERA)
        cameras = [IndoorCamera(site=site, device=d, api=api) for d in devices]
        for camera in cameras:
            print(camera.get_shutter_state())
        devices = api.get_devices(site_id=site.id, category=Category.INDOOR_SIREN)
        indoor_sirens = [IndoorSiren(site=site, device=d, api=api) for d in devices]
        for siren in indoor_sirens:
            print(siren.sound('ok'))
            import time; time.sleep(1)
            print(siren.sound('intrusion'))

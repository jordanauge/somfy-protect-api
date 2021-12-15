"""Somfy Protect Api"""
#
# Source:
# https://api.myfox.io/api/methods
#
# V3
#calendarScenario
#GET /site/{site_id}/scenario-calendarGet list of calendar scenarios
#POST /site/{site_id}/scenario-calendarCreate a calendar scenario
#DELETE /site/{site_id}/scenario-calendar/{scenario_id}Delete a calendar scenario
#GET /site/{site_id}/scenario-calendar/{scenario_id}Get a calendar scenario
#PUT /site/{site_id}/scenario-calendar/{scenario_id}Update a calendar scenario
#coreScenarioShow/HideList OperationsExpand Operations
#GET /site/{site_id}/scenario-coreGet list of core scenarios
#GET /site/{site_id}/scenario-core/{trigger}Get a core scenarios
#PUT /site/{site_id}/scenario-core/{trigger}Update a core scenarios
#defaultShow/HideList OperationsExpand Operations
#GET /site/{site_id}/user/{user_id}/token_action/{token}Send a token action to a link between a site and an user
#PUT /site/{site_id}/user/{user_id}/locationSend location information to a link between a site and an user
#GET /user/{user_id}Get user information
#device : Configure your devicesShow/HideList OperationsExpand Operations
#POST /site/{site_id}/device/{device_id}/calibrationStart calibration of a device
#POST /site/{site_id}/device/{device_id}/calibration/stopStop calibration of a device
#DELETE /site/{site_id}/device-install/{model}Stop installation of a device
#POST /site/{site_id}/device-install/{model}Start installation of a device
#POST /site/{site_id}/device-install-homekit/{model}Start installation of a device
#POST /site/{site_id}/device-install/{model}/extendExtend installation duration of a device
#POST /site/{site_id}/device/{device_id}/resetBuild an encrypted reset payload for the mobile app
#POST /site/{site_id}/device/{device_id}/reset_wifiReset wifi for a video device
#DELETE /site/{site_id}/device/{device_id}/uninstallStop uninstall process of a device
#POST /site/{site_id}/device/{device_id}/uninstallUninstall a device previously installed on this site
#GET /site/{site_id}/device-compatibleGet list of devices compatible for installation on site
#GET /site/{site_id}/deviceGet list of installed devices on site
#GET /site/{site_id}/device/{device_id}Get details of a device
#PUT /site/{site_id}/device/{device_id}Set details of a device
#POST /site/{site_id}/device/{device_id}/actionRun an action on a device
#POST /site/{site_id}/device/{device_id}/sound/{sound_ref}Play a sound on a device
#POST /site/{site_id}/device/{device_id}/updateAsk firmware update for a device
#POST /site/{site_id}/device/lorawan/testLoRawan device trame test
#POST /site/{site_id}/device/backup-gsm/testBackup GSM device test
#GET /site/{site_id}/device/{device_id}/homekit/qrcodeList of mandatory updates
#GET /site/{site_id}/mode/{mode_name}Get details of a mode
#PUT /site/{site_id}/mode/{mode_name}Update HKP mode settings
#diagnosisShow/HideList OperationsExpand Operations
#POST /site/{site_id}/device/diagnosisStart the global testing of all devices for a site
#POST /site/{site_id}/device/diagnosis/extendExtends the global testing of all devices for a site
#POST /site/{site_id}/device/diagnosis/stopStops the global testing of all devices for a site
#installerSiteShow/HideList OperationsExpand Operations
#DELETE /site/{site_id}/installer/{user_id}Delete the link between a site and the installer
#POST /site/{site_id}/installerAdd a link between a site and the installer
#invitation : Invite users to your siteShow/HideList OperationsExpand Operations
#POST /site/{site_id}/invitationSend an invitation for using a site
#POST /site/invitationAnswer to an invitation
#invoice : Manage service invoicesShow/HideList OperationsExpand Operations
#GET /site/{site_id}/invoiceGet invoices list
#GET /site/{site_id}/invoice/{invoice_id}Get PDF invoice
#misc : Other API pointsShow/HideList OperationsExpand Operations
#GET /dictionary/{dictionary_id}/{locale}Get a dictionary file for translations
#GET /infoGet cloud version and enabled features
#GET /job/{job_id}Get user job
#POST /user/{user_id}/feedbackSend feedback
#mobile : Manage user mobile phonesShow/HideList OperationsExpand Operations
#POST /user/{user_id}/mobileProvide details of mobile phone for a user
#DELETE /user/{user_id}/mobile/{phone_id}Remove association between an user and a mobile
#photo : Upload and download photosShow/HideList OperationsExpand Operations
#POST /photoUpload a new photo
#GET /photo/{photo_id}Get a photo uploader by user
#plan : Manage and subscribe to site plansShow/HideList OperationsExpand Operations
#POST /site/{site_id}/payment-method/updateGet an URL to update the payment method
#POST /site/{site_id}/plan/checkoutSend cart and get checkout result
#POST /site/{site_id}/plan/unsubscribe/immediatelyCancellation imma
#DELETE /site/{site_id}/plan/unsubscribeRemove scheduled cancellation
#GET /site/{site_id}/plan/currentGet current plans
#GET /site/{site_id}/plan/availableGet available plans
#roomShow/HideList OperationsExpand Operations
#GET /site/{site_id}/roomList rooms
#POST /site/{site_id}/roomCreate a new room
#DELETE /site/{site_id}/room/{room_id}Delete a room
#PUT /site/{site_id}/room/{room_id}Update a room
#scenario : Manage your scenariosShow/HideList OperationsExpand Operations
#GET /site/{site_id}/scenarioGet list of scenarios
#POST /site/{site_id}/scenarioCreate a new scenario on a specific site
#DELETE /site/{site_id}/scenario/{scenario_id}Delete a scenario
#PUT /site/{site_id}/scenario/{scenario_id}Update a scenario
#site : Manage your siteShow/HideList OperationsExpand Operations
#GET /site/{site_id}/device/{device_id}/updateList of mandatory updates
#PUT /site/{site_id}/securityChange security level
#GET /site/{site_id}/historyGet filtered and sorted site events
#GET /siteList available sites for the current user
#POST /siteCreates a new site
#DELETE /site/{site_id}Delete a site
#GET /site/{site_id}Get a specific site for the current user
#PUT /site/{site_id}update a site
#POST /site/{site_id}/panicPut site in panic mode
#PUT /site/{site_id}/alarm/stopStop current site alarm
#PUT /site/{site_id}/domestic-alarm/{alarm_id}/stopStop domestic alarm
#PUT /site/{site_id}/alarm/trigger_manual_alarmTrigger site alarm
#PUT /site/{site_id}/privacySet the privacy state
#GET /site/{site_id}/lorawan/covertestLoRawan Cover test on site
#user : Manage usersShow/HideList OperationsExpand Operations
#POST /user/registerCreate a user account
#POST /user-guestCreates a guest user account
#PUT /user/{user_id}Update an user
#POST /user/password/sendSend password change token via email to user
#PUT /user/secureUpdate a user with a secure token sent by email
#PUT /user/{user_id}/passwordUpdate user password
#GET /user/validate-email/{email}Is email valid
#DELETE /user/gdpr-deleteDelete SP data for the current user
#userSite : Manage link between a site and an userShow/HideList OperationsExpand Operations
#GET /site/{site_id}/userRetrieves the list of users of the site
#DELETE /site/{site_id}/user/{user_id}Delete the link between a site and an user
#GET /site/{site_id}/user/{user_id}Get the link between a site and an user
#PUT /site/{site_id}/user/{user_id}Update the link between a site and an user
#POST /site/{site_id}/user/{user_id}/actionSignal an action to a link between a site and an user
#
# TODO:
#  - application strings (android & ios)
#  - api v2 v3
#  - relationship with client id
#
import base64
from json import JSONDecodeError
from typing import Any, Callable, Dict, List, Optional, Union

from oauthlib.oauth2 import LegacyApplicationClient, TokenExpiredError
from requests import Response
from requests_oauthlib import OAuth2Session

from somfy_protect_api.api.devices.category import Category
from somfy_protect_api.api.model import (
    AvailableStatus,
    Device,
    Site,
)

BASE_URL = "https://api.myfox.io"

SOMFY_PROTECT_TOKEN = "https://sso.myfox.io/oauth/oauth/v2/token"

ACTION_LIST = [
    "shutter_open",
    "shutter_close",
    "autoprotection_pause",
    "light_on",
    "light_off",
    "reboot",
    "halt",
    "sound_test",
    "measure_ambiant_light",
]

SOUND_REFS = (
    'armed',
    'disarmed',
    'ok',
    'intrusion',
    'siren1s', # 90DB
    'partial',
)

class SomfyProtectApi:
    """Somfy Protect Api Class"""

    def __init__(
        self,
        username: str,
        password: str,
        token: Optional[Dict[str, str]] = None,
        token_updater: Optional[Callable[[str], None]] = None,
        user_agent: Optional[str] = "Somfy Protect",
    ):

        self.username = username
        self.password = password
        self.client_id = base64.b64decode(
            "ODRlZGRmNDgtMmI4ZS0xMWU1LWIyYTUtMTI0Y2ZhYjI1NTk1XzQ3NWJ1cXJmOHY4a2d3b280Z293MDhna2tjMGNrODA0ODh3bzQ0czhvNDhzZzg0azQw"
        ).decode("utf-8")
        self.client_secret = base64.b64decode(
            "NGRzcWZudGlldTB3Y2t3d280MGt3ODQ4Z3c0bzBjOGs0b3djODBrNGdvMGNzMGs4NDQ="
        ).decode("utf-8")
        self.token_updater = token_updater

        extra = {"client_id": self.client_id, "client_secret": self.client_secret}

        self._oauth = OAuth2Session(
            client=LegacyApplicationClient(client_id=self.client_id),
            token=token,
            auto_refresh_kwargs=extra,
            token_updater=token_updater,
        )
        self._oauth.headers["User-Agent"] = user_agent

    def get_sites(self) -> List[Site]:
        """Get All Sites

        Returns:
            List[Site]: List of Site object
        """
        response = self.get("/v3/site")
        response.raise_for_status()
        return [Site(**s) for s in response.json().get("items")]

    def get_site(self, site_id: str) -> Site:
        """Get Site

        Args:
            site_id (str): Site ID


        Returns:
            Site: Site object
        """
        response = self.get(f"/v3/site/{site_id}")
        response.raise_for_status()
        return Site(**response.json())

    def update_security_level(self, site_id: str, security_level: AvailableStatus) -> Dict:
        """Set Alarm Security Level

        Args:
            site_id (str): Site ID
            security_level (AvailableStatus): Security Level
        Returns:
            Dict: requests Response object
        """
        security_level = {"status": security_level.lower()}
        response = self.put(f"/v3/site/{site_id}/security", json=security_level)
        response.raise_for_status()
        return response.json()

    def stop_alarm(self, site_id: str) -> Dict:
        """Stop Current Alarm

        Args:
            site_id (str): Site ID
        Returns:
            Dict: requests Response object
        """
        response = self.put(f"/v3/site/{site_id}/alarm/stop", json={})
        response.raise_for_status()
        return response.json()

    def trigger_alarm(self, site_id: str, mode: str) -> Dict:
        """Trigger Alarm

        Args:
            site_id (str): Site ID
            mode (str): Mode (silent, alarm)
        Returns:
            Dict: requests Response object
        """
        if mode not in ["silent", "alarm"]:
            raise ValueError("Mode must be 'silent' or 'alarm'")
        payload = {"type": mode}
        response = self.post(f"/v3/site/{site_id}/panic", json=payload)
        response.raise_for_status()
        return response.json()

    def action_device(
        self,
        site_id: str,
        device_id: str,
        action: str,
    ) -> Dict:
        """Make an action on a Device

        Args:
            site_id (str): Site ID
            device_id (str): Device ID
            action (str): Action

        Returns:
            str: Task ID
        """
        if action not in ACTION_LIST:
            raise ValueError(f"Unknown action {action}")

        response = self.post(f"/v3/site/{site_id}/device/{device_id}/action", json={"action": action})
        response.raise_for_status()
        return response.json()

    def update_device(
        self,
        site_id: str,
        device_id: str,
        device_label: str,
        settings: Dict,
    ) -> Dict:
        """Update Device Settings

        Args:
            site_id (str): Site ID
            device_id (str): Device ID
            device_label (str): Device Label
            settings (Dict): Settings (as return by get_device)

        Returns:
            str: Task ID
        """
        if settings is None or device_label is None:
            raise ValueError(f"Missing settings and/or device_label")

        # Clean Settings Dict
        settings.pop("object")
        # settings.pop('disarmed')
        # settings.pop('partial')
        # settings.pop('armed')

        payload = {"settings": settings, "label": device_label}
        response = self.put(f"/v3/site/{site_id}/device/{device_id}", json=payload)
        response.raise_for_status()
        return response.json()

    def camera_snapshot(self, site_id: str, device_id: str) -> Dict:
        """Get Camera Snapshot

        Args:
            site_id (str): Site ID
            device_id (str): Site ID

        Returns:
            Response: Response Image
        """
        response = self.post(f"/video/site/{site_id}/device/{device_id}/snapshot", json={"refresh": 10})
        response.raise_for_status()
        # path = "file.jpeg"
        if response.status_code == 200:
            # with open(path, "wb") as f:
            #    for chunk in response:
            #        f.write(chunk)
            return response

    def camera_refresh_snapshot(self, site_id: str, device_id: str) -> Device:
        """Get Camera Snapshot

        Args:
            site_id (str): Site ID
            device_id (str): Site ID

        Returns:
            Task: Somfy Task
        """
        response = self.post(f"/video/site/{site_id}/device/{device_id}/refresh-snapshot", json={})
        response.raise_for_status()
        return response.json()

    def get_devices(self, site_id: str, category: Optional[Category] = None) -> List[Device]:
        """List Devices from a Site ID

        Args:
            site_id (Optional[str], optional): Site ID. Defaults to None.
            category (Optional[Category], optional): [description]. Defaults to None.

        Returns:
            List[Device]: List of Device object
        """
        devices = []  # type: List[Device]
        response = self.get(f"/v3/site/{site_id}/device")
        try:
            content = response.json()
        except JSONDecodeError:
            response.raise_for_status()

        devices += [
            Device(**d)
            for d in content.get("items")
            if category is None or category.value.lower() in Device(**d).device_definition.get("label").lower()
        ]

        return devices

    def get_device(self, site_id: str, device_id: str) -> Device:
        """Get Device details

        Args:
            site_id (str): Site ID
            device_id (str): Site ID

        Returns:
            Device: Device object
        """
        response = self.get(f"/v3/site/{site_id}/device/{device_id}")
        response.raise_for_status()
        return Device(**response.json())

    # new api

    def device_sound(self, site_id: str, device_id: str, sound_ref: 'str') -> Dict:
        """
        """
        assert(sound_ref in SOUND_REFS)
        return self.post(f'/v3/site/{site_id}/device/{device_id}/sound/{sound_ref}', json={})

    # mimic in indoor siren, or there only?

    def get(self, path: str) -> Response:
        """Fetch an URL from the Somfy Protect API.

        Args:
            path (str): Path to request

        Returns:
            Response: requests Response object
        """
        return self._request("get", path)

    def post(self, path: str, *, json: Dict[str, Any]) -> Response:
        """Post data to the Somfy Protect API.

        Args:
            path (str): Path to request
            json (Dict[str, Any]): Data in json format

        Returns:
            Response: requests Response object
        """
        return self._request("post", path, json=json)

    def put(self, path: str, *, json: Dict[str, Any]) -> Response:
        """Put data to the Somfy Protect API.

        Args:
            path (str): Path to request
            json (Dict[str, Any]): Data in json format

        Returns:
            Response: requests Response object
        """
        return self._request("put", path, json=json)

    def request_token(
        self,
    ) -> Dict[str, str]:
        """Generic method for fetching a Somfy Protect access token.

        Returns:
            Dict[str, str]: Token
        """

        return self._oauth.fetch_token(
            SOMFY_PROTECT_TOKEN,
            username=self.username,
            password=self.password,
            client_id=self.client_id,
            client_secret=self.client_secret,
            include_client_id=True,
        )

    def refresh_tokens(self) -> Dict[str, Union[str, int]]:
        """Refresh and return new Somfy tokens.

        Returns:
            Dict[str, Union[str, int]]: Token
        """
        token = self._oauth.refresh_token(SOMFY_PROTECT_TOKEN)

        if self.token_updater is not None:
            self.token_updater(token)

        return token

    def _request(self, method: str, path: str, **kwargs: Any) -> Response:
        """Make a request.

        We don't use the built-in token refresh mechanism of OAuth2 session because
        we want to allow overriding the token refresh logic.

        Args:
            method (str): HTTP Methid
            path (str): Path to request

        Returns:
            Response: requests Response object
        """

        url = f"{BASE_URL}{path}"
        try:
            return getattr(self._oauth, method)(url, **kwargs)
        except TokenExpiredError:
            self._oauth.token = self.refresh_tokens()

            return getattr(self._oauth, method)(url, **kwargs)

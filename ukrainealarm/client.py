from aiohttp import ClientSession, ClientResponse


class Client:
    """Class to make authenticated requests."""

    BASE_PATH = "https://api.ukrainealarm.com/api/v3"
    REQUEST_TIMEOUT = 10

    def __init__(self, session: ClientSession, access_token: str):
        """Initialize the client."""
        self.session = session
        self.access_token = access_token

    async def __request(self, method: str, path: str) -> ClientResponse:
        """Make a request."""

        headers = {
            "accept": "application/json",
            "authorization": self.access_token
        }

        r = await self.session.request(
            method,
            f"{Client.BASE_PATH}/{path}",
            headers=headers,
            timeout=Client.REQUEST_TIMEOUT
        )
        r.raise_for_status()
        return await r.json()

    async def get_alerts(self, region_id: str = None) -> ClientResponse:
        """Get alerts."""
        return await self.__request("GET", "alerts" if region_id is None else f"alerts/{region_id}")

    async def get_last_alert_index(self) -> ClientResponse:
        """Get last alert index."""
        return await self.__request("GET", "alerts/status")

    async def get_regions(self) -> ClientResponse:
        """Get regions."""
        return await self.__request("GET", "regions")

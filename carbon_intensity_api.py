from datetime import datetime, timedelta
import requests
from typing import Dict, Optional


class CarbonIntensityAPI:
    """
    A class to interact with the API to retrieve carbon intensity history.
    """

    API_URL = "https://api.electricitymap.org/v3/carbon-intensity/history"

    def __init__(self, api_token: str) -> None:
        """
        Initialize the CarbonIntensityAPI with the given API token.

        Parameters
        ----------
        api_token : str
            API token for authorization.
        """
        self.api_token = api_token

    def fetch_carbon_intensity_history(self, region: str) -> Optional[Dict]:
        """
        Fetch the carbon intensity history for a given region.

        Parameters
        ----------
        region : str
            The region code ("GB" for United Kingdom).

        Returns
        -------
        Optional[Dict]
            A dictionary containing the carbon intensity history data or None if the request fails.
        """
        headers = {"auth-token": self.api_token}
        params = {"zone": region}

        # Calculate the time range for the last 24 hours
        now = datetime.now()
        start_time = now - timedelta(hours=24)
        params.update({
            "start": start_time.isoformat(),
            "end": now.isoformat()
        })

        try:
            response = requests.get(self.API_URL, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Request error occurred: {err}")
            return None

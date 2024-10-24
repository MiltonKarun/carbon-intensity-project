from carbon_intensity_api import CarbonIntensityAPI
from carbon_intensity_processor import CarbonIntensityProcessor


class CarbonIntensityService:
    """
    A high-level class to perform fetching, processing and displaying carbon intensity data.
    """

    def __init__(self, api_token: str, region: str) -> None:
        """
        Initialize the CarbonIntensityService with the provided API token and region.

        Parameters
        ----------
        api_token : str
            API token for authorization.
        region : str
            The region code for which to fetch carbon intensity data.
        """
        self.api = CarbonIntensityAPI(api_token)
        self.processor = CarbonIntensityProcessor()
        self.region = region

    def run(self) -> None:
        """
        Run the carbon intensity service to fetch, process, display data and average intensity.
        """
        data = self.api.fetch_carbon_intensity_history(self.region)
        if not data:
            print("Failed to retrieve data.")
            return

        processed_data = self.processor.process_data(data)
        if not processed_data:
            print("No valid data to process.")
            return

        self.processor.display_data(processed_data)

        intensities = [entry['intensity'] for entry in processed_data]
        try:
            avg_intensity = self.processor.calculate_average_intensity(intensities)
            print(f"\nAverage Carbon Intensity over the last 24 hours: {avg_intensity:.2f} gCO2eq/kWh")
        except ValueError as ve:
            print(ve)

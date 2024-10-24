import numpy as np
from datetime import datetime
from typing import List, Dict


class CarbonIntensityProcessor:
    """
    A class to process carbon intensity data and calculate mean.
    """

    @staticmethod
    def process_data(data: Dict) -> List[Dict]:
        """
        Process the raw carbon intensity data and extract relevant information.

        Parameters
        ----------
        data : Dict
            The raw carbon intensity data from the API.

        Returns
        -------
        List[Dict]
            A list of dictionaries containing timestamps and carbon intensity values.
        """
        history = data.get('history', [])
        processed_data = [
            {
                "timestamp": datetime.strptime(entry['datetime'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S"),
                "intensity": entry['carbonIntensity']
            }
            for entry in history if 'datetime' in entry and 'carbonIntensity' in entry
        ]
        return processed_data

    @staticmethod
    def calculate_average_intensity(intensities: List[float]) -> float:
        """
        Calculate the average carbon intensity using NumPy (for effective mean).

        Parameters
        ----------
        intensities : List[float]
            A list of carbon intensity values.

        Returns
        -------
        float
            The average carbon intensity.

        Raises
        ------
        ValueError
            If the intensity list is empty.
        """
        if not intensities:
            raise ValueError("Intensity list is empty.")
        return np.mean(intensities)

    @staticmethod
    def display_data(processed_data: List[Dict]) -> None:
        """
        Display the processed carbon intensity data in a tabular format.

        Parameters
        ----------
        processed_data : List[Dict]
            A list of dictionaries with timestamp and intensity values.
        """
        print(f"{'Timestamp':<20} | Carbon Intensity (gCO2eq/kWh)")
        print("-" * 50)
        for entry in processed_data:
            print(f"{entry['timestamp']:<20} | {entry['intensity']:.2f}")

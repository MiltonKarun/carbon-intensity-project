import numpy as np
import csv
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
        Generate .csv and .html files for user visualisation.

        Parameters
        ----------
        processed_data : List[Dict]
            A list of dictionaries with timestamp and intensity values.
        """
        print(f"{'Timestamp':<20} | Carbon Intensity (gCO2eq/kWh)")
        print("-" * 50)
        for entry in processed_data:
            print(f"{entry['timestamp']:<20} | {entry['intensity']:.2f}")

        # Generate .csv file using carbon intensity data
        output_file_csv = "carbon_intensity_data.csv"

        with open(output_file_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Carbon Intensity (gCO2eq/kWh)"])  # Header
            for entry in processed_data:
                writer.writerow([entry['timestamp'], f"{entry['intensity']:.2f}"])
                
        print(f"\nData saved to {output_file_csv}")

        # Generate .html file using carbon intensity data
        output_file_html = "carbon_intensity_data.html"
        
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Carbon Intensity Data</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2>Carbon Intensity Data</h2>
            <table>
                <tr>
                    <th>Timestamp</th>
                    <th>Carbon Intensity (gCO2eq/kWh)</th>
                </tr>
        """
        
        # Add each data entry as a row in the table
        for entry in processed_data:
            html_content += f"""
                <tr>
                    <td>{entry['timestamp']}</td>
                    <td>{entry['intensity']:.2f}</td>
                </tr>
            """
        
        html_content += """
            </table>
        </body>
        </html>
        """
        
        with open(output_file_html, "w") as file:
            file.write(html_content)
        
        print(f"\nData saved to {output_file_html}")

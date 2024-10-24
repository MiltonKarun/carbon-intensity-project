# Carbon Intensity Service

## Overview
This project fetches and processes the carbon intensity data from the Electricity Maps API and calculates the average carbon intensity over a given period. The results are displayed in a tabular format along with the calculated average.

## Project Structure

```bash
carbon-intensity-project/
├── carbon_intensity_service.py   # High-level orchestration
├── carbon_intensity_api.py       # API interaction class
├── carbon_intensity_processor.py # Data processing class
├── main.py                       # Entry point for running the application
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Installation

Clone the repository  
```git clone https://github.com/MiltonKarun/carbon-intensity-project.git```

Navigate to the project directory  
```cd carbon-intensity-project```

Install the required dependencies  
```pip install -r requirements.txt```

Usage: Run the project using the following command  
```python main.py```

### Coding Practices Followed:
1. **Separation of Concerns**: Each class has its own responsibility and is placed in separate files.
2. **Error Handling**: Used `try-except` blocks for error handling when making API requests.
3. **Static Methods**: Used `@staticmethod` when the method did not need access to the instance.
4. **Docstrings**: Provided clear docstrings for all methods and classes.
5. **Type Annotations**: Used type hints to improve code readability and maintainability.
6. **Version Control**: Organized the project structure for easy version control using Git.

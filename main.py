from carbon_intensity_service import CarbonIntensityService


if __name__ == "__main__":
    API_TOKEN = "myapitoken"
    REGION = "GB"  # GB for United Kingdom

    carbon_service = CarbonIntensityService(api_token=API_TOKEN, region=REGION)
    carbon_service.run()

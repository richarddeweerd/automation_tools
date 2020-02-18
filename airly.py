'''Class and functions to communicate with Airly'''
import requests


class Airly:
    '''Class to communicate with Airly'''
    def __init__(self, host, apikey, inst):
        self.host = host
        self.apikey = apikey
        self.inst = inst
        self.pm1 = None
        self.pm10 = None
        self.pm25 = None
        self.temp = None
        self.hum = None
        self.baro = None
        self.caqi = None

    def update(self):
        '''Get info from Airly'''
        url = self.host + "v2/measurements/installation"
        parameters = {}
        parameters["installationId"] = self.inst
        parameters["apikey"] = self.apikey
        headers = {}
        payload = {}

        response = requests.request("GET", url, headers=headers, data=payload, params=parameters)
        if response.status_code == 200:
            json_response = response.json()
            for value in json_response["current"]["values"]:

                if value["name"] == "PM1":
                    self.pm1 = value["value"]

                if value["name"] == "PM25":
                    self.pm25 = value["value"]

                if value["name"] == "PM10":
                    self.pm10 = value["value"]

                if value["name"] == "TEMPERATURE":
                    self.temp = value["value"]

                if value["name"] == "HUMIDITY":
                    self.hum = value["value"]

                if value["name"] == "PRESSURE":
                    self.baro = value["value"]

            for value in json_response["current"]["indexes"]:

                if value["name"] == "AIRLY_CAQI":
                    self.caqi = value["value"]
        return response.status_code

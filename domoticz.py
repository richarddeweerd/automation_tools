'''Class and functions to communicate with Domoticz'''
import requests


class Domoticz:
    '''Classto communicate with Domoticz'''
    def __init__(self, host, username, password):
        self.host = host
        self.url = host + "json.htm"
        self.username = username
        self.password = password

    def set_sensor(self, idx, nval=0, sval=0):
        '''Set sensor'''
        parameters = {}
        parameters["username"] = self.username
        parameters["password"] = self.password
        parameters["type"] = "command"
        parameters["param"] = "udevice"
        parameters["idx"] = idx
        parameters["sval"] = sval
        parameters["nval"] = nval
        headers = {}
        payload = {}
        response = requests.request("GET", self.url, headers=headers, data=payload, params=parameters)
        return response.status_code

    def log(self, message):
        '''Send logmessage to domoticz'''
        parameters = {}
        parameters["username"] = self.username
        parameters["password"] = self.password
        parameters["type"] = "command"
        parameters["param"] = "addlogmessage"
        parameters["message"] = message

        headers = {}
        payload = {}
        response = requests.request("GET", self.url, headers=headers, data=payload, params=parameters)

        return response.status_code

    def set_sensor_thb(self, idx, temp, hum, baro):
        '''Set tem/hum/baro sensor'''
        sval = str(temp) + ";" + str(hum) + ";0;" + str(baro) + ";0"
        return self.set_sensor(idx, sval)

    def set_sensor_custom(self, idx, value):
        '''Set custom sensor'''
        return self.set_sensor(idx, sval=value)

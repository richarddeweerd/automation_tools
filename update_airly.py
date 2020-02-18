'''
Script to read information from airly and post it in Domoticz
'''
import configparser
import domoticz
import airly

def main():
    '''main function'''
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    dom = domoticz.Domoticz(config["Domoticz"]["Host"], config["Domoticz"]["Username"], config["Domoticz"]["Password"])
    air = airly.Airly(config["Airly"]["Host"], config["Airly"]["APIKey"], config["Airly"]["Installation"])
    if air.update() == 200:
        if air.temp:
            res = dom.set_sensor_thb(config["idx"]["airly_thb"], air.temp, air.hum, air.baro)
            print(res)

        if air.pm1:
            dom.set_sensor_custom(config["idx"]["airly_pm1"], air.pm1)

        if air.pm10:
            dom.set_sensor_custom(config["idx"]["airly_pm10"], air.pm10)

        if air.pm25:
            dom.set_sensor_custom(config["idx"]["airly_pm25"], air.pm25)

        if air.caqi:
            dom.set_sensor_custom(config["idx"]["airly_caqi"], air.caqi)

if __name__ == "__main__":
    main()

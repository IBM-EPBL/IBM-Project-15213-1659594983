import wiotp.sdk.device
import time
import random

myConfig = {
    "identity": {
        "orgId": "0lchi7",
        "typeId": "ESP32_Controller",
        "deviceId": "HC-SR04_Sensor"
    },
    "auth": {
        "token": "pKM00oySMURsO5npF)"
    }
}


def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m = cmd.data['command']


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temperature =random.randint(-20, 500)
    humidity =random.randint(0, 100)
    myData = {'temperature': temperature, 'humidity': humidity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(60)
client.disconnect()

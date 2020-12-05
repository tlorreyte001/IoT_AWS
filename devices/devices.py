from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from random import *
import time

MQTT_ENDPOINT = "a27g8v3y378vq3-ats.iot.us-east-1.amazonaws.com"
MQTT_PORT = 8883

# Configure logging
# import logging
# logger = logging.getLogger("AWSIoTPythonSDK.core")
# logger.setLevel(logging.DEBUG)
# streamHandler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)


def create_client(id_client):

    myAWSIoTMQTTClient = AWSIoTMQTTClient(id_client)

    myAWSIoTMQTTClient.configureEndpoint(MQTT_ENDPOINT, MQTT_PORT)
    myAWSIoTMQTTClient.configureCredentials("root-CA.crt", "Python1.private.key", "Python1.cert.pem")
    # myAWSIoTMQTTClient.configureCredentials("./keys/root-CA.crt", "./keys/Python1.private.key", "./keys/Python1.cert.pem")

    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    return myAWSIoTMQTTClient


def main():
    seed(1)
    myAWSIoTMQTTClient = create_client("Python1")
    myAWSIoTMQTTClient.connect()
    while True:
        Temp = randint(0, 10)
        myAWSIoTMQTTClient.publish("Temperature", str(Temp), 1)
        print("Temperature envoyee : " + str(Temp))
        print("--------------")
        time.sleep(3)
    myAWSIoTMQTTClient.disconnect()


if __name__ == '__main__':
    main()
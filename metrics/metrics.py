from prometheus_client import start_http_server, Gauge
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

MQTT_ENDPOINT = "a27g8v3y378vq3-ats.iot.us-east-1.amazonaws.com"
MQTT_PORT = 8883

g = Gauge('temperature_gauge', 'Temperature in C')

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

def callback(client, userdata, message):
    print("Received a new message: ")
    print("Temperature : " + str(message.payload))
    g.set(int(message.payload))
    print("--------------")


def main():
    print("Start !")
    myAWSIoTMQTTClient = create_client("Python2")
    print("Client created !")
    myAWSIoTMQTTClient.connect()
    print("Connected !")
    myAWSIoTMQTTClient.subscribe("Temperature", 1, callback)
    print("Subscribed !")
    start_http_server(8000)
    print("Server started !")
    print("--------------")
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
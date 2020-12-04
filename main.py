from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time

MQTT_ENDPOINT = "a27g8v3y378vq3-ats.iot.us-east-1.amazonaws.com"
MQTT_PORT = 8883

# Configure logging
#logger = logging.getLogger("AWSIoTPythonSDK.core")
#logger.setLevel(logging.DEBUG)
#streamHandler = logging.StreamHandler()
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#streamHandler.setFormatter(formatter)
#logger.addHandler(streamHandler)


def create_client(id_client):

    myAWSIoTMQTTClient = AWSIoTMQTTClient(id_client)

    myAWSIoTMQTTClient.configureEndpoint(MQTT_ENDPOINT, MQTT_PORT)
    myAWSIoTMQTTClient.configureCredentials("keys/root-CA.crt", "keys/Python1.private.key", "keys/Python1.cert.pem")

    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    return myAWSIoTMQTTClient

def callback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("From topic: " + message.topic)
    print("--------------\n\n")

def subscriber():
    myAWSIoTMQTTClient = create_client("Python1")
    myAWSIoTMQTTClient.connect()
    myAWSIoTMQTTClient.subscribe("Temperature", 1, callback)
    while True:
        time.sleep(1)
    #myAWSIoTMQTTClient.unsubscribe("Temperature")
    #myAWSIoTMQTTClient.disconnect()


def publisher():

    myAWSIoTMQTTClient = create_client("Python1")

    myAWSIoTMQTTClient.connect()
    myAWSIoTMQTTClient.publish("Temperature", "22", 1)
    myAWSIoTMQTTClient.disconnect()


def main():
    #publisher()
    subscriber()



if __name__ == '__main__':
    main()
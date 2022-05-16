import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

def on_connect(client, userdata, flags, rc):
    print("connected")

while True:
    client.on_connect = on_connect
    client.publish("topic2/teste", input("Message:"))

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt", 1883, 60)
client.publish("ALSW/temp",  "99")
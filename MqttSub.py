import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("cd746dd1addd", 1883, 60)
client.publish("ALSW/temp",  "99")
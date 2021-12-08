import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt", 1883, 60)
client.publish("test/prueba",  "hola")

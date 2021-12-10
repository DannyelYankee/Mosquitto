import paho.mqtt.client as mqtt
from datetime import datetime
client = mqtt.Client()
client.connect("mqtt", 1883, 60)
name = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
client.publish("test/"+name,  "hola")

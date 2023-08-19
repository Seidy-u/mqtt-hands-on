import paho.mqtt.client as mqtt

MQTT_PORT = 1883
KEEP_ALIVE = 60
TOPIC = "topic/01/"

#Brokerに接続できたとき
def on_connect(client, userdata, flag, rc):
  print("Connect Broker:" + str(rc))

#Brokerと切断したとき
def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
     print("disconnect broker")

#publishが完了したとき
def on_publish(client, userdata, mid):
  print("publish Done")


client = mqtt.Client()
#コールバックを登録 
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect("localhost", MQTT_PORT, KEEP_ALIVE)  

client.publish(TOPIC,"Hello!")
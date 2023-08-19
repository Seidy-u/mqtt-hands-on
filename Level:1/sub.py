import paho.mqtt.client as mqtt 

MQTT_PORT = 1883
KEEP_ALIVE = 60
TOPIC = "topic/01/"

#Brokerに接続できたとき
def on_connect(client, userdata, flag, rc):
  print("connect broker:OK")
  client.subscribe(TOPIC) 

#Brokerと切断したとき
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("disconnect broker")

#メッセージ受信
def on_message(client, userdata, msg):
  print(msg)
  print("Received message '" + str(msg.payload) + "' on topic '" + 
        msg.topic + "' with QoS " + str(msg.qos))


client = mqtt.Client()  
#コールバックを登録     
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("localhost", MQTT_PORT, KEEP_ALIVE)

#待ち受け
client.loop_forever()
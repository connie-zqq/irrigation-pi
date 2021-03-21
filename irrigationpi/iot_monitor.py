import csv
import os
import time

import Adafruit_DHT as DHT
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from irrigationpi import app, config

load_dotenv()

# The hostname of the ThingSpeak MQTT service
server_address = "mqtt.thingspeak.com"
port = 1883

# ThingSpeak Channel Settings
channel_id = os.getenv("CHANNEL_ID")
write_api_key = os.getenv("THINGSPEAK_WRITE_API_KEY")

# Create the topic string
topic = "channels/" + channel_id + "/publish/" + write_api_key

client = mqtt.Client()
client.connect(server_address, port)

sensor = DHT.DHT22
pin = 27

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time (s)', 'Temperature (C)', 'Humidity (%)'])

    running_time = 0
    water_pump_rf_outlet = app.RFOutlet('water-pump',
                                        config.water_pump_outlet_codes[0],
                                        config.water_pump_outlet_codes[1],
                                        app.RFCodeSender())

    while True:
        h, t = DHT.read_retry(sensor, pin)
        print("Temp: ", t)
        print("Humidity : ", h)

        # Get the current status of rf_outlet
        rf_outlet_status = water_pump_rf_outlet.status()

        # Adjust required temperature and humidity to water the plants
        if t > 28 and h < 40:
            # Cloud Backup: Publish DHT22 sensor data to a ThingSpeak Channel Using MQTT
            data = "field1=" + str(t) + "&field2=" + str(h)
            client.publish(topic, data)

            # Check if the current status of water pump is off
            if rf_outlet_status["status"] == "off":
                # Turning on the outlet for 300 seconds
                water_pump_rf_outlet.on()
                time.sleep(300)  # duration=300
                running_time += 300
                water_pump_rf_outlet.off()

                # Send the SMS activity notification via Twilio
                exec(open("sms_notification.py").read())
        else:
            if rf_outlet_status["status"] == "on":
                water_pump_rf_outlet.off()

        writer.writerow([running_time, t, h])

        # Suspend execution for 1 hour
        time.sleep(3600)

        running_time += 3600

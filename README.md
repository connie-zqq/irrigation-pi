# Raspberry pi controlled smart irrigation system

## Hardware

Raspberry Pi 3, DHT22 sensor, an RF transmitter, a remote-control outlet, a submersible water pump.

## Software stack

Python 3, CherryPy, APScheduler, WiringPi, Adafruit_DHT, ThingSpeak, Twilio.

## Progress

v.1 - It supports remote control on a web page via REST APIs and has a cron job for periodic irrigation. (May - June, 2020)

v.2 - Improved irrigation scheduling based on real-time temperature and humidity data from DHT22 sensor, monitored live data streams through ThingSpeak and sent SMS activity notifications using Twilio.  (Mar - Apr, 2021)  

![image](https://user-images.githubusercontent.com/60984454/136063397-cb0cce66-2fa0-4bb9-bd53-0a9b8d04e344.png)

v.3 - TODO: Using Google Assistant / IFTTT to control the raspberry pi 

## RF outlet

Kudoes to the [433Utils](https://github.com/ninjablocks/433Utils/tree/master/RPi_utils) project, which offers `RFSniffer` and `codesend` to sniffer the RF outlet code and send the control code.

TODO:  How `RFSniffer` and `codesend` works






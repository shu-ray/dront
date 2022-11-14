# dront (WIP)
Mini forelimb-controlled drone with an ESP8266 and an ESP32

- The drone system consist of MPU-6050 gyro sensor, an ultrasonic, 4 cordless motor (2 clockwise,2 counter-clockwise) with [D1 Mini ESP8266EX](https://www.wemos.cc/en/latest/d1/d1_mini.html#features)

- The remote system consist of 2 MPU-6050, few buttons as function/shift control keys on ESP32

- Both system will communicate through LoRa transceiver but in this experimental stage, ~~bluetooth will be used instead to debug on pc with python (look remote.py)~~ we'll use [Blynk](https://play.google.com/store/apps/details?id=cloud.blynk&hl=en&gl=US) on android through wifi connection

- FuturePlanThatMightNeverBeImplemented™ : ESP32CAM on drone system to capture live feed view and stream to remote system with 320x240 pixels TFT display on WiFi.
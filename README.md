# ![](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png) Intelligent	Power	Solution &	Intrusion	Detection System
### Department	of	Computer	Science	and	Engineering, Sharda University
### Tinkering	Lab	– 2nd	Year
#### 	Mentor:	Prof.	Ishan	Ranjan (Head of Department, CSE)
#### April,	2016
# ![](IoT_Power.png)

---
## ACKNOWLEDGEMENT
Working on this project on Internet of Things was a source of immense knowledge to me. I would like express my sincere gratitude to Prof. Ishan Ranjan for his guidance and valuable support throughout the course of this project work. I acknowledge with deep sense of gratitude, the encouragement and inspiration received from my faculty members and colleagues. I would also like to thank my friends for helping and supporting throughout the preparation of this project work. Altogether, it was a great experience.

## SUMMARY

The Internet of Things (IoT) is the network of physical objects (devices, vehicles, buildings and other items) embedded with electronics, software, sensors, and network connectivity that enables these objects to collect and exchange data.

An Arduino Yun board will be used as a programmable interface which will be used to send & receive data. We will be taking input from a passive infrared sensor and turning the alarm on while also taking the picture of the intruder & turning on the emergency light.

The same model can also be programmed used for intelligent power savings as we can turn a number of electronic devices on or off when the user/organization intends it to using sensors to detect movement in a particular area.

## REQUIREMENTS
### Hardware Prerequisites
    • Logitech C270 720p HD Webcam (1)
    • Arduino Yun (1)
    • Solid State Relay 25Amp (1)
    • PIR (Passive Infrared) Sensor HC-SR501 (1) 
    • Crompton 5W Small Tube Light (1)
    • nPn Transistor (1)
    • Connecting Wires (20)
    • Regulated Power Supply Board (1) 
    • SMPS Adapter 1A (1)
    • Arduino Yun Adapter 1.5A(1)
    • Piezo Buzzer (1)
    • Wire Cutters (1)

### Software Prerequisites
#### Temboo API
```sh
pip install temboo
```
#### Temboo API Inputs
* AppSecret
* AccessToken
* FileName
* AccessTokenSecret
* AppKey
* FileContents
* Root

#### Requirements
* Python 3
* Temboo SDK
* Dropbox Account
* Active Internet Connection in Arduino
    
## WORKING
    • The output of PIR Sensor will be connected to one of the analog ports of the Arduino Yun.
    • The input of the Solid State Relay will be connected to the nPn transistor which will then be connected to the input of the Yun board.
    • All ground must be kept short so that all electronic devices have the same low & high potentials.
    • A HIGH signal from the PIR Sensor when motion will be detected to the Yun Board.
    • The Yun Board will then send a HIGH signal to the buzzer, transistor & the camera attached.
    • The buzzer will beep continuously, and the transistor will send a high signal to the relay connecting the circuit so as to turn on the emergency light.
    • The camera will take a picture and send it to any Cloud Storage account instantly.
    • All the devices will be in LOW mode until the sensor captures any movement. 


    
## A FEW REAL WORLD APPLICATIONS

    • Break-in detection & alarm (Security)
    • Intelligent Power Solutions:  Turning any electronic device ON/OFF automatically using motion detection
    • Smart Parking
    • Home, Building Automation



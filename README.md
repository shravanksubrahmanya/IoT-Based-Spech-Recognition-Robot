# Iot-Based-Speech-Recognition-Robot

### Domain:
Internet of Things - Speech Recognition

### Description:
The implementation of speech recognition based robot performs motion through speech inputs as well as text inputs.

 This project gives an idea on working with a voice recognition software to control a robot, which can be further implemented for the semi-autonomous voice-controlled wheelchair in hospitals and other purposes.
 
 ### Checkout YouTube Video
 ![Youtube Video](https://youtu.be/3WwrHXjeO9Y)

### Software Specifications:
* Arduino IDE
* Python 3.9

### Electronics parts:
* Arduino Uno
* L293D Motor Driver
* two DC Motors
* one Servo Motor

### Software libraries used:
#### python libraries:
* speechrecognition
* pyaudio
* pyttsx3
* pywhatkit
* pyserial

#### Arduino library:
* Adafruit Motor Shield

### Principle:
Before getting into the actual building, it is great to have an idea of what we will be doing.

Thhe main code or AI part of the code will run on the computer, because it supports python and has more processing power than the little Arduino, also as the AI bot will control/automate some tasks of my pc it has to run on my pc. So, the Arduino board is connected to my computer using the USB cable.

The idea is to run a  python program that will do the Speech to text part, process the text and will also do Text to speech. it means the robot will listen, understand and talk back. For robot movement I saved some movements (encapsulated in functions) in Arduino board. The function for each movements are executed by the python code.

For an example – if the robot has to move forward , the ‘forward / move forward’ command will be given followed by robots name. the python interpretter will process the speech and will send a byte ‘f’ to the arduino board through serial port, Arduino then execute the forward() function. As simple as that.

### Architecture Diagram:
![Architecture Diagram](https://github.com/shravanksubrahmanya/IoT-Based-Spech-Recognition-Robot/blob/31cd08cee65c3f7224c73dc8214e799e39044f22/bluetooth%20car%20circuit234.jpg)

### Installation process:
1. Install the above given python libraries using the command "pip install <library name>"
2. Install the Adafruit motor shield library in Arduino IDE
3. Burn the "robot1" Arduino code into Arduino UNO
4. Set up the "serial port" name in the python file.
5. Run the python file and start giving commands.
6. In case you are not using bluetooth module, use serial cable to connect Arduino Uno and PC

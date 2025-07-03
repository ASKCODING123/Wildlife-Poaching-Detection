# Wildlife-Poaching-Detection
Wildlife Poaching Detection is a real time poaching detetction initiative, which detects poaching during day and night time as well, and gives Alerts. It was done using YOLO Model. This Project was selected by the KSCST and Karnataka Govt is funding our project.

There are 3 majour tasks in this project : 
 - Human Detection (for both Day and Night Time using YOLO Model)
 - Weapon Detection (YOLO Model)
 - Animal Classification (YOLO Model, Resnet18 Model, PyTorch)

To make poaching detection real time, we have used the following sensors for Hardware Setup : 
 - PIR Sensor     : For Motion Detection
 - ESP32 Cam      : For Capturing Photo
 - NPN Transister : It acts as a switch, when PIR Sensor detects motion, it instructs ESP32 Cam to take picture
 - Arduino UNO    : For Controlling Sensors

The ESP32 Cam sends the captured photo to the Email via SMTP Protocol, and the device automatically downloads the image attached in the email with the help of imaplib library, and detects for any illegal activity and gives alerts.

Hardware Setup : 

![image](https://github.com/user-attachments/assets/8842d819-4d5f-4ed2-8ca9-20b899ad7a25)

Circuit Diagram : 

![image](https://github.com/user-attachments/assets/a7f8fe60-5a06-41c3-9be5-345d49a62290)




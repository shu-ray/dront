#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "YourAuthToken";
char ssid[] = "Usrati Jannati";  // Your WiFi credentials.
char pass[] = "adira2000";       // Set password to "" for open networks.

// Value ranging 12bit (esp32 adc precision)
int thumbstickX = 0;
int thumbstickY = 0;

// Execute only when V1 virtual pin changes
BLYNK_WRITE(V1) {
  thumbstickX = param[0].asInt();
  thumbstickY = param[1].asInt();
}

Adafruit_MPU6050 mpu;
sensors_event_t a, g, temp;

void setup()
{
    Serial.begin(115200);
    Blynk.begin(auth, ssid, pass);

    if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
}

void loop()
{
  Blynk.run();
  mpu.getEvent(&a, &g, &temp);

  Serial.print("AccelX:");
  Serial.print(a.acceleration.x);
  Serial.print(",");
  Serial.print("AccelY:");
  Serial.print(a.acceleration.y);
  Serial.print(",");
  Serial.print("AccelZ:");
  Serial.print(a.acceleration.z);
  Serial.print(", ");
  Serial.print("GyroX:");
  Serial.print(g.gyro.x);
  Serial.print(",");
  Serial.print("GyroY:");
  Serial.print(g.gyro.y);
  Serial.print(",");
  Serial.print("GyroZ:");
  Serial.print(g.gyro.z);
  Serial.println("");
  
}
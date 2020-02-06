#include <DHT.h>  
#include <ESP8266WiFi.h>  
#include <WiFiClient.h>  
#include <ThingSpeak.h>



#define DHTPIN D4  
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE);  

const char* ssid = "TP-Link_0106";  
const char* password = "Basketballer??106";  
WiFiClient client;  
unsigned long myChannelNumber = 526842;  
const char * myWriteAPIKey = "6PJBLZIJL9FEFCBF";  
uint8_t temperature;
void setup()  
{  
  Serial.begin(115200);   

  dht.begin();  
  delay(10); 
  // Connect to WiFi network  
  Serial.println();  
  Serial.println();  
  Serial.print("Connecting to ");  
  Serial.println(ssid);  
  WiFi.begin(ssid, password);  
  while (WiFi.status() != WL_CONNECTED)  
  {  
   delay(500);  
   Serial.print(".");  
  }  
  Serial.println("");  
  Serial.println("WiFi connected");  
  // Print the IP address  
  Serial.println(WiFi.localIP());  
  ThingSpeak.begin(client);  
}  
void loop()   
{  
  temperature = dht.readTemperature(); 
  Serial.print("Temperature Value is :");  
  Serial.print(temperature);  
  Serial.println("C");  
 
   
  ThingSpeak.writeField(myChannelNumber,1,temperature,myWriteAPIKey); 
  Serial.println("done"); 
      
  delay(3000); // ThingSpeak will only accept updates every 15 seconds.  
} 




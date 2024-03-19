#include <Arduino.h>

int input = A5;
int R = 11;
int G = 10;
int B = 9;

void setup() {
    Serial.begin(9600);
}
void loop(){
    int PinVal = analogRead(input);
    float DC = (0.09778134 * PinVal - 24.14032404);
    float DF = (DC * (9.0/5.0) + 32);
    Serial.print("Analog = "); 
    Serial.print(PinVal);
    Serial.print("    Temperature = "); 
    Serial.print(DC, 4); 
    Serial.print("degC = "); 
    Serial.print(DF, 3); 
    Serial.println("degF");

    if(PinVal>500){
        analogWrite(B, 0)
        // 0-255 (0=500,255=1000)

        // if above 255 for some reason
        if (((PinVal-500)*0.51) > 255){
            analogWrite(R, 255);
        }
        // 0-255 fade mapping
        else{
            analogWrite(R, ((analogRead(input)-500)*0.51));
            analogWrite(G, 255-((analogRead(input)-500)*0.51));
        }
    }
    // static blue at room temp
    else{
        analogWrite(B, 255);
        analogWrite(R, 0);
        analogWrite(G, 0);
    }
}

#include <Arduino.h>

///////////////////////////////////
//PINS//
int input = A5;         //pin//
int fan = 13;           //pin//
int heater = 12;        //pin//
int R = 11;             //pin//
int G = 10;             //pin//
int B = 9;              //pin//

//SETPOINT//
float setpointC = 22.1; //uservar//

//STANDARD DEVIATION//
int stdv = 2;           //uservar//
///////////////////////////////////

//CONVERSION FUNCTIONS//
//analog to celsius (y = 0.10445576x - 27.94654789;)
float AtoC(float x){
    return 0.10445576 * x - 28.94654789;
}
//celsius to analog (y = 9.57343x + 267.54432)
float CtoA(float x){ 
    return 9.57343089 * x + 277.11777588;
}
//celsius to f
float CtoF(float x){
    return x * (9.0/5.0) + 32;
}
//constrain number to 0,255
int ConstrainA(int x){
    if(x < 0){return 0;}
    if(x > 255){return 255;}
    else{return x;}
}

//VARIABLE INIT//
int setpointA = CtoA(setpointC);
int tempA = analogRead(input);
float tempC = AtoC(tempA);

int UCLA = setpointA + (stdv * 3);
int LCLA = setpointA - (stdv * 3);
float UCLC = AtoC(UCLA);
float LCLC = AtoC(LCLA);

bool Heater = false;
bool Fan = false;

//LIGHTING//
void Off(){
    analogWrite(R,0);
    analogWrite(G,0);
    analogWrite(B,0);
}

void Rainbow(int s, float d){
    analogWrite(B,0*d);
    analogWrite(R,255*d);
    for(float a=255; a>0; a--){
        analogWrite(R,a*d); analogWrite(G, (255-a)*d);
        delay(s);
    }
    analogWrite(R,0*d);
    analogWrite(G,255*d);
    for(float a=255; a>0; a--){
        analogWrite(G,a*d); analogWrite(B, (255-a)*d);
        delay(s);
    }
    analogWrite(G,0*d);
    analogWrite(B,255*d);
    for(float a=255; a>0; a--){
        analogWrite(B,a*d); analogWrite(R, (255-a)*d);
        delay(s);
    }
}

void Static(int r,int g,int b, float d) {
    analogWrite(R,r*d);
    analogWrite(G,g*d);
    analogWrite(B,b*d);
}

void setup() {
    pinMode(heater, OUTPUT);
    pinMode(fan, OUTPUT);
    Serial.begin(9600);

    //header for print out
    Serial.println("\n\n\n\n\n");
    Serial.println("Value | Celsius Analog");Serial.println("-=-=-=|=-=-=-=-=-=-=-=-");
    Serial.print("Setpt |\t");Serial.print(setpointC);Serial.print("\t");Serial.println(setpointA);
    Serial.print("UCL   |\t");Serial.print(UCLC);Serial.print("\t");Serial.println(UCLA);
    Serial.print("LCL   |\t");Serial.print(LCLC);Serial.print("\t");Serial.println(LCLA);
    Serial.println("-=-=-=-=-=-=-=-=-=-=-=-");
    Serial.println("Status| Celsius Analog  Heater  Fan");
    Serial.println("-=-=-=|=-=-=-=-=-=-=-=-=-=-=-=-=-=-");

    // Value | Celsius Analog
    // -=-=-=|=-=-=-=-=-=-=-=-
    // Setpt | C       A
    // UCL   | C       A
    // LCL   | C       A
    // -=-=-=-=-=-=-=-=-=-=-=-
    // Status| Celsius Analog  Heater  Fan
    // -=-=-=|=-=-=-=-=-=-=-=-=-=-=-=-=-=-

}
void loop(){
    //set temp in A for cycle
    int tempA = analogRead(input);
    //set temp in C for cycle
    float tempC = AtoC(tempA);

    //map A to range of 0-255
    //int AMap = map(tempA,470,510,0,255);
    int AMap = ConstrainA(map(tempA,LCLA,UCLA,0,255));
    int AltAMap = 255-AMap;
    
    //fade rgb led with temp
    Static(AMap,0,AltAMap,1);

    //logic
    //below
    if(tempC<LCLC){
        Heater=true;
        digitalWrite(heater,HIGH);
    }
    //above
    if(tempC>UCLC){
        Heater=false;
        digitalWrite(heater,LOW);
        Fan=true;
        digitalWrite(fan,HIGH);
    }
    //below setpoint
    if(tempC<setpointC){
        Fan=false;
        digitalWrite(fan,LOW);
    }

    //construct print message
    //status
    if(tempC<LCLC){
        Serial.print("Below |\t");
    }
    else if(tempC>UCLC){
        Serial.print("Above |\t");
    }
    else{
        Serial.print("      |\t");
    }
    //temp
    Serial.print(tempC);Serial.print("\t");Serial.print(tempA);Serial.print("\t");
    //heater
    if(Heater){
        Serial.print("ON");
    }
    else{
        Serial.print("OFF");
    }
    Serial.print("\t");
    //fan
    if(Fan){
        Serial.println("ON");
    }
    else{
        Serial.println("OFF");
    }
}

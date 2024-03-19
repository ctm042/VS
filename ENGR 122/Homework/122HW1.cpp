void setup(){
    pinMode(12, INPUT);
    Serial.begin(9600);
    tone(13,38000);
}

void loop(){
    Serial.println(digitalRead(12));
    digitalWrite(11, digitalRead(12));
}
int pinout = 8;
int tempo = 102;
int timeunit = (60.0/tempo)*1000.0;

float C4 = 261.686;
float Db4 = 277.262;
float D4 = 293.724;
float Eb4 = 311.194;
float E4 = 329.724;
float F4 = 349.309;
float Gb4 = 370.081;
float G4 = 392.089;
float Ab4 = 415.413;
float a4 = 440.001;
float Bb4 = 466.150;
float B4 = 493.858;

float C2 = C4/4;
float Db2 = Db4/4;
float D2 = D4/4;
float Eb2 = Eb4/4;
float E2 = E4/4;
float F2 = F4/4;
float Gb2 = Gb4/4;
float G2 = G4/4;
float Ab2 = Ab4/4;
float a2 = a4/4;
float Bb2 = Bb4/4;
float B2 = B4/4;
float C3 = C4/2;
float Db3 = Db4/2;
float D3 = D4/2;
float Eb3 = Eb4/2;
float E3 = E4/2;
float F3 = F4/2;
float Gb3 = Gb4/2;
float G3 = G4/2;
float Ab3 = Ab4/2;
float a3 = a4/2;
float Bb3 = Bb4/2;
float B3 = B4/2;

float C5 = C4*2;
float Db5 = Db4*2;
float D5 = D4*2;
float Eb5 = Eb4*2;
float E5 = E4*2;
float F5 = F4*2;
float Gb5 = Gb4*2;
float G5 = G4*2;
float Ab5 = Ab4*2;
float a5 = a4*2;
float Bb5 = Bb4*2;
float B5 = B4*2;
float C6 = C4*4;
float Db6 = Db4*4;
float D6 = D4*4;
float Eb6 = Eb4*4;
float E6 = E4*4;
float F6 = F4*4;
float Gb6 = Gb4*4;
float G6 = G4*4;
float Ab6 = Ab4*4;
float a6 = a4*4;
float Bb6 = Bb4*4;
float B6 = B4*4;
float C7 = C4*8;
float Db7 = Db4*8;
float D7 = D4*8;
float Eb7 = Eb4*8;
float E7 = E4*8;
float F7 = F4*8;
float Gb7 = Gb4*8;
float G7 = G4*8;
float Ab7 = Ab4*8;
float a7 = a4*8;
float Bb7 = Bb4*8;
float B7 = B4*8;

void setup(){
    Serial.begin(9600);
    pinMode(8, OUTPUT);
    Serial.println(timeunit);
}
void loop(){
    The_Only_Thing_They_Fear_Is_You();
}
//Notes

void note(int length, int note1, int notebend1 = 0, int note2 = 0, int notebend2 = 0){
    notebend1 = ( notebend1 == 0 ) ? note1 : notebend1;
    notebend2 = ( notebend2 == 0 ) ? note2 : notebend2;
    // single note
    if (note2 = 0){
        tone(pinout, note);
    }
    // double note
    else{

    }
}


void wholenote(int note){
    tone(pinout, note);
    delay((timeunit*4)-(timeunit/8));
    noTone(pinout); 
    delay(timeunit/8);
}
void halfnote(int note){
    tone(pinout, note);
    delay((timeunit*2)-(timeunit/8));
    noTone(pinout); 
    delay(timeunit/8);
}
void quarternote(int note){
    tone(pinout, note);
    delay((timeunit)-(timeunit/8));
    noTone(pinout); 
    delay(timeunit/8);
}
void eighthnote(int note){
    tone(pinout, note);
    delay((timeunit/2)-(timeunit/8));
    noTone(pinout); 
    delay(timeunit/8);
}
void sixteenthnote(int note){
    tone(pinout, note);
    delay((timeunit/4)-(timeunit/8));
    noTone(pinout); 
    delay(timeunit/8);
}

//Legato Notes
void wholenotel(int note){
    tone(pinout, note);
    delay(timeunit*4);
    noTone(pinout);
}
void halfnotel(int note){
    tone(pinout, note);
    delay(timeunit*2);
    noTone(pinout); 
}
void quarternotel(int note){
    tone(pinout, note);
    delay(timeunit);
    noTone(pinout); 
}
void eighthnotel(int note){
    tone(pinout, note);
    delay(timeunit/2);
    noTone(pinout); 
}
void sixteenthnotel(int note){
    tone(pinout, note);
    delay(timeunit/4);
    noTone(pinout); 
}

//Double Notes
void wholedouble(int note1, int note2){
    for (int i = 0 ; i < 32 ; i++){
        tone(pinout, note1);
        delay((timeunit/4)/4);
        tone(pinout, note2);
        delay((timeunit/4)/4);
    }
    noTone(pinout);
}
void halfdouble(int note1, int note2){
    for (int i = 0 ; i < 16 ; i++){
        tone(pinout, note1);
        delay((timeunit/4)/4);
        tone(pinout, note2);
        delay((timeunit/4)/4);
    }
    noTone(pinout);
}
void quarterdouble(int note1, int note2){
    for (int i = 0 ; i < 8 ; i++){
        tone(pinout, note1);
        delay((timeunit/4)/4);
        tone(pinout, note2);
        delay((timeunit/4)/4);
    }
    noTone(pinout);
}
void eighthdouble(int note1, int note2){
    for (int i = 0 ; i < 4 ; i++){
        tone(pinout, note1);
        delay((timeunit/4)/4);
        tone(pinout, note2);
        delay((timeunit/4)/4);
    }
    noTone(pinout);
}
void sixteenthdouble(int note1, int note2){
    for (int i = 0 ; i < 2 ; i++){
        tone(pinout, note1);
        delay((timeunit/4)/4);
        tone(pinout, note2);
        delay((timeunit/4)/4);
    }
    noTone(pinout);
}

//Rests
void wholerest(){
    delay(timeunit*4);
}
void halfrest(){
    delay(timeunit/2);
}
void quarterrest(){
    delay(timeunit);
}
void eighthrest(){
    delay(timeunit/2);
}
void sixteenthrest(){
    delay(timeunit/4);
}

void The_Only_Thing_They_Fear_Is_You(){
    //The Only Thing They Fear Is You - Mick Gordon
    //Doom on a piezo speaker
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnote(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    sixteenthnote(D4);
    sixteenthnote(E4);
    ///
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(E3);
    sixteenthnote(E3);

    eighthnotel(E4);
    sixteenthnote(E4);

    eighthnote(F3);
    ///
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnote(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    sixteenthnote(D4);
    sixteenthnote(E4);
    ///
    eighthnote(Eb4);//
    eighthnote(Eb3);

    sixteenthnote(Eb3);//
    sixteenthnote(Eb3);
    sixteenthnote(Db4);
    sixteenthnote(Eb4);

    sixteenthnote(D4);//
    eighthnote(D3);
    sixteenthnote(D3);

    sixteenthnote(D3);//
    eighthnotel(D3);
    sixteenthnote(D3);

    ///

    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnote(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    sixteenthnote(D4);
    sixteenthnote(E4);
    ///
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(E3);
    sixteenthnote(E3);

    eighthnotel(E4);
    sixteenthnote(E4);

    eighthnote(F3);
    ///
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    eighthnote(Eb3);
    sixteenthnote(Eb3);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    sixteenthnote(D4);
    sixteenthnote(E4);
    ///
    eighthnote(Eb4);

    eighthnotel(Eb3);
    sixteenthnote(Eb3);

    sixteenthnote(Eb3);
    sixteenthnote(Db4);
    sixteenthnote(Eb4);
    sixteenthnote(D4);

    sixteenthnote(D3);
    sixteenthrest();

    sixteenthnote(D3);
    eighthrest();
    
    sixteenthnote(D3);
    sixteenthrest();

    ///

    eighthdouble(Eb4,Eb5);//
    eighthdouble(Eb3,Eb5);

    sixteenthdouble(Eb3,D6);//
    eighthdouble(Eb3,D6);
    sixteenthdouble(Eb3,D6);

    eighthdouble(Eb3,B5);//
    sixteenthdouble(Eb3,B5);
    sixteenthdouble(Eb3,B5);

    eighthdouble(Eb3,Bb5);//
    sixteenthdouble(D4,Bb5);
    sixteenthdouble(E4,Bb5);
    ///
    eighthdouble(Eb4,Eb6);//
    eighthdouble(Eb3,Eb6);

    sixteenthdouble(Eb3,D6);//
    eighthdouble(Eb3,D6);
    sixteenthdouble(Eb3,D6);

    eighthdouble(E3,B5);//
    sixteenthdouble(E3,B5);
    sixteenthdouble(E4,B5);

    eighthdouble(E4,Bb5);//
    eighthdouble(F3,Bb5);
    ///
    eighthdouble(Eb4,Ab5);//
    eighthdouble(Eb3,Ab5);

    sixteenthdouble(Eb3,G5);//
    eighthdouble(Eb3,G5);
    sixteenthdouble(Eb3,G5);

    eighthdouble(Eb3,G5);//
    sixteenthdouble(Eb3,G5);
    sixteenthdouble(Eb3,G5);

    eighthdouble(Eb3,G5);//
    sixteenthdouble(D4,G5);
    sixteenthdouble(E4,G5);
    ///
    eighthdouble(Eb4,G5);//
    eighthdouble(Eb3,G5);

    sixteenthdouble(Eb3,G5);//
    sixteenthdouble(Eb3,G5);
    sixteenthdouble(Db4,G5);
    sixteenthdouble(Eb4,G5);

    sixteenthnote(D4);//
    eighthnote(D3);
    sixteenthnote(D3);

    sixteenthnote(D3);//
    eighthnotel(D3);
    sixteenthnote(D3);
    
    //

    eighthdouble(Eb4,Eb5);//
    eighthdouble(Eb3,Eb5);

    sixteenthdouble(Eb3,D6);//
    eighthdouble(Eb3,D6);
    sixteenthdouble(Eb3,D6);

    eighthdouble(Eb3,B5);//
    sixteenthdouble(Eb3,B5);
    sixteenthdouble(Eb3,B5);

    eighthdouble(Eb3,Bb5);//
    sixteenthdouble(D4,Bb5);
    sixteenthdouble(E4,Bb5);
    ///
    eighthdouble(Eb4,Eb6);//
    eighthdouble(Eb3,Eb6);

    sixteenthdouble(Eb3,D6);//
    eighthdouble(Eb3,D6);
    sixteenthdouble(Eb3,D6);

    eighthdouble(E3,B5);//
    sixteenthdouble(E3,B5);
    sixteenthdouble(E4,B5);

    eighthdouble(E4,E6);//
    eighthdouble(F3,E6);
    ///
    eighthdouble(Eb4,Eb6);//
    eighthdouble(Eb3,Eb6);

    sixteenthdouble(Eb3,Eb6);//
    eighthdouble(Eb3,Eb6);
    sixteenthdouble(Eb3,Eb6);

    eighthdouble(Eb3,Eb6);//
    sixteenthdouble(Eb3,Eb6);
    sixteenthdouble(Eb3,Eb6);

    eighthdouble(Eb3,Eb6);//
    sixteenthdouble(D4,Eb6);
    sixteenthdouble(E4,Eb6);
    ///
    eighthdouble(Eb4,Eb6);//
    eighthdouble(Eb3,Eb6);

    sixteenthdouble(Eb3,Eb6);//
    sixteenthdouble(Eb3,Eb6);
    sixteenthdouble(Db4,Eb6);
    sixteenthdouble(Eb4,Eb6);

    sixteenthnote(D4);//
    eighthnote(D3);
    sixteenthnote(D3);

    sixteenthnote(D3);//
    eighthnotel(D3);
    sixteenthnote(D3);
}
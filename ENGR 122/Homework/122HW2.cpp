int pinout = 8;

int tempo = 102;

int timeunit = (60.0/tempo)*1000.0;

float whole = timeunit*4;
float dwhole = whole*1.5;
float half = timeunit*2;
float dhalf = half*1.5;
float quarter = timeunit;
float dquarter = quarter*1.5;
float eighth = timeunit/2;
float deighth = eighth*1.5;
float sixteenth = timeunit/4;
float dsixteenth = sixteenth*1.5;

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

#define PRINT(x) ", " << #x << ": " << x

void setup(){
    Serial.begin(9600);
    pinMode(pinout, OUTPUT);
    Serial.println(timeunit);
}

void note(int length, float note1=0, float note2=0, float notebend1=0, float notebend2=0){
    Serial.print(PRINT(note1));Serial.print(" -> ");Serial.print(notebend1);Serial.print(" ");
    Serial.print(note2);Serial.print(" -> ");Serial.print(notebend2);
    Serial.print(" Length = ");Serial.println(length);

    //rest
    if (note1 == 0.00){
        delay(length);
    }

    //single note
    else if (notebend1 == 0.00 && note2 == 0.00){
        tone(pinout, note1);
        delay((length)-(timeunit/8));
        noTone(pinout); 
        delay(timeunit/8);
    }

    //double note
    else if (notebend1 == 0.00 && notebend2 == 0.00){
        for (float i = 0 ; i < (length/timeunit)*32 ; i++){
            tone(pinout, note1);
            delay(timeunit/16);
            tone(pinout, note2);
            delay(timeunit/16);
        }
        noTone(pinout);
    }

    //bend note
    else if (note2 == 0.00){
        for (float f = note1 ; f < notebend1 ; f = f + ((notebend1-note1)/(length/timeunit))/32){
            tone(pinout, f);
            delay(timeunit/32);
        }
        noTone(pinout);
    }
}


void loop(){
    note(half, C4, 0, C5);
    //The_Only_Thing_They_Fear_Is_You();
}

//Songs
void The_Only_Thing_They_Fear_Is_You(){
    //The Only Thing They Fear Is You - Mick Gordon
    //Doom on a piezo speaker
    int tempo = 102;

    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(eighth,Eb3);
    note(sixteenth,Eb3);

    note(deighth,Eb3);

    note(sixteenth,D4);
    note(sixteenth,E4);
    ///
    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(deighth,E3);

    note(deighth,E4);

    note(eighth,F3);
    ///
    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(eighth,Eb3);
    note(sixteenth,Eb3);

    note(deighth,Eb3);

    note(sixteenth,D4);
    note(sixteenth,E4);
    ///
    note(eighth,Eb4);//
    note(eighth,Eb3);

    note(sixteenth,Eb3);//
    note(sixteenth,Eb3);
    note(sixteenth,Db4);
    note(sixteenth,Eb4);

    note(sixteenth,D4);//
    note(eighth,D3);
    note(sixteenth,D3);

    note(sixteenth,D3);//
    note(deighth,D3);

    ///

    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(eighth,Eb3);
    note(sixteenth,Eb3);

    note(deighth,Eb3);

    note(sixteenth,D4);
    note(sixteenth,E4);
    ///
    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(deighth,E3);

    note(deighth,E4);

    note(eighth,F3);
    ///
    note(eighth,Eb4);

    note(deighth,Eb3);

    note(deighth,Eb3);

    note(eighth,Eb3);
    note(sixteenth,Eb3);

    note(deighth,Eb3);

    note(sixteenth,D4);
    note(sixteenth,E4);
    ///
    note(eighth,Eb4);

    note(deighth,Eb3);

    note(sixteenth,Eb3);
    note(sixteenth,Db4);
    note(sixteenth,Eb4);
    note(sixteenth,D4);

    note(sixteenth,D3);
    note(sixteenth);

    note(sixteenth,D3);
    note(eighth);
    
    note(sixteenth,D3);
    note(sixteenth);

    ///

    note(eighth,Eb4,Eb5);//
    note(eighth,Eb3,Eb5);

    note(sixteenth,Eb3,D6);//
    note(eighth,Eb3,D6);
    note(sixteenth,Eb3,D6);

    note(eighth,Eb3,B5);//
    note(sixteenth,Eb3,B5);
    note(sixteenth,Eb3,B5);

    note(eighth,Eb3,Bb5);//
    note(sixteenth,D4,Bb5);
    note(sixteenth,E4,Bb5);
    ///
    note(eighth,Eb4,Eb6);//
    note(eighth,Eb3,Eb6);

    note(sixteenth,Eb3,D6);//
    note(eighth,Eb3,D6);
    note(sixteenth,Eb3,D6);

    note(eighth,E3,B5);//
    note(sixteenth,E3,B5);
    note(sixteenth,E4,B5);

    note(eighth,E4,Bb5);//
    note(eighth,F3,Bb5);
    ///
    note(eighth,Eb4,Ab5);//
    note(eighth,Eb3,Ab5);

    note(sixteenth,Eb3,G5);//
    note(eighth,Eb3,G5);
    note(sixteenth,Eb3,G5);

    note(eighth,Eb3,G5);//
    note(sixteenth,Eb3,G5);
    note(sixteenth,Eb3,G5);

    note(eighth,Eb3,G5);//
    note(sixteenth,D4,G5);
    note(sixteenth,E4,G5);
    ///
    note(eighth,Eb4,G5);//
    note(eighth,Eb3,G5);

    note(sixteenth,Eb3,G5);//
    note(sixteenth,Eb3,G5);
    note(sixteenth,Db4,G5);
    note(sixteenth,Eb4,G5);

    note(sixteenth,D4);//
    note(eighth,D3);
    note(sixteenth,D3);

    note(sixteenth,D3);//
    note(deighth,D3);
    
    //

    note(eighth,Eb4,Eb5);//
    note(eighth,Eb3,Eb5);

    note(sixteenth,Eb3,D6);//
    note(eighth,Eb3,D6);
    note(sixteenth,Eb3,D6);

    note(eighth,Eb3,B5);//
    note(sixteenth,Eb3,B5);
    note(sixteenth,Eb3,B5);

    note(eighth,Eb3,Bb5);//
    note(sixteenth,D4,Bb5);
    note(sixteenth,E4,Bb5);
    ///
    note(eighth,Eb4,Eb6);//
    note(eighth,Eb3,Eb6);

    note(sixteenth,Eb3,D6);//
    note(eighth,Eb3,D6);
    note(sixteenth,Eb3,D6);

    note(eighth,E3,B5);//
    note(sixteenth,E3,B5);
    note(sixteenth,E4,B5);

    note(eighth,E4,E6);//
    note(eighth,F3,E6);
    ///
    note(eighth,Eb4,Eb6);//
    note(eighth,Eb3,Eb6);

    note(sixteenth,Eb3,Eb6);//
    note(eighth,Eb3,Eb6);
    note(sixteenth,Eb3,Eb6);

    note(eighth,Eb3,Eb6);//
    note(sixteenth,Eb3,Eb6);
    note(sixteenth,Eb3,Eb6);

    note(eighth,Eb3,Eb6);//
    note(sixteenth,D4,Eb6);
    note(sixteenth,E4,Eb6);
    ///
    note(eighth,Eb4,Eb6);//
    note(eighth,Eb3,Eb6);

    note(sixteenth,Eb3,Eb6);//
    note(sixteenth,Eb3,Eb6);
    note(sixteenth,Db4,Eb6);
    note(sixteenth,Eb4,Eb6);

    note(sixteenth,D4);//
    note(eighth,D3);
    note(sixteenth,D3);

    note(sixteenth,D3);//
    note(deighth,D3);
}
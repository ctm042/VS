#include <Arduino.h>
#include <Servo.h>

// status LEDs
int led1 = 6 ;
int led2 = 5 ;
int led3 = 3 ;

// input pin
int pinIn = 2 ;
int AnaIn = 0 ;

// servo pins
int pinL = 11 ;
int pinR = 10 ;

int counter = 1 ;
int selcounter = 0 ;
int stopval = 1500 ;

Servo ServoL ;
Servo ServoR ;



void setup() {
  Serial.begin(9600);
  Serial.println("setup");

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  pinMode(pinIn, INPUT);

  pinMode(pinL, OUTPUT);
  pinMode(pinR, OUTPUT);

  ServoL.attach(pinL) ;
  ServoR.attach(pinR) ;

  digitalWrite(led1, HIGH);
}

// TOOLS
// speed correction
int LSC(int percent) {
  return 1500+(500*((float)percent/100));
}
int RSC(int percent) {
  return 1500-(420*((float)percent/100));
}

// press detection
int pressdet() {
  if(digitalRead(pinIn)==1) {
    return 1 ;
  }
  return 0 ;
}



// ACTIONS
// go(leftspeed, rightspeed, time)
void go(int ls, int rs, int t) {
  if(pressdet()==0) {
    ServoL.writeMicroseconds(LSC(ls)) ;
    ServoR.writeMicroseconds(RSC(rs)) ;
    delay(t);
    ServoL.writeMicroseconds(stopval) ;
    ServoR.writeMicroseconds(stopval) ;
  }
}
// sets speed of servos and excecutes next command after t delay
// gofree(leftspeed, rightspeed, time)
void gofree(int ls, int rs, int t) {
  if(pressdet()==0) {
    ServoL.writeMicroseconds(LSC(ls)) ;
    ServoR.writeMicroseconds(RSC(rs)) ;
    delay(t);
  }
}
// stops servos and waits t delay
// stop(time)
void stop(int t) {
  if(pressdet()==0) {
    ServoL.writeMicroseconds(stopval) ;
    ServoR.writeMicroseconds(stopval) ;
    delay(t);
  }
}
// turns on led for t time
// blink(bool1, bool2, bool3, time)
void blink(bool b1, bool b2, bool b3, int t) {
  if(pressdet()==0) {
    if(b1) {
      digitalWrite(led1, HIGH);
      Serial.println("1");
    }
    else{
      digitalWrite(led1, LOW);
    }
    if(b2) {
      digitalWrite(led2, HIGH);
      Serial.println("2");
    }
    else{
      digitalWrite(led2, LOW);
    }
    if(b3) {
      digitalWrite(led3, HIGH);
      Serial.println("3");
    }
    else{
      digitalWrite(led3, LOW);
    }
    delay(t);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  }
}
// used for selection indication
void led_on(int counter) {
  digitalWrite(led1, LOW) ; 
  digitalWrite(led2, LOW) ; 
  digitalWrite(led3, LOW) ;
  if (counter == 1) {
    digitalWrite(led1, HIGH) ;
    Serial.println("1 selected");
  }
  else if (counter == 2) {
    digitalWrite(led2, HIGH) ;
    Serial.println("2 selected");
  }
  else if (counter == 3) {
    digitalWrite(led3, HIGH) ;
    Serial.println("3 selected");
  }
}


// PROGRAMS
void program1() {
  // testing puposes
  gofree(100,100,1000);
  gofree(90,90,1000);
  gofree(80,80,1000);
  gofree(70,70,1000);
  gofree(60,60,1000);
  gofree(50,50,1000);
  gofree(40,40,1000);
  gofree(30,30,1000);
  gofree(20,20,1000);
  gofree(10,10,1000);
}
void program2() {
  // ### CHALLENGE 2 ### //
  // ### FIGURE-8 ### //
  gofree(50,50,2000);
  gofree(20,60,3000);
  gofree(50,50,4000);
  gofree(60,20,2400);
  gofree(50,50,2000);
  stop(100);
  // refine
}
void program3() {
  // ### CHALLENGE 3 ### //
  // ### PATTERN ### //

  // timings
  // 6th = 80
  // 3rd = 160
  // 8th = 240
  // qtr = 480
  // hlf = 960

  // alter delays in pattern portion
  int timescale = 1 ;
  
  // enable movement pattern
  bool movpat = false;

  // move pattern
  // 20th Century Fox Fanfare
  if(movpat){
    gofree(80,80,200*timescale);
    stop(40*timescale);
    gofree(80,80,200*timescale);
    stop(40*timescale);
    stop(480*timescale);
    gofree(80,80,200*timescale);
    stop(40*timescale);
    gofree(80,80,200*timescale);
    stop(40*timescale);
    stop(480*timescale);
    //
    gofree(-80,80,960*timescale);
    stop(40*timescale);
    gofree(80,80,200*timescale);
    stop(40*timescale);
    gofree(80,80,200*timescale);
    stop(40*timescale);
    stop(480*timescale);
    //
    gofree(80,80,280*timescale);
    stop(40*timescale);
    gofree(80,80,40*timescale);
    stop(40*timescale);
    gofree(80,80,40*timescale);
    stop(40*timescale);
    gofree(80,80,440*timescale);
    stop(40*timescale);
    stop(320*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    //
    gofree(80,80,280*timescale);
    stop(40*timescale);
    gofree(80,80,40*timescale);
    stop(40*timescale);
    gofree(80,80,40*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    //
    gofree(80,80,280*timescale);
    stop(40*timescale);
    gofree(80,80,120*timescale);
    stop(40*timescale);
    gofree(80,80,440*timescale);
    stop(40*timescale);
    stop(480*timescale);
    gofree(0,50,120*timescale);
    stop(40*timescale);
    gofree(0,60,120*timescale);
    stop(40*timescale);
    gofree(0,70,120*timescale);
    stop(40*timescale);
    //
    gofree(0,80,440*timescale);
    stop(40*timescale);
    gofree(50,0,280*timescale);
    stop(40*timescale);
    gofree(50,0,120*timescale);
    stop(40*timescale);
    gofree(50,0,440*timescale);
    stop(40*timescale);
    gofree(0,60,120*timescale);
    stop(40*timescale);
    gofree(0,70,120*timescale);
    stop(40*timescale);
    gofree(0,80,120*timescale);
    stop(40);
    //
    gofree(0,90,440*timescale);
    stop(40*timescale);
    gofree(50,0,280*timescale);
    stop(40*timescale);
    gofree(50,0,120*timescale);
    stop(40*timescale);
    gofree(50,0,440*timescale);
    stop(40*timescale);
    gofree(0,70,120*1.2*timescale);
    stop(40*1.2*timescale);
    gofree(0,80,120*1.2*timescale);
    stop(40*1.2*timescale);
    gofree(0,90,120*1.2*timescale);
    stop(40*1.2*timescale);
    //
    gofree(0,100,440*1.2*timescale);
    stop(40*1.2*timescale);
    gofree(0,70,120*1.2*timescale);
    stop(40*1.2*timescale);
    gofree(0,50,120*1.2*timescale);
    stop(40*1.2*timescale);
    gofree(0,70,120*1.2*timescale);
    stop(40*1.2*timescale);
    //
    gofree(50,80,960*1.2*timescale);
    stop(40*timescale);
    go(50,0,240*1.2*timescale);
  }


  // blink pattern
  // 4:5:6 polyrhythm

  // how long in ms leds turn on in blink, scales with timescale2
  int blinkdur2 = 30 ;

  // alters delays in blink portion
  int timescale2 = 3 ;

  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  
  while(pressdet()==0) {
    blink(true,true,true,blinkdur2*timescale2);
    delay(166.66*timescale2-blinkdur2);
    blink(false,false,true,blinkdur2*timescale2);
    delay(33.33*timescale2-blinkdur2);
    blink(false,true,false,blinkdur2*timescale2);
    delay(50*timescale2-blinkdur2);
    blink(true,false,false,blinkdur2*timescale2);
    delay(83.33*timescale2-blinkdur2);
    blink(false,false,true,blinkdur2*timescale2);
    delay(66.66*timescale2-blinkdur2);
    blink(false,true,false,blinkdur2*timescale2);
    delay(100*timescale2-blinkdur2);
    blink(true,false,true,blinkdur2*timescale2);
    delay(100*timescale2-blinkdur2);
    blink(false,true,false,blinkdur2*timescale2);
    delay(66.66*timescale2-blinkdur2);
    blink(false,false,true,blinkdur2*timescale2);
    delay(83.33*timescale2-blinkdur2);
    blink(true,false,false,blinkdur2*timescale2);
    delay(50*timescale2-blinkdur2);
    blink(false,true,false,blinkdur2*timescale2);
    delay(33.33*timescale2-blinkdur2);
    blink(false,false,true,blinkdur2*timescale2);
    delay(166.66*timescale2-blinkdur2);
    digitalWrite(led1,HIGH);
  }
}
void program4() {
  // ### CHALLENGE 4 ### //
  // ### OBSTACLE ### //
  // write in class
}
void program5() {
  // ### CHALLENGE 5 ### //
  // ### LIGHT DETECTION ### //
  // average ambient light in room is 910
  while(pressdet()==0) {
    Serial.println(analogRead(AnaIn));
    //under ambient
    if((analogRead(AnaIn)<900)) {
      led_on(2);
      gofree(-40,-40, 50);
    }
    //at ambient
    else if((analogRead(AnaIn)>=900)&&(analogRead(AnaIn)<920)) {
      led_on(1);
      gofree(60, 60, 50);
    }
    // above ambient
    else{
      led_on(3);
      gofree(60, -60, 50);
    }
  }  
}
void program6() {
    // extra
}




// 'menu' for selecting actions and programs
void select() {
  stop(0);
  if (digitalRead(pinIn)==1) {
  // press duration
    while (digitalRead(pinIn)==1) {
      selcounter++ ; 
      delay(10) ;
    }
  // cycle LED counter
    if (selcounter < 100) {
      counter++ ;
      if(counter == 4) {
        counter = 1 ;
        }
      led_on(counter);
    }
  // program execution 1-3
    if (selcounter >= 100 && selcounter < 300) {
      if(counter==1) {
        Serial.println("Starting prog 1");
        delay(250);
        program1();
        }
      else if (counter==2) {
        Serial.println("Starting prog 2");
        delay(250);
        program2();
      }
      else {
        Serial.println("Starting prog 3");
        delay(250);
        program3();
      }
      led_on(counter);
    }
  // program execution 4-6
    if (selcounter >= 300) {
      if (counter == 1) {
        Serial.println("Starting prog 4");
        delay(250);
        program4();
      }
      if (counter == 2) {
        Serial.println("Starting prog 5");
        delay(250);
        program5();
      }
      if (counter == 3) {
        Serial.println("Starting prog 6");
        delay(250);
        program6();
      }
    }
    selcounter = 0 ;
  }
}

//main loop
void loop() {
  select() ;
}
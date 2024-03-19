// Pin to Index lookup

// Columns 1-13 (0-12)

// Rows 1-4 (0-3)
int ROWS = 4;
int COLUMNS = 13;

// set row pins
int[] rows = {1,2,3,4};

// set column
int[] columns = {1,2,3,4,5,6,7,8,9,10,11,12,13};



string keymap[ROWS][COLUMNS] = {
    {"M1",    "M2", "M3", "M4", "M5", "M6", "M7",  "R1", "R2", "R3",  "",  "",  "",}
    {"Esc",   "Q",  "W",  "E",  "R",  "T",  "Fn1", "Y",  "U",  "I",   "O", "P", "Return"},
    {"Tab",   "A",  "S",  "D",  "F",  "G",  "Fn2", "H",  "K",  "K",   "L", ";", "Backspace"},
    {"Shift", "Z",  "X",  "C",  "V",  "B",  " ",   "N",  "M",  ".",   ",", "/", "Mod"}
};







void setup(){
    // configure rows
    for(int row = 0; row < rows.length; row++){
        pinMode(row, OUTPUT);
    }
    // configure columns
    for(int column = 0; column < columns.length; column++){
        pinMode(column, INPUT);
    }
}

void loop(){
    getPressedKey()
}

int[] get(){
    if ()
}

int* getCoord(){
    for (int row = 0; row < ROWS; row++){
        digitalWrite(row, HIGH);
        for (int column = 0; column < COLUMNS; column++){
            if (digitalRead(column) == HIGH){
                return {column, row};
            }
        } 
        digitalWrite(row, LOW);
    }
    return {-1,-1};
}
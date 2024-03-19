class Fraction {
    // instance variables
    private int numerator;
    private int denominator;

    // default constructor
    public Fraction(){
        numerator = 0;
        denominator = 1;
    }

    // second constructor (allws for inputs when creating a fraction object)
    public Fraction(int n, int d){
        numerator = n;
        if(d != 0)
            denominator = d;
        else
            denominator = 1;
    }

    // accessor(getter) for the numerator
    public int getNumerator(){
        return numerator;
    }

    // mutator(setter) for the numerator
    public void setNumerator(int value){
        numerator = value;
    }

    // accessor(getter) for the denominator
    public int getDenominator(){
        return denominator;
    }

    // mutator(setter) for the denominator
    public void setDenominator(int value){
        if(value != 0)
            denominator = value;
    }

    // addition of two fractions
    public Fraction add(Fraction f){
        Fraction sum = new Fraction();
        sum.numerator = numerator * f.denominator + denominator * f.numerator;
        sum.denominator = denominator * f.denominator;
        return sum;
    }
    // subtraction of two fractions
    public Fraction sub(Fraction f){
        Fraction neg_f = new Fraction(f.numerator * -1, f.denominator);
        Fraction diff = this.add(neg_f);
        return diff;
        
    }

    // string representation of a Fraction
    public String toString(){
        return numerator + "/" + denominator;
    }
}

class FractionTest{
    public static void main(String[] args){
        Fraction f1 = new Fraction(1, 2); // creates a fraction object f
        Fraction f2 = new Fraction();
        System.out.println(f1); 
        System.out.println(f2);
    }
}
abstract class Shape {
    protected int length;
    protected int width;

    // constructor
    public Shape(int l, int w){
        length = l;
        width = w;
    }

    // draw the shape
    public void draw(){
        for(int i = 0; i < width; i++){
            for(int j = 0; j < length; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    // abstract method
    //abstract void area();

}

class Rectangle extends Shape{
    // constructor
    public Rectangle(int l, int w){
        super(l, w);
    }
}

class Triangle extends Shape{
    public Triangle(int s){
        super(s, s);
    }

    public void draw(){
        for(int i = 0; i < width; i++){
            for(int j = 0; j < width - i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}

class ShapeTest{
    public static void main(String[] args){
        Rectangle r = new Rectangle(10, 4);
        Triangle t = new Triangle(7);

        r.draw();
        System.out.println();
        t.draw();
    }
}

class Fruit {
    private String name;
    Fruit(String name) {
      this.name = name;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
  }

  class Apple extends Fruit {
    public Apple(){
      super("Apple");
    }
  }
  
  public class Main {
    public static void main(String[] args) {
      Fruit fruit = new Fruit("Banana");
      Apple apple = new Apple();
      System.out.println(apple.getName());
    }
  }
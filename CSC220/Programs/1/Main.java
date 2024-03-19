/**
 * Name: Caleb Matherne
 * Date: 9/17/2022
 * Description: Program 1: Java vs Python
 */
 
/** <INSERT BRIEF DESCRIPTION OF CLASS> */
/** In the Person class, name, age, and isStudent are all declared
 *  and instantiated in the constructor. The constructor only takes
 *  name and age as parameters and sets isStudent as false. The
 *  birthday method is created in which the object's age is increased
 *  by 1. The toString method is created to return a string when
 *  System.out.println() is used. 
*/
class Person {
  //instance variables
  String name;
  int age;
  boolean isStudent;

  //constructor
  Person(String name, int age) {
    this.name = name;
    this.age = age;
    this.isStudent = false;
  }
  
  public void birthday(){
    this.age += 1;
  }

  public String toString(){
    String result = "";
    result += this.name + " is ";
    if (this.isStudent){
      result += "a student ";
    }
    else {
      result += "not a student ";
    }
    result += "and is " + String.valueOf(this.age) + " years old";
    return result;
  }
}

/** <INSERT BRIEF DESCRIPTION OF CLASS> */
/** The constructor of the Student class passes name and age to
 *  the super class (Person) to be instantiated by its constructor.
 *  It then sets isStudent to true.
 */
class Student extends Person {
  //constructor
  public Student(String name, int age){
    //uses parent's constructor
    super(name, age);
    this.isStudent = true;
  }
}

/** Main class - contains entry point */
public class Main {
  public static void main(String[] args) {
    Student student = new Student("Bob", 20);
    System.out.println(student);
    student.birthday();
    System.out.println(student);

    Person person = new Person("Rob", 22);
    System.out.println(person);
  }
}

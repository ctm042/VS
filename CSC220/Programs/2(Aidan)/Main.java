/**
 * Name: Aidan Schardien
 * Date: 9/26/22
 * Description:  Program 2, introducing people class
 */
// Create People class here
class People{

  private Person[] group;
  private int index;

  // constructor baybee
  public People(){
    this.group = new Person[5];
    this.index = 0;
  }

  public boolean addPerson(Person p){
    // implements a counting system that will count 
    // how many spaces in the array, group, are occupied
    int count = 0;
    for(Person person : this.group) {
        if(person != null) {
            count++;
    }
  }

  // checks if the count (aka the space used in the array) 
  // to see if it is equal to 5

  if(count == 5){
      return false;
    }else{
      return true;
    }
  }

  public Person findPersonByName(String name){
    for (Person index : this.group){
        if(index.name.equals(name)){
            return index;
        }
    }
    return null;
  }

  public Person findPersonByAge(int age){
    for (Person index : this.group){
        if (index.age == (age)){
            return index;
        }
    }
    return null;
  }
}


// Put Person class from last assignment here (Student class is not needed)
class Person {
  /** initializes int age, String name, and the boolean isStudent */
  int age;
  String name;
  boolean isStudent;

  // constructor
  public Person(String name, int age) {
    this.age = age;
    this.name = name;
    this.isStudent = false;
  }
 /** Birthday
 * when called, takes the integer age and increases it by one (1)
 */
  public void birthday(){
    this.age += 1;
  }

  /** Magic string function
   * tests if the isStudent variable is true, 
   * determining the result of the string returned being a student or not, 
   * as well as including the age of said student
   */
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


/** Main class - contains entry point */
// DO NOT MODIFY ANY CODE BELOW
public class Main {
  public static void main(String[] args) {
    // instantiate a new People object
    People people = new People();

    // add some Person objects
    boolean addedAllPeople = true;
    addedAllPeople &= people.addPerson(new Person("Eleanor",    38));
    addedAllPeople &= people.addPerson(new Person("Tahani",     33));
    addedAllPeople &= people.addPerson(new Person("Chidi",      39));
    addedAllPeople &= people.addPerson(new Person("Jason",      31));
    addedAllPeople &= people.addPerson(new Person("Michael", 20000));
    addedAllPeople &= people.addPerson(new Person("Janet",   10000));
    
    // create pointers to two Persons
    Person p1;
    Person p2;
    
    // initialize them with the results of our searches
    p1 = people.findPersonByName("Chidi");
    p2 = people.findPersonByAge(10000);
    
    // check if our results are correct
    Mysterious.checkAnswer(addedAllPeople, p1, p2);
  }
}

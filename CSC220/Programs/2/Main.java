/**
 * Name: Caleb Matherne
 * Date: 9/23/2022
 * Description:  Program #2 (Java Arrays)
 *               "The Good Place is the best show ever"
 *               Never watched it but I heard it was pretty good.
 */
// Create People class here

/**
 * Groups objects from the Person class.
 */
class People {

  public Person[] group;
  private int index;

  // Constructor
  public People(){
    this.group = new Person[5];
    this.index = 0;
  }

  /**
   * Checks if 5 Person object have been created. If true, adds Person object to group array.
   * @param p
   * @return
   */
  public boolean addPerson(Person p) {
    if (this.index<5) {
      this.group[this.index] = p;
      this.index++;
      return true;
    }
    return false;
  }

  /**
   * Returns a Person object that has the given name.
   * @param name
   * @return
   */
  public Person findPersonByName(String name) {
    for (Person i : this.group) {
      if (i.name.equals(name)) return i;
    }
    return null;
  }

  /**
   * Returns a Person object that has the given age.
   * @param age
   * @return
   */
  public Person findPersonByAge(int age) {
    for (Person i : this.group) {
      if (i.age==age) return i;
    }
    return null;
  }
}



// Put Person class from last assignment here (Student class is not needed)

/**
   * Creates person objects that have name and age properties.
   * @param name
   * @param age
   */
class Person {

  // Instance variables
  String name;
  int age;
  boolean isStudent;

  // Constructor
  Person(String name, int age) {
    this.name = name;
    this.age = age;
    this.isStudent = false;
  }
  
  /**
   * Increments the person object's age by 1.
   */
  public void birthday(){
    this.age += 1;
  }

  /**
   * Prints information in a set format.
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

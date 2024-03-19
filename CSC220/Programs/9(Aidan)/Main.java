public class Main {
    public static void main(String[] args) {
        Dictionary<String, Integer> dict = new Dictionary<>();

        dict.insert("Bob", 50);
        dict.insert("Bill", 120);
        dict.insert("Roger", 80);
        dict.insert("Kevin", 350);
        dict.insert("Jerry", 65);
        dict.insert("Liam", 500);
        
        System.out.println("Bob makes $" + dict.search("Bob") + "k a year");
        System.out.println("Bill makes $" + dict.search("Bill") + "k a year");
        System.out.println("Roger makes $" + dict.search("Roger") + "k a year");
        System.out.println("Kevin makes $" + dict.search("Kevin") + "k a year");
        System.out.println("Jerry makes $" + dict.search("Jerry") + "k a year");
        System.out.println("Liam makes $" + dict.search("Liam") + "k a year");
        System.out.println("");

        dict.delete("Bob");
        dict.delete("Roger");
        dict.delete("Jerry");

        dict.insert("Liam", 650);
        
        if(dict.search("Bob") == null) {
            System.out.println("Bob got fired");
        } else {
            System.out.println("Bob makes $" + dict.search("Bob") + "k a year");
        }

        if(dict.search("Bill") == null) {
            System.out.println("Bill got fired");
        } else {
            System.out.println("Bill makes $" + dict.search("Bill") + "k a year");
        }
        
        if(dict.search("Roger") == null) {
            System.out.println("Roger got fired");
        } else {
            System.out.println("Roger makes $" + dict.search("Roger") + "k a year");
        }
        
        if(dict.search("Kevin") == null) {
            System.out.println("Kevin got fired");
        } else {
            System.out.println("Kevin makes $" + dict.search("Kevin") + "k a year");
        }
        
        if(dict.search("Jerry") == null) {
            System.out.println("Jerry got fired");
        } else {
            System.out.println("Jerry makes $" + dict.search("Jerry") + "k a year");
        }
        
        if(dict.search("Liam") == null) {
            System.out.println("Liam got fired");
        } else {
            System.out.println("Liam makes $" + dict.search("Liam") + "k a year");
        }
        
    }
}

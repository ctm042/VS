public class Main {
    public static void main(String[] args){
        Dictionary<String, Integer> dict = new Dictionary<>();

        String[] names = {"Bob","Bill","Roger","Kevin","Jerry","Liam"};

        // hire some people
        dict.insert(names[0], 50);
        dict.insert(names[1], 120);
        dict.insert(names[2], 80);
        dict.insert(names[3], 350);
        dict.insert(names[4], 65);
        dict.insert(names[5], 500);

        // print
        for (String name : names){
            if (dict.search(name) == null) System.out.println(name + " got fired");
            else System.out.println(name + " makes $" + dict.search(name) + "k a year");
        }

        // fire some people
        dict.delete("Bob");
        dict.delete("Roger");
        dict.delete("Jerry");

        // liam got a raise! good job liam!
        dict.insert("Liam", 650);


        // print
        System.out.println();
        for (String name : names){
            if (dict.search(name) == null) System.out.println(name + " got fired");
            else System.out.println(name + " makes $" + dict.search(name) + "k a year");
        }
    }
}

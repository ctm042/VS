/* I know that my code is disgusting. Literal definition of spaghetti code. Sorry for that
 * I know that it can probably be done much simpler and faster, but I'll have to rewrite everything.
 * I could've but I spent too much time trying to decypher what I wrote. Attempting to switch parts 
 * out for better code only broke more things, which wasted more of my time trying to fix. So I
 * just decided to settle on code that (somehow) works. 
 * I'm disapointed that this is my last assignment for the class. I would have liked to go all out on 
 * the last assignment of the course, but I shouldve probably followed the lecture more closely.
 * 
 * Anyways, I learned a lot from the class. Probably my favorite class so far. I really enjoyed
 * your enthusiasm about whatever topic you were teaching. Very few professors are like that.
 * I'm sad that I wont be taking your class next quarter, but you'll be my first pick if you're
 * teaching a class I need!
 * 
 * (Please have mercy when grading my sloppy code bc of my heartfelt message <3)
 * (Just kidding, give me no bias)
 * (Unless?)
 * (Jk)
 *
 * 
 *
 * (Unless...)
*/


public class Dictionary<K,V> {
    // Declare class attributes
    int capacity;
    KeyValuePair<K,V>[] table;
    private final KeyValuePair<K,V> DELETED;

    public Dictionary(){
        // Initialize class attributes
        capacity = 2;
        table = new KeyValuePair[capacity];
        DELETED = new KeyValuePair<K,V>(null, null);
    }

    /**
     * Adds the specified key and value into the dictaonary.
     * @param key
     * @param value
     */
    public void insert(K key, V value){
        // if in table
        if (search(key) != null) {table[getindex(key)].setValue(value);}

        // if not in table
        else {
            int index = hash(key);
            int attempt = 1;
            while (attempt <= capacity){
                if (table[index] == null || table[index] == DELETED) {
                    table[index] = new KeyValuePair<K,V>(key, value);
                    break;
                }
                else {
                    index++; index %= capacity;
                    attempt++;
                }
                
            }

            // double table size if cant find spot (full)
            if (attempt >= capacity){
                capacity *= 2;
                KeyValuePair<K,V>[] temptable = table.clone();
                table = new KeyValuePair[capacity];
                for (int i = 0; i < temptable.length; i++) {
                    insert(temptable[i].getKey(),temptable[i].getValue());
                }
                insert(key, value);

            }
        }
    }

    /**
     * Searches for the value that belongs to the given key. Returns null if not found.
     * @param key
     * @return
     */
    public V search(K key){
        int index = hash(key);
        int attempt = 1;
        if (table[index] == null) return null;
        while (table[index].getKey() != key){
            attempt++; if (attempt >= capacity) return null;
            index++; index %= capacity;
            while (table[index] == null) {
                attempt++; if (attempt >= capacity) return null;
                index++; index %= capacity;
            }
            
        }
        return table[index].getValue();
    }

    /**
     * Deletes the key and value from the dictionary.
     * @param key
     */
    public void delete(K key){
        if (search(key) == null) return;
        table[getindex(key)] = DELETED;
    }

    /**
     * Map integers of a large range into a smaller range.
     * @param key
     * @param value
     */
    private int hash(K key){
<<<<<<< HEAD
        return key.hashCode() % capacity;
=======
        return key.hashCode() % capacity; 
>>>>>>> cc8a9a48a7250a255a678834d8484dd1172e56ee
    }    

    private int getindex(K key){
        int index = hash(key);
        int attempt = 1;
        while (table[index] == null) {
            attempt++; if (attempt >= capacity) return -1;
            index++; index %= capacity;
        }
        while (true) {
            if (table[index].getKey() == key) {return index;}
            attempt++; if (attempt >=capacity){return -1;}
            index++; index %= capacity;
            while (table[index] == null) {
                attempt++; if (attempt >=capacity){return -1;}
                index++; index %= capacity;
            }
        }
    }
}

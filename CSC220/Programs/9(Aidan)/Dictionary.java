public class Dictionary<K, V> {

    int size;
    private KeyValuePair<K, V>[] kvp;
    private final KeyValuePair<K, V> DELETED;

    public Dictionary(){
        size = 7;
        DELETED = new KeyValuePair<K, V>(null, null);
        kvp = (KeyValuePair<K,V>[]) new KeyValuePair[size];
    }

    private int prehash(K key) {
        return key.hashCode() % size;
    }

    private int hash(int p, int attempt) {
        return (p + (attempt - 1)) % size;
    }

    public void insert(K key, V value) {
        int m = size;
        int p = prehash(key);
        int attempt = 1;

        while (attempt < m) {
            int index = hash(p, attempt);
            if (kvp[index] == null || kvp[index] == DELETED) {
                kvp[index] = new KeyValuePair<K, V>(key, value);
            } else if (kvp[index].getKey() == key) {
                kvp[index].setValue(value);
            }
        }
    }

    public void delete(K key) {
        int p = prehash(key);
        int attempt = 1;

        for (int index = hash(p, attempt); index < size; index ++) {
            if(kvp[index] == key){
                kvp[index] = DELETED;
            }
        }
    }

    public V search(K key) {
        int p = prehash(key);
        int attempt = 1;

        for(int index = hash(p, attempt); index < size; index++) {
            if (kvp[index] == key) {
                return kvp[index].getValue();    
            }
        }

        return null;
    }
}
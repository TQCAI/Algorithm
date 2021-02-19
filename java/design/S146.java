package design;

import java.util.LinkedHashMap;

class LRUCache {
    int capacity;
    LinkedHashMap<Integer, Integer> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new LinkedHashMap<>();
    }

    public int makeRecently(int key) {
        int val = cache.get(key);
        cache.remove(key);
        cache.put(key, val);
        return val;
    }

    public void addRecently(int key, int value) {
        cache.put(key, value);
    }

    public void removeLeastRecently() {
        int oldestKey = cache.keySet().iterator().next();
        cache.remove(oldestKey);
    }

    public void removeKey(int key) {
        cache.remove(key);
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            return makeRecently(key);
        }
        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            removeKey(key);
            cache.put(key, value);
        } else {
            if (cache.size() == capacity)
                removeLeastRecently();
            addRecently(key, value);
        }
    }
}

public class S146 {
    public static void main(String[] args) {

    }
}

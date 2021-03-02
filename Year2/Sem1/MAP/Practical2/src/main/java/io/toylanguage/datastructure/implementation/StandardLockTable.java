package io.toylanguage.datastructure.implementation;

import io.toylanguage.datastructure.LockTable;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.stream.Stream;

public class StandardLockTable implements LockTable {
    private static int nextLocation = 1;
    private final Map<Integer, Integer> map = new HashMap<>();

    @Override
    public synchronized void update(Integer key, Integer value) {
        map.put(key, value);
    }

    @Override
    public synchronized Integer lookup(Integer key) {
        return map.get(key);
    }

    @Override
    public boolean containsKey(Integer key) {
        return map.containsKey(key);
    }

    @Override
    public Integer add(Integer value) {
        map.put(nextLocation, value);
        ++nextLocation;
        return nextLocation - 1;
    }

    @Override
    public Stream<Map.Entry<Integer, Integer>> stream() {
        return map.entrySet().stream();
    }

    @Override
    public String toString() {
        Iterator<Map.Entry<Integer, Integer>> iterator = map.entrySet().iterator();
        String result = "\n";
        while (iterator.hasNext()) {
            java.util.Map.Entry<Integer, Integer> entry = iterator.next();
            result = result.concat("\t%s: %s\n".formatted(entry.getKey(), entry.getValue()));
        }

        return result;
    }
}

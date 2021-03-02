package io.toylanguage.datastructure.implementation;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.exception.KeyNotFoundException;
import javafx.util.Pair;

import java.util.*;
import java.util.stream.Stream;

public class StandardMap<K, V> implements Map<K, V> {
    protected final java.util.Map<K, V> map;

    public StandardMap() {
        map = new HashMap<>();
    }

    protected StandardMap(java.util.Map<K, V> map) {
        this.map = new HashMap<>(map);
    }

    @Override
    public synchronized void set(K key, V value) {
        map.put(key, value);
    }

    @Override
    public synchronized V get(K key) throws KeyNotFoundException {
        if (map.containsKey(key)) {
            return map.get(key);
        } else {
            throw new KeyNotFoundException();
        }
    }

    @Override
    public synchronized boolean containsKey(K key) {
        return map.containsKey(key);
    }

    @Override
    public synchronized void removeKey(K key) {
        map.remove(key);
    }

    @Override
    public synchronized Collection<V> values() {
        return map.values();
    }

    @Override
    public synchronized Set<K> keys() {
        return map.keySet();
    }

    @Override
    public synchronized StandardMap<K, V> deepCopy() {
        return new StandardMap<>(map);
    }

    @Override
    public Stream<java.util.Map.Entry<K, V>> stream() {
        return map.entrySet().stream();
    }

    @Override
    public synchronized boolean isEmpty() {
        return map.isEmpty();
    }

    @Override
    public synchronized int size() {
        return map.size();
    }

    @Override
    public synchronized String toString() {
        Iterator<java.util.Map.Entry<K, V>> iterator = map.entrySet().iterator();
        String result = "\n";
        while (iterator.hasNext()) {
            java.util.Map.Entry<K, V> entry = iterator.next();
            result = result.concat("\t%s: %s\n".formatted(entry.getKey(), entry.getValue()));
        }

        return result;
    }
}

package io.toylanguage.datastructure;

import io.toylanguage.datastructure.exception.KeyNotFoundException;

import java.util.stream.Stream;

public interface Map<K, V> extends Collection {
    void set(K key, V value);

    V get(K key) throws KeyNotFoundException;

    boolean containsKey(K key);

    void removeKey(K key);

    java.util.Collection<V> values();

    java.util.Set<K> keys();

    Map<K, V> deepCopy();

    Stream<java.util.Map.Entry<K, V>> stream();
}

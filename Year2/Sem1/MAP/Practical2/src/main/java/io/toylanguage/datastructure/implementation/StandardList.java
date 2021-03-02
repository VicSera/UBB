package io.toylanguage.datastructure.implementation;

import io.toylanguage.datastructure.List;

import java.util.Iterator;
import java.util.stream.Stream;

public class StandardList<T> implements List<T> {
    private final java.util.List<T> list = new java.util.ArrayList<>();

    @Override
    public synchronized T get(int index) {
        return list.get(index);
    }

    @Override
    public synchronized void add(T value) {
        list.add(value);
    }

    @Override
    public synchronized boolean contains(T value) {
        return list.contains(value);
    }

    @Override
    public Stream<T> stream() {
        return list.stream();
    }

    @Override
    public synchronized boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public synchronized int size() {
        return list.size();
    }

    @Override
    public synchronized String toString() {
        Iterator<T> iterator = list.iterator();
        String result = "\n";
        while (iterator.hasNext()) {
            T entry = iterator.next();
            result = result.concat("\t%s\n".formatted(entry));
        }

        return result;
    }
}

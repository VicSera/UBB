package io.toylanguage.datastructure;

import java.util.stream.Stream;

public interface List<T> extends Collection {
    T get(int index) throws IndexOutOfBoundsException;

    void add(T value);

    boolean contains(T value);

    Stream<T> stream();
}

package io.toylanguage.datastructure;

import java.util.List;
import java.util.stream.Stream;

public interface Stack<T> extends Collection {
    T pop();

    T peek();

    void push(T value);

    Stream<T> stream();
}

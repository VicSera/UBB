package io.toylanguage.datastructure.implementation;

import io.toylanguage.datastructure.Stack;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;
import java.util.stream.Stream;

public class StandardStack<T> implements Stack<T> {
    private final Deque<T> deque = new ArrayDeque<>();

    @Override
    public synchronized T pop() {
        return deque.pop();
    }

    @Override
    public T peek() {
        return deque.peek();
    }

    @Override
    public synchronized void push(T value) {
        deque.push(value);
    }

    @Override
    public Stream<T> stream() {
        return deque.stream();
    }

    @Override
    public synchronized boolean isEmpty() {
        return deque.isEmpty();
    }

    @Override
    public synchronized int size() {
        return deque.size();
    }

    @Override
    public synchronized String toString() {
        Iterator<T> iterator = deque.iterator();
        String result = "\n";
        while (iterator.hasNext()) {
            T entry = iterator.next();
            result = result.concat("\t%s\n".formatted(entry));
        }

        return result;
    }
}

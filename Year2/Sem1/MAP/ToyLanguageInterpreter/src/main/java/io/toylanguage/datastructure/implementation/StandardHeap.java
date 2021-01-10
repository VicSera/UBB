package io.toylanguage.datastructure.implementation;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.model.value.Value;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.stream.Stream;

public class StandardHeap extends HashMap<Integer, Value> implements Heap {
    private int nextAddress = 1;

    @Override
    public synchronized int allocate(Value value) {
        this.put(nextAddress, value);
        ++nextAddress;

        return nextAddress - 1;
    }

    @Override
    public synchronized void setContent(Heap heap) {
        this.clear();
        this.putAll(heap);
    }

    @Override
    public synchronized void setContent(Map<Integer, Value> map) {
        this.clear();
        this.putAll(map);
    }

    @Override
    public Stream<Entry<Integer, Value>> stream() {
        return entrySet().stream();
    }

    @Override
    public synchronized String toString() {
        Iterator<Entry<Integer, Value>> iterator = this.entrySet().iterator();
        String result = "\n";
        while (iterator.hasNext()) {
            java.util.Map.Entry<Integer, Value> entry = iterator.next();
            result = result.concat("\t%s: %s\n".formatted(entry.getKey(), entry.getValue()));
        }

        return result;
    }
}

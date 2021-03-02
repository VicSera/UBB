package io.toylanguage.datastructure;

import io.toylanguage.model.value.Value;

import java.util.Map;
import java.util.stream.Stream;

public interface Heap extends Map<Integer, Value> {
    int allocate(Value value);

    void setContent(Heap heap);

    void setContent(Map<Integer, Value> map);

    Stream<Entry<Integer, Value>> stream();
}

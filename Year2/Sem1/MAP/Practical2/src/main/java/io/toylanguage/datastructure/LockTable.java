package io.toylanguage.datastructure;

import java.util.Map;
import java.util.stream.Stream;

public interface LockTable {
    void update(Integer key, Integer value);

    Integer lookup(Integer key);

    boolean containsKey(Integer key);

    Integer add(Integer value);

    Stream<Map.Entry<Integer, Integer>> stream();
}

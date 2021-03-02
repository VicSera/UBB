package io.toylanguage.datastructure.map;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.exception.KeyNotFoundException;
import io.toylanguage.datastructure.implementation.StandardMap;
import org.junit.Assert;
import org.junit.Test;

public class StandardMapTest {
    @Test
    public void constructorCreatesEmptyMap() {
        Map<Integer, String> map = new StandardMap<>();

        Assert.assertTrue(map.isEmpty());
    }

    @Test
    public void addKVPairIncreasesSize() {
        Map<Integer, String> map = new StandardMap<>();

        map.set(1, "John");

        Assert.assertEquals(1, map.size());
    }

    @Test
    public void removeKeyDecreasesSize() {
        Map<Integer, String> map = new StandardMap<>();

        map.set(1, "John");
        map.removeKey(1);

        Assert.assertTrue(map.isEmpty());
    }

    @Test
    public void sizeReturnsAmountOfElements() {
        Map<Integer, String> map = new StandardMap<>();

        map.set(1, "John");
        map.set(2, "John");
        map.set(3, "John");
        map.set(4, "John");
        map.set(5, "John");
        map.removeKey(1);
        map.removeKey(3);
        map.removeKey(5);

        Assert.assertEquals(2, map.size());
    }

    @Test
    public void getValueFromKeyReturnsRightValue() {
        Map<Integer, String> map = new StandardMap<>();

        map.set(1, "John");
        map.set(2, "Bob");
        map.set(3, "Ike");

        try {
            Assert.assertTrue(
                    map.get(1).equals("John") &&
                    map.get(2).equals("Bob") &&
                    map.get(3).equals("Ike"));
        } catch (KeyNotFoundException exception) {
            Assert.fail("One of the keys was not found");
        }
    }

    @Test
    public void getKeyWithNonExistentKeyThrows() {
        Map<Integer, String> map = new StandardMap<>();

        try {
            map.get(100);
            Assert.fail("Get should have thrown KeyNotFoundException");
        } catch (KeyNotFoundException ignored) {

        }
    }
}

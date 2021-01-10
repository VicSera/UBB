package io.toylanguage.datastructure.list;

import io.toylanguage.datastructure.List;
import io.toylanguage.datastructure.implementation.StandardList;
import org.junit.Assert;
import org.junit.Test;

public class StandardListTest {
    @Test
    public void constructorCreatesEmptyList() {
        List<Integer> list = new StandardList<>();

        Assert.assertTrue(list.isEmpty());
    }

    @Test
    public void addIncreasesSize() {
        List<Integer> list = new StandardList<>();

        list.add(1);

        Assert.assertEquals(1, list.size());
    }

    @Test
    public void getReturnsRightElement() {
        List<Integer> list = new StandardList<>();

        list.add(1);
        list.add(2);
        list.add(3);
        Assert.assertTrue(list.get(0).equals(1) &&
                list.get(1).equals(2) &&
                list.get(2).equals(3));
    }

    @Test
    public void getThrowsIndexOutOfBounds() {
        List<Integer> list = new StandardList<>();

        list.add(1);

        try {
            list.get(1);
            Assert.fail("get didn't throw");
        } catch (IndexOutOfBoundsException ignored) { }
    }

    @Test
    public void containsReturnsTrueIfElementIsInList() {
        List<Integer> list = new StandardList<>();

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        Assert.assertTrue(list.contains(2));
    }

    @Test
    public void containsReturnsFalseIfElementIsNotInList() {
        List<Integer> list = new StandardList<>();

        list.add(1);
        list.add(2);
        list.add(3);

        Assert.assertFalse(list.contains(4));
    }
}

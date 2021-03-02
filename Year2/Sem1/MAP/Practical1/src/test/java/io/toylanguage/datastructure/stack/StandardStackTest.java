package io.toylanguage.datastructure.stack;

import io.toylanguage.datastructure.Stack;
import io.toylanguage.datastructure.implementation.StandardStack;
import org.junit.Assert;
import org.junit.Test;

import java.util.NoSuchElementException;

public class StandardStackTest {
    @Test
    public void constructorCreatesEmptyStack() {
        Stack<Integer> stack = new StandardStack<>();

        Assert.assertTrue(stack.isEmpty());
    }

    @Test
    public void pushChangesSizeBy1() {
        Stack<Integer> stack = new StandardStack<>();
        stack.push(5);

        Assert.assertEquals(1, stack.size());
    }

    @Test
    public void push10ValuesChangesSizeBy10() {
        Stack<Integer> stack = new StandardStack<>();
        for (int i = 0; i < 10; ++i) {
            stack.push(i);
        }

        Assert.assertEquals(10, stack.size());
    }

    @Test
    public void popSingleElementMakesStackEmpty() {
        Stack<Integer> stack = new StandardStack<>();
        stack.push(5);
        stack.pop();

        Assert.assertTrue(stack.isEmpty());
    }

    @Test
    public void popElementDecrementsSize() {
        Stack<Integer> stack = new StandardStack<>();
        stack.push(5);
        stack.push(6);
        stack.pop();

        Assert.assertEquals(1, stack.size());
    }

    @Test
    public void popReturnsLastValue() {
        Stack<Integer> stack = new StandardStack<>();
        stack.push(5);
        stack.push(6);

        Integer lastValue = stack.pop();
        Integer firstValue = stack.pop();

        Assert.assertTrue(firstValue == 5 && lastValue == 6);
    }

    @Test
    public void popOnEmptyStackThrows() {
        Stack<Integer> stack = new StandardStack<>();

        try {
            stack.pop();
            Assert.fail("Pop didn't throw");
        } catch (NoSuchElementException ignored) { }
    }
}

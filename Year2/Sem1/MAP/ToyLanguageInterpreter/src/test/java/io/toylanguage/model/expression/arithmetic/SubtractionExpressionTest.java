package io.toylanguage.model.expression.arithmetic;

import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.implementation.StandardHeap;
import io.toylanguage.datastructure.implementation.StandardMap;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.expression.arithmetic.implementation.SubtractionExpression;
import io.toylanguage.model.expression.value.ValueExpression;
import io.toylanguage.model.value.implementation.IntValue;
import org.junit.Assert;
import org.junit.Test;

import java.util.Collections;
import java.util.Random;

public class SubtractionExpressionTest {
    @Test
    public void testSubtract3Minus2Equals1() {
        performTest(3, 2, 1);
    }

    @Test
    public void test1000RandomAdditions() {
        Random randomNumberGenerator = new Random();
        for (int i = 0; i < 1000; ++i) {
            int operand1 = randomNumberGenerator.nextInt(1000);
            int operand2 = randomNumberGenerator.nextInt(1000);
            int expectedResult = operand1 - operand2;

            performTest(operand1, operand2, expectedResult);
        }
    }

    private void performTest(int operand1, int operand2, int expectedResult) {
        try {
            Assert.assertEquals(
                    expectedResult,
                    new SubtractionExpression(
                            new ValueExpression(new IntValue(operand1)),
                            new ValueExpression(new IntValue(operand2))
                    ).evaluate(new SymbolTable(), new StandardHeap()).getValue()
            );
        } catch (ToyLanguageException exception) {
            Assert.fail("Evaluate threw an exception - " + exception.toString());
        }
    }
}

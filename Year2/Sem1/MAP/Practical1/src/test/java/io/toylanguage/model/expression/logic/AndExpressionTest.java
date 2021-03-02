package io.toylanguage.model.expression.logic;

import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.implementation.StandardHeap;
import io.toylanguage.datastructure.implementation.StandardMap;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.expression.logic.implementation.AndExpression;
import io.toylanguage.model.expression.value.ValueExpression;
import io.toylanguage.model.value.implementation.BoolValue;
import org.junit.Assert;
import org.junit.Test;

import java.util.Collections;

public class AndExpressionTest {
    @Test
    public void testTrueAndTrueEqualsTrue() {
        performTest(true, true, true);
    }

    @Test
    public void testTrueAndFalseEqualsFalse() {
        performTest(true, false, false);
    }

    @Test
    public void testFalseAndTrueEqualsFalse() {
        performTest(false, true, false);
    }

    @Test
    public void testFalseAndFalseEqualsFalse() {
        performTest(false, false, false);
    }

    private void performTest(boolean operand1, boolean operand2, boolean expectedResult) {
        try {
            Assert.assertEquals(
                    expectedResult,
                    new AndExpression(
                            new ValueExpression(new BoolValue(operand1)),
                            new ValueExpression(new BoolValue(operand2))
                    ).evaluate(new SymbolTable(), new StandardHeap()).getValue()
            );
        } catch (ToyLanguageException exception) {
            Assert.fail("Evaluate threw an exception - " + exception.toString());
        }
    }
}

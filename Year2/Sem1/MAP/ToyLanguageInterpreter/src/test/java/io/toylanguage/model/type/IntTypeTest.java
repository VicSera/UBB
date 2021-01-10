package io.toylanguage.model.type;

import io.toylanguage.model.type.implementation.IntType;
import org.junit.Assert;
import org.junit.Test;

public class IntTypeTest {
    @Test
    public void testTypeEquality() {
        Assert.assertEquals(new IntType(), new IntType());
    }
}

package io.toylanguage.model.type;

import io.toylanguage.model.type.implementation.BoolType;
import org.junit.Assert;
import org.junit.Test;

public class BoolTypeTest {
    @Test
    public void testTypeEquality() {
        Assert.assertEquals(new BoolType(), new BoolType());
    }
}

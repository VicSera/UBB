package exception

import entity.Product

class InventoryException(
    product: Product,
    expected: Int,
    actual: Int
) : CheckStateException("INVENTORY EXCEPTION: ", product.name, expected.toString(), actual.toString())

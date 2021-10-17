package util

import entity.Product
import entity.Sale
import kotlin.random.Random

class MockDataUtil {
    companion object {
        fun generateProducts(quantity: Int): Set<Product> {
            val products = emptySet<Product>().toMutableSet()

            repeat(quantity) { number ->
                products.add(Product("Product$number", Random.nextFloat() * 100f))
            }

            return products
        }

        fun generateInventory(products: Set<Product>, minQty: Int, maxQty: Int): Map<Product, Int> {
            val inventory = emptyMap<Product, Int>().toMutableMap()

            products.forEach { product ->
                inventory[product] = Random.nextInt(minQty, maxQty + 1)
            }

            return inventory;
        }

        fun generateSales(inventory: Map<Product, Int>): List<Sale> {
            val sales = emptyList<Sale>().toMutableList()

            inventory.forEach { (product, quantity) ->
                var remaining = quantity
                while (remaining > 0) {
                    val newSaleQuantity = if (remaining > 3) Random.nextInt(1, 4) else remaining
                    remaining -= newSaleQuantity
                    sales.add(Sale(product, newSaleQuantity))
                }
            }
            sales.shuffle()

            return sales
        }
    }
}

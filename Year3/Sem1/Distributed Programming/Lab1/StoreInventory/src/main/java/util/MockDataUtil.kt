package util

import entity.Product
import entity.Sale
import kotlin.random.Random

/**
 * Util class that creates [Product]s, Inventories and [Sale]s
 */
class MockDataUtil {
    companion object {
        fun generateProducts(quantity: Int): Set<Product> {
            val products = emptySet<Product>().toMutableSet()

            repeat(quantity) { number ->
                products.add(Product("Product$number", Random.nextFloat() * 100f + 1))
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

            inventory.forEach { (product, _) ->
                repeat(50) {
                    val newSaleQuantity = Random.nextInt(1, 4)
                    sales.add(Sale(product, newSaleQuantity))
                }
            }
            sales.shuffle()

            return sales
        }
    }
}

package store

import entity.Sale

interface Store {
    suspend fun registerSale(sale: Sale)
    suspend fun checkState()
}

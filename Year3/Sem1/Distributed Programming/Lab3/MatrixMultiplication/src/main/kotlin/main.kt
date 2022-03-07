import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import java.util.concurrent.Executors
import kotlin.concurrent.thread
import kotlin.system.measureTimeMillis

enum class Approach {
    ON_ROWS, ON_COLUMNS, SKIP
}

const val numberOfThreads = 2
const val matSize = 50
const val usePool = false
val approach = Approach.ON_ROWS

lateinit var mat1: List<List<Int>>
lateinit var mat2: List<List<Int>>
lateinit var res: MutableList<MutableList<Int>>

@ExperimentalStdlibApi
fun main() {
    mat1 = buildList {
        repeat(matSize) {
            add(buildList {
                repeat(matSize) { n ->
                    add(n + 1)
                }
            } )
        }
    }
    mat2 = mat1.toList()
    res = buildList {
        repeat(matSize) {
            add(buildList {
                repeat(matSize) {
                    add(0)
                }
            }.toMutableList() )
        }
    }.toMutableList()


    val time = if (usePool) {
        val dispatcher = Executors.newFixedThreadPool(numberOfThreads).asCoroutineDispatcher()

        measureTimeMillis {
            runBlocking {
                withContext(dispatcher) {
                    compute(numberOfThreads, approach)
                }
            }
        }
    } else {
        val threads = buildList {
            repeat(numberOfThreads) { n ->
                add(thread(start = false) {
                    when (approach) {
                        Approach.ON_ROWS -> threadSequentialOnRows(n)
                        Approach.ON_COLUMNS -> threadSequentialOnColumns(n)
                        Approach.SKIP -> threadSkip(n)
                    }
                })
            }
        }

        measureTimeMillis {
            threads.forEach { it.start() }
            threads.forEach { it.join() }
        }
    }

    res.forEach { row ->
        row.forEach { elem ->
            print("$elem ")
        }
        println()
    }

    println("Finished in $time milliseconds")
}

suspend fun compute(threads: Int, approach: Approach) {
    coroutineScope {
        repeat(threads) { threadNumber ->
            launch {
                when (approach) {
                    Approach.ON_ROWS -> threadSequentialOnRows(threadNumber)
                    Approach.ON_COLUMNS -> threadSequentialOnColumns(threadNumber)
                    Approach.SKIP -> threadSkip(threadNumber)
                }
            }
        }
    }
}

fun threadSequentialOnRows(threadNumber: Int) {
    val elements = matSize * matSize
    val startingElem = elements / numberOfThreads * threadNumber
    val endingElem = elements / numberOfThreads * (threadNumber + 1)
    val start = elementNumberOnRows(startingElem)
    val end = elementNumberOnRows(endingElem)

    println("Starting row-sequential thread ($threadNumber - ${Thread.currentThread().id}) from ${start.row}, ${start.col} to ${end.row}, ${end.col}")

    var row = start.row
    var col = start.col

    while (row != end.row || col != end.col) {
        res[row][col] = computeProductRowCol(row, col)
        println("Thread $threadNumber computed res[$row][$col] = ${res[row][col]}")

        col += 1
        if (col == matSize) {
            col = 0
            row += 1
        }
    }
}

fun threadSequentialOnColumns(threadNumber: Int) {
    val elements = matSize * matSize
    val startingElem = elements / numberOfThreads * threadNumber
    val endingElem = elements / numberOfThreads * (threadNumber + 1)
    val start = elementNumberOnColumns(startingElem)
    val end = elementNumberOnColumns(endingElem)

    println("Starting col-sequential thread ($threadNumber - ${Thread.currentThread().id}) from ${start.row}, ${start.col} to ${end.row}, ${end.col}")

    var row = start.row
    var col = start.col

    while (row != end.row || col != end.col) {
        res[row][col] = computeProductRowCol(row, col)
        println("Thread $threadNumber computed res[$row][$col] = ${res[row][col]}")

        row += 1
        if (row == matSize) {
            row = 0
            col += 1
        }
    }
}

fun threadSkip(threadNumber: Int) {
    println("Starting skip thread $threadNumber")

    val start = elementNumberOnRows(threadNumber)
    var row = start.row
    var col = start.col

    println("Starting skip-sequential thread ($threadNumber - ${Thread.currentThread().id}) from ${start.row}, ${start.col}")

    while (row < mat1.size && col < mat1.size) {
        res[row][col] = computeProductRowCol(row, col)
        println("Thread $threadNumber computed res[$row][$col] = ${res[row][col]}")

        col += numberOfThreads
        while (col >= mat1.size) {
            col -= mat1.size
            row += 1
        }
    }
}

fun elementNumberOnRows(elementNumber: Int): RowCol {
    val elements = matSize * matSize
    val elemsPerRow = elements / matSize
    return Pair(elementNumber / elemsPerRow, elementNumber % elemsPerRow)
}

fun elementNumberOnColumns(elementNumber: Int): RowCol {
    val elements = matSize * matSize
    val elemsPerCol = elements / matSize
    return Pair(elementNumber % elemsPerCol, elementNumber / elemsPerCol)
}

fun computeProductRowCol(row: Int, col: Int): Int {
    var result = 0
    mat1[row].zip(mat2.map { rows -> rows[col] }).forEach { (el1, el2) ->
        result += el1 * el2
    }

    return result
}

typealias RowCol = Pair<Int, Int>
val RowCol.row get() = this.first
val RowCol.col get() = this.second

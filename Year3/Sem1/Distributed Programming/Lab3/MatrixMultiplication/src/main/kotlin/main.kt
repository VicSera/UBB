import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import java.util.concurrent.Executors

enum class Approach {
    ON_ROWS, ON_COLUMNS, SKIP
}

const val threads = 4
const val matSize = 9

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


    val dispatcher = Executors.newFixedThreadPool(threads).asCoroutineDispatcher()

    runBlocking {
        withContext(dispatcher) {
            compute(threads, Approach.SKIP)
        }
    }

    res.forEach { row ->
        row.forEach { elem ->
            print("$elem ")
        }
        println()
    }
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
    val elements = mat1.size * mat1.first().size
    val startingElem = elements / threads * threadNumber
    val endingElem = elements / threads * (threadNumber + 1)
    val start = elementNumberToRowAndCol(startingElem)
    val end = elementNumberToRowAndCol(endingElem)

    println("Starting row-sequential thread ($threadNumber) from ${start.row}, ${start.col} to ${end.row}, ${end.col}")

    var row = start.row
    var col = start.col

    while (row != end.row || col != end.col) {
        res[row][col] = computeProductRowCol(row, col)
        println("Thread $threadNumber computed res[$row][$col] = ${res[row][col]}")

        col += 1
        if (col == mat1.size) {
            col = 0
            row += 1
        }
    }
}

fun threadSequentialOnColumns(threadNumber: Int) {
    val elements = mat1.size * mat1.first().size
    val startingElem = elements / threads * threadNumber
    val endingElem = elements / threads * (threadNumber + 1)
    val start = elementNumberToRowAndCol(startingElem)
    val end = elementNumberToRowAndCol(endingElem)

    println("Starting col-sequential thread from ${start.row}, ${start.col} to ${end.row}, ${end.col}")

    var row = start.row
    var col = start.col

    while (row != end.row || col != end.col) {
        res[row][col] = computeProductRowCol(row, col)

        row += 1
        if (row == mat1.size) {
            row = 0
            col += 1
        }
    }
}

fun threadSkip(threadNumber: Int) {
    println("Starting skip thread $threadNumber")

    val start = elementNumberToRowAndCol(threadNumber)
    var row = start.row
    var col = start.col

    while (row < mat1.size && col < mat1.size) {
        res[row][col] = computeProductRowCol(row, col)

        col += threads
        while (col >= mat1.size) {
            col -= mat1.size
            row += 1
        }
    }
}

fun elementNumberToRowAndCol(elementNumber: Int): RowCol {
    val elements = mat1.size * mat1.first().size
    val elemsPerRow = elements / mat1.size
    return Pair(elementNumber / elemsPerRow, elementNumber % elemsPerRow)
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

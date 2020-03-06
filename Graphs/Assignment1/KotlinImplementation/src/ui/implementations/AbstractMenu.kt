package ui.implementations

import ui.interfaces.IMenu

abstract class AbstractMenu: IMenu {
    protected abstract fun handleAddEdge()

    protected abstract fun handleAddVertex()

    protected abstract fun printNumberOfVertices()

    protected abstract fun printVertices()

    protected abstract fun printIsEdge()

    protected abstract fun printInboundEdges()

    protected abstract fun printOutboundEdges()

    protected abstract fun printCost()
}
package entity

val List<Int>.isCycle get() = this.first() == this.last()

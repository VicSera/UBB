(defun depthOfList(l)
    (cond
        (
            (null l)
                1
        )
        (
            (numberp (car l))
                (depthOfList (cdr l))
        )
        (
            (listp (car l))
                (max (+ 1 (depthOfList (car l))) (depthOfList (cdr l)))
        )
    )
)

(print (depthOfList '(1 2 (3 (1 2) 4) 4 (1 2))))
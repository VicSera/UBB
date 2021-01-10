;; associationList(l1..ln, m1..mn) = 
;;      [] if lists are empty
;;      (l1 . m1) U associationList(l2..ln, m2..mn) otherwise

(defun associationList(listA listB)
    (if (not (null listA))
        (cons (cons (car listA) (car listB)) (associationList (cdr listA) (cdr listB)))
    )
)

(print (associationList '(1 2 3) '(a b c)))
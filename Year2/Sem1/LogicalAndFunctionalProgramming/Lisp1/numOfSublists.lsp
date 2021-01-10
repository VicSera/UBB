;; numOfSublists(l1..ln) = 
;;      0 if list is empty
;;      1 + numOfSublists(l2..ln) + numOfSublists(l1) if l1 is a list
;;      numOfSublists(l2..ln) otherwise

(defun numOfSublists(lst)
    (cond 
        (
            (null lst) 
                0
        )
        (
            (listp (car lst)) 
                (+ 1 (numOfSublists (cdr lst)) (numOfSublists (car lst)))
        )
        (
            (not (listp (car lst))) 
                (numOfSublists (cdr lst))
        )
    )
)

(print (numOfSublists '(1 2 (3 (1 2) 4) 4 (1 2))))
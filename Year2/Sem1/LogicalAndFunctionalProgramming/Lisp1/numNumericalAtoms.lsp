;; numNumericalAtoms(l1..ln) = 
;;      0 if list is empty
;;      1 + numNumericalAtoms(l2..ln) if l1 is a numerical atom
;;      numNumericalAtoms(l2..ln) otherwise

(defun numNumericalAtoms (lst)
    (cond
        (
            (null lst)
                0
        )
        (
            (numberp (car lst))
                (+ 1 (numNumericalAtoms (cdr lst)))
        )
        (
            t
                (numNumericalAtoms (cdr lst))
        )
    )
)

(print (numNumericalAtoms '(1 2 (3 (1 2) 4) 4 (1 2))))
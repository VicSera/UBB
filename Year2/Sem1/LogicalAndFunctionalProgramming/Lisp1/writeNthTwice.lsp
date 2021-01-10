;; writeNthTwice(l1..ln, c, n) = 
;;      [] if list is empty
;;      l1 U writeNthTwice(l2..ln, c + 1, n) if c != n
;;      l1 U l1 U writeNthTwice(l2..ln, c + 1, n) if c == n

(defun writeNthTwice(lst c n)
    (if (not (null lst)) 
        (if (= c n)
            (cons (car lst) (cons (car lst) (writeNthTwice (cdr lst) (+ c 1) n)))
            (cons (car lst) (writeNthTwice (cdr lst) (+ c 1) n))))
        
)

(print (writeNthTwice '(1 2 3 4 5) 1 3))
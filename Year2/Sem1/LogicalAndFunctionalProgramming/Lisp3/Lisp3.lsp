;; replaceNode(tree, a, b) = 
;;      b if tree is an atom and tree = a
;;      U replaceNode(subtree, a, b) if tree is a list
;; (subtree1..subtreen in tree)
;;      a if tree is an atom and tree != a (otherwise)

(defun replaceNode(tree a b)
    (cond
        (
            (and (atom tree) (eq tree a))
            b
        )
        (
            (listp tree)
            (mapcar #'(lambda (subtree) (funcall #'replaceNode subtree a b)) tree)
        )
        (
            t
            tree
        )
    )
)

(defun replaceNodeOdd(tree v &optional(odd 1))
    (cond
        (
            (and (atom tree) (= odd 1))
            v
        )
        (
            (listp tree)
            (mapcar #'(lambda (subtree) (replaceNodeOdd subtree v (- 1 odd))) tree)
        )
        (
            t
            tree
        )
    )
)

(print (replaceNodeOdd '(a (b (g)) (c (d (e)) (f))) 'X))
(print (replaceNodeOdd '(A (B (D E) C (F G))) 'X))
(print (replaceNodeOdd '(A (B (D E) C (F G))) 'X))
;;   a
;; b   c 
;;g   d f
;;   e 
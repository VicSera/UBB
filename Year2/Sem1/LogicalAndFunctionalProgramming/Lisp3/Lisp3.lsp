;; replaceNode(tree, a, b) = 
;;      b if tree is an atom and tree = a
;;      a if tree is an atom and tree != a
;;      U replaceNode(subtree, a, b) if tree is a list
;; (subtree in tree)

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

(print (replaceNode '(A (B (D E) C (F G))) 'E 'X))
;;   a
;; b   c
;;d e f g 
;; (A (B) (C (D) (E)))

;; preorder (lst) = 
;;      empty_list if lst is empty
;;      head(lst) U preorder(head(tail(lst))) U preorder(head(tail(tail(lst)))) 

(defun preorder(treeList)
    (cond 
        (
            (null treeList)
                '()
        )
        (
            T
                (append (list (car treeList)) (preorder (cadr treeList)) (preorder (caddr treeList)))
        )
    )
)

(print (preorder '(A)))
(print (preorder '(A (B) (C (D) (E)))))
(print (preorder '(A (B (D (H) (I (J) (K))) (E)) (C (F (L)) (G)))))
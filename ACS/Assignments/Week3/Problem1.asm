bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Here we declare the variables used by our program
    a DB 1
    b DB 3
    c DB 7
    d DB 5
    
; our code starts here
segment code use32 class=code
    start:
        ; This program computes (b+c)+(a+b-d)  #29 on the assignment list
        
        ; First paranthesis
        mov al, [b] ; AX = b
        add al, [c] ; AX = b + c
        
        ; Second paranthesis
        mov bl, [a] ; BX = a
        add bl, [b] ; BX = a + b
        sub bl, [d] ; BX = a + b - d

        ; We have the first paranthesis in AX, and the second paranthesis in BX
        ; We just have to add them up now
        
        add al, bl ; AX = (b + c) + (a + b - d)
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

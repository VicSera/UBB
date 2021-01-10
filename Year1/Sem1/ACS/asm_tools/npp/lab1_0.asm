bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
; extern printf
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern printf
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll
 ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DB 2
    b DB 3
    c DB 4
    d DW 10
    newline DB 10
    format DB 'Number is: %d\n', 0
    
; our code starts here
segment code use32 class=code
    start:
    ;ax = b * c
        mov al, [b] ;al = b
        mul byte [c] ;ax = al * c = b * c
    ;bx = b * c (keep the result in a separate place to free up ax)
        mov bx, ax ;bx = ax = b * c
    ;ax = b * 2
        mov al, 2
        mul byte [b]
    ;ax = ax + d = 2b + d
        add ax, [d]
    ;ax = ax - bx = 2b + d - bc = d - bc + 2b
        sub ax, bx
    ;al = (d - bc + 2b) / a
    ;ah = (d - bc + 2b) % a
        div byte [a]
        
        push eax
        push dword format
        
        call [printf]
         
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

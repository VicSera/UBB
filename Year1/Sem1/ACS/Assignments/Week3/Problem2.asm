bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Declare the variables needed by the program
    e DW 5
    g DW 3
    b DB 1
    c DB 2

; our code starts here
segment code use32 class=code
    start:
        ; The program computes (e+g-2*b)/(a+b)  #26 in the problem list
        
        ; Compute 2*b and store it in a separate register
        mov al, [b] ; AL = b (b is a byte)
        mov bx, 2 ; temporarily store 2 into bx for the next multiplication
        mul bx ; AX = AL * 2 (this mul returns a word)
        mov bx, ax ; BX = AX
        
        ; Compute e + g - 2*b
        mov ax, [e] ; AX = e (e is a word)
        add ax, [g] ; AX = e + b
        sub ax, bx ; AX = AX - BX = e + g - 2*b
        
        ; Divide by c
        div byte [c] ; AL = AX / b and AH = AX % b, but we only care about AL in this case
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

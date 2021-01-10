bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DD 15
    b DB 1
    c DB 6
    d DB 3
    x DQ 5

; our code starts here
segment code use32 class=code
    start:
        ; a-(7+x)/(b*b-c/d+2); a-doubleword; b,c,d-byte; x-qword
        
        ; c/d
        mov AL, [c]  ; AL = c
        cbw  ; AX = c
        idiv byte [d]  ; AL = AX/d = c/d
        cbw  ; AX = AL = c/d
        mov BX, AX  ; BX = c/d
        
        ; b*b
        mov AL, [b]  ; AL = b
        imul byte [b]  ; AX = AL * b = b*b
        
        ; b*b-c/d+2
        sub AX, BX  ; AX = b*b - c/d
        add AX, 2  ; AX = b*b - c/d + 2
        cwd  ; EAX = AX
        
        ; Save that result in EBX
        mov EBX, EAX  ; BX = (b*b-c/d+2)
        
        ; 7+x in EDX:EAX
        mov EAX, [x]  ; Low dword
        mov EDX, [x + 4]  ; High dword
        add EAX, 7  ; EDX:EAX = 7 + x
        
        ; (7+x)/(b*b-c/d+2)
        idiv EBX  ; EAX = (7+a)/(b*b - c/d + 2)
        
        ; a - (7+x)/(b*b-c/d+2)
        mov EBX, [a]  ; EBX = a
        sub EBX, EAX  ; EBX = a-(7+x)/(b*b-c/d+2)
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

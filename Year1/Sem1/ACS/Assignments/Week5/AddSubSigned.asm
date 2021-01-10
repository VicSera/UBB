bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DB 50
    b DW 31627
    c DD 2017
    d DQ 4294967296

; our code starts here
segment code use32 class=code 
    start:
        ; (a + b + c) - d + (b - c)
    
        ; (a + b + c)
        mov AL, [a]  ; AL = a
        cbw  ; AX = a
        add AX, [b]  ; AX = a + b
        cwde  ; EAX = a + b
        add EAX, [c]  ; EAX = a + b + c
        cdq  ; EDX:EAX = a + b + c
        
        ; (a + b + c) - d
        sub EAX, [d]  ; EAX = (a + b + c) - d (low dword)
        sbb EDX, [d + 4]  ; EDX = (a + b + c) - d (hight dword)

        ; Store the results in separate registers
        mov EBX, EAX
        mov ECX, EDX
        
        ; (b - c)
        mov AX, [b]  ; AX = b
        cwde  ; EAX = b
        sub EAX, [c]  ; EAX = b - c
        cdq  ; EDX:EAX = b - c
        
        ; (a + b + c) - d + (b - c)
        add EAX, EBX  ; Add the low dwords
        adc EDX, ECX  ; Add the high dwords
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

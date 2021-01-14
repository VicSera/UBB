bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
                          
;%include "factorial.asm"
extern factorial

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    format db "%d", 0
    n dd 0

; our code starts here
segment code use32 class=code
    start:
        push n
        push format
        call [scanf]
        add esp, 4 * 2
        
        push dword [n]
        call factorial
        
        push eax
        push format
        call [printf]
        add esp, 4 * 2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
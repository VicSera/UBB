bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nr DD 3218
    format DB '%d', 0

; our code starts here
segment code use32 class=code
    start:
        mov edx, [nr]
        mov eax, 0
        mov ecx, 32
        
        bucla:
            shl edx, 1
            adc eax, 0
            
            pusha
            
            push eax
            push format
            call [printf]
            add esp, 4 * 2
            
            popa
            
            mov eax, 0
            loop bucla
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

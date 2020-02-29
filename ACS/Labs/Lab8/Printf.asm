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
    a DD 1, 2, 3, 10, 14, 20
    len EQU ($ - a) / 4
    format DB "a[%d] = %d", 10, 0

; our code starts here
segment code use32 class=code
    start:
        mov esi, a
        mov ecx, len
        cld
        mov ebx, 0
        
        my_loop:
            lodsd
            
            pusha
            
            push eax
            push ebx
            push format
            
            call [printf]
            
            add esp, 4 * 3
            
            popa
            
            inc ebx
            loop my_loop
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

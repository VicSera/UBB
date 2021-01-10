bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DD 1, 2, 3, 4, 5
    len EQU ($ - a) / 4

; our code starts here
segment code use32 class=code
    start:
        ; int a[]
        ; for (i = len(a); i > 0; i--)
        ;   sum += a[i-1]
    
        mov eax, 0  ; sum
        mov esi, 0  ; index for a
        mov ecx, len  ; number of iterations
        
        jecxz over
    
        my_loop:
        add eax, [a + esi]
        add esi, 4
        loop my_loop
        
        over:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

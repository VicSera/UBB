bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    array DB 0, 1, 2, 3, 4, 5, 6
    len EQU ($ - array) / 1 ; position in the data segment - the position of a, divided by size(word)

; our code starts here
segment code use32 class=code
    start:
        ; Get the sum of all elements in array
        
        mov AL, 0   ; sum
        mov ECX, 0  ; i
        
    loop:
        cmp ECX, len
        jge out
        
        add AL, [array + ECX]
        
        inc ECX ; i++
        jmp loop
        
    out:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

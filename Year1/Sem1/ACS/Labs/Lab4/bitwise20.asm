bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 123 
    b dw 3332
    c dd 0

; our code starts here
segment code use32 class=code
    start:
        ; Implementation of problem 20
        
        ; 4
        mov ecx, 0  ; make all the bits of ecx 0, which will be the temporary storage for c
        
        ; 1
        mov ax, [a]
        and ax, 0000000111111000b  ; isolate bits 3-8 in ax
        shr ax, 3  ; move bits 3-8 to 0-5
        
        ; 2
        mov bx, [b]
        and bx, 0000000000011100b  ; isolate bits 2-4 in bx
        shl bx, 4  ; move bits 2-4 to 6-8
        or cx, bx  ; make bits 6-8 in cx = 6-8 in bx = 2-4 in b
        
        ; 3
        mov ax, [a]
        and ax, 0001111111000000b  ; isolate bits 6-12 in ax
        shl ax, 3  ; move bits 6-12 to 9-15
        or cx, ax  ; make bits 9-15 in cx = bits 9-16 in bx = bits 6-12 in a
        
        ; Now, ecx = c
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

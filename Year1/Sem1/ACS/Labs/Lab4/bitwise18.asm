bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start  

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dw 1010110111100110b
    b dd 0
    
; our code starts here
segment code use32 class=code
    start:
        ; Implementation of problem 18
        ; 1
        mov ebx, 0  ; 0-3 bits of B have value 0 (i)
        
        ; 2
        mov ax, [a]
        and ax, 0000111100000000b  ; mask that keeps only the 8-11 bits of a
        shr ax, 4  ; ax = 0000000011110000b  ; move 8-11 to 4-7
        or bx, ax  ; change bits 4-7 in bx to the bits 4-7 in ax, which are 8-11 of a
        
        ; 3
        mov ax, [a]  ; ax = a
        not ax  ; invert all the bits
        and ax, 0000000000000011b  ; isolate the first 2 bits
        shl ax, 8  ; shift bits 0-1 to 8-9
        or bx, ax  ; change bits 8-9 in bx
        shl ax, 2  ; shift bits 8-9 to 10-11
        or bx, ax  ; change bits 10-11 in bx
        
        ; 4
        or bx, 1111000000000000b  ; make bits 12-15 of bx 1
        ; the same as or bh, 11110000b
        
        ; 5
        mov ax, bx  ; save the lower bits of bx in ax
        shl ebx, 16  ; move the lower part of ebx to the higher part of ebx
        or bx, ax  ; same as mov bx, ax, this is to restore the lower part of ebx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

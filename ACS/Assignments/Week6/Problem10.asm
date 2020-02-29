bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    b DB 00000000b
    a DW 0000011100000000b

; our code starts here
segment code use32 class=code
    start:
        ; Replace the bits 0-3 of the byte B by the bits 8-11 of the word A.
        
        mov AX, [a]  ; bits 8-11 of a are now bits 8-11 of AX, and more precisely bits 0-3 of AH
        mov BL, [b]
        and BL, 11111000b  ; set bits 0-3 of b to 0
        or AH, BL  ; set bits 0-3 of b to bits 0-3 in AH 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call [exit]
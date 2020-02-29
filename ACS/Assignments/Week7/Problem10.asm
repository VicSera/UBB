bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    S1 DB '+22b86X8'
    len_1 EQU $ - S1
    S2 DB 'a45'
    len_2 EQU $ - S2
    D times (len_1 / 2 + len_2) DB 0

; our code starts here
segment code use32 class=code
    start:
        ; Two character strings S1 and S2 are given. Obtain the string D by concatenating the elements of S2 in reverse order and the elements found on even positions in S1
    
        mov ecx, len_2
        mov esi, S2 + len_2 - 1
        mov edi, D
        
        mov edx, 0
    
        std  ; DF = 1 so that we parse S2 from right to left
        first_loop:
            lodsb  ; AL = next character from S2
            
            cld ; DF = 0, because we need to store characters from left to right in the destination string
            stosb
            std ; DF = 1 for the next iteration
            
            loop first_loop
            
        mov esi, S1
        mov ecx, len_1
        cld ; S1 is parsed from left to right
        
        second_loop:
            lodsb ; AL = next character from S1
            
            test ecx, 00000001b  ; ZF = 1 if the index is even, and ZF = 0 if the index in odd
            jz next_iter  ; if ZF = 0 (odd index), go to the next iteration
            stosb ; otherwise, store the character to the destination
            
            next_iter:
            loop second_loop
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

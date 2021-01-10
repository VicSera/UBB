bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    A DW 1234h, 5678h, 1425h
    len_A EQU ($ - A) / 2
    
    B1 times len_A DB 0
    B2 times len_A DB 0

; our code starts here
segment code use32 class=code
    start:
        ; Given an array A of words, build two arrays of bytes:  
        ;   - array B1 contains as elements the higher part of the words from A
        ;   - array B2 contains as elements the lower part of the words from A
    
        ; prepare to parse the string
        mov esi, A
        mov ecx, len_A
        cld
        
        mov edi, B2
        mov ebx, B1
        
        my_loop:
            lodsw  ; AX = A[i]
            
            ; get the low part (AL)
            stosb  ; B2[i] = AL
            
            ; change the destination
            push edi
            mov edi, ebx  ; get the current offset in B1
            
            ; swap AH and AL
            ror ax, 8
            stosb  ; B1[i] = AL (which was originally AH)
            
            ; save the current offset in B1, and set EDI back to the current offset in B2
            mov ebx, edi
            pop edi
            
            loop my_loop
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

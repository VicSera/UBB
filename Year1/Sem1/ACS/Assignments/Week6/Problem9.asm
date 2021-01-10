bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DW 111100001111000b
    b DB 11001100b
    c DD 0

; our code starts here
segment code use32 class=code
    start:
        ; Given the word A and the byte B, compute the doubleword C as follows:
        ;  the bits 0-3 of C are the same as the bits 6-9 of A
        ;  the bits 4-5 of C have the value 1
        ;  the bits 6-7 of C are the same as the bits 1-2 of B
        ;  the bits 8-23 of C are the same as the bits of A
        ;  the bits 24-31 of C are the same as the bits of B
        
        mov ECX, [c]  ; ECX = c = 0
    
        ; 1
        mov AX, [a]
        shr AX, 6  ; bits 6-9 are now 0-3
        and AL, 00000111b  ; mask all the other bits
        or CL, AL  ; make bits 0-3 of CL = 0-3 of AL = 6-9 of a
        
        ; 2
        or CL, 00110000b  ; make bits 4-5 = 1
        
        ; 3
        mov BL, [b]
        shl BL, 5  ; bits 1-2 are now 6-7
        and BL, 11000000b  ; mask all the other bits
        or CL, BL  ; make bits 6-7 of CL = 6-7 of BL = 1-2 of b
        
        ; 4
        mov EAX, 0
        mov AX, [a]  ; bits of a are now on pos 0-15 in EAX
        shl EAX, 8  ; bits 0-15 are now 8-23
        or ECX, EAX  ; bits 8-23 in ECX = bits 8-23 in EAX = all bits of a
        
        ; 5
        mov EAX, 0
        mov AL, [b]  ; bits of b are now on pos 0-7 in EAX
        shl EAX, 24  ; bits 0-7 are now 24-31
        or ECX, EAX  ; bits 24-31 in ECX = bits 24-31 in EAX = all bits of b
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

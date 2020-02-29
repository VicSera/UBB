bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DD 1, 2, 3, 0xABCDEF00
    ; 01 00 00 00
    ; 02 00 00 00
    ; 03 00 00 00
    ; 00 EF CD AB
    ;        ^
    len_a EQU ($ - a) / 4
    b TIMES len_a DB 0
    
; our code starts here
segment code use32 class=code
    start:
        ; A string of doublewords is given. Compute the string formed by the high bytes of the low words from the elements of the doubleword string and these bytes should be multiple of 10
    
        ; Initialize our values
        mov ecx, len_a
        cld ; DF = 0, REALLY IMPORTANT
        mov esi, a ; ADDRESSES!
        mov edi, b
        
        jecxz the_end
        
        my_loop:
            lodsd ; eax = a[i]
            mov al, ah ; get the high byte of the low word into place (same as shr ax, 8)
            mov dl, al ; save al into dl
            cbw ; al -> ax
            
            mov bl, 10
            idiv bl ; al = quotient, ah = remainder
            ; if ah == 0, then the nr is a multiple of 10
            cmp ah, 0
            jne next
            ; else (if divisible by 0)
            mov al, dl ; restore saved byte from before
            stosb ; b[j] = al (a[i])
            
            next:
            loop my_loop
        
        the_end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

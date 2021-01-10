bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DD 11

; our code starts here
segment code use32 class=code
    start:
        ; if a % 2 == 1
        ; ECX = 10
        ; else ECX = 15
        
        mov EAX, [a]
        
        test EAX, 1  ; if last_digit(a) is 0
        jz even  ; then go to even
        ; else execute odd
        mov ECX, 10
        jmp end
    even: 
        mov ECX, 15
    end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

        
        
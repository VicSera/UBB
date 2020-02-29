bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a times 100 DD 0
    len DD 0
    format DB "%d", 0
    msg_len DB "len=", 0
    msg_elem DB "a[%d] = ", 0

; our code starts here
segment code use32 class=code
    start:
        push msg_len
        call [printf]
        add esp, 4
        
        ; scanf
        push len
        push format
        call [scanf]
        add esp, 4 * 2
        
        mov ecx, [len]
        jecxz the_end
        
        mov ebx, 0  ; index
        mov edi, a
        cld
        
        my_loop:
            pusha
            
            ;printf(msg_elem, ebx)
            push ebx
            push msg_elem
            call [printf]
            add esp, 4 * 2
            
            ;scanf(format, edi)
            push edi
            push format
            call [scanf]
            add esp, 4 * 2
            
            popa
            add edi, 4  ;  go to next elem
            inc ebx
            
            loop my_loop
            
        
        the_end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

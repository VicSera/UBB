bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DD 10
    b DD 15
    format DB "sum = %d", 10, 0
    
; our code starts here
segment code use32 class=code
    add_nums:
        ; create stackframe
        push ebp
        mov ebp, esp
    
        ; ebp has old_ebp
        ; ebp + 4 has return address
        mov eax, [ebp + 8]
        add eax, [ebp + 12]
        
        ; restore stack
        pop ebp
        ; return
        ret
    
    start:
        push dword [b]
        push dword [a]
        
        call add_nums
        
        add esp, 4 * 2
        
        ; printf(format, eax)
        push eax
        push format
        
        call [printf]
        
        add esp, 4 * 2
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

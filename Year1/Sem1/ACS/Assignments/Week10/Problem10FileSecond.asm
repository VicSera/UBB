bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fprintf, fopen, fclose, printf, gets               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

import scanf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import gets msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name times 30 db 0
    text times 120 db 0
    
    format db '%s', 0
    file_handle DD 0
    mode_write db 'w', 0
    
; our code starts here
segment code use32 class=code
    start:
        ; get file name
        push dword file_name
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        ; get text
        push dword text
        call [gets]
        add esp, 4 * 1
        
        
        ; open (or create) file
        push dword mode_write
        push dword file_name
        call [fopen]
        add esp, 4 * 2
        ; check if all is good
        cmp eax, 0
        je the_end
        ; else
        mov [file_handle], eax

        ; write to file
        push dword text
        push dword format
        push dword [file_handle]
        call [fprintf]
        add esp, 4 * 3
                
        ; close the file
        push dword [file_handle]
        call [fclose]
        add esp, 4 * 1
    
        the_end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

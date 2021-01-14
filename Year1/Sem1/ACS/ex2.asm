bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf, scanf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name times 50 db 0
    acc_mode db "r", 0
    file_descriptor dd -1
    
    len equ 100
    text times len db 0
    
    msg_filename db "file name: ", 0
    format_filename db "%s", 0
    
    format db "number of words: %d", 0
    format2 db "number of words that start with an uppercase: %d", 0

; our code starts here
segment code use32 class=code
    start:
        ;printf(msg_filename)
        push msg_filename
        call [printf]
        add esp, 4
        
        ;scanf(format, file_name)
        push file_name
        push format_filename
        call [scanf]
        add esp, 4*2
        
        ; open the file
        push dword acc_mode
        push dword file_name
        call [fopen]
        add esp, 4*2 ;clean the stack
        
        mov [file_descriptor], eax ;store the file descriptor returned by fopen
        
        ;check if fopen() has successfully created the file
        ;eax != 0
        cmp eax, 0
        je final
        
        ;read the text from file fread()
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov ecx, eax ; number of characters
        mov esi, text
        mov ebx, 0
        cld
        
        do:
            lodsb
            
            cmp al, ' '
            jne not_space
            
            inc ebx
            
            not_space:
                loop do
                
        inc ebx
        
        push ebx
        push format
        call [printf]
        add esp, 4*2
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
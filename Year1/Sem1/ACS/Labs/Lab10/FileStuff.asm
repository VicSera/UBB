bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fread, fopen, fclose, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name db 'input', 0
    access_mode db 'r', 0
    file_desc dd 0
    
    len equ 100
    buffer times len db 0
    
    format db '%d', 10, 0
    digit_count dd 0

; our code starts here
segment code use32 class=code
    count_digits:
        push ebp
        mov ebp, esp
        
        mov ebx, 0
        mov esi, [ebp + 8]
        mov ecx, [ebp + 12]
        cld
        
        count:
            lodsb ; get the current char in AL
            
            cmp al, '0'
            jl next
            cmp al, '9'
            jg next
            
            inc ebx
            
            next:
            loop count
            
        mov eax, ebx
        
        pop ebp
        ret

    start:
        ; count digits in a file
        
        ; open file
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4 * 1
        mov [file_desc], eax
        
        cmp eax, 0
        je the_end
        
        mov edx, 0
        
        ; read + count digits while eax > 0
        do:
            ; fread(buffer, 1, len, fd)
            push dword [file_desc]
            push dword len
            push dword 1
            push dword buffer
            call [fread]
            add esp, 4 * 4
            
            cmp eax, 0
            je close_file
            
            push eax
            push dword buffer
            call count_digits
            add esp, 4 * 2
            
            add [digit_count], eax
            
            jmp do
        
            
        ; close file
        close_file:
        push dword [file_desc]
        call [fclose]
        add esp, 4 * 1
        
        push dword [digit_count]
        push dword format
        call [printf]
        add esp, 4 * 2
    
        the_end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

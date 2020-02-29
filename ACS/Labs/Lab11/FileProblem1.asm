bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, scanf, fprintf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    fd DD 0
    file_name resb 30
    print_format db '%s ', 0
    mode_write db 'w', 0
    debug_format db 'This word has %d vowels', 10, 0
    
    scan_format db '%s', 0
    current_word resb 30
    
    vowels db 'aeiouAEIOU'
    vow_len equ $ - vowels

; our code starts here
segment code use32 class=code
    count_vowels:
        push ebp
        mov ebp, esp
        
        mov esi, [ebp + 8]
        mov ebx, 0
        
        for_char:
            lodsb ; al = current char in string
            
            cmp al, 0 ; check if we're at the end of the word
            je return
            
            mov ecx, vow_len
            for_vowel:
                cmp al, [vowels + ecx - 1]
                jne next
                
                inc ebx
                jmp for_char
                
                next:
                loop for_vowel
            jmp for_char
        
        return:
        mov eax, ebx
        
        pop ebp
        ret
        
    start:
        ; scanf('%s', file_name)
        push file_name
        push scan_format
        call [scanf]
        add esp, 4 * 2
        
        ; fopen(file_name, 'w')
        push mode_write
        push file_name
        call [fopen]
        add esp, 4 * 2
        
        mov [fd], eax
        
        cmp eax, 0
        je the_end
        
        read_word:
            ; scanf('%s', current_word)
            push current_word
            push scan_format
            call [scanf]
            add esp, 4 * 2
            
            cmp byte [current_word], '$'
            je close_file
            
            push current_word
            call count_vowels ; eax now has the number of vowels in the current word
            add esp, 4 * 1
            
            test eax, 1 ; check parity
            jnz read_word
            
            ; call fprintf(fd, format, string)
            push current_word
            push print_format
            push dword [fd]
            call [fprintf]
            add esp, 4 * 3
        
            jmp read_word
    
        close_file:
        ; fclose(fd)
        push dword [fd]
        call [fclose]
        add esp, 4 * 1
    
        the_end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

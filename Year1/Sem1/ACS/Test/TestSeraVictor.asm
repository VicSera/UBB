bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fprintf, fopen, fclose, printf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    N dd 0
    current_word db 0
    
    file_name db 'file.txt', 0
    access_mode db 'w', 0
    file_descriptor dd 0
    
    scan_number_format db '%d', 0
    scan_word_format db '%s', 0
    print_format db '%s ', 0
    print_number_format db '%d', 10, 0
    compare_format db 'Comparing %d with %d', 10, 0
    
    vowels db 'aeiouAEIOU'
    len_vowels equ 10

; our code starts here
segment code use32 class=code
    count_vowels:
        push ebp
        mov ebp, esp
        
        mov esi, [ebp + 8] ; esi now has the starting address of the current word
        mov edx, 0
        
        for_char:
            lodsb ; al now has current the character
            
            ; check if we're at \0
            cmp al, 0
            je return
            
            ; otherwise, check if the current character is a vowel
            mov ecx, len_vowels
            for_vowel:
                cmp al, byte [vowels + ecx - 1]
                je is_vowel
                
                loop for_vowel
            
            jmp for_char
            is_vowel:
                inc edx
                jmp for_char
                
        return:
        mov eax, edx
        
        pop ebp
        ret
    start:
        ; read a number N from console
        ; read multiple words until # is read
        ; write in a text file only the words that have N vowels
    
        ; open file
        ; fopen(file_name, access_mode)
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4 * 2
        
        ; store the file descriptor
        mov [file_descriptor], eax
        
        ; if file was not opened correctly, end the program
        cmp eax, 0
        je the_end
    
        ; read N from the keyboard
        ; scanf('%d', &N)
        push dword N
        push dword scan_number_format
        call [scanf]
        add esp, 4 * 2
        
        ; start reading words
        for_word:
            ; scanf('%s', current_word)
            push dword current_word
            push dword scan_word_format
            call [scanf]
            add esp, 4 * 2
            
            ; check for #
            cmp byte [current_word], '#'
            je close_file
            
            ; the word that was read in not #
            push dword current_word
            call count_vowels
            add esp, 4 * 1
              
            ; number of vowels is in eax
            cmp eax, [N]
            jne for_word
            
            ; else
            ; fprintf(file_descriptor, '%s ', current_word)
            push dword current_word
            push dword print_format
            push dword [file_descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            jmp for_word
            
            
        close_file:
        ; fclose(file_descriptor)
        push dword [file_descriptor]
        call [fclose]
        add esp, 4 * 1
        
        the_end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

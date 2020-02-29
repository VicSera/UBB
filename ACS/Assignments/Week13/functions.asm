bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf, match_words               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    scanf_format db '%s', 0
    printf_format db '%s', 0
    
    print_match db 'The string %s is a substring of %s', 10, 0
    print_no_match db 'The string %s is NOT a substring of %s', 10, 0
    
    template times 20 db 0
    current_word times 20 db 0

; our code starts here
segment code use32 class=code
    start:
        ; scan the first word
        push dword template
        push dword scanf_format
        call [scanf]
        add esp, 4 * 2
        
        read_word:
            ; scan another word
            push dword current_word
            push dword scanf_format
            call [scanf]
            add esp, 4 * 2
            
            ; check if word is == '$' so that the loop ends
            cmp byte [current_word], '$'
            je the_end
            
            ; otherwise, check for a match between the current word and the template word (first one)
            ; match_words(current_word, template)
            push dword template
            push dword current_word
            call match_words
            add esp, 4 * 2
            
            ; eax will now be 0 if the words don't match, or 1 if they do match
            cmp eax, 0
            jne match
            
            no_match:
                push dword current_word              
                push dword template
                push dword print_no_match
                call [printf]
                add esp, 4 * 3
                jmp read_word
            match:
                push dword current_word
                push dword template
                push dword print_match
                call [printf]
                add esp, 4 * 3
                jmp read_word
           
        the_end:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 'ana are mere'
    len_a equ $ - a
    
    voc db 'aeiouAEIOU'
    len_voc equ $ - voc

; our code starts here
segment code use32 class=code
    start:
        mov esi, a
        mov edi, voc
        
        cld
        
        mov ecx, len_a
        jecxz end
        
        mov ebx, 0  ; vowel counter
        
        loop_1:
            lodsb  ; get element from a into AL
            push ecx
            
            mov ecx, len_voc
            loop_2:
                scasb  ; cmp AL, [edi], inc edi
                jne noincrement
                inc ebx  ; found a vowel
                
                noincrement:
                loop loop_2
                
            pop ecx
            mov edi, voc  ; reinitialize edi to the beginning of the string of vowels
            
            loop loop_1
        
        end:
        
        ; ebx now stores the number of vowels found in the string a
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
extern printf
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 'ana are mere'
    len_a equ $ - a
    
    b db 'AnA arE Mere'
    len_b equ $ - b
    
    format db 'Nr. identical characters is %d', 10, 0  ; %d for decimal, %x hexa, 
    
; our code starts here
segment code use32 class=code
    start:
        mov esi, a
        mov edi, b
        cld ; l->r
        
        mov ebx, 0
        
        mov ecx, len_a
        jecxz the_end
        
        my_loop:
            cmpsb  ; cmp [esi], [edi]
            jne noincrement
                inc ebx
            
            noincrement:
            loop my_loop
        
        the_end:
        
        ; printf(format, ebx) parameters get pushed from right to left
        push ebx
        push format
        call [printf]
        add esp, 4*2 ; <=> pop eax, pop eax
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

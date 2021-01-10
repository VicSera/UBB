bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fprintf, fopen, fclose, fscanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name db 'ana.txt', 0
    input_file db 'input.txt', 0
    access_mode db 'w', 0
    mode_read db 'r', 0
    handle dd 0
    handle_input dd 0
    
    a dd 0
    len dd 0

    format db '%d', 0
    
; our code starts here
segment code use32 class=code
    start:
        ; fopen ( filename, access_mode )
        ; fprintf ( file_handle, format, ... )
        ; fscanf ( file_handle, format, ... )
        ; fclose ( file_handle )
    
        ; open input file
        push dword mode_read
        push dword input_file
        call [fopen]
        add esp, 4 * 2
        mov [handle_input], eax
        
        cmp eax, 0
        je final
        
        push len
        push dword format
        push dword handle_input
        call [fscanf]  ; read length
        add esp, 4 * 3
        
        ; print length
        push dword [len]
        push dword format
        call [printf]
        add esp, 4 * 2
    
        ; open output file
        push dword access_mode
        push dword file_name
        call [fopen]
        ; clear stack
        add esp, 4 * 2
        ; get the returned handle
        mov [handle], eax
        ; check if file was opened correctly
       cmp eax, 0
        je final
        
        mov ecx, [len]
        jecxz final
        
        do:
            ; read number from file
            pusha 
            
            push a
            push format
            push handle_input
            call [fscanf] ; fscanf(input_file, format, &a)
            add esp, 4 * 3
            ; mov eax, [a]
            
            ; print the number to the output file
            push dword [a]
            push format
            push dword [handle]
            call [fprintf]
            add esp, 4 * 3
            
            popa
            loop do
            
        ; close file with fclose
        push dword [handle]
        call [fclose]
        add esp, 4 * 1
        
        push dword [input_file]
        call [fclose]
        add esp, 4 * 1
            
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

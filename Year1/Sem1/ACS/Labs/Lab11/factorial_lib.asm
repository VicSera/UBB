bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global factorial 

segment code use32 public code
    ; factorial (int n) => n!
    factorial:
        push ebp
        mov ebp, esp
        
        mov eax, 1
        mov ecx, [ebp + 8] ; n
        
        next_multiply:
            mul ecx
            loop next_multiply
        
        pop ebp
        ret 4 ; STDCALL Convention
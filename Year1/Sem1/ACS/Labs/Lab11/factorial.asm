%ifndef _FACTORIAL_ASM_
%define _FACTORIAL_ASM_


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


%endif
bits 32
global start
extern exit
import exit msvcrt.dll
segment data use32 class=data
;a,b,c-byte; d-doubleword; e-qword
    a db 7
    b db -2
    c db -3
    d dd 4
    e dq 5

segment code use32 class=code
;2/(a+b*c-9)+e-d
    start:
        mov al, [b]    ;al=b=-2
        imul byte [c]  ;al=al*c=-2*(-3)=6
        add ax,  [a]    ;ax=ax+a=6+7=13
        sub ax, 9      ;ax=ax-9=13-9=4
        cwde           ;Converts the word AX to the doubleword EAX in the signed interpretation
        cdq            ;Converts the doubleword EAX to the qword EDX:EAX in the signed interpretation
        mov ebx, [e]   ;ebx=3=5
        add eax, ebx   ;eax=edx+ebx
        adc edx, ecx   ;edx=eax+ecx+CF
        sub eax, [d]   ;edx=edx-d
        sbb edx, 0 

        push dword 0
        call [exit]

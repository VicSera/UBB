bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s DB 1, 2, 3, 4, 5, 6, 1
    len EQU $ - s

; our code starts here
segment code use32 class=code
    start:
        ; A byte string S is given. Obtain the maximum of the elements found on the even positions and the minimum of the elements found on the odd positions of S.
        ; for (i = 0; i < len(s)/2; i++)
        ;   if (a[2i] > max)
        ;       max = a[2i]
        ;   if (a[2i+1] < min)
        ;       min = a[2i+1]
        ; if len(s) % 2 == 1
        ;   if a[len(s) - 1] > max
        ;       max = a[len(s) - 1]
    
        mov ecx, len ; num iterations
        mov esi, 0 ; index
        
        mov al, 0xFF ; min
        mov bl, 0 ; max
        
        my_loop:
        cmp bl, [s + esi]
        jae max_ok
        ; else update max
        mov bl, [s + esi]
       
        max_ok: ; max was updated
        ; final sir?
        dec ecx
        cmp ecx, 0
        je the_end
        
        inc esi
        cmp al, [s + esi]
        jbe min_ok
        ; else update min
        mov al, [s + esi]
        
        min_ok:
        inc esi
        dec ecx
        cmp ecx, 0
        jne my_loop
        
        the_end: ; we reached the end of the string
   
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

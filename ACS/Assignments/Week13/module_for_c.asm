global match_words

extern printf

section .data
    print_format db 'Comparing %s with %s', 10, 0

match_words:
    push ebp
    mov ebp, esp
    
    ; current_word is in [ebp + 8]
    ; template word is in [ebp + 12]
    mov esi, [ebp + 8] ; current word
    mov edi, [ebp + 12] ; template
    
    pusha
    push esi
    push edi
    push print_format
    call printf
    add esp, 4 * 3
    popa
    
    mov ebx, -1 ; this will serve as our offset
    
    for_offset:
        inc ebx 
        mov ecx, 0
        for_char:
            push ecx
            mov eax, 0
            mov al, [edi + ecx]
            add ecx, ebx
            mov edx, 0
            mov dl, [esi + ecx]
            pop ecx
            ; al now has the i'th term in the template word and ah has the i + offset'th term in the current word
            
            ; check if we're at the end of the template string: (if so, we have a match)
            cmp al, 0
            je match
            
            ; check if we're at the end of the current string: (if so, there is no match at all)
            cmp dl, 0
            je no_match
            
            ; if no string is at the end, simply compare the letters
            cmp al, dl
            jne for_offset
            
            inc ecx
            jmp for_char
    
    match:
        mov eax, 1
        jmp return
    no_match:
        mov eax, 0
        jmp return
    
    return:
    pop ebp
    ret
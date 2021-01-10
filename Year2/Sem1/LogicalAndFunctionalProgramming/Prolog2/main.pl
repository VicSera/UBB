% has_divisors_in_range(number, left, right) = 
%   true if number % left = 0
%   false if left >= right
%   has_divisors_in_range(number, left + 1, right)

has_divisors_in_range(E, Left, _):- 
    0 is mod(E, Left),
    !.
has_divisors_in_range(E, Left, Right):-
    Left < Right,
    NewLeft is Left + 1,
    has_divisors_in_range(E, NewLeft, Right).


% is_prime(number) = 
%   false if number < 2
%   true if number = 2
%   !has_divisors_in_range(number, 2, number - 1) otherwise
is_prime(2).
is_prime(E):-
    E > 2,
    Left is 2,
    Right is E - 1,
    \+has_divisors_in_range(E, Left, Right).

% duplicate_primes(l1...ln)
%   l1 U duplicate_primes(l2..ln) if !is_prime(l1)
%   l1 U l1 U duplciate_primes(l2..ln) if is_prime(l1)
%   [] if n = 0
duplicate_primes([], []).
duplicate_primes([H | T], Out):-
    is_prime(H),
    duplicate_primes(T, Out1),
    Out = [H, H | Out1].
duplicate_primes([H | T], Out):-
    \+is_prime(H),
    duplicate_primes(T, Out1),
    Out = [H | Out1].


% duplicate_primes_heterog_list(l1..ln)
%   [] if n = 0
%   duplicate_primes(l1) U duplicate_primes_heterog_list(l2..ln) if l1 is a list
%   l1 U duplicate_primes_heterog_list(l2..ln) if l1 is NOT a list
duplicate_primes_heterog_list([], []).
duplicate_primes_heterog_list([H | T], Out):-
    is_list(H),
    duplicate_primes_heterog_list(T, Out1),
    duplicate_primes(H, Out2),
    Out = [Out2 | Out1].
duplicate_primes_heterog_list([H | T], Out):-
    number(H), 
    duplicate_primes_heterog_list(T, Out1),
    Out = [H | Out1].

% isOdd(L) - true if list has odd nr of elems / false otherwise
% count how many sublists have odd nr of elems
count_odd_sublists([], 0).
count_odd_sublists([H | T], Out):-
    is_list(H),
    isOdd(H),
    count_odd_sublists(T, Out1),
    Out = Out1 + 1.
count_odd_sublists([H | T], Out):-
    is_list(H),
    \+isOdd(H),
    count_odd_sublists(T, Out1),
    Out = Out1.
count_odd_sublists([H | T], Out):-
    number(H),
    count_odd_sublists(T, Out1),
    Out = Out1.
% is_in_list(l1..ln,E) =
%   true if l1 = E
%   is_in_list(l2..ln,E) if l1 != E and n > 0
%   (false if l1 != E and n = 0)

is_in_list([H|_],H).
is_in_list([_|T],E) :- is_in_list(T,E).

is_set([]).
is_set([H|T]) :-
    \+is_in_list(T,H),
    is_set(T).

% union_of(l1..ln,m1..mp) =
%   empty_set if n = 0 and p = 0
%   l1..ln if p = 0
%   m1..mp if n = 0
%   l1 U union_of(l2..ln,m1..mp) if n != 0 and p != 0 and is_in_list(m1..mp, l1) = false
%   union_of(l2..ln,m1..mp) if n != 0 and p != 0 and is_in_list(m1..mp, l1) = true

union_of([],[],[]).
union_of([],[H2|T2],Out) :-
    union_of([],T2,Out1),
    Out = [H2|Out1].
union_of([H1|T1],[],Out) :-
    union_of(T1,[],Out1),
    Out = [H1|Out1].
union_of([H1|T1],L2,Out) :-
    \+is_in_list(L2,H1),
    union_of(T1,L2,Out1),
    Out = [H1|Out1].
union_of([H1|T1],L2,Out) :-
    is_in_list(L2,H1),
    union_of(T1,L2,Out).

% pair_element_with_each_from_list(e, l1..ln) =
%   empty_list if n = 0
%   [e, l1] U pair_element_with_each_from_list(e, l2..ln) if n > 0

pair_element_with_each_from_list(_,[],[]).
pair_element_with_each_from_list(E,[H|T],Out) :-
    pair_element_with_each_from_list(E,T,Out1),
    Out = [[E,H]|Out1].

% concatenate_lists(l1..ln,m1..mp) =
%   empty_list if n = 0 and p = 0
%   l1..ln if p = 0
%   m1..mp if n = 0
%   l1 U concatenate_lists(l2..ln,m1..mp) otherwise

concatenate_lists([],[],[]).
concatenate_lists([H|T],[],Out) :-
    concatenate_lists(T,[],Out1),
    Out = [H|Out1].
concatenate_lists([],[H|T],Out) :-
    concatenate_lists([],T,Out1),
    Out = [H|Out1].
concatenate_lists([H1|T1],[H2|T2],Out) :-
    concatenate_lists(T1,[H2|T2],Out1),
    Out = [H1|Out1].

% pairs_of_elements_in(l1..ln) =
%   empty_list if n = 0
%   concatenate_lists(
%       pair_element_with_each_from_list(l1, l2..ln),
%       pairs_of_elements_in(l2..ln)
%   ) otherwise

pairs_of_elements_in([],_).
pairs_of_elements_in([H|T],Out) :-
    pairs_of_elements_in(T,Out1),
    pair_element_with_each_from_list(H, T, Pairs),
    concatenate_lists(Pairs,Out1,Out2),
    Out = Out2.

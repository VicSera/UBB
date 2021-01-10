% For a list a1... an with integer and distinct numbers, define a predicate to determine all subsets with
% sum of elements divisible with n

% concatenateLists(l1..ln,m1..mp) =
%   empty_list if n = 0 and p = 0
%   l1..ln if p = 0
%   m1..mp if n = 0
%   l1 U concatenateLists(l2..ln,m1..mp) otherwise
concatenateLists([],[],[]).
concatenateLists([H|T],[],Out) :-
    concatenateLists(T,[],Out1),
    Out = [H|Out1].
concatenateLists([],[H|T],Out) :-
    concatenateLists([],T,Out1),
    Out = [H|Out1].
concatenateLists([H1|T1],[H2|T2],Out) :-
    concatenateLists(T1,[H2|T2],Out1),
    Out = [H1|Out1].

% divisibleWithN(E, N) = 
%   E % N == 0
divisibleWithN(E, N) :-
    0 is E mod N.

% sumOfElements(l1..ln) = 
%   0 if n == 0
%   l1 + sumOfElements(l2..ln) otherwise
sumOfElements([], 0).
sumOfElements([H | T], Out) :-
    sumOfElements(T, Out1),
    Out = H + Out1.

% sumOfElementsDivisibleWithNAndMoreThanTwoElements(List, N) = 
%   divisibleWithN(sumOfElements(List), N)
sumOfElementsDivisibleWithNAndMoreThanTwoElements(List, N) :-
    countElements(List, Count),
    Count > 2,
    sumOfElements(List, Out),
    divisibleWithN(Out, N).

% countElements(l1..ln) = 
%   0 if n == 0
%   1 + countElements(l2..ln) otherwise
countElements([], 0).
countElements([_ | T], Out) :-
    countElements(T, Out1),
    Out = Out1 + 1.

% addToEnd(l1..ln, E) = 
%   [E] if n == 0
%   l1 U addToEnd(l2..ln, E) otherwise
addToEnd([], E, [E]).
addToEnd([H | T], E, Out) :-
    addToEnd(T, E, Out1),
    Out = [H | Out1].

% determineSublists(l1..ln, N, CurrentSublist) = 
%   nothing if n == 0
%   printwrapper(l1 U CurrentSublist) 
%       and determineSublists(l2..ln, l1 U CurrentSublist)
%       and determineSublists(l2..ln, CurrentSublist)
%       if sumOfElementsDivisibleWithNAndMoreThanTwoElements(l1 U CurrentSublist, N)
%   determineSublists(l2..ln, l1 U CurrentSublist)
%       and determineSublists(l2..ln, CurrentSublist)
%       otherwise
determineSublists([], _, _, []).
determineSublists([H | T], N, CurrentSublist, Out) :-
    addToEnd(CurrentSublist, H, NewSublist),
    sumOfElementsDivisibleWithNAndMoreThanTwoElements(NewSublist, N),
    determineSublists(T, N, NewSublist, Out1),
    determineSublists(T, N, CurrentSublist, Out2),
    concatenateLists(Out1, Out2, NextResults),
    Out = [NewSublist | NextResults].
determineSublists([H | T], N, CurrentSublist, Out) :-
    addToEnd(CurrentSublist, H, NewSublist),
    \+sumOfElementsDivisibleWithNAndMoreThanTwoElements(NewSublist, N),
    determineSublists(T, N, NewSublist, Out1),
    determineSublists(T, N, CurrentSublist, Out2),
    concatenateLists(Out1, Out2, NextResults),
    Out = NextResults.

% determineSublistsWrapper(List) = 
%   printWrapper(EMPTY_LIST)
%       and determineSublists(List, countElements(List), EMPTY_LIST)
determineSublistsWrapper(List, Out) :-
    countElements(List, N),
    determineSublists(List, N, [], Out1),
    Out = [[] | Out1].
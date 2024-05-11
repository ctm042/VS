myfun(N,R) :- integer(N), N>2, N1 is N-1, N2 is N-2, myfun(N1,R1), myfun(N2,R2), R is R1+R2.
myfun(1,3).
myfun(2,7).

myfun2(N,R) :- integer(N), N>2, N1 is N-1, myfun2(N1,X), myfun2(X,R1), Y is N-X, myfun2(Y,R2), R is R1+R2.
myfun2(1,1).
myfun2(2,1).
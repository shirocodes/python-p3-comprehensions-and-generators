#!/usr/bin/env python3

def return_evens(num_list):
   evens = [n for n in num_list if n % 2 == 0] 
   return evens

return_evens([1,2,3,4,5,6,8,9])

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

make_exclamation(["Hello", "I'm doing great", "Python is fun"])

# def get_fibo(length):
#     fibo_seq = []

#     if length == 0:
#         print(fibo_seq)
#         return
#     elif length == 1:
#         fibo_seq = [0]
#     elif length == 2:
#         fibo_seq = [0, 1]
#     else:
#         fibo_seq = [0,1]
#         for i in range(2, length):
#             next_num = fibo_seq[i-1] + fibo_seq[i-2]
#             fibo_seq.append(next_num)
#     print(fibo_seq)

# get_fibo(9)
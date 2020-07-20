# Programming Assignment-1: Computing Paradox

'''
	Question : You are provided with a playlist containing N songs, each has a unique positive integer length.
		   Assume you like all the songs from this playlist, but there is a song, which you like more than others.
		   It is named "Computing Paradox".

		   You decided to sort this playlist in increasing order of songs length.
		   For example, if the lengths of the songs in the playlist were {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}.
		   Before the sorting, "Computing Paradox" was on the kth position (1-indexing is assumed for the playlist) in the playlist.

	   	   Your task is to find the position of "Computing Paradox" in the sorted playlist.


'''

# Code

n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=l[k-1]
l.sort()
for i in range(n):
  if l[i]==a:
    print(i+1)
    exit()
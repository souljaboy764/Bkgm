#!,usr,bin,python
import random

board=map(int,raw_input().split(' '))
bar=raw_input()
a=0
b=0
if bar!='e':	
	for i in bar:
		if i=='a':
			a=a+1
		elif i=='b':
			b=b+1
	bar=[a, b]
else:
	bar=[0,0]

dice=map(int,raw_input().split(' '))
r1=max(dice)
r2=min(dice)

dicecom=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
board=[111]+board
s1=0
s2=0
d1=0
d2=0
moves=[]
m=0
poss=[]
Lv1=[]
Lv2=[]
h=[]
temp=[]
def Generate(state1, roll1,roll2, Z, F):
	
	state3=state1[:]
	arr=[]
	if Z>0:
		if(state3[roll2]>=-1 or state3[roll1]>=-1):
			
			if(state3[roll2]>=1):
				#Z->R2
				#Moves(0, roll2)
				state3[roll2]=state3[roll2]+1
				roll2=0
				
			elif(state3[roll1]>=1):
				#Moves(0, roll1)
				state3[roll1]=state3[roll1]+1
				roll1=0
		
			elif(state3[roll2]>=-1):			
				#Moves(0, roll2)
				if state3[roll2]==-1:
					state3[roll2]=1
				else:
					state3[roll2]=state3[roll2]+1
				roll2=0
				
			elif(state3[roll1]>=-1):			
				#Moves(0, roll1)
				if state3[roll1]==-1:
					state3[roll1]=1
				else:
					state3[roll1]=state3[roll1]+1
				roll1=0
			roll1=max(roll1,roll2)
			roll2=0
			Z=Z-1
		else:
			return arr
			#Moves(-1,-1)
			#if no possible moves, what to do??
	
	if Z>0:
		if(state3[roll1]>=-1):		
			#Moves(0, roll1)
			if state3[roll1]==-1:
				state3[roll1]=1
			else:
				state3[roll1]=state3[roll1]+1
			if(state3 not in arr):
				arr.append(state3)
				return arr
			roll1=0
			roll1=max(roll1,roll2)
			roll2=0
			Z=Z-1
		else:
			arr.append(state3)
			return arr
			#Moves(-1,-1)

	else:
		moves=0
		state=state3[:]
		state2=state3[:]
		flagi=0
		flagj=0
		rx= max(roll1, roll2)
		ry=min(roll1, roll2)
		roll1=rx
		roll2=ry

		for i in range(1,25):

			#roll 1 then roll 2
			if state[i]>=1 and i+roll1<=24 and state[i+roll1]>=-1 :
				flagi=0
				state[i]=state[i]-1
				state[i+roll1]=state[i+roll1]+1
				if(state[i+roll1]==0):
					state[i+roll1]=1
					flagi=1
				temp2=state[:]
				if roll2!=0:
					for j in range(1,25):
						if state[j]>=1 and j+roll2<=24 and state[j+roll2]>=-1 :
							flagj=0
							state[j]=state[j]-1
							state[j+roll2]=state[j+roll2]+1
							if state[j+roll2]==0:
								state[j+roll2]=1
								flagj=1
							if F==1:
								state.append(i)
								state.append(i+roll1)
								state.append(j)
								state.append(j+roll2)
								arr.append(state)
							else:
								if(state not in arr):
									arr.append(state)
						#revert back to i
							state=temp2[:]
				else:
					if F==1:
						state.append(i)
						state.append(i+roll1)
						arr.append(state)
					else:
						if state not in arr:
							arr.append(state)

			state=state3[:]

			#roll 2 then roll 1
			if roll2!=0 and state2[i]>=1 and i+roll2<=24 and state2[i+roll2]>=-1 :
				state2[i]=state2[i]-1
				state2[i+roll2]=state2[i+roll2]+1
				if(state2[i+roll2]==0):
					state2[i+roll2]=1
				temp2=state2[:]
				for j in range(1,25):
					if state2[j]>=1  and j+roll1<=24 and state2[j+roll1]>=-1:
						state2[j]=state2[j]-1
						state2[j+roll1]=state2[j+roll1]+1
						if state2[j+roll1]==0:
							state2[j+roll1]=1

						if F==1:
							state2.append(i)
							state2.append(i+roll2)
							state2.append(j)
							state2.append(j+roll1)
							arr.append(state2)
						else:
							if(state2 not in arr):
								arr.append(state2)
						#revert back to i
						state2=temp2[:]
			state2=state3[:]		
	return arr

def Moves(s1,d1):
	global moves
	global m
	global bar
	if s1==0:
		bar[0]= bar[0] - 1
	moves.append(s1)
	m=m+1
	moves.append(d1)
	m=m+1
	if m==4:
		for i in range(0, 4, 2):
			if moves[i]==0:
				print "Z",moves[i+1]
			elif moves[i]==-1:
				print "pass"
			else:
				print moves[i],moves[i+1]
		exit(0)

def bmove():
	global bar
	global board
	global r1
	global r2

	if(board[r2]>=-1 or board[r1]>=-1):
		
		if(board[r2]>=1):
			#Z->R2
			Moves(0, r2)
			board[r2]=board[r2]+1
			r2=0
			
			
			
		elif(board[r1]>=1):
			Moves(0, r1)
			board[r1]=board[r1]+1
			r1=0
			
			
	
		elif(board[r2]>=-1):
			Moves(0, r2)
			if board[r2]==-1:
				board[r2]=1
			else:
				board[r2]=board[r2]+1
			r2=0
			
			
			
			
		elif(board[r1]>=-1):	
			Moves(0, r1)
			if board[r1]==-1:
				board[r1]=1
			else:
				board[r1]=board[r1]+1
			r1=0
			
		r1=max(r1,r2)
		r2=0
	else:
		Moves(-1,-1)
		
	
	if bar[0]>0:
			
		if(board[r1]>=-1):	
			
			Moves(0, r1)
			if board[r1]==-1:
				board[r1]=1
			else:
				board[r1]=board[r1]+1
			r1=0
			r1=max(r1,r2)
			r2=0
			
		else:
			
			Moves(-1,-1)#only for our board state. bar move.

def prob(a):
	if a[0]==a[1]:
		return 1/36
	else:
		return 1/18

kill={}
kill[1]=11
kill[2]=12
kill[3]=13
kill[4]=14
kill[5]=15
kill[6]=16
kill[7]=6
kill[8]=5
kill[9]=4
kill[10]=3
kill[11]=2
kill[12]=1

def value(state, pre):
	vv=0
	global kill
	if state == '[]':
		vv=-300
	else:
		count=0

		if (state[5]>=2 and pre[5]<=1) or (state[6]>=2 and pre[6]<=1) or (state[18]>=2 and pre[18]<=1):
			vv= vv+110
		
		if (state[5]==1 and pre[5]<1) or (state[6]==1 and pre[6]<1) or (state[18]==1 and pre[18]<1):
			vv= vv+20
		
		if (state[5]>pre[5] and pre[5]>=2) or (state[6]>pre[6] and pre[6]>=2) or (state[18]>pre[18] and pre[18]>=2):
			vv= vv+40
		if state[17]>=2 :
			count=count+40
		if state[18]>=2 :
			count=count+40
		if state[19]>=2:
			count=count+40 
		if state[20]>=2:
			count=count+40
		vv=vv+count
		for i in range(1, 25):
			if pre[i]<state[i] and i<16:
				vv=vv+i
			if state[i]==1 and pre[i]>=1:
				vv= vv - 50

			if state[i]>1 and pre[i]==1:
				vv=vv+70

			if state[i]==1:
				if i>12:
					lim2=24
				else:
					lim2=i+12
				prob=0

				for j in range(i+1,lim2+1):
					if state[j]<=-1:
						prob=prob+kill[j-i]
				vv=vv - (prob*100)

			if state[i]==-1:
				if i>12:
					lim2=24
				else:
					lim2=i+12
				prob=0
				for j in range(i+1,lim2+1):
					if state[j]>=1:
						prob=prob+kill[j-i]
				vv=vv + 5*prob

			if pre[i]==-1 and state[i]>=0:
				vv=vv + 30

	return vv

#main

if board==[111,2,0,0,0,0,-5,0,-3,0,0,0,5,-5,0,0,0,3,0,5,0,0,0,0,-2]:
	if (r1,r2)==(2,1):	
		Moves(12,14)
		Moves(19,20)	
	elif (r1,r2)==(3,1):	
		Moves(17,20)
		Moves(19,20 )	
	elif (r1,r2)==(4,1):	
		Moves(1,2)
		Moves(12,16) 	
	elif (r1,r2)==(5,1):	
		Moves(1,2)
		Moves(12,17 )	
	elif (r1,r2)==(6,1):	
		Moves(12,18)
		Moves(17,18 )	
	elif (r1,r2)==(3,2):	
		Moves(1,4)
		Moves(12,14 )
	elif (r1,r2)==(4,2):	
		Moves(17,21)
		Moves(19,21 )	
	elif (r1,r2)==(5,2):	
		Moves(1,3)
		Moves(12,17 )	
	elif (r1,r2)==(6,2):	
		Moves(1,7)
		Moves(12,14 )	
	elif (r1,r2)==(4,3):	
		Moves(12,15)
		Moves(12,16 )	
	elif (r1,r2)==(5,3):	
		Moves(17,22)
		Moves(19,22) 	
	elif (r1,r2)==(6,3):	
		Moves(1,7)
		Moves(12,15) 	
	elif (r1,r2)==(5,4):	
		Moves(1,5)
		Moves(12,17 )	
	elif (r1,r2)==(6,4):	
		Moves(1,7)
		Moves(12,16 )	
	elif (r1,r2)==(6,5):	
		Moves(1,7)
		Moves(7,12)

if bar[0] > 1:
	
	bmove()
	

else:
	if bar[0]>0:
		bmove()
		#Lv1=Generate(board,r1,r2, bar[0],1)
	bear=0
	last=0
	
	for i in range(19,25):
		if i>0:
			bear=bear+board[i]
			if last==0:
				last=i

	if bear!=15:

		Lv1=Generate(board,r1,r2, bar[0],1)
		val1=[]
		
		for i in Lv1:
			val1.append(value(i,board))
		avg=sum(val1)/float(len(val1))
		mv=[]
		
		for i in range(len(Lv1)):
			if val1[i]>avg:
				mv.append(Lv1[i])
		
		p=random.randint(1,101)
		
		if(p<25):
			ans=mv[random.randint(0,len(mv)-1)][:]
		
		else:
			minn=[]
			d={}

			for i in Lv1:
				summ=0

				for j in range(0, 21):
					x=i[:]
					x[:]= [k*-1 for k in x]
					x.reverse()
					Lv2.append(Generate(x,dicecom[j][0],dicecom[j][1], bar[1], 0)) #need to multiply by -1, since it is enemys move.
					maxx=[]
					maxx.append(-300)
					for p in Lv2:
						for q in p:
							maxx.append(value(q, x))
					summ=summ+(max(maxx)*prob(dicecom[j])) #prob func is if dicecomm[j][0]==dicecomm[j][1], return 1/36 else 1/18
					Lv2=[]
				val=summ
				minn.append(val)
				if val in d.keys():
					d[val].append(i)
				else:
					d[val]=[]
					d[val].append(i)

			ans=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
			ans1=[]
			for i in d[min(minn)]:
				if   (i[25]<18 and len(i)==27) or(i[25]<18 and len(i)>27 and i[27]<18):
					ans1.append(i)
			if ans1!=[]:
				index=random.randint(0,len(ans1)-1)
				ans=ans1[index][:]
			else:
				if minn!=[]:
					index=random.randint(0,len(d[min(minn)])-1)
					ans=d[min(minn)][index][:]

		Moves(ans[25], ans[26])
		Moves(ans[27],ans[28])

	else:#what is the 'O'??
		if r1>=25-last:
			Moves(last,'O')
		else:
			Moves(last,last+r1)
		if r2>=25-last:
			Moves(last,'O')
		else:
			Moves(last,last+r2)

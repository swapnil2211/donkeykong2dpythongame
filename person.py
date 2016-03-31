#Donkey Kong
#Created by Swapnil

from board import *
import sys
from random import *
class Person():

	def __init__(self):
		self.updatedposition=(0,0)

	def move(self,b):
		pass
	

	def update_updatedposition(self,b,inp):
		pass

	def checkWall(self,b):
		if b.getvalue(self.updatedposition)=='X' or b.getvalue(self.updatedposition)=='.':
			return True
		else:
			return False

	def checkStairs(self,b):
		if b.getvalue(self.updatedposition)=='H':
			return True
		else:
			return False
	def checkCoin(self,b):
		if b.getvalue(self.updatedposition)=='C':			
			return True
		else:
			return False

	def checkPlayer(self,b):
		if b.getvalue(self.updatedposition)=='P':
			return True
		else:
			return False

	def checkDonkey(self,b):
		if b.getvalue(self.updatedposition)=='D':
			return True
		else:
			return False

	def checkQueen(self,b):
		if b.getvalue(self.updatedposition)=='Q':
			return True
		else:
			return False

	def checkFireball(self,b):
		if b.getvalue(self.updatedposition)=='O':
			return True
		else:
			return False
	def checkAirFireball(self,b):
		if b.getvalue(self.updatedposition)=='.':
			return True
		else:
			return False
	def checkAir(self,b):
		if b.getvalue(self.updatedposition)=='.':
			return True
		else:
			return False


class  Player(Person):
	
	def __init__(self,b,sc):
		self.__score=sc
		self.__prev=' '
		self.__position=(0,0)
		self.__reloadcount=0			
		self.setPlayerPosition(b)

		
	def getScore(self):
		return self.__score

	def incrementScore(self):
		self.__score+=5
	
	def setPlayerPosition(self,b):
		self.__position = (24,3)
		b.setvalue((24,3),'P')
	
	def getPlayerPosition(self):
		return self.__position
	
	def update_updatedposition(self,b,inp):
		if inp=='w':
			self.updatedposition = ((self.__position[0]-1)%b.getrow(),self.__position[1]%b.getcol())
		
		elif inp=='a':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
	
		elif inp=='s':
			self.updatedposition = ((self.__position[0]+1)%b.getrow(),self.__position[1]%b.getcol())
	
		elif inp=='d':
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		else:
			pass

	def move(self,b,inp,gamelevel,last):

		if(inp ==' '):
			max=b.getrow()
			if(last==1):
			    self.updatedposition = ((self.__position[0])%b.getrow(),(self.__position[1]+4)%b.getcol()) 
			    if b.getvalue(self.updatedposition)=='-' or b.getvalue(self.updatedposition)=='C':
			      self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]+1)%b.getcol())	
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)

			      self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]+1)%b.getcol())
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,' ')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)
			      self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]+1)%b.getcol())
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,' ')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)
			      self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]+1)%b.getcol())
			      b.setvalue(self.__position,' ')
			      b.setvalue(self.updatedposition,'P')
			      self.__position = self.updatedposition	
		       	      b.printlist()
			      time.sleep(0.2)
			elif(last==0):
			    self.updatedposition = ((self.__position[0])%b.getrow(),(self.__position[1]-4)%b.getcol()) 
			    if b.getvalue(self.updatedposition)=='-' or b.getvalue(self.updatedposition)=='C':
			      self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]-1)%b.getcol())	
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)
			      self.updatedposition = ((self.__position[0]-1)%b.getrow(),(self.__position[1]-1)%b.getcol())
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,' ')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)
			      self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]-1)%b.getcol())
			      if b.getvalue(self.updatedposition)=='.':
				b.setvalue(self.__position,' ')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition	
				b.printlist()
				time.sleep(0.2)
			      self.updatedposition = ((self.__position[0]+1)%b.getrow(),(self.__position[1]-1)%b.getcol())
			      b.setvalue(self.__position,' ')
		              b.setvalue(self.updatedposition,'P')
		              self.__position = self.updatedposition	
			      b.printlist()	
			      time.sleep(0.2)
		else:
			self.update_updatedposition(b,inp)
			if self.checkDonkey(b)==True:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'D')
				self.__position = self.updatedposition
				return -1
		
			elif self.checkQueen(b)==True:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'W')
				self.__position = self.updatedposition
				time.sleep(0.2)
				return 5

			if self.checkFireball(b)==True:
				b.setvalue(self.__position,'_')			
				prev=b.getvalue(self.updatedposition)
				b.setvalue(self.updatedposition,'O')	
				self.__position = self.updatedposition
				return -1
	
			elif self.checkWall(b)==True:
				print "You have hit the wall. Can't Go"
		
			elif self.checkCoin(b)==True:
				h = self.collectCoin(gamelevel) 			
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition
				if h==-1:
					return 2	
			elif  inp=='w' and self.checkStairs(b)==True:
				b.setvalue(self.__position,'H')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition
			
			elif inp=='s' and b.getvalue(self.__position)=='H' and self.checkStairs(b)==True:
				b.setvalue(self.__position,'H')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition
			else:
				if( inp=='w'):
					b.setvalue(self.__position,'H')
				else:
					b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'P')
				self.__position = self.updatedposition

	def collectCoin(self,gamelevel):
		self.incrementScore()
		self.__reloadcount+=1
		if self.__reloadcount%(25*(gamelevel))==0:
			return -1

class Donkey(Person):
	
	def __init__(self,b):
		self.__position = (0,0)
		self.setDonkeyPosition(b)
		
	def setDonkeyPosition(self,b):
		self.__position = (4,3)
		b.setvalue((4,3),'D')
	
	def getDonkeyPosition(self):
		return self.__position

	def update_updatedposition(self,b):
		mov = randint(1,2)
		if mov==1:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())

		elif mov==2:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())

	def move(self,b):
		self.update_updatedposition(b)
		if self.checkPlayer(b)==True and b.getvalue(self.__position)!='D/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'D')
			self.__position = self.updatedposition
			return -1			
		elif self.checkPlayer(b)==True:
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'D')
			self.__position = self.updatedposition
			return -1			
		elif self.checkWall(b)==True:
			pass
		elif self.checkDonkey(b)==True:
			pass

		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='-':
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='D/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='C/D':
			b.setvalue(self.__position,'C')
			b.setvalue(self.updatedposition,'D/H')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True:
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'D/H')
			self.__position = self.updatedposition		
		
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='D/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='D/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='C/D':
			b.setvalue(self.__position,'C')
			b.setvalue(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalue(self.__position)!='C/D':
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'C/D')
			self.__position = self.updatedposition
		elif b.getvalue(self.__position)=='D/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'D')
			self.__position = self.updatedposition
		elif self.checkAir(b)==True:
			pass		
		else:
			if b.getvalue(self.__position)=='C/D':
				b.setvalue(self.__position,'C')
				b.setvalue(self.updatedposition,'D')
				self.__position = self.updatedposition

			else:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'D')
				self.__position = self.updatedposition
	
class Fireball(Person):
	def __init__(self,b):
		self.__position = (4,4)
		b.setvalue((4,4),'O')
		self.__prev='d'
	
	def getFireballPosition(self):
		return self.__position
	def getFireballx(self):
		return self.__position[0]

	def update_updatedposition(self,b):
		if(self.__prev=='d'):
			mov=2
		else:
			mov=1
		if mov==1:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]-1)%b.getcol())
		elif mov==2:
			self.updatedposition = (self.__position[0]%b.getrow(),(self.__position[1]+1)%b.getcol())
		if self.updatedposition[0]==24 and self.updatedposition[1]==1:						
			if self.checkPlayer(b)==True:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'O')
				self.__position = (-1,-1)
				return -1
			else:			
				b.setvalue(self.updatedposition,'-')
				b.setvalue(self.__position,'-')
				self.updatedposition = (-1,-1)
				self.__position=self.updatedposition

	def move(self,b):
		self.update_updatedposition(b)
		if self.updatedposition[0]==-1 and self.updatedposition[1]==-1:
			pass
		if(self.updatedposition[0]+1=='H'):
			ab=randint(1,2)
			if(ab==1):
				self.updatedposition = ((self.updatedposition[0]+4)%b.getrow(),self.updatedposition[1]%b.getcol())
		if self.checkPlayer(b)==True and b.getvalue(self.__position)=='O/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'O')
			self.__position = self.updatedposition
			return -1			
		elif self.checkPlayer(b)==True:
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'O')
			self.__position = self.updatedposition
			return -1				
		elif self.checkDonkey(b)==True:
			pass
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='O/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalue(self.__position)!='C/O':
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='-':
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='O/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True and b.getvalue(self.__position)=='C/O':
			b.setvalue(self.__position,'C')
			b.setvalue(self.updatedposition,'O/H')
			self.__position = self.updatedposition
		elif self.checkFireball(b)==True:
			b.setvalue(self.__position,'O')
			b.setvalue(self.updatedposition,'O')
			self.__position = self.updatedposition
		elif self.checkStairs(b)==True:
			b.setvalue(self.__position,'-')
			b.setvalue(self.updatedposition,'O/H')
			self.__position = self.updatedposition		
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='O/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif self.checkCoin(b)==True and b.getvalue(self.__position)=='C/O':
			b.setvalue(self.__position,'C')
			b.setvalue(self.updatedposition,'C/O')
			self.__position = self.updatedposition
		elif b.getvalue(self.__position)=='O/H':
			b.setvalue(self.__position,'H')
			b.setvalue(self.updatedposition,'O')
			self.__position = self.updatedposition
		elif self.checkAirFireball(b)==True:			
			if self.__prev=='d':
				self.updatedposition = ((self.__position[0]+4)%b.getrow(),(self.__position[1]+1)%b.getcol())
			else:
				self.updatedposition = ((self.__position[0]+4)%b.getrow(),(self.__position[1]-1)%b.getcol())
			if self.checkCoin(b)==True and b.getvalue(self.__position)=='C/O':
				b.setvalue(self.__position,'C')
				b.setvalue(self.updatedposition,'C/O')
				self.__position = self.updatedposition
			elif self.checkCoin(b)==True:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'C/O')
				self.__position=self.updatedposition
			else:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'O')
				self.__position=self.updatedposition
			dd=randint(1,2)
			if dd==1:
				self.__prev='d'
			else:
				self.__prev='a'
		elif self.checkWall(b)==True:
			if self.__prev=='d':
				self.__prev='a'
			else:
				self.__prev='d'
			self.update_updatedposition(b)	
		else:
			if b.getvalue(self.__position)=='C/O':
				b.setvalue(self.__position,'C')
				b.setvalue(self.updatedposition,'O')
				self.__position = self.updatedposition

			else:
				b.setvalue(self.__position,'-')
				b.setvalue(self.updatedposition,'O')
				self.__position = self.updatedposition	









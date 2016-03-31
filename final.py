#Donkey Kong
#Created by Swapnil
from random import *
from person import *
from board import *
import sys
import time

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

def my_print(text,colour):
                sequence = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
		p = sys.stdout                
		p.write(sequence)

def getchar():

  	import tty, termios, sys
   	fd = sys.stdin.fileno()
  	old_settings = termios.tcgetattr(fd)
   	try:
      		tty.setraw(sys.stdin.fileno())
      		ch = sys.stdin.read(1)
   	finally:
      		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   	return ch
   



def main():
	try:
		lev = (int)(raw_input("Enter difficulty level(1/2/3):\n"))	
		b = Board(26,35,lev)
		b.set_board()
		sc=0
		p = Player(b,sc)
		donkeys=1
		loop_end = False

		d = []
		f = []
		life=3
		chances=0
		numoffball=1		
	
		if lev==1:
			donkeys = 1
		elif lev==2:
			donkeys = 3
		elif lev==3:
			donkeys = 5
		else:
			print "Level Invalid\n"
			return

		for i in range(0,donkeys):
			dk = Donkey(b)
			d.append(dk)
		
		fir=Fireball(b)
		f.append(fir)
	
		b.printlist()
		print "Score: %d"%(p.getScore())
		print "To begin game, enter 'W/A/S/D/:SPACE:/Q' only."	
		y = getchar()
		y = y.lower()
		prev= 1	
		while y!='q':
			retforplayer = p.move(b,y,lev,prev) 
			sc=p.getScore()
			chances=chances+1
			if lev==1:
				if(chances%30==0):
					fir = Fireball(b)
					f.append(fir)
					numoffball=numoffball+1
			elif lev==2:
				if(chances%20==0):
					fir = Fireball(b)
					f.append(fir)
					numoffball=numoffball+1
			elif lev==3:
				if(chances%15==0):
					fir = Fireball(b)
					f.append(fir)
					numoffball=numoffball+1
			if(retforplayer==-1):
				life=life-1
				if(life==0):
					point=(24,1)
					b.setvalue(point,'-')
					b.printlist()
					print "Final Score: %d"%(p.getScore())
					print "Game Ends. You have been eaten!\n"			
					break
				else:
					p=Player(b,sc-25)

			elif(retforplayer==5):
				b.printlist()				
				b = Board(26,35,lev)
				b.set_board()
				p = Player(b,sc+50)				
				donkeys=1
				numoffball=1
				chances=0
				d = []		
				f = []
				if lev==1:
					donkeys = 1
				elif lev==2:
					donkeys = 3
				elif lev==3:
					donkeys = 5
				for i in range(0,donkeys):
					don = Donkey(b)
					d.append(don)
				fir = Fireball(b)
				f.append(fir)	
				b.printlist()

			if(d[0].move(b)==-1 or d[0].getDonkeyPosition()==p.getPlayerPosition()):
				life=life-1
				p=person.Player(b,sc-25)				
				if(life==0):				
					loop_end=True
			else:
				for i in range(0,numoffball):
					xval=f[i].getFireballx()
					if(xval==-1):
						continue
					if f[i].move(b)==-1 or p.getPlayerPosition()==f[i].getFireballPosition():
						life=life-1
						p=Player(b,sc-25)
						if(life==0):							
							loop_end = True			
							break


	
			b.printlist()
			print "Score: %d"%(p.getScore())
			if loop_end == True:
				point=(24,1)
				b.setvalue(point,'-')
				b.printlist()
				print "Final Score: %d"%(p.getScore())
				print "Game Ends!! Donkey has eaten you.\n"
				break		
			if y=='d':
				prev=1
			elif y=='a':
				prev=0
			print "Enter your move(Type Character W/A/S/D/:space:/Q): "
			y = getchar()
			y = y.lower()

			if y=='q':
				break
		if y=='q':
			b.printlist()
			print "Final Score: %d"%(p.getScore())
			print "You have chosen to quit.\n"
	except (AttributeError):
		print "To begin game, enter 'W/A/S/D/:space:/Q only. Then you can enter anything."


if __name__ == "__main__":
	main() 



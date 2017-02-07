#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import random

class Deck:
	def __init__(self):
		self.deck = []
		self.deck_num = 51

	def create_deck(self):
		count = 0
		for i in range(4):
			if i == 0: mark = 'c' # クローバー
			elif i == 1: mark = 'd' # ダイヤ
			elif i == 2: mark = 'h' # ハート
			else: mark = 's' # スペード
			for j in range(1,14):
				lis = []
				lis.append(mark)
				lis.append(j)
				self.deck.append(lis)
		return self.deck

	def prize_dic(self):
		dic = {
			0:"No Pair",
			1:"One Pair",
			2:"Two Pair",
			3:"Three of a Kind",
			4:"Straight",
			5:"Flush",
			6:"Full House",
			7:"Four of a Kind",
			9:"Straight Flush",
			10:"Royal Straight Flush"
		}
		return dic

class Player:
	def __init__(self):
		self.hand = list
	def deal_card(self, deck, deck_num, num):
		if num != 1: return_cards = []
		for i in range(num):
			rand = random.randint(0, deck_num)
			if num == 1: return_cards = deck[rand]
			else: return_cards.append(deck[rand])
			del deck[rand]
			deck_num -= 1
		return return_cards

	def change(self, deck, deck_num):
		print "\n%s, Prease enter the number you want to change"%self.name
		change = raw_input()
		change = map(int, change)
		for r in change:
			if r > 0 and r < 6:
				self.hand[r-1] = self.deal_card(deck, deck_num, 1)
				deck_num -= 1
		return len(change)

	def print_hand(self):
		print " \t -*- %s's hand -*- \t "%self.name
		print " 1\t 2\t 3\t 4\t 5\t"
		for i in self.hand:
			h = map(str, i)
			print "-".join(h) + "\t",
		print ""

	def judge(self):
		flush = 0
		straight = 0
		pair = 0
		prize = 0
		hand = sorted(self.hand, key=lambda x:x[1])
		suto = self.hand[0][0]
		for i, h in enumerate(self.hand):
			#フラッシュ判別
			if h[0] == suto: flush += 1
			#ストレート判別
			if i == 0: num = h[1]
			else:
				if num+1 == h[1]:
					straight += 1
					num = h[1]
		#ペア判別
		for i in range(4):
			for j in range(i+1, 5):
				if self.hand[i][1] == self.hand[j][1]:
					pair += 1
		if pair == 4: prize == 6
		elif pair == 6: prize == 7
		else: prize = pair
		if straight == 4: prize += 4
		if flush == 5: prize += 5
		return prize

def main():
	d = Deck()
	p1 = Player()
	p2 = Player()
	p1.name = "player1"
	p2.name = "player2"
	d.deck = d.create_deck()
	#手札を配る
	p1.hand = sorted(p1.deal_card(d.deck, d.deck_num, 5))
	d.deck_num -= 5
	p2.hand = sorted(p2.deal_card(d.deck, d.deck_num, 5))
	d.deck_num -= 5
	p1.print_hand()
	p2.print_hand()
	#手札を変える
	d.deck_num -= p1.change(d.deck, d.deck_num)
	d.deck_num -= p2.change(d.deck, d.deck_num)
	#役判別
	dic = d.prize_dic()
	p1.print_hand()
	result1 = p1.judge()
	print dic[result1]
	p2.print_hand()
	result2 = p2.judge()
	print dic[result2]
	if result1 > result2: print "\n --%s is win!"%p1.name
	elif result1 < result2: print "\n --%s is win!"%p2.name
	else: print "draw"

if __name__ == '__main__':
	main()

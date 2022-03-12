# -*- coding: utf8 -*-
import scr
import config
PPP = config.NUM_PC
def pc_prov(pc):
	stroka=''
	if 1:
		for i in range(len(pc)):
			if pc[i]=='{':
				stroka+=pc[i:]
				break
			elif pc[i]!=' ':
				stroka+=pc[i]
				if pc[i].isdigit() and pc[i+1]==" ":
					l=stroka[:i+1]
					stroka+=' '
		for i in range(len(stroka)):
			if stroka[i]==' ' and stroka[i+1].isalpha():
				commj=stroka[i+1:]
				break
		if l.lower()==config.TOKEN_PC[PPP][0] or l=="pc999":
			kop=scr.com_bot(commj)
			return kop
		else: return 0
	else: return 0
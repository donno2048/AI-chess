import threading,random,chess;pi='';dic={ 'P': 100, 'N':320, 'B': 330, 'R': 500, 'Q': 900,'K':0}
board=chess.Board();board.push(chess.Move.from_uci('0'*4))
def g(b:str,x:str,d:dict,y:int):
	z=0;xx=x.capitalize()
	for i in range(64):
		if b.replace(' ','').replace('\n','')[i]==x:z+=dic[xx]+int(d[xx][i])
	if xx==y*x:z=-z
	return z
def ai(b,d:dict,y:int):
	zq=[]
	for i in list(b.legal_moves):
		b.push(i);z=[]
		if b.is_checkmate():return list(b.legal_moves)[i]
		for j in list(b.ligal_moves):
			b.push(j)
			q=b.is_checkmate()*(-1000000)
			bb=str(b)
			b.pop()
			bbb=0
			for k in 'PpRrNnBbQqKk':bbb+=g(bb,k,d,y)
			z+=[bbb+q]
		b.pop();zq+=[min(z)]
	return list(b.legal_moves)[zq.index(max(zq))]
def fi():input('to stop the process press enter')
def play():
    while True:
        F=input('from: ')+input('to: ').lower()
        if chess.Move.from_uci(F+'q') in board.legal_moves :F+=input('what would you like to promote to?/n')
        if chess.Move.from_uci(F) in board.legal_moves:board.push(chess.Move.from_uci(F));break
        else:print('you cannot do that')
def y(x:str):
	y=''
	for i in range(8):y+=x.split('\n')[i]+' '+str(8-i)+'\n'
	return y
if input('t for train and p for play')=='t':
	r=0;t=threading.Thread(target=fi);t.start()
	while t.is_alive():
		r+=1;t=r%48;board=chess.Board();sos=open('ai.txt','r').readlines();so=sos[3*t*2**9:3*(t+1)*2**9];ii,jj=random.randint(0,2**9-1),random.randint(0,2**9-1);di,dict=dict(so[ii*3]),dict(so[jj*3])
		while True:
			if board.result()[0]=='*':board.push(ai(board,di,-1))
			elif '/' not in board.result():so[3*ii+1]=str(int(so[3*ii+1])+1);so[3*ii+2]=str(int(so[3*ii+2]-1));so[3*jj+2]=str(int(so[3*jj+2])+1);so[3*jj+1]=str(int(so[3*jj+1])+1);break
			if board.result()[0]=='*':board.push(ai(board,dict,1))
			elif '/' not in board.result():so[3*ii+1]=str(int(so[3*ii+1])+1);so[3*ii+2]=str(int(so[3*ii+2])+1);so[3*jj+2]=str(int(so[3*jj+2])-1);so[3*jj+1]=str(int(so[3*jj+1])+1);break
			if '/' in board.result():so[3*ii+1]=str(int(so[3*ii+1])+1);so[3*jj+1]=str(int(so[3*jj+1])+1);break
		sos[3*t*2**9:3*(t+1)*2**9]=so;open('ai.txt','w').writelines(sos)
else:
	for i in range(48):fi=[(int(open('ai.txt','r').readlines()[3*i*2**9+j*3+2])+1)/(int(open('ai.txt','r').readlines()[3*i*2**9+j*3+1])+1) for j in range(2**9)];d[i]=list(open('ai.txt','r').readlines()[3*i*2**9+3*fi.index(max(fi))])[i*8:(i+1)*8]
	di={'P':d[0:64],'N':d[64:128],'B':d[128:192],'R':d[192:256],'Q':d[256:320],'K':d[320:384]}
	while board.result()[0]=='*':
		print(y(board.unicode().replace('·','⧈'))+'A B C D\U00002006E F G H'.replace(' ','\U0000205F'+'\U00002006'));play();q=[]
		if board.result()[0]=='*':board.push(ai(board,di,1))
	print('black wins'*(((int(str(board.result())[2])*(3-int(str(board.result())[2])))-2)/(-2))+'white wins'*(int((str(board.result())[0])-1)**2)+'draw'*(str(board.result()).count('/')/2))

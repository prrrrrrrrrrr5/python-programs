'''
Realizza le funzioni ricorsive e/o iterative

Sapendo che:
1)Nel Cifrario di Cesare:
	ogni carattere diventa quello k posizioni dopo						
	es. cesare("abc",3)="def" 
		perchè a->d b->e c->f
	per ritornare un carattere k posizioni dopo usa:
		chr(ord(s[0])+k) 
		in cui:
			ord restituisce il valore sulla tabella ASCII 
				corrispondente al carattere
			sommo k 
			chr trasforma il numero nel carattere corrispondente

2)La Sequenza di ungu è:
	dato n
		se n=1 ritorna 100
		se n>1 ritorna 
			n*2 se n pari 
			n+1 se n dispari 
	 es n=10	ungu=20 10 16 8 12 6 8 4 4 100 perchè
			10*2=20
			9+1=10
			8*2=16
			7+1=8
			6*2=12
			5+1=6
			4*2=8
			3+1=4
			2*2=4
			100
	usa str(n) per renderla stringa e concatenare


Crea una classe che data una stringa: 
	1)la codifica col codice di cesare									punti 20	16
	2)con l'ord() del primo carattere della stringa 					punti 20	20
		crea la sequenza di ungu
	3)crea una lista con gli ord() di tutti i caratteri					punti 20	20
	4)cerca all'interno della lista										punti 20	20
realizza get set e __str__												punti 20	20
																Totale	punti 100	96
															Sufficienza	punti 60
Voto			9,6
Voto reale		9,75
Note		Ottima verifica!
'''
class VerRic:
    def __init__(self,stringa,k): #Inizializza la lista
        self.__s=stringa
        self.__k=k
        self.__l,self.__lOrd=self.codifica(self.__k)
        self.__ungu=self.ungu(ord(self.getLista()[0]))
    
    
    
    def getUngu(self):
        return self.__ungu
        
    def getStringa(self): #Ritorna la stringa
        return self.__s
    
    def getK(self):
        return self.__k

    def getLista(self): #Ritorna la lista chr
        return self.__l
    
    def getListaOrd(self): #Ritorna la lista ord
        return self.__lOrd
    
    
    
    def setStringa(self,s): #Setta la stringa
        #self.__init__(s, self.__k)
        self.__s=s
        self.__l,self.__lOrd=self.codifica(self.__k)
        self.__ungu=self.ungu(ord(self.getLista()[0]))
        
    def setK(self,k):
        self.__k=k
        self.__l,self.__lOrd=self.codifica(self.__k)
        self.__ungu=self.ungu(ord(self.getLista()[0]))
        
    def setLista(self,k): #Setta la lista
        self.__l,self.__lOrd=self.codifica(k)
    
    
    
    def codifica(self,k,n=0,l=[],lOrd=[]): #Codifica di cesare
        if n!=len(self.__s):
            l.append(chr(ord(self.__s[n])+k))
            lOrd.append(ord(self.__s[n]))
            self.codifica(k,n+1)
        return l,lOrd
    
    def ungu(self,n,l=[]): #Funzione ungu
        if n==1:
            l.append(str(100))
            #return str(100)
        else:
            if n%2==0:
                l.append(str(n*2))
                self.ungu(n-1)
                #return str(n*2)+self.ungu(n-1)
            else:
                l.append(str(n+1))
                self.ungu(n-1)
                #return str(n+1)+self.ungu(n-1)
        return l
    
    def cercaR(self,x,l,i=0): #Ricerca
        if i==len(l): return False,i
        else:
            if l[i]==x: return True,i
            else:
                return self.cercaR(x,l,i+1)
    
    def __str__(self): #Str
        return 'Stringa = '+self.getStringa()+'\nLista_ORD = '+str(self.getListaOrd())+'\nK = '+str(self.getK())+'\nLista_CHR = '+str(self.getLista())+'\nSeguenza di Ungu = '+str(self.getUngu())


stringa=input("Inserisci una stringa \n --> ")
k=int(input("Inserisci di seguito il k \n --> "))
v=VerRic(stringa,k)
#print(v.ungu(ord(v.getLista()[0])))
#print(v.getLista())
#print(v.getListaOrd())
t=input("Inserire un chr o un ord da cercare \n --> ")
if t.isnumeric():
    t=int(t)
    trovato,index=v.cercaR(t, v.getListaOrd())
else:
    trovato,index=v.cercaR(t, v.getLista())
print(v)
if trovato:
    print("Trovato alla posizione ",index)
else:
    print("Non trovato")
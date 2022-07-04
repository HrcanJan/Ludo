def Sachovnica(n):
    #Funkcia kresli šachovnicu n*n a vrati maticu a
    a = [[' ' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1):
                if(j<int((n/2)-1) or j>int((n/2)+1)):
                    a[i][j]=' '
                else:
                    a[i][j]='*'
            if((i>0 and i<int((n/2)-1)) or (i<n-1 and i>int((n/2)+1))):
                if(j<int((n/2))-1 or j>int((n/2)+1)):
                    a[i][j]=' '
                elif(j!=int(n/2)):
                    a[i][j]='*'
                else:
                    a[i][j]='D'
            if(i==int((n/2)-1) or i==int((n/2)+1)):
                if(j!=int(n/2)):
                    a[i][j]='*'
                else:
                    a[i][j]='D'
            if(i==int(n/2)):
                if(j==0 or j==n-1):
                    a[i][j]='*'
                elif(j!=int(n/2)):
                    a[i][j]='D'
                else:
                    a[i][j]='X'
    pisi(a, n)
    return a

def pisi(a, n):
    #Funcia vypisuje maticu. Prvo vypíše celé j, potom i a i-ty riadok 
    print(" ", end=' ')
    for j in range(n):
        if(j>9):
            print(j%10, end=' ')
        else:
            print(j, end=' ')
    print('')
    for i in range(n):
        if(i>9):
            print(i%10, end=' ')
        else:
            print(i, end=' ')
        for j in range(n):
            print(a[i][j], end=' ')
        print('')
    print('')

def Hra(a, n):
    #Tu sa koná tok hry. Hra je v infinite loope. Každého hráča predstavuje jeden infinite loop ktorého sa brakeujeme ak x nie je 6, alebo ak x bolo 6 3 krat za radom
    max=int(n/2)-1
    r1=max #Predstavuje počet figúrov prvého hráča, ktoré sa NEnachádzajú na tabuli
    r2=max #To isté pre druhého hráča
    while True:
        z=0 #Je rovno setovaný na 0, zväčšuje sa vždy keď je x=6, ak je x=6 tri kráť tak bude na šore následovný hráč
        while True:
            s=0 #Keď sa vykoná funkia Tah() tak sa chcem zbaviť 2 for loopy, to konám skom
            c=0 #Predstavuje counter počet figúrov jedného hráča na tabule
            w=0 #w=1 je indikator, že hráč chce postaviť svoju figúru na tabuľu
            y=1 #indikátor, ktorý povie hráč ktorou figúrou hráč chce vykonať poťah. Pozýva sa len ak na tabule jesto viac ako jeden hráč. Maticu preveráva kým nenajde prvú figúru, ak hráč si zvolil ťah s druhov figúrov tak sa pokračuje hľadanie.
            game=0 #Ak game=1 hráč zvíťazil
            x=random.randint(1,6) #Generuje random celé číslo od 1 do 6
            print("x =", x)
            for i in range(n):
                for j in range(n):
                    if(a[i][j]=='A'):
                        c+=1
            r1=max-c #Počet figúrov jedného hráča na šachovnice
            if(c>1):
                print("Vyberte si ktorou figurou odohrate tah (1):")
                while True:
                    y=int(input())
                    if(y>0 and y<=c):
                        break
            if(x==6 and r1!=max):
                z+=1
                if(r1>0):
                    print("Chcete postavit figuru na tabulu? (1) 1 - Ano, 0 - Nie:")
                    while True:
                        w=int(input())
                        if(w==0 or w==1):
                            break
            if(z==3):
                break
            if(r1!=max and w!=1):
                for i in range(n):
                    for j in range(n):
                        if(a[i][j]=='A'):
                            if(y!=1):
                                y-=1
                                continue
                            if(i<int(n/2) and i>0 and j==int(n/2)):
                                Garaz(a, n, i, j, 'A', x) #Ak hráč chybov vybral ťah figúre, ktorej poťah nie je možný, ťah vykoná prvá voľná figúra po nej ak jestvuje
                            else:
                                Tah(a, n, i, j, i, j, 'A', 'B', x)
                                s=1
                                break
                        if(s==1):
                            break
            pisi(a, n)
            if(r1==max):
                w=1
            if(r1!=0):
                if(x==6 and w==1):
                    a[0][int((n/2)+1)]='A';
                    pisi(a, n)
                    r1-=1
            for i in range(1, int(n/2)): #Tento for cyklus preveráva, či sú namiesto všetkých D postavené A
                if(a[i][int(n/2)]!='A'):
                    game=0
                    break
                game=1
            if(game==1):
                print("Gratulujeme, zvitazili ste! (1)")
                exit(9) #Funkcia vystupuje z programe aj končí sa hra
            if(x!=6):
                break
            
        z=0    
        while True:
            s=0
            c=0
            w=0
            y=1
            game=0
            x=random.randint(1,6)
            print("x =", x)
            for i in range(n):
                for j in range(n):
                    if(a[i][j]=='B'):
                        c+=1
            r2=max-c
            if(c>1):
                print("Vyberte si ktorou figurou odohrate tah (2):")
                while True:
                    y=int(input())
                    if(y>0 and y<=c):
                        break
            if(x==6 and r2!=max):
                z+=1
                if(r2>0):
                    print("Chcete postavit figuru na tabulu? (2) 1 - Ano, 0 - Nie:")
                    while True:
                        w=int(input())
                        if(w==0 or w==1):
                            break
            if(z==3):
                break
            if(r2!=max and w!=1):
                for i in range(n):
                    for j in range(n):
                        if(a[i][j]=='B'):
                            if(y!=1):
                                y-=1
                                continue
                            if(i>int(n/2) and i<n-1 and j==int(n/2)):
                                Garaz(a, n, i, j, 'B', x)
                            else:
                                Tah(a, n, i, j, i, j, 'B', 'A', x)
                                s=1
                                break
                        if(s==1):
                            break
            pisi(a, n)
            if(r2==max):
                w=1
            if(r2!=0):
                if(x==6 and w==1):
                    a[n-1][int((n/2)-1)]='B';
                    pisi(a, n)
                    r2-=1
            for i in range(n-2, int(n/2), -1):
                if(a[i][int(n/2)]!='B'):
                    game=0
                    break
                game=1
            if(game==1):
                print("Gratulujeme, zvitazili ste! (2)")
                exit(9)
            if(x!=6):
                break

def Tah(a, n, i, j, p, q, c, d, x):
    s=0 #s=1 je indikátor, že poťah nie možný, vteda nič sa nedeje
    k=0 #Musel som postaviť k na 0, žeby mi nerobilo chybu v 257 rade
    if(i<=int(n/2) and j>int(n/2)): #Predstavuje kvadrant, vteda 1/4 celkovej šachovnice
        for k in range (x):
            if(a[i+1][j]=='*'):
                i+=1
            elif(j!=n-1 and a[i][j+1]=='*'): #j!=n-1 dáva pozor aby som nevychádzal z rangeu matice
                j+=1
            elif(j!=n-1 and (a[i][j+1]==c or a[i][j+1]==d)):
                j+=1
            elif(a[i+1][j]==c or a[i+1][j]==d):
                i+=1
            else:
                k=k-1
                break
        x=(x-k-1) #V prípade, že ani jedné if nebolo splnené, prechádzame na následovný kvadrant, predsa v tom kvadrante sa odohrá x-k lebo toľko ešte chýbalo sa pohybovať
    if(i>int(n/2) and j>=int(n/2)):
        for k in range (x):
            if(c=='B' and j==int(n/2)): #V prípade, že hráč stojí pred svojou garážou, koná sa tento if
                i-=1;
                if(a[i][j]=='X' or a[i][j]==c):
                    x=0
                    s=1
                    break
            elif(a[i][j-1]=='*'):
                j-=1
            elif(i!=n-1 and a[i+1][j]=='*'):
                i+=1
            elif(i!=n-1 and (a[i+1][j]==c or a[i+1][j]==d)):
                i+=1
            elif(a[i][j-1]==c or a[i][j-1]==d):
                j-=1
            else:
                k=k-1
                break
        x=(x-k-1)
    if(i>=int(n/2) and j<int(n/2)):
        for k in range (x):
            if(a[i-1][j]=='*'):
                i-=1
            elif(j!=0 and a[i][j-1]=='*'):
                j-=1
            elif(j!=0 and (a[i][j-1]==c or a[i][j-1]==d)):
                j-=1
            elif(a[i-1][j]==c or a[i-1][j]==d):
                i-=1
            else:
                k=k-1
                break
        x=(x-k-1)
    if(i<int(n/2) and j<=int(n/2)):
        for k in range (x):
            if(c=='A' and j==int(n/2)):
                i+=1;
                if(a[i][j]=='X' or a[i][j]==c):
                    x=0
                    s=1
                    break
            elif(a[i][j+1]=='*'):
                j+=1
            elif(i!=0 and a[i-1][j]=='*'):
                i-=1
            elif(i!=0 and (a[i-1][j]==c or a[i-1][j]==d)):
                i-=1
            elif(a[i][j+1]==c or a[i][j+1]==d):
                j+=1
            else:
                k=k-1
                break
        x=(x-k-1)
    if(x>0):
        Tah(a, n, i, j, p, q, c, d, x) #V prípade, že prechádzame z 4. kvadrantu do 1., tak použijeme rekurziu.
    elif(s==0 and a[i][j]!=c):
        a[i][j]=c
        a[p][q]='*'

def Garaz(a, n, i, j, c, x):
    #Funkcia sa pozýva len ak sa určitý hráč nachádza v garáže. Ak poťahom by hráč stupil na svoju figúru alebo by dostál veľké číslo, nič sa nedeje.
    if(c=='A'):
        if(i+x<=int((n/2)-1)):
            if(a[i+x][int(n/2)]!='A'):
                a[i+x][int(n/2)]='A'
                a[i][j]='D'
    if(c=='B'):
        if(i-x>=int((n/2)+1)):
            if(a[i-x][int(n/2)]!='B'):
                a[i-x][int(n/2)]='B';
                a[i][j]='D';
     
import random #Používam randint z tejto library
while True:
    n=int(input())
    if(n%2==1):
        break  
a=Sachovnica(n)
Hra(a, n)


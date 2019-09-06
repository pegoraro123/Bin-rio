num=int(input('digite um número em forma decimal: '))#interage com o usuário
x=num
k=[]
while (num>0):#executa só se o número for maior que 0
    a=int(num%2)
    k.append(a)#coloca a na lista k 
    num=(num-a)/2
k.append(0)
string=""
for j in k[::-1]:#itera k no j fazendo com que o número resultante seja mudado de trás para frente para ficar coerente com os números binários
    string=string+str(j)#transforma em string
print('O binário de %d é %s'%(x, string))
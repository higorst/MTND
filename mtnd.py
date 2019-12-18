# lista de estados
estados = input().split()

# alfabeto de entrada
alfabeto_entrada = input().split()

# alfabeto da fita
alfabeto_fita = input().split()

# simbolo que limita a fita a esquerda
limite = input()

# simbolo de branco da fita
simbolo_branco = input()

# numero total de transicoes
n = int(input())
t = dict()  # armazena as transicoes

# quintuplas ( estado origem, caracater a ser lido, estado destino, simbolo a ser escrito, direcao [E, D] )
#					s[0]			s[1]				s[2]				s[3]				s[4]
for i in range(n):
	q = input().split() # quintupla
	k = (q[0],q[1]) 	# chave
	if k not in t:
		t[k] = []
	t[k].append([q[2], q[3], q[4]])

# estado inicial
estado_inicial = input()

# lista de estados finais
estados_finais = input().split()

# lista de palavras a serem testadas
palavras = input().split()

for palavra in palavras:
	strg = list((limite + palavra))
	strg.append(simbolo_branco)

	# Possibilidades de caminho
	# para garantir o nao determinismo
	c = [(estado_inicial, 1, strg)] 

	# variavel que verifica o fim da execucao (MT parada)
	s = True 
	aceita = False
	while s:

		# desempilhar pilha de possibilidades
		m = c.pop()
		est_atual = m[0] # estado atual da MT
		posicao = m[1]   # posicao na fita
		string = m[2]    # fita
		
		# aceita?: 1 - esta em estado final e 
		#		   2 - nao possui mais caminhos para percorrer?
		if est_atual in estados_finais and (est_atual, string[posicao]) not in t:
			aceita = True
			break
			
		# verifica quais as possibilidades de caminho para empilhar
		# essas possibilidades estao relacionadas com as transicoes entre os estados
		# garantindo as bifurcacoes de um estado A se direcionar para os estados B e C
		# lendo o mesmo simbolo
		if (est_atual, string[posicao]) in t:

			# pecorre as possibilidades
			for ps in t[(est_atual, string[posicao])]:
				aux = []
				for str_ in string:
					aux.append(str_)
					
				# realiza escrita na posicao atual da string
				# de acordo com a transicao
				if aux[posicao] == simbolo_branco:
					aux.append(simbolo_branco)
					string.append(simbolo_branco)

				aux[posicao] = ps[1]
				# posicao na fita para a direita
				if ps[2] == 'D':
					# possibilidade empilhada
					c.append((ps[0], (posicao + 1), aux))

				# posicao na fita para a esquerda
				elif ps[2] == 'E': 
					# possibilidade empilhada
					c.append((ps[0], (posicao - 1), aux))

				# fita imovel
				elif ps[2] == 'I':
					# possibilidade empilhada para cabecote imovel
					c.append((ps[0], posicao, aux))

		# caso MT parou sem reconhecer
		if (est_atual, string[posicao]) not in t and len(c) == 0:
		# if len(c) == 0:
			s = False
			# finalizado quando nao existe mais possibilidades 
			# de caminho para o estado atual
			break 
	if aceita:
		print("S")
	else:
		print("N")
	# break
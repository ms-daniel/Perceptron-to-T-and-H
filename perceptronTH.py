class Perceptron():
    v = 0.0

    def __init__(self, W, limiar, aprendizagem):
        self.w = W
        self.limiar = limiar*-1
        self.aprendizagem = aprendizagem

    def answerPerceptron(self, inp):
        self.v = 0
        for x in range(len(inp)):
            if(len(inp) < 10):
                self.v += self.limiar * 1
            self.v += self.w[x]*inp[x]

        if (self.v >= 0):
            return +1
        else:
            return -1

    def attWeight(self, inp):
        for x in range(len(inp)):
            self.w[x] += self.aprendizagem *inp[x]*(self.outp - self.y)


    def learn(self, inp, outp):
        print('')

        self.inp = []
        self.inp.append(1)
        for x in range(len(inp)):
            self.inp.append(inp[x])

        self.outp = outp
        self.y = self.answerPerceptron(self.inp)
        print('y: ', self.y)
        
        while(self.y != outp):
            print('Atualizando pesos...')

            self.attWeight(self.inp)

            print('Novos pesos:')
            for x in range(len(inp)):
                print('w', x, ':', self.w[x])

            self.y = self.answerPerceptron(self.inp)
            print('y: ', self.y)

        return 1  


T = [ 1,1,1,
      0,1,0,
      0,1,0
    ]

H = [
    1,0,1,
    1,1,1,
    1,0,1
]

T2 = [ 1,1,1,
      0,1,0,
      0,0,0
    ]

H2 = [
    1,0,1,
    1,1,1,
    0,0,1
]

w = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, -0.1]

percep = Perceptron(w, 0.4, 0.5)
nome = 's'
tt = 's'
while tt:
    tt = input('1 - Treinar ou 2 - testar? ')
    if tt == '1':
        percep.learn(T, 1)
        percep.learn(H, -1)
        
        print('PARA T: ', percep.answerPerceptron(T))
        print('PARA H: ', percep.answerPerceptron(H))

    elif tt == '2':
        print('Teste com eles distorcidos:')
        print('para T: ', percep.answerPerceptron(T2))
        print('para H: ', percep.answerPerceptron(H2))
    else:
        print('fechando ou escolha errada')
    


    
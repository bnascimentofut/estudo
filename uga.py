
while True:

    print('-'*50)
    print('Aperte 1 para calcular a fórmula de Bhaskara')
    print('')
    print('Aperte 2 para calcular uma soma')
    print('')
    print('Aperte 3 para informar seu município')
    print('-'*50)
    print('')

    opcao = int(input('Digite a opção desejada:'))

    if opcao == 1:

        print('-'*50)
        a = float(input('Digite o valor de a:'))

        print('-'*50)
        b= float(input('Digite o valor de b:'))
        print('')
        c= float(input('Digite o valor de c:'))
        print('')

        delta = b**2-4*a*c
        x1 =-b * 0.5*(delta)/2*a
        x2 =+b * 0.5*(delta)/2*a


        print('-'*50)
        print(f"O valor de x1 é {x1} e o valor de x2 é {x2}")
        print('')
    elif opcao == 2:
        print('-'*50)
        qnt_num=int(input('Digite a quantidade de números que deseja somar:'))
        num =1
        lista=[]
        while num <= qnt_num:
            nums = float(input('Insira o número:'))
            print('')
            lista.append(nums)
            soma = sum(lista)
            print(soma, ('A soma dos números é:'))
            num = num +1
        print('-'*50)
    elif opcao == 3:

        cont = 0
        Tatuí = 1
        Cerquilho = 2
        Boituva = 3

        qdt_num_Tatuí = 0
        qdt_num_Cerquilho = 0
        qdt_num_Boituva = 0


        print('')
        print('-'*50)
        qtd_pessoas = int (input('Quantas pessoas há nessa região:'))
        print('')

        while cont <qtd_pessoas:
            
            print('Considere que os municípios Tatuí, Cerquilho e Boituva representam 1, 2,3 respectivamente')
            print('')
            num_municipio = int(input('Você mora em qual município?'))

            if num_municipio ==1:
                print('você escolheu Tatuí, vamos para o próximo registro')
                qdt_num_Tatuí = qdt_num_Tatuí +1
            if num_municipio ==2:
                print('você escolheu Cerquilho, vamos para o próximo registro')
                qdt_num_Cerquilho = qdt_num_Cerquilho +1
            if num_municipio ==3:
                print('você escolheu Boituva, vamos para o próximo registro')
                qdt_num_Boituva = qdt_num_Boituva +1
            

            cont= cont +1
        if cont == qtd_pessoas:
            print('')
            print(f'O número de moradores de Tatuí é {qdt_num_Tatuí} , em Cerquilho é {qdt_num_Cerquilho}, em Boituva é {qdt_num_Boituva}')
            print('-'*50)


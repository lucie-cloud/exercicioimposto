# Simulação de Alíquota Efetiva - Cálculo Mensal
import tabela

regraAtual = False # Padrão regra antiga

# Apresentação
print('\n\t\t\t -- Recolhimento de Imposto sobre Renda Mensal Pessoa Física --\n')

# Entradas
rendimentoTributavel = float(input('Informe o salário: '))
dependente = int(input('Informe o número de dependentes: '))
atual = input('Rendimento recebido depois de abril/2023 (s/n)? ')
if atual.lower() == 's':
    regraAtual = True

# Processamento
descontoDependente = dependente * 189.59
salarioBase = rendimentoTributavel - descontoDependente

if salarioBase < 1903.98:
    aliquota = 0.0
    dedução = 0.0
elif salarioBase <= 2826.65:
    aliquota = 0.075
    dedução = 142.8
elif salarioBase <= 3751.05:
    aliquota = 0.15
    dedução = 354.8
elif salarioBase <= 4664.8:
    aliquota = 0.225
    dedução = 636.13
else:
    aliquota = 0.275
    dedução = 869.36

impostoBruto = salarioBase * aliquota
irDevido = impostoBruto - dedução
salarioLiquido = rendimentoTributavel - irDevido
aliquotaEfetiva = irDevido/rendimentoTributavel
impostoRenda = tabela.imposto(rendimentoTributavel, dependente, regraAtual)

# Processamento
print('\n\t\t\t -- Dados do IR --\n')
print('Salário Bruto..............R$ {:.2f}'.format(rendimentoTributavel))
print('Núm. de dependente..................{}'.format(dependente))
print('Salário Bruto..............R$ {:.2f}'.format(impostoRenda['salarioBruto']))
print('Núm. de dependente.................{}'.format(impostoRenda['dependente']))
print('-'*36)
print('Salário Base...............R$ {:.2f}'.format(salarioBase))
print('Alíquota........................{:.2f}%'.format((aliquota*100)))
print('IR Devido....................R$ {:.2f}'.format(irDevido))
print('Salário Base..................R$ {:.2f}'.format(impostoRenda['salarioBase']))
print('Alíquota........................{:.2f}%'.format((impostoRenda['aliquota']*100)))
print('IR Devido....................R$ {:.2f}'.format(impostoRenda['irDevido']))
print('-'*36)
print('Salário Líquido.............R$ {:.2f}'.format(impostoRenda['salarioLiquido']))
print('Alíquota Efetiva.................{:.2f}%'.format((aliquotaEfetiva*100)))








print('Salário Líquido.............R$ {:.2f}'.format(impostoRenda['salarioLiquido']))
print('Alíquota Efetiva.................{:.2f}%'.format((impostoRenda['aliquotaEfetiva']*100)))

#print(impostoRenda)
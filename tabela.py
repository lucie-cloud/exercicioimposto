# Processamento do sistema

def imposto(rendimentoTributavel, dependente, novaRegra):
    # Calculo do desconto por dependente
    descontoDependente = dependente * 189.59

    if descontoDependente < 528 and novaRegra:
        # Desconto simplificado
        salarioBase = rendimentoTributavel - 528

        # Tabelas de IR
        if salarioBase < 2112:
            aliquota = 0.0
            dedução = 0.0
        elif salarioBase <= 2826.65:
            aliquota = 0.075
            dedução = 158.4
        elif salarioBase <= 3751.05:
            aliquota = 0.15
            dedução = 370.4
        elif salarioBase <= 4664.68:
            aliquota = 0.225
            dedução = 651.73
        else:
            aliquota = 0.275
            dedução = 884.96
    else:
            # Desconto por dependente
        salarioBase = rendimentoTributavel - descontoDependente

        # Tabela s de IR atual
        if salarioBase < 1903.98:
            aliquota = 0.0
            dedução = 0.0
        elif salarioBase <= 2826.65:
            aliquota = 0.075
            dedução = 142.8
        elif salarioBase <= 3751.05:
            aliquota = 0.15
            dedução = 354.8
        elif salarioBase <= 4664.68:
            aliquota = 0.225
            dedução = 636.13
        else:
            aliquota = 0.275
            dedução = 869.36


    impostoBruto = salarioBase * aliquota
    irDevido = impostoBruto - dedução
    salarioLiquido = rendimentoTributavel - irDevido
    aliquotaEfetiva = irDevido/rendimentoTributavel

    return {
        'salarioBruto': rendimentoTributavel,
        'dependente': dependente,
        'salarioBase': salarioBase,
        'aliquota': aliquota,
        'irDevido': irDevido,
        'salarioLiquido': salarioLiquido,
        'aliquotaEfetiva': aliquotaEfetiva
    }
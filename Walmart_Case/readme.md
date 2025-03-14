# Projeto de Data Science: Detecção de Fraudes em Entregas do Walmart

## Objetivo do Projeto
 

O Walmart é a maior rede de varejo dos Estados Unidos gerando em média de US$ 1,6 bilhão em receita por dia. Em termos de vendas na loja, o Walmart faz uma média de: US$ 17.000 por segundo, US$ 1,1 milhão por minuto e US$ 68 milhões por hora.

 

A plataforma online e as vendas no varejo do Walmart contribuem com uma grande parte de seus lucros. O Walmart é o maior varejista de alimentos dos Estados Unidos, com mais de US$ 264 bilhões em vendas de alimentos nos EUA no ano passado.

 

De acordo com uma pesquisa recente da Lending Tree, o roubo em caixas de autoatendimento é um problema real, e os indivíduos que se envolvem nisso provavelmente repetirão o comportamento. O Walmart enfrentou perdas com roubos no varejo, com estimativas de 3 bilhões em 2021, 6,1 bilhões em 2022 e US$ 6,5 bilhões em 2023, o que mostra um crescimento de $400 milhões de dólares em perdas por furto no último ano.

 

Você é o cientista de dados do Walmart trabalhando exclusivamente para a área de e-commerce. Foi indentificado que o maior aumento proporcional em furtos aconteceu nas compras efetuadas via e-commerce em que usuários relatam não receberem todos os pedidos feitos nas suas compras. Do crescimento de roubos de 2022 para 2023, 53% do aumento veio das compras online.

 

Você foi designado a cuidar deste projeto para diminuir o número de fraudes e roubos através dos sites de e-commerce do Walmart. Foi identificado que estes roubos acontecem na entrega.

 

Neste projeto, o objetivo principal é identificar possíveis fraudes em entregas realizadas pelo Walmart na região Central da Flórida para servir de modelo (caso o resultado do projeto seja positivo) para as demais regiões dos EUA.

 

O foco é analisar os dados de entrega para detectar padrões e anomalias que possam indicar que itens declarados como entregues pelo motorista não foram efetivamente recebidos pelo cliente. O Walmart tem enfrentado reclamações de consumidores sobre entregas incompletas e, com a análise dos dados, deseja entender se a responsabilidade pela fraude pode ser atribuída aos consumidores, aos entregadores ou a outra causa.

## Descrição do Problema
 

Nos EUA o Walmart possui um sistema similar ao Uber em que entregadores se cadastram para entregar pedidos feitos através do site do Walmart. Estes entregadores (motoristas) não são funcionários do Walmart, mas trabalham independentemente aceitando pedidos de entrega e fazendo o recebimento destes pedidos pela equipe do Walmart e entrega destes pedidos ao endereço do consumidor. Muitos consumidores relataram que certos itens de seus pedidos não foram entregues, apesar de o sistema marcar a entrega como concluída. Isso levanta algumas questões críticas:

 

1. Fraude do Entregador (Motorista): Há evidências de que motoristas possam estar reportando a entrega de itens que, na realidade, não chegaram até o cliente. Eles podem estar omitindo ou desviando itens do pedido, registrando, no entanto, a entrega total.

2. Erro do Sistema ou Processo: Pode ser que o problema esteja em falhas no sistema de registro ou no processo de entrega, não se limitando a fraudes intencionais.

3. Fraude do Consumidor: Em alguns casos, o consumidor pode estar declarando como não ter recebido um produto que foi entregue para assim pedir o reembolso do produto.
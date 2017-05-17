# MC733-Projeto2
Public repository for the second project

## Roteiro
Primeiramente, vamos escolher qual a melhor configuração da memória cache L1 unificada, semelhante ao que fizemos no exercício 2, a partir dos resultados com três programas. Escolhida essa configuração, vamos testar todas as combinações dos outros parâmetros que escolhemos:
tamanho de pipeline (5, 7, 13 estágios), processadores escalares e superescalares e técnicas de branch prediction. No caso do superescalar, vamos testar com duas instruções em paralelo. Assim, para cada combinação possível entre esses parâmetros, vamos analisar os resultados para os três programas. Os resultados finais serão mostrados no formato de gráficos e tabela. Faremos os testes com os programas ##_x, y e z_##.

## Fundamentos Teóricos
Os tópicos abaixo descrevem como cada característica afeta o desempenho de uma arquitetura de hardware. Enquanto os quatro primeiros (configuração de cache, tamanho de pipeline, escalar vs superescalar, branch predictor) produzem efeitos sobre a execução de um programa, o último (hazard) é um efeito em si da manipulação de configurações do hardware (ou, em nosso caso, dos parâmetros da simulação).

### Cache
- Associatividade: o desempenho tende a aumentar de acordo com o aumento de associatividade. No entanto, a taxa de misses tende a se estabilizar conforme esse número de vias aumenta. Além disso, o aumento de associatividade leva a um aumento no hit time.

- Tamanho dos blocos: quanto maior o tamanho dos blocos, melhor o desempenho, devido à localidade espacial. No entanto, o desempenho volta a diminuir a partir de determinado ponto, visto que haverá menos blocos, portanto maiores miss rates.

- Tamanho da cache (Quantidade de blocos): o aumento da quantidade de blocos tende a diminuir o miss rate em conformidade, porém aumenta o hit time.

### Pipeline

### Proc. Escalar e Superescalar

### Branch Predictor

### Hazard

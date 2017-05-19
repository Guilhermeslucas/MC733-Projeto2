# MC733-Projeto2
Repository for the second project

## 1. Introdução e Objetivo
Cada vez mais, são pesquisadas técnicas para aproveitar melhor o processamento de dispositivos computacionais, procurando realizar mais operações com maior qualidade e menos tempo. Algumas dessas descobertas foram memória cache, diferentes números de estágios no pipeline, superescalar e técnicas de branch predicition. Assim, o objetivo desse experimento é testar como obter melhores resultados de performance combinando as quatro técnicas acima.

## 2. Roteiro
Primeiramente, vamos escolher qual a melhor configuração da memória cache L1 unificada, semelhante ao que fizemos no exercício 2, a partir dos resultados com três programas. Escolhida essa configuração, vamos testar todas as combinações dos outros parâmetros que escolhemos:
tamanho de pipeline (5 e 7 estágios), processadores escalares e superescalares e técnicas de branch prediction. No caso do superescalar, vamos testar com duas instruções em paralelo. Assim, para cada combinação possível entre esses parâmetros, vamos analisar os resultados para os três programas. Os resultados finais serão mostrados no formato de gráficos e tabela. Faremos os testes com os programas 
**Dijkstra, BasicMath e SHA**. Dentre essas escolhas, o **Dijkstra** e **SHA** são a versão **large** e a **BasicMath** a versão **small**.

## 3. Fundamentos Teóricos
Os tópicos abaixo descrevem como cada característica afeta o desempenho de uma arquitetura de hardware. Enquanto os quatro primeiros (configuração de cache, tamanho de pipeline, escalar vs superescalar, branch predictor) produzem efeitos sobre a execução de um programa, o último (hazard) é um efeito em si da manipulação de configurações do hardware (ou, em nosso caso, dos parâmetros da simulação).

### 3.1 Cache
- Associatividade: o desempenho tende a aumentar de acordo com o aumento de associatividade. No entanto, a taxa de misses tende a se estabilizar conforme esse número de vias aumenta. Além disso, o aumento de associatividade leva a um aumento no hit time.

- Tamanho dos blocos: quanto maior o tamanho dos blocos, melhor o desempenho, devido à localidade espacial. No entanto, o desempenho volta a diminuir a partir de determinado ponto, visto que haverá menos blocos, portanto maiores miss rates.

- Tamanho da cache (Quantidade de blocos): o aumento da quantidade de blocos tende a diminuir o miss rate em conformidade, porém aumenta o hit time.

### 3.2 Pipeline
O aumento da profundidade (ou quantidade de estágios) de um pipeline aumenta a quantidade de instruções sendo executadas simultaneamente.

### 3.3 Proc. Escalar e Superescalar
Processador superescalar é capaz de executar mais de uma instrução por ciclo, de modo que duas ou mais instruções estão presentes em cada estágio do pipeline. Esse tipo de processador usa o conceito de paralelismo para poder realizar todas as suas operações necessárias de maneira mais eficiente.

### 3.4 Branch Prediction
Branch Prediction é uma técnica usada em pipelines para que este não perca tanto tempo se recuperando de uma operação de branch, já que, caso exista uma instrução de branch no pipeline, todas as que estão antes dessa dentro do pipeline terão que ser descarregadas. Assim, fica fácil notar que seria muito mais eficiente somente colocar no pipeline instruções que realmente serão executadas.

### 3.5 Hazard
- Estrutural: acontece quando há competição por recurso. Exemplo: se há uma única memória (sem separação entre dados e instruções), o estágio de instruction fectch (IF) do pipeline pode ser _stalled_ durante uma instrução de load/store.

- Dados: se uma instrução depende de um dado ser atualizado em outro estágio do pipeline. Exemplo: duas instruções de adição em sequência no pipeline. O pipeline terá que ser _stalled_ por dois ciclos, caso não seja usado forwarding. Forwarding permite que uma informação seja disponibilizada com antecedência para outro estágio do pipeline.

- Controle: instruções de branch deslocam o fluxo de execução, fazendo com que a execução da próxima instrução dependa do resultado da instrução de branch. O uso de branch predictor auxilia na diminuição de ocorrências desse tipo de hazard.

## 4. Experimento e Resultados
### 4.1 Tamanho de Cache
Como dito no roteiro, primeiramente decidimos qual foi é a melhor configuração para a cache única, para posteriormente, com esses parâmetros, encontrar os melhores resultados para os outros componentes que estamos testando nesse experimento. Assim, segue abaixo os gráficos de **miss rate** na **cache l1** de dados. Decidimos considerar somente a **cache de dados**, pois a taxa de miss nessa varia bem mais, levando a uma melhor análise do problema. Além disso, o valor de miss da **cache de instruções** chegava a 0 muito rapidamente em vários testes que realizamos, não se mostrando tão interessante para uma análise. Assim:  

#### 4.1.1 BasicMath

| Tamanho   | Miss Rate          |
|-----------|--------------------|
| 8.192     | 0,03900 |
| 16.384    | 0,03010 |
| 32.768    | 0,02670 |
| 65.536    | 0,02640 |
| 131.072   | 0,02610 |
| 262.144   | 0,00700 |
| 524.288   | 0,00500 |
| 1.048.576 | 0,00400 |  


![BasicMath](graficos/basic_math_cache_size.jpeg)  


#### 4.1.2 Dijsktra  

| Tamanho de Cache | Miss Rate (%)      |
|------------------|--------------------|
| 8.192            | 0,3045 |
| 16.384           | 0,1536 |
| 32.768           | 0,0934 |
| 65.536           | 0,0105 |
| 131.072          | 0,0006 |
| 262.144          | 0,0004 |
| 524.288          | 0,0004 |
| 1.048.576        | 0,0004 |  


![Djikstra](graficos/dijkstra_cache_size.jpeg)  

#### 4.1.3 SHA

| Tamanho de Cache | Miss Rate(%)       |
|------------------|--------------------|
| 8.192            | 0,1125 |
| 16.384           | 0,0323|
| 32.768           | 0,0305|
| 65.536           | 0,0241|
| 131.072          | 0,0238 |
| 262.144          | 0,0233 |
| 524.288          | 0,0226|
| 1.048.576        | 0,0217 |

![SHA](graficos/sha_cache_size.jpeg) 

Observando os gráficos, fica simples notar que quanto maior o **tamanho da cache** menor é a **taxa de miss**, o que justifica utilizar o maior encontrado, que nesse caso é **1.048.576** bytes. Além disso, escolhemos o tamanho de bloco como **64 kb** e a associatividade de **16**.  

### 4.2 Análise das demais configurações  
Aqui, vamos analisar cada programa com as diferentes configurações propostas pelo grupo. As configurações que adotamos foram as seguintes:  

- **Configuração 1:** 
Predição:``` Branch always not taken```  
```Escalar```  

- **Configuração 2:**  
Predição: ``` Branch always not taken```  
```Superescalar```  

- **Configuração 3:**  
Predição: ``` 1 bit predictor```  
```Superescalar```  

- **Configuração 4:**  
Predição: ``` 1 bit predictor```  
```Escalar```  

Decidimos plotar gráficos da soma dos números de stalls e discriminá-los por meio de uma tabela que está logo acima de cada gráfico. 

#### 4.2.1 SHA  

|               | Configuração 1 | Configuração 2 | Configuração 3 | Configuração 4 |
|---------------|----------------|----------------|----------------|----------------|
| Data Stalls   | 42650721       | 219347812      | 219347812      | 42650721       |
| Branch Stalls | 10934856       | 10934856       | 1464304        | 1464304        |
| Jump Stalls   | 819980         | 819980         | 819980         | 819980         |  

![SHA Stalls](graficos/sha_stalls.jpeg)
Aqui é notável a diferença entre as configurações 1 e 4 das demais. Essas tem um número de stalls muito menor que as outras aprensentadas. Observando a configuração de ambos, é possível notar que o que possuem em comem é o processador escalar. Faz muito sentido o superescalar ter mais stalls, já que, da maneira que foi implementado(sem forward), quando uma instrução necessita de outra que está em outro pipeline, essa deve esperar o término do outro para completar sua operação. Além disso, é possível notar uma melhora no desempenho quando usamos **1 bit predictor**, muito notável na diferença entre as configurações 2 e 3.

#### 4.2.2 Dijkstra  
|               | Configuração 1 | Configuração 2 | Configuração 3 | Configuração 4 |
|---------------|----------------|----------------|----------------|----------------|
| Data Stalls   | 112021848      | 332985213      | 332985213      | 112021840      |
| Branch Stalls | 35912170       | 35912170       | 32639320       | 32639320       |
| Jump Stalls   | 18839754       | 18839754       | 18839754       | 18839754       |  

![](graficos/djikstra_stalls.jpeg)

Aqui, como no exemplo anterior, também fica muito claro como usar um processador superescalar sem tomar os devidos cuidados de sincronização e forwards pode ser catastrófico para a performance do processador. Além disso, o **1 bit predictor** continua sendo melhor que o a tecnica de **branch not taken**.  

#### 4.2.3 BasicMath
|               | Configuração 1 | Configuração 2 | Configuração 3 | Configuração 4 |
|---------------|----------------|----------------|----------------|----------------|
| Data Stalls   | 4258045941     | 1594369841     | 1594369814     | 4258045941     |
| Branch Stalls | 116116210      | 116116210      | 102946028      | 102946028      |
| Jump Stalls   | 78024780       | 78024780       | 78024780       | 78024780       | 

![](graficos/basic_math_stalls.jpeg) 

Mais uma vez, fica claro que implementar processadores superescalares sem o devido cuidado, atrapalha muito o desempenho, ao invés de aumentar a velocidade do processamento,que é a principal busca. Além disso, o **1 bit predictor** continua sendo a melhor opção entre os dois que estamos analisando.

#### 4.2.4 Resultados Gerais e Análise

|                         |           |  Config.1 |            |           |  Config.2 |             |           |  Config.3 |            |           |  Config.4 |            |
|-------------------------|:---------:|:---------:|:----------:|:---------:|:---------:|:-----------:|:---------:|:---------:|:----------:|:---------:|:---------:|:----------:|
|                         |  Dijkstra |    SHA    |  BasicMath |  Dijkstra |    SHA    | P3BasicMath |  Dijkstra |    SHA    |  BasicMath |  Dijkstra |    SHA    |  BasicMath |
| Instruções              | 223690619 | 143581254 | 1089764766 | 223690619 | 143581254 |  1089764766 | 223690619 | 143581254 | 1089764766 | 223690619 | 143581254 | 1089764766 |
| % de branches corretos  |    0.57   |    0.07   |    0.54    |    0.57   |    0.07   |     0.54    |    0.61   |    0.87   |    0.59    |    0.61   |    0.87   |    0.59    |
| Ciclos                  | 390464383 | 197986811 | 1709710347 | 305713878 | 187341951 |  1439137785 | 304077453 | 182606675 | 1432552694 | 387191533 | 188516259 | 1696540165 |
| CPI                     |    1.75   |    1.38   |    1.57    |    1.37   |    1.30   |     1.32    |    1.36   |    1.27   |    1.31    |    1.73   |    1.31   |    1.56    |
| Tempo                   |   13.46   |    9.06   |    79.96   |   22.31   |   14.97   |    129.23   |   21.83   |   14.77   |   132.40   |   14.67   |    9.79   |    80.49   |

Instruções: não mudaram.
Branches corretos: alterações conforme config. de predição.
CPI: p/ branch always not taken - melhor superescalar (config 2). p/ predictor - melhor superescalar (config 3).

![Branches x Configs](graficos/branches-x-configs.png)
![CPI x Configs](graficos/cpi-x-configs.png)
![Wall Time x Configs](graficos/walltime-x-configs.png)

## 5. Conclusão
Após realizar todos os experimentos propostos, notamos que pequenas técnicas em um processador ajudam muito a aumentar sua performance. Porém,essas devem ser implementadas com o devido cuidado, uma vez que podem ter o efeito contrário.








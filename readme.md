## Introdução
Esse é um script simples, a partir do arquivo do lab, e os arquivos de input e output disponibilizados pelo professor, executa cada lab baseado em um dos inputs e salva na pasta ```actual``` e então verifica quais testes a saida é igual ao do professor e quais são diferentes, caso sejam diferentes é mostrada a diferença.

## Como executar
Para executar, este é o template
```bash
python test.py <arquivo-lab> <pasta-teste> 
```
Ambos são opcionais, caso indentifique a pasta de teste, o programa considerara ela a pasta ```tests``` no mesmo diretorio do arquivo do lab, e caso não defina o arquivo de lab, ele solicitara que insiera
### Exemplo
```bash
python test.py ~/Unicamp/testador-lab/exemplo/lab00.py
```

```bash
python test.py ~/Unicamp/testador-lab/exemplo/lab00.py ~/Unicamp/testador-lab/exemplo/testes00
```
Exemplos seguintes apenas funciona caso seja executado na mesma pasta do lab e dos testes 
```bash
python ~/Unicamp/testador-lab/test.py lab00.py
```
```bash
python ~/Unicamp/testador-lab/test.py lab00.py testes00
```
## Nota
O script foi testado apenas num linux, não garanto funcionar em outros SO.

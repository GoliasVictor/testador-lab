## Introdução
Esse é um script simples, a partir do arquivo do lab, e os arquivos de input e output disponibilizados pelo professor, executa cada lab baseado em um dos inputs e salva na pasta ```actual``` e então verifica quais testes a saida é igual ao do professor e quais são diferentes, caso sejam diferentes é mostrada a diferença.

## Como executar
Para executar, este é o template
```bash
nome_do_script.py test.py caminho_para_pasta_de_testes
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

## Teste To CPH
Foi recomendado em sala de aula a extensão do VS code [Competitive Programming Helper (cph)](https://marketplace.visualstudio.com/items?itemName=DivyanshuAgrawal.competitive-programming-helper), porém um problema é que é preciso adicionar manualmente cada um dos testes, então foi feito um segundo script ```test-to-cph.py```, que ele converte os testes do professor, no arquivo usado pelo CPH para teste.

## Notas

- O script foi testado apenas num linux, não garanto funcionar em outros SO.
- Existe a pasta ```testes```, que já são os testes que o professor disponibiliza, que foram adicionados aqui, a cada novo teste que o professor disponibilizar. Então, caso você execute o script e não definir uma pasta de teste, nem ter a pasta ```tests```, o script ira procura na propria pasta a pasta com mesmo nome do seu lab na pasta ```testes```. E os testes são os testes da turma W de MC102 do 1º semestre de 2023. 
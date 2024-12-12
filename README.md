# PokemonEntropy

# Análise da Complexidade de Pokémons

Este projeto foi desenvolvido para analisar a complexidade dos designs de Pokémons, calculando a proporção de informação contida no contorno principal da imagem do Pokémon. O código processa imagens de Pokémons carregadas, extrai várias métricas e visualiza os resultados.

## Objetivos

O principal objetivo deste projeto é fornecer uma maneira sistemática de avaliar a complexidade dos designs de Pokémons. Isso pode ser útil para:

1. Entender as características visuais de diferentes Pokémons e como eles se comparam em termos de complexidade.
2. Auxiliar no desenvolvimento de novos designs de Pokémons, fornecendo insights sobre o equilíbrio entre simplicidade e detalhes.
3. Apoiar análises e pesquisas sobre a estética e a evolução dos designs de Pokémons ao longo do tempo.

## Recursos

O projeto oferece os seguintes recursos:

- Carregamento e processamento de imagens de Pokémons
- Cálculo do número total de pixels do Pokémon
- Cálculo do número de pixels no contorno principal do Pokémon
- Cálculo da proporção de informação (razão entre pixels do contorno principal e pixels totais)
- Representações visuais da imagem original, imagem dilatada e imagem "negaposi"
- Geração de um gráfico comparativo da proporção de informação para múltiplos Pokémons

## Uso

1. Instale as bibliotecas necessárias:

```
!pip install opencv-python numpy matplotlib pillow scikit-image
```

2. Execute o código fornecido, que solicitará o carregamento das imagens de Pokémons que você deseja analisar.

3. O código processará cada imagem e exibirá as seguintes informações para cada Pokémon:
   - Nome do arquivo da imagem
   - Número total de pixels do Pokémon
   - Número de pixels no contorno principal
   - Proporção de informação (pixels do contorno principal / pixels totais)

4. Um gráfico comparativo será gerado no final, mostrando a proporção de informação para cada Pokémon analisado.

## Exemplos de Resultados

Aqui estão algumas imagens de exemplo e seus resultados da análise:

Imagem 1: 
![Imagem 1](https://i.imgur.com/7SRrciK.png)

Imagem 2:
![Imagem 2](https://i.imgur.com/mH9UbOX.png)

Imagem 3: 
![Imagem 3](https://i.imgur.com/8cdkxYj.png)

## Melhorias Futuras

Para melhorar o projeto, as seguintes iniciativas podem ser consideradas:

- Implementar técnicas de processamento de imagem mais avançadas para melhorar a precisão da detecção do contorno principal.
- Explorar o uso de modelos de aprendizado de máquina para classificar os designs de Pokémons com base em sua complexidade.
- Fornecer visualizações e métricas adicionais para melhor compreender as características de design de diferentes Pokémons.

## Contribuição

Se você tiver sugestões ou quiser contribuir com o projeto, sinta-se à vontade para criar uma nova issue ou enviar um pull request.

## Referências

O projeto faz uso das seguintes bibliotecas e recursos:

- [Biblioteca OpenCV](https://opencv.org/)
- [Biblioteca Numpy](https://numpy.org/)
- [Biblioteca Matplotlib](https://matplotlib.org/)
- [Biblioteca Pillow](https://pillow.readthedocs.io/)
- [Biblioteca Scikit-image](https://scikit-image.org/)

A ideia foi inspirada no seguinte post realizado num [Forum](https://qiita.com/mrok273/items/6f0bcdc62b6184f79308) 

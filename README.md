# Monitor de Sistema Inteligente

Este script em Python monitora o uso de CPU, GPU e RAM, além de verificar a temperatura do sistema. Ele exibe as informações em tempo real e sugere ações caso algum componente esteja com uso ou temperatura elevada.

## Funcionalidades
- Exibe o uso da CPU e sua temperatura (quando disponível)
- Mostra a utilização da memória RAM
- Coleta informações sobre a GPU, incluindo uso, temperatura e memória
- Exibe alertas caso algum componente esteja operando em níveis críticos

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes pacotes instalados:

```bash
pip install psutil GPUtil
```

## Como Usar
Execute o script com o seguinte comando:

```bash
python monitor_sistema.py
```

## Notas
- A temperatura da CPU pode não estar disponível no Windows sem software adicional.
- O script é compatível com sistemas Linux e Windows.

## Contribuição
Sinta-se à vontade para contribuir com melhorias e sugestões! Caso encontre problemas, abra uma issue no repositório.

## Licença
Este projeto é licenciado sob a MIT License.


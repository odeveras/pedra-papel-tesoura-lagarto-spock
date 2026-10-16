# Pedra, Papel, Tesoura, Lagarto, Spock

Jogo baseado na versão popularizada pela série *The Big Bang Theory*, em duas versões:

- **Web** (`index.html`): abre direto no navegador, sem instalar nada. Tem placar, histórico das últimas rodadas, lista de regras e atalhos de teclado (1 a 5).
- **Terminal** (`jogo.py`): versão em Python com menu de texto e placar.

## Como jogar

### Versão web

Abra o arquivo `index.html` no navegador. Se o GitHub Pages estiver ativado no repositório, o jogo também fica disponível em um link público.

### Versão Python

Requer Python 3.6 ou superior.

```bash
python jogo.py
```

## Regras

| Vencedor | Ação | Perdedor |
|----------|------|----------|
| Tesoura | corta | Papel |
| Papel | cobre | Pedra |
| Pedra | esmaga | Lagarto |
| Lagarto | envenena | Spock |
| Spock | quebra | Tesoura |
| Tesoura | decapita | Lagarto |
| Lagarto | come | Papel |
| Papel | refuta | Spock |
| Spock | vaporiza | Pedra |
| Pedra | amassa | Tesoura |

## Estrutura

```
index.html   # versão web (HTML, CSS e JavaScript em um único arquivo)
jogo.py      # versão para terminal
README.md
```

# ♻️ Projeto Jogo da Coleta Seletiva

Projeto educativo e interativo voltado para a conscientização sobre sustentabilidade e descarte correto de resíduos sólidos através da mecânica de coleta seletiva.

---

## 📌 Visão Geral do Projeto

O **Jogo da Coleta Seletiva** tem como objetivo ensinar de maneira lúdica as cores e categorias das lixeiras de reciclagem (Papel, Plástico, Vidro, Metal e Orgânico). O jogador controla uma lixeira móvel na parte inferior da tela, alternando seu tipo para coletar os diferentes resíduos que caem do topo da tela.

Originalmente concebido/estruturado a partir de uma lógica de blocos (estilo Scratch, documentado em `project.json`), o projeto foi portado e disponibilizado para múltiplos ambientes de execução:
1. **Web Nativo (HTML5 Canvas + JavaScript)**: Versão leve, responsiva e pronta para deploy direto no navegador ou plataformas estáticas (Vercel, Netlify, GitHub Pages).
2. **Streamlit (Python)**: Interface interativa para visualização embutida com componentes de controle e estatísticas.
3. **Pygame (Python Desktop)**: Execução local em janela desktop via engine nativa de jogos em Python.
4. **Servidor Local Python (`http.server`)**: Servidor leve sem dependências externas para jogar via rede local (PC ou celular).

---

## 🏗️ Arquitetura e Estrutura de Arquivos

```text
jogo_ecologico/
├── README.md
└── Jogo_Coleta_Seletiva/
    └── coleta_seletiva/
        ├── index.html            # Aplicação Web completa (HTML5 Canvas + JS)
        ├── app.py                # Versão em Streamlit (Python)
        ├── jogo_coleta.py        # Versão desktop em Pygame (Python)
        ├── iniciar_jogo.py       # Servidor HTTP local sem bibliotecas externas
        ├── jogar.bat             # Atalho batch para inicialização rápida no Windows
        ├── requirements.txt      # Dependências Python (streamlit, pygame, pymupdf)
        ├── project.json          # Metadados e lógica original dos atores e cenários
        └── dependencias/         # Assets gráficos (SVG, PNG) e de áudio (WAV)
```

---

## 🧩 Módulos e Utilitários

### 1. `index.html` (Módulo Web Principal)
* **Tecnologia**: HTML5, CSS3, JavaScript puro (Vanilla JS), Web Audio API e Canvas 2D.
* **Propósito**: Execução independente em qualquer navegador moderno sem necessidade de runtime Python.
* **Recursos**:
  - Renderização fluida via `requestAnimationFrame`.
  - Suporte a teclado (setas, teclas numéricas 1–5, atalhos P/M) e toques em tela (touch screen) para dispositivos móveis.
  - Carregamento de áudio com fallbacks para evitar bloqueios de autoplay.
  - Ideal para hospedagem em nuvem (Vercel, GitHub Pages).

### 2. `app.py` (Módulo Streamlit)
* **Tecnologia**: Python + Streamlit.
* **Propósito**: Embutir o jogo em uma interface amigável do Streamlit com instruções e legendas das lixeiras.
* **Funcionamento**:
  - Lê os assets locais da pasta `dependencias/` e converte-os dinamicamente em Data URIs (`base64`).
  - Injeta o canvas e o código do jogo em um `st.components.v1.html`, permitindo compartilhamento fácil no **Streamlit Community Cloud**.

### 3. `jogo_coleta.py` (Módulo Desktop Pygame)
* **Tecnologia**: Python, Pygame, PyMuPDF (`fitz`).
* **Propósito**: Execução nativa para computadores desktop.
* **Destaques**:
  - Converte vetores SVG em bitmaps dinamicamente usando o PyMuPDF para rasterização de alta qualidade.
  - Mapeia o sistema de coordenadas centrado (típico do Scratch) para o sistema de coordenadas do Pygame (`scratch_para_pygame`).
  - Gerenciamento de eventos de teclado e loop clássico de jogos (`pygame.time.Clock`).

### 4. `iniciar_jogo.py` (Servidor Local de Rede)
* **Tecnologia**: Python Standard Library (`http.server`, `socket`, `webbrowser`).
* **Propósito**: Executar localmente sem precisar instalar `pip install`.
* **Utilidade**:
  - Descobre o IP da máquina na rede local (`obter_ip_local()`).
  - Abre o navegador automaticamente em `http://localhost:8000`.
  - Exibe no terminal o endereço IP e instruções para jogar através de celulares conectados à mesma rede Wi-Fi.

### 5. `jogar.bat` (Script de Automação Windows)
* **Propósito**: Script em lote simples para iniciar `iniciar_jogo.py` com um duplo clique no Windows.

### 6. `dependencias/` (Pasta de Recursos Multimídia)
* **Imagens**: Sprites em `.svg` e `.png` das 5 lixeiras, resíduos descartáveis (latas, maçãs, garrafas plásticas, folhas de papel, vidros quebrados), cenários e telas de início/fim/vitória.
* **Áudios**: Efeitos sonoros em formato `.wav` para acerto, erro, vitória e derrota (game over).

---

## 🎮 Regras e Mecânicas do Jogo

1. **Objetivo**: Capturar os resíduos que caem com a lixeira correspondente antes que atinjam o solo.
2. **Categorias de Coleta**:
   - 🟦 **1 · Papel** (Azul)
   - 🟥 **2 · Plástico** (Vermelho)
   - 🟩 **3 · Vidro** (Verde)
   - 🟨 **4 · Metal** (Amarelo)
   - 🟫 **5 · Orgânico** (Marrom)
3. **Controles**:
   - **Mover Lixeira**: Teclas `A` / `D` ou `Setas Esquerda / Direita`. Em telas móveis, toque e arraste.
   - **Trocar Tipo de Lixeira**: Teclas numéricas `1` a `5` ou botões visíveis na interface.
   - **Pausar**: Tecla `P`.
   - **Mutar/Desmutar Som**: Tecla `M`.
4. **Pontuação e Vidas**:
   - Acerto: +1 ponto e efeito sonoro de acerto.
   - Erro (capturar com a lixeira errada ou deixar o lixo cair): perda de vida/ponto de erro.

---

## 🚀 Como Executar o Projeto

### Opção 1: Direto no Navegador (Localmente)
Basta abrir o arquivo [index.html](file:///d:/Programacao/Jogo_Coleta_Seletiva/jogo_ecologico/Jogo_Coleta_Seletiva/coleta_seletiva/index.html) em qualquer navegador web moderno.

### Opção 2: Servidor Local (PC + Celular)
Abra o terminal na pasta do jogo e execute:
```bash
python iniciar_jogo.py
```
*(Ou execute o atalho `jogar.bat`)*

### Opção 3: Versão Streamlit
Instale as dependências e rode:
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Opção 4: Versão Desktop (Pygame)
Instale o Pygame e PyMuPDF:
```bash
pip install pygame pymupdf
python jogo_coleta.py
```

---

## 🌐 Publicação na Web (Vercel)

Para hospedar na Vercel:
1. **Root Directory**: Configure como `Jogo_Coleta_Seletiva/coleta_seletiva`.
2. **Framework Preset**: Escolha **Other** (não utilize o preset *Python*, pois o jogo na web é estático via `index.html`).
3. O deploy será concluído instantaneamente como um site estático de alta performance.

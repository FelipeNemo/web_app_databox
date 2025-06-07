# 🧠 Databox Master System

Um sistema gamificado de autogerenciamento pessoal, feito para impulsionar a evolução física, emocional, profissional e estratégica do seu criador: **Feliper Augusto**.

> 🎯 Objetivo: evoluir como pessoa, gerar valor com a Databox, conquistar liberdade financeira e emocional — e voltar a ver minha família com orgulho e presença.

---

## 🌟 Visão Geral

O **Master System** é a alma do projeto `databox`. Um assistente digital e motivacional que transforma sua rotina em um jogo inteligente de progresso.

- ✅ Personalização com GPT
- ✅ Missões diárias adaptativas
- ✅ Recompensas e penalidades
- ✅ Feedback visual e notificações
- ✅ Integração futura com Google Calendar, comandos de voz e leitura emocional

---

## 🧩 Módulos

### `homeMaster.py`

- Classe `Master`: representa o jogador principal (você)
  - `nome`, `xp`, `nivel`, `emblemas`, `moedas`, `quests_concluidas`
- Interface (via Streamlit): tela dividida em 3 partes:
  - **Habilidades**: físico, emocional, profissional, social
  - **Sistema**: chat GPT, voz, notificações
  - **Status**: nível, XP, progresso
- Geração de **missões diárias** personalizadas:
  - Tipos: Física | Intelectual/Profissional | Personalizada (por GPT)
  - Recompensas: moedas, XP, emblemas
  - Penalidades: leve → moderada

---

### `system.py`

- Coração do sistema de notificações e dinâmica
- Personalização automática baseada em:
  - Seu comportamento
  - Calendário e compromissos
  - Falhas e acertos
- Eventos aleatórios que estimulam novos hábitos

---

### `rewards.py`

- Controle do sistema de recompensas
  - XP, moedas, emblemas
- Tabela de conversão
- Lógica de atribuição de prêmios e penalidades

---

### `dashboard.py`

- Visualizações do progresso:
  - Gráficos de XP
  - Missões pendentes/concluídas
  - Emojis/indicadores subjetivos de humor e foco

---

### `ui.py`

- Estética e organização visual
- Interface dividida em três blocos:
  - 🧠 Habilidades
  - 🤖 Sistema Inteligente
  - 📊 Status

---

### `chat_gpt.py`

- Núcleo de personalização via IA
  - Sugere missões, hábitos, reflexões
  - Analisa padrão de comportamento
  - Atua como mentor, conselheiro e planejador

---

### `areas.py`

- Define e organiza as áreas de desenvolvimento:
  - Saúde Física
  - Conhecimento e Estudo
  - Família e Conexões
  - Projeto Databox e Carreira
  - Equilíbrio Emocional

---

## 📌 Ideias Futuras

- Persistência dos dados do Master com histórico
- Registro emocional diário + interpretação do GPT
- Skill Tree desbloqueável com XP
- Missões semanais e mensais
- Modo “mentor” por voz
- Rankings internos (vs você do passado)
- Desafios surpresa (ex: "ligue para alguém especial")

---

## 🚀 Por que esse projeto existe?

Porque eu quero **transformar minha vida em algo intencional, épico e lucrativo**.  
Porque eu sou o herói da minha própria história.  
Porque evoluir e vencer é minha missão.  
E porque **ver minha família feliz** e **viver da Databox** é o final feliz que estou construindo.

---

**Feliper Augusto**  
*Criador do Databox e protagonista do Master System*

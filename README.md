🤖 Agente CLI Termux

Um agente de inteligência artificial executado pelo terminal do Termux, desenvolvido em Python e integrado ao Google Gemini.

O projeto está em desenvolvimento e tem como objetivo criar um agente capaz de analisar projetos, utilizar ferramentas, executar comandos e realizar tarefas de forma autônoma.

🧠 O que o agente faz?

O agente recebe uma tarefa em linguagem natural e pode utilizar ferramentas para tentar realizá-la.

Por exemplo, em vez de apenas perguntar:

Como criar um arquivo Python?

você pode pedir:

Crie um arquivo chamado calculadora.py com uma calculadora simples.

O agente pode analisar o diretório, criar o arquivo utilizando suas ferramentas e verificar o resultado.

Outro exemplo:

Leia o arquivo calculadora.py e encontre possíveis erros.

O agente pode utilizar a ferramenta de leitura para analisar o código.

🔧 Recursos atuais

- Integração com a API do Google Gemini
- Memória persistente entre execuções
- Contexto durante a execução
- Sistema de ferramentas através de plugins
- Leitura de arquivos
- Criação e escrita de arquivos
- Edição de arquivos
- Execução de comandos no terminal
- Execução de testes
- Busca no código do projeto
- Visualização de diferenças entre arquivos
- Informações sobre o projeto
- Tentativas automáticas em caso de falhas
- Detecção de chamadas duplicadas de ferramentas

🛠️ Ferramentas disponíveis

O agente possui atualmente os seguintes plugins:

Plugin| Função
"busca.py"| Busca informações dentro do código
"diff.py"| Mostra diferenças entre arquivos
"edicao.py"| Edita arquivos
"escrever.py"| Cria e escreve arquivos
"info.py"| Obtém informações do projeto
"ler.py"| Lê arquivos
"listar.py"| Lista diretórios e arquivos
"shell.py"| Executa comandos no terminal
"testes.py"| Executa testes

📱 Como usar no Termux

1. Instale o Termux

Tenha o Termux instalado no Android.

2. Instale o Git

No Termux:

pkg update
pkg install git

3. Instale o Python

pkg install python

Verifique:

python --version

4. Baixe o projeto

No Termux:

git clone https://github.com/rickeiphou/agente-cli-termux.git

Entre na pasta:

cd agente-cli-termux

5. Configure a API Gemini

O agente precisa de uma chave da API do Google Gemini.

A chave deve ser configurada como uma variável de ambiente.

No Termux:

export GEMINI_API_KEY="SUA_CHAVE_AQUI"

Substitua "SUA_CHAVE_AQUI" pela sua própria chave.

Nunca publique sua chave no GitHub e nunca coloque a chave diretamente no código.

6. Execute o agente

O programa principal atual é:

python gmemoria.py

Para enviar uma tarefa ao agente, coloque o pedido entre aspas:

python gmemoria.py "Olá, agente"

Por exemplo:

python gmemoria.py "Qual é a capital da França?"

O agente receberá a tarefa, conversará com o Gemini e apresentará o resultado.

💻 Usando o agente para programar

O agente pode trabalhar dentro do diretório em que está sendo executado.

Por exemplo, crie um diretório para um projeto:

mkdir meu-projeto
cd meu-projeto

Depois execute o agente apontando para esse diretório:

python /caminho/para/agente-cli-termux/gmemoria.py "Crie um programa Python simples que calcule a média de três números. Crie os arquivos necessários e teste o programa."

O agente poderá utilizar suas ferramentas para analisar, criar, editar e testar arquivos.

«Recomenda-se testar o agente primeiro em projetos separados para evitar alterações acidentais em arquivos importantes.»

🧠 Memória persistente

O agente possui um sistema de memória persistente.

A memória é armazenada localmente em:

memory.json

Ela permite que informações relevantes de execuções anteriores sejam utilizadas em novas execuções.

O arquivo "memory.json" está incluído no ".gitignore" e não deve ser enviado para o GitHub.

🔑 Segurança da API

A chave da API é obtida através da variável:

GEMINI_API_KEY

Exemplo:

export GEMINI_API_KEY="SUA_CHAVE_AQUI"

O projeto não fornece uma chave de API.

Cada usuário deve utilizar sua própria chave.

Nunca compartilhe sua chave de API publicamente.

📂 Estrutura do projeto

agente-cli-termux/
├── gmemoria.py
├── plugins/
│   ├── busca.py
│   ├── diff.py
│   ├── edicao.py
│   ├── escrever.py
│   ├── info.py
│   ├── ler.py
│   ├── listar.py
│   ├── shell.py
│   └── testes.py
├── .gitignore
└── README.md

🚧 Estado do projeto

Este projeto ainda está em desenvolvimento.

A arquitetura está sendo construída gradualmente para permitir que o agente evolua de um simples agente de ferramentas para um sistema capaz de realizar tarefas de programação de forma cada vez mais autônoma.

Entre os próximos objetivos estão melhorias no planejamento, diagnóstico de erros, criação de projetos, testes e ciclos automáticos de correção.

📄 Licença

Este projeto ainda não possui uma licença definida.

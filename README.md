<div align="center">
  <picture>
    <source media="(max-width: 640px) and (prefers-reduced-motion: reduce)" srcset="assets/flayks-hero-mobile-static.svg">
    <source media="(max-width: 640px)" srcset="assets/flayks-hero-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/flayks-hero-static.svg">
    <img src="assets/flayks-hero.svg" alt="FLAYKS OLIVEIRA — Software Engineer · Founder · AI · Cybersecurity" width="100%">
  </picture>
</div>

<br>

<div align="center">

### Engenharia de software com foco em **Inteligência Artificial** e **Cibersegurança**

IA que ajuda a defender sistemas · Sistemas de IA que precisam ser defendidos

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-flayks--oliveira-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/flayks-oliveira/)
[![E-mail](https://img.shields.io/badge/E--mail-flayksdev@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:flayksdev@gmail.com)
[![Netsenti AI](https://img.shields.io/badge/Netsenti_AI-netsenti.com-0B1220?style=for-the-badge&logo=googlechrome&logoColor=22D3EE)](https://netsenti.com)

<sub>[IA](#-inteligência-artificial) · [Cibersegurança](#-cibersegurança) · [IA × Segurança](#-onde-ia-e-cibersegurança-se-encontram) · [Projetos](#-projetos) · [Stack](#-stack) · [Contato](#-contato)</sub>

</div>

<img src="assets/divider.svg" alt="" width="100%">

## 🎯 Foco

Sou fundador da [Netsenti AI](https://netsenti.com) e trabalho na interseção de duas áreas que se influenciam o tempo todo:

| | |
| :-- | :-- |
| 🤖 **IA aplicada** | Usar modelos de aprendizado de máquina e IA generativa como parte do produto, com avaliação e limites claros. |
| 🛡️ **Cibersegurança** | Projetar sistemas seguros desde o início e entender como eles são atacados para defendê-los melhor. |
| ⚙️ **Engenharia de software** | Transformar essas ideias em código mantível: interfaces, APIs e dados. |

> 🇯🇵 Representante brasileiro no **SusHi Tech Tokyo 2026** · 🥉 **Bronze Winner, Best AI Innovation** — International AI Awards 2026

<img src="assets/divider.svg" alt="" width="100%">

## 🤖 Inteligência Artificial

Um mapa resumido do que a área contém e de como eu a organizo.

<details open>
<summary><b>Tipos de IA por capacidade</b></summary>
<br>

| Tipo | O que é | Situação |
| :-- | :-- | :-- |
| **IA estreita (ANI)** | Resolve tarefas específicas: recomendação, classificação, tradução, geração de texto. | É toda a IA em uso hoje. |
| **IA geral (AGI)** | Capacidade de aprender e raciocinar em qualquer domínio, como uma pessoa. | Conceito ainda teórico. |
| **Superinteligência (ASI)** | Inteligência acima da humana em praticamente tudo. | Hipotética. |

</details>

<details open>
<summary><b>Paradigmas de aprendizado</b></summary>
<br>

| Paradigma | Como aprende | Exemplos de uso |
| :-- | :-- | :-- |
| **Supervisionado** | A partir de dados com resposta conhecida (rótulos). | Classificar e-mails como phishing, prever preços. |
| **Não supervisionado** | Encontra estrutura em dados sem rótulo. | Agrupamento de usuários, detecção de anomalias. |
| **Auto-supervisionado** | Gera os próprios rótulos a partir dos dados. | Pré-treino de modelos de linguagem. |
| **Por reforço** | Aprende por tentativa e erro, guiado por recompensas. | Jogos, robótica, otimização de decisões. |

</details>

<details open>
<summary><b>Famílias de modelos</b></summary>
<br>

| Família | Exemplos | Quando faz sentido |
| :-- | :-- | :-- |
| **Machine learning clássico** | Regressão, árvores de decisão, Random Forest, gradient boosting, SVM | Dados tabulares, problemas com poucos dados, necessidade de explicabilidade. |
| **Deep learning** | Redes convolucionais (CNN), recorrentes (RNN/LSTM), Transformers | Imagem, áudio, texto e dados complexos em grande volume. |
| **IA generativa** | LLMs, modelos de difusão, GANs, VAEs | Gerar texto, código, imagem; conversar; resumir. |
| **Sistemas com agentes** | LLM + ferramentas + memória + planejamento | Tarefas de várias etapas que exigem consultar e agir em outros sistemas. |

</details>

<details>
<summary><b>Técnicas que uso ou estudo em aplicações com LLM</b></summary>
<br>

- **Engenharia de prompt:** instruções claras, exemplos e formato de saída definido.
- **RAG (Retrieval-Augmented Generation):** o modelo consulta uma base de conhecimento (via embeddings e busca vetorial) antes de responder, o que reduz respostas inventadas e mantém o conteúdo atualizado.
- **Fine-tuning:** ajustar um modelo a um domínio ou estilo específico quando o prompt não basta.
- **Uso de ferramentas (tool use):** o modelo chama APIs e funções com argumentos estruturados.
- **Avaliação:** testes com casos reais e métricas (precisão, recall, taxa de falsos positivos) antes de confiar no resultado.
- **Guardrails:** validação de entrada e saída, limites de permissão e revisão humana em ações sensíveis.

</details>

<img src="assets/divider.svg" alt="" width="100%">

## 🛡️ Cibersegurança

<details open>
<summary><b>Princípios que guiam as decisões</b></summary>
<br>

| Princípio | Ideia central |
| :-- | :-- |
| **Tríade CIA** | Proteger a **confidencialidade**, a **integridade** e a **disponibilidade** da informação. |
| **Menor privilégio** | Cada pessoa e cada serviço recebe só o acesso de que precisa. |
| **Defesa em profundidade** | Várias camadas de controle, para que uma falha isolada não derrube tudo. |
| **Zero Trust** | Nenhuma conexão é confiável por padrão: verificar sempre, dentro e fora da rede. |
| **Secure by design** | Segurança entra na arquitetura, não como remendo no final. |

</details>

<details open>
<summary><b>Técnicas defensivas</b></summary>
<br>

| Camada | Técnicas |
| :-- | :-- |
| **Identidade e acesso** | Autenticação multifator (MFA), controle de acesso por papéis (RBAC), gestão de sessões e tokens |
| **Criptografia** | TLS em trânsito, criptografia em repouso, hash de senhas com algoritmos próprios para isso (bcrypt, Argon2), gestão de segredos |
| **Código seguro** | Validação e sanitização de entrada, consultas parametrizadas, tratamento de erros, revisão de código |
| **Cadeia de suprimentos** | Análise de dependências, atualização de pacotes vulneráveis, lockfiles |
| **Detecção** | Logs centralizados, monitoramento, alertas, SIEM, análise de comportamento |
| **Resposta a incidentes** | Preparação → detecção e análise → contenção, erradicação e recuperação → lições aprendidas |
| **Resiliência** | Backups testados, segmentação de rede, plano de recuperação |

</details>

<details>
<summary><b>Frameworks de referência</b></summary>
<br>

- **OWASP Top 10:** os riscos mais comuns em aplicações web (controle de acesso quebrado, injeção, falhas criptográficas, entre outros).
- **MITRE ATT&CK:** catálogo de táticas e técnicas de atacantes, útil para mapear detecções.
- **NIST Cybersecurity Framework:** organiza a gestão de risco em funções, da governança à recuperação.
- **ISO/IEC 27001:** padrão para sistemas de gestão de segurança da informação.

</details>

<img src="assets/divider.svg" alt="" width="100%">

## 🔗 Onde IA e cibersegurança se encontram

<table>
<tr>
<td width="50%" valign="top">

### IA para defender

- **Detecção de anomalias** em logs e tráfego de rede
- **Classificação** de phishing, spam e malware
- **Análise de comportamento** de usuários e contas (UEBA)
- **Triagem de alertas** e resumo de incidentes com LLMs, sempre com revisão humana

</td>
<td width="50%" valign="top">

### Proteger a IA

- **Prompt injection:** instruções maliciosas escondidas em texto que o modelo processa
- **Vazamento de dados sensíveis** em respostas ou no treino
- **Excesso de autonomia:** agentes com permissões demais
- **Envenenamento de dados** e ataques à cadeia de suprimentos de modelos
- **Ataques adversariais:** entradas feitas para enganar o modelo

</td>
</tr>
</table>

Referência para esse segundo lado: o projeto **OWASP Top 10 for LLM Applications**. As defesas combinam validação de entrada e saída, menor privilégio para agentes, separação entre dados e instruções, monitoramento e revisão humana.

<img src="assets/divider.svg" alt="" width="100%">

## 🚀 Projetos

<a href="https://netsenti.com">
  <picture>
    <source media="(max-width: 640px)" srcset="assets/project-netsenti-ai-mobile.svg">
    <img src="assets/project-netsenti-ai.svg" alt="Netsenti AI — IA aplicada à cibersegurança e à segurança digital. Site: netsenti.com" width="100%">
  </picture>
</a>

**[Netsenti AI](https://netsenti.com)** é um projeto próprio, criado por mim do conceito ao protótipo, que une inteligência artificial e cibersegurança.
**Status:** protótipo em desenvolvimento. · **Código:** [github.com/flayksdev/netsent_ai](https://github.com/flayksdev/netsent_ai)

<br>

<picture>
  <source media="(max-width: 640px)" srcset="assets/project-larmatch-mobile.svg">
  <img src="assets/project-larmatch.svg" alt="LarMatch — descoberta e matching personalizado de imóveis" width="100%">
</picture>

**LarMatch** é um produto de descoberta de imóveis personalizada, que conecta cada pessoa aos imóveis que fazem sentido para o que ela procura.

<img src="assets/divider.svg" alt="" width="100%">

## 🛠️ Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

<img src="assets/divider.svg" alt="" width="100%">

## 🎓 Formação e estudos

- **Engenharia de Software** — graduação em andamento.
- **Alura (2026)** — React 19, React com TypeScript, React full stack, JavaScript, Python, HTML e CSS, Padrões de API e Lógica de programação, além de trilhas introdutórias de Node.js, **Cloud Security**, Engenharia de Dados, Governança de Dados e UI Design.
- **Idiomas** — português nativo, inglês intermediário.

## 💼 Disponível para oportunidades

Busco vaga de **desenvolvedor de software** (web, Android e IA), de preferência em **regime remoto**. Trabalho bem em equipe e gosto de aprender com quem sabe mais.

<img src="assets/divider.svg" alt="" width="100%">

## 📊 Atividade no GitHub

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=flayksdev&show_icons=true&theme=tokyonight&bg_color=050A18&title_color=22D3EE&icon_color=3B82F6&text_color=F0F7FF&border_color=1E3A8A&count_private=true" alt="Estatísticas do GitHub de flayksdev">
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=flayksdev&layout=compact&theme=tokyonight&bg_color=050A18&title_color=22D3EE&text_color=F0F7FF&border_color=1E3A8A" alt="Linguagens mais usadas por flayksdev">

</div>

<sub>Gráficos gerados por serviço de terceiros a partir de dados públicos do perfil; não são dados oficiais do GitHub. Se a imagem não carregar, o perfil completo está em [github.com/flayksdev](https://github.com/flayksdev).</sub>

<img src="assets/divider.svg" alt="" width="100%">

## 📬 Contato

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-flayks--oliveira-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/flayks-oliveira/)
[![E-mail](https://img.shields.io/badge/E--mail-flayksdev@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:flayksdev@gmail.com)
[![Netsenti AI](https://img.shields.io/badge/Netsenti_AI-netsenti.com-0B1220?style=for-the-badge&logo=googlechrome&logoColor=22D3EE)](https://netsenti.com)
[![GitHub](https://img.shields.io/badge/GitHub-flayksdev-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/flayksdev)

<sub>FLAYKS OLIVEIRA · Software Engineer · Founder · AI · Cybersecurity</sub>

</div>

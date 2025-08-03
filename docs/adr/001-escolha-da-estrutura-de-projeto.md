# 1. Título

ADR 001: Escolha da Estrutura de Projeto por Features (Vertical Slices)

## 2. Status

Aceito

## 3. Contexto

Ao criar o template base para microsserviços, precisamos definir um padrão de organização de código-fonte que seja escalável, de fácil manutenção e intuitivo para os desenvolvedores. As principais alternativas consideradas para organizar o código dentro da pasta `src/` foram o padrão MVC (Model-View-Controller) e a organização por Features (também conhecida como Vertical Slices).

## 4. Decisão

Decidimos adotar a **estrutura por Features (Vertical Slices)**. Nesta abordagem, todo o código relacionado a um único domínio de negócio (ex: `users`, `products`) é agrupado em sua própria pasta. Cada pasta de feature contém seus próprios arquivos de rotas, controllers (lógica de negócio) e schemas (validação de dados).

## 5. Consequências

### Positivas:
* **Alta Coesão:** O código relacionado a uma mesma funcionalidade permanece junto, facilitando a localização e a modificação.
* **Baixo Acoplamento:** As features são mais independentes umas das outras. Alterar a feature de "usuários" tem menos chance de impactar a de "produtos".
* **Escalabilidade:** Fica muito mais simples extrair uma feature que cresceu demais para o seu próprio microsserviço no futuro.
* **Facilidade de Navegação:** Para entender uma funcionalidade, o desenvolvedor precisa olhar para apenas uma pasta.

### Negativas:
* Pode gerar um número ligeiramente maior de arquivos no início do projeto em comparação com o modelo MVC.
* Requer disciplina da equipe para não criar dependências cruzadas indevidas entre as features.
# Primeiros Passos no Google Cloud: Criando e Configurando um Projeto

Este guia rápido vai te ensinar como criar um novo projeto no Google Cloud Platform (GCP) e vincular uma conta de faturamento (como créditos promocionais), um passo essencial para começar a usar os serviços da Google Cloud. Além disso, mostraremos como obter o **ID do seu projeto**, que é fundamental para interagir com o Google Cloud via linha de comando (`gcloud CLI`).

---

## 1. Resgatando Seus Créditos (Se Aplicável)

Se você recebeu um link para **resgatar créditos do Google Cloud**, siga estes passos primeiro:

1.  **Acesse o Link de Resgate**: Você receberá um link por e-mail, geralmente de um domínio como `tripegcp.dev`. Clique nele para iniciar o processo.
2.  **Faça Login com o Google**: Ao acessar a página, você será solicitado a fazer login com sua conta Google. Selecione a conta que deseja usar.
3.  **Autorize o Compartilhamento**: O site de resgate de créditos pode pedir permissão para compartilhar seu nome, e-mail e foto de perfil com eles. Clique em **"Continuar"** para prosseguir.
4.  **Confirme o Resgate**: Após a autorização, uma mensagem confirmará que seus créditos estão disponíveis. Clique no botão indicado (geralmente algo como "clique aqui para ter acesso aos seus créditos").
5.  **Aplique os Créditos**: Você será redirecionado para uma página do Google Cloud para aplicar o cupom. Verifique seus dados (nome, sobrenome) e o código do cupom. Clique em **"Aceitar e continuar"**.
6.  **Confirmação**: Uma mensagem de "Crédito aplicado com sucesso" aparecerá. Seus créditos agora estão vinculados à sua conta do Google Cloud!

---

## 2. Criando um Novo Projeto

No Google Cloud, todos os recursos são organizados em **projetos**. É como um contêiner para seus aplicativos, dados e configurações.

1.  **Acesse o Console do Google Cloud**: Vá para [console.cloud.google.com](https://console.cloud.google.com/).
2.  **Abra o Seletor de Projetos**: No topo da página, ao lado do logo "Google Cloud", procure um ícone de seleção de projeto (geralmente com o nome do projeto atual ou "Meu Primeiro Projeto"). Clique nele.
3.  **Crie um Novo Projeto**: Na janela que se abre, clique em **"Novo Projeto"**.
4.  **Nomeie Seu Projeto**: Dê um nome para o seu projeto (ex: `imersao-alura`, `meu-app-incrivel`). Escolha um nome que seja fácil de identificar.
5.  **Crie o Projeto**: Clique em **"Criar"**. Aguarde alguns instantes até que o projeto seja provisionado.
6.  **Selecione o Projeto Recém-Criado**: Após a criação, o Google Cloud pode não selecionar o novo projeto automaticamente. No seletor de projetos, clique no seu novo projeto para alternar para ele.

---

## 3. Obtendo o ID do Projeto

O **ID do projeto** é um identificador único globalmente para o seu projeto e é diferente do nome que você deu a ele. Você precisará dele para muitas operações de linha de comando.

1.  **Localize o ID do Projeto**: Com o seu projeto selecionado no console (você pode verificar o nome do projeto no topo da página), procure pelo **"ID do Projeto"** logo abaixo do nome do projeto. Geralmente ele aparece como um texto cinza menor.
    * Exemplo: Se o nome do seu projeto é "Alura Imersão", o ID pode ser algo como `alura-imersao-123456`.
2.  **Copie o ID do Projeto**: Anote ou copie esse ID. Ele será usado em comandos como o `gcloud CLI`.
3.  **Configure o Projeto no gcloud CLI (Opcional, mas recomendado)**: Se você tiver o SDK do Google Cloud instalado, pode definir o projeto padrão para seus comandos, evitando digitá-lo sempre:
    ```bash
    gcloud config set project [ID_DO_PROJETO_DO_GOOGLE_CLOUD]
    ```
    **Lembre-se de substituir `[ID_DO_PROJETO_DO_GOOGLE_CLOUD]` pelo ID que você copiou!**

---

## 4. Vinculando a Conta de Faturamento ao Seu Projeto

Mesmo com créditos, você precisa **vincular uma conta de faturamento** ao seu projeto para que ele possa usar esses créditos e para que você possa implantar aplicações.

1.  **Acesse a Seção de Faturamento**: Com o seu novo projeto selecionado, navegue até o menu de navegação lateral (geralmente as três linhas horizontais no canto superior esquerdo). Procure e clique em **"Faturamento"**.
2.  **Vincular Conta de Faturamento**: O Google Cloud informará que "Este projeto não tem nenhuma conta de faturamento". Clique em **"Vincular uma conta de faturamento"**.
3.  **Selecione Sua Conta de Créditos**: Uma janela aparecerá com suas contas de faturamento disponíveis. Selecione a conta de faturamento que possui os créditos (geralmente terá um nome como "Conta de faturamento de avaliação no Google Cloud Platform").
4.  **Definir Conta**: Clique em **"Definir conta"**.
5.  **Confirmação**: Você será redirecionado para a página de faturamento do projeto e verá que os créditos estão ativos. Você pode verificar o saldo restante na seção **"Créditos"** (abaixo de "Estimativa de custo e preço" no menu lateral esquerdo).

---

Agora seu projeto está criado, configurado com seus créditos e você sabe como encontrar seu ID! Você está pronto para começar a explorar os serviços do Google Cloud e fazer o deploy da sua aplicação.

Se tiver alguma dúvida, sinta-se à vontade para perguntar!
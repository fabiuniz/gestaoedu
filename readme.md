<!-- 
  Tags: DevOps,Dev,Monolíto
  Label: Sistema de Gestão Escolar
  Description: Descrição do projeto
  path_hook: hookfigma.hook6,hookfigma.hook7,hookfigma.hook14
-->

# Sistema de Gestão Escolar

![Logo](images/gestaoedu.png)

## Descrição
O **Sistema de Gestão Escolar** é uma aplicação web desenvolvida para gerenciar alunos, cursos e matrículas em uma instituição de ensino. A aplicação possui uma API backend construída com **FastAPI** e um frontend interativo desenvolvido com **React** e **Tailwind CSS**. O banco de dados é gerenciado por **SQLAlchemy** com SQLite, e a aplicação é containerizada utilizando **Docker**. Este projeto foi desenvolvido como parte da **Imersão DevOps da Alura**.

## Funcionalidades
- **Gerenciamento de Alunos**:
  - Criar, editar e excluir alunos.
  - Buscar alunos por nome (parcial ou completo) ou email.
- **Gerenciamento de Cursos**:
  - Criar e atualizar cursos.
  - Visualizar detalhes de cursos (exclusão de cursos não é permitida).
- **Gerenciamento de Matrículas**:
  - Criar matrículas associando alunos a cursos.
  - Consultar matrículas por nome do aluno ou código do curso.
- **Validações**:
  - Validação robusta de email no frontend.
  - Tratamento de erros da API com mensagens detalhadas.
- **Interface de Usuário**:
  - Navegação por abas (Alunos, Cursos, Matrículas).
  - Modais para formulários de criação/edição.
  - Notificações de sucesso ou erro.
- **Containerização**:
  - Configuração para rodar a aplicação em um container Docker.
- **CI/CD**:
  - Configuração inicial de pipeline CI no GitHub Actions para construção de imagens Docker.

## Tecnologias Utilizadas
- **Backend**:
  - **Python 3.9+**: Linguagem principal.
  - **FastAPI**: Framework para construção da API.
  - **SQLAlchemy**: ORM para gerenciamento do banco de dados SQLite.
  - **Pydantic**: Validação de dados.
- **Frontend**:
  - **React 18**: Biblioteca para construção da interface de usuário.
  - **Tailwind CSS**: Framework CSS para estilização.
  - **Babel**: Para transpilar JSX no navegador.
- **Infraestrutura**:
  - **Docker**: Containerização da aplicação.
  - **Docker Compose**: Gerenciamento de serviços para desenvolvimento local.
  - **GitHub Actions**: Pipeline CI para construção de imagens Docker.
- **Banco de Dados**:
  - **SQLite**: Banco de dados leve para desenvolvimento.

## Estrutura do Projeto
```
gestaoedu/
├── routers/
│   ├── alunos.py         # Rotas para gerenciamento de alunos
│   ├── cursos.py         # Rotas para gerenciamento de cursos
│   ├── matriculas.py     # Rotas para gerenciamento de matrículas
├── templates/
│   ├── index.html        # Frontend React com Tailwind CSS
├── app.py                # Ponto de entrada da API FastAPI
├── database.py           # Configuração do banco de dados SQLite
├── models.py             # Modelos SQLAlchemy (Aluno, Curso, Matricula)
├── schemas.py            # Esquemas Pydantic para validação
├── requirements.txt      # Dependências do Python
├── docker-compose.yml    # Configuração do Docker Compose
├── .github/
│   ├── workflows/
│   │   ├── docker-image.yml  # Pipeline CI para Docker
```

## Pré-requisitos
- **Python 3.9+**: Para rodar o backend localmente.
- **Docker** e **Docker Compose**: Para rodar a aplicação em containers.
- **Node.js** (opcional): Caso queira trabalhar diretamente com o frontend fora do container.
- **Git**: Para clonar o repositório.

## Instalação e Configuração
1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd gestaoedu
   ```

2. **Instale as dependências do Python** (se não usar Docker):
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o ambiente**:
   - O banco de dados SQLite (`escola.db`) será criado automaticamente na primeira execução.
   - Certifique-se de que a porta `8000` está livre.

4. **Execute a aplicação localmente** (sem Docker):
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```
   Acesse o frontend em `http://localhost:8000` e a documentação da API em `http://localhost:8000/docs`.

5. **Execute com Docker**:
   ```bash
   docker-compose up --build
   ```
   - O Docker Compose construirá a imagem e iniciará o container.
   - Acesse o frontend em `http://localhost:8000`.

## Uso
- **Frontend**:
  - Acesse `http://localhost:8000` para interagir com a interface.
  - Use as abas "Alunos", "Cursos" e "Matrículas" para gerenciar as entidades.
  - A busca por alunos e matrículas é feita por nome (parcial ou completo) ou código do curso.
  - Notificações aparecem no canto superior direito para ações realizadas ou erros.

- **API**:
  - A documentação interativa está disponível em `http://localhost:8000/docs`.
  - Endpoints principais:
    - **Alunos**: `GET /alunos`, `POST /alunos`, `PUT /alunos/{aluno_id}`, `DELETE /alunos/{aluno_id}`, `GET /alunos/nome/{nome_aluno}`, `GET /alunos/email/{email_aluno}`
    - **Cursos**: `GET /cursos`, `POST /cursos`, `PUT /cursos/{codigo_curso}`, `GET /cursos/{codigo_curso}`
    - **Matrículas**: `POST /matriculas`, `GET /matriculas/aluno/{nome_aluno}`, `GET /matriculas/curso/{codigo_curso}`

## Solução de Problemas
- **Erro 422 (Unprocessable Entity)**:
  - Verifique se os dados enviados (ex.: email, IDs) são válidos.
  - Certifique-se de que os campos obrigatórios estão preenchidos no formulário.
- **Erro de CORS**:
  - Adicione a URL do frontend à lista `origins` em `app.py` (ex.: `http://localhost:3000` se o frontend estiver em outra porta).
- **Erro de chave única no React**:
  - Certifique-se de que cada elemento em listas (ex.: alunos, cursos, matrículas) tenha um `key` único. No componente `MatriculasTab`, use `index` ou outro identificador único para os itens renderizados.
- **Erro de conexão com a API**:
  - Verifique se o backend está rodando (`http://localhost:8000` ou `http://vmlinuxd:8000` no caso de containers).
  - Confirme que a variável `API_BASE_URL` em `index.html` está correta.

## Créditos
Este projeto foi desenvolvido durante a **Imersão DevOps da Alura**:

## Contribuição
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE).

## 👨‍💻 Autor

[Fabiano Rocha/Fabiuniz](https://github.com/SeuUsuarioGitHub)
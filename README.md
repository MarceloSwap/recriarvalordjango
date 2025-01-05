# ReCriarValor

## Seu lixo pode ser matéria-prima para outros.

## Descrição
O **ReCriarValor** é uma aplicação web desenvolvida para facilitar a interação entre usuários conectando doadores de resíduos a outros interessados em reaproveitá-los para gerar valor social e econômico.

## Tecnologias Utilizadas

- **Python** e **Django**: Para o desenvolvimento do backend.
- **PostgreSQL**: Como banco de dados principal.
- **Tailwind CSS**: Para estilização e design responsivo.
- **Bootstrap**: Alguns formulários.
- **Railway**: Como plataforma de deploy.

## Funcionalidades Principais

- Cadastro e edição de perfis de usuários.
- Integração com bancos de dados para persistência de dados.
- Design responsivo.

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/recriarvalor.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd recriarvalor
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure as variáveis de ambiente para o banco de dados PostgreSQL e outros segredos:
   ```bash
   export DATABASE_URL=postgres://usuario:senha@localhost:5432/nome_do_banco
   export SECRET_KEY=sua_chave_secreta
   ```

6. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

8. Acesse a aplicação no navegador em: [http://localhost:8000](http://localhost:8000).

## Deploy
O deploy do projeto pode ser realizado no Railway seguindo os passos:

1. Configure o repositório no Railway.
2. Defina as variáveis de ambiente, incluindo `DATABASE_URL` e `SECRET_KEY`.
3. Configure os arquivos estáticos utilizando o `whitenoise` ou similar.

## Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Minha feature"
   ```
4. Envie as alterações para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a [LICENÇA MIT](LICENSE).

---

Sinta-se à vontade para ajustar e expandir conforme necessário!

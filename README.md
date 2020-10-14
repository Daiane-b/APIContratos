<h1 align="center">API Contratos</h1>

## Descrição do Projeto
<p align="center">API elaborada para gerenciar contratos e o envio de documentos</p>
<h1 align="center">
    <a href="https://www.djangoproject.com/">🔗 Django</a>
</h1>
<p align="center">Python framework para agilizar o desenvolvimento </p>
<h1 align="center">
    <a href="https://www.django-rest-framework.org/">🔗 Django Rest Framework</a>
</h1>
<p align="center">Toolkit para construção de web APIs</p>

### Features

- [x] Cadastro de contratos
- [x] Cadastro de documentos
- [x] Delete contratos
- [x] Update contratos
- [ ] Update de documentos
- [ ] Delete documentos

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [mySQL](https://www.mysql.com/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

### Documentação
<p><b>POST</b> Adicionar Contrato</p>
<p>api/addContrato<p>

<table>
<tr>
    <th>Parâmetro</th>
    <th>Descrição</th>
</tr>
<tr>
<td>nome</td>
<td>(Obrigatório) nome do contratante VARCHAR</td>
</tr>
<tr>
<td>email</td>
<td>(Obrigatório) email do contratante VARCHAR</td>
</tr>
<tr>
<td>CPF</td>
<td>(Obrigatório) CPF do contratante VARCHAR</td>
</tr>
<tr>
<td>Renda</td>
<td>(Obrigatório) Renda do contratante FLOAT</td>
</tr>
<tr>
<td>Rua</td>
<td>(Opcional) Rua onde o contratante mora VARCHAR</td>
</tr>
<tr>
<td>Numero</td>
<td>(Opcional) Número onde o contratante mora INT</td>
</tr>
<tr>
<td>Bairro</td>
<td>(Opcional) Bairro onde o contratante mora VARCHAR</td>
</tr>
<tr>
<td>Cidade</td>
<td>(Opcional) Cidade onde o contratante mora VARCHAR</td>
</tr>
<tr>
<td>Estado</td>
<td>(Opcional) Estado onde o contratante mora, formato (RJ, SP...) VARCHAR</td>
</tr>
<tr>
<td>Estado Civil</td>
<td>(Opcional) Estado civil do contratante VARCHAR</td>
</tr>
<tr>
<td>Data de Nascimento</td>
<td>(Opcional) Data de nascimento do contratante DATE</td>
</tr>
<tr>
<td>Valor</td>
<td>(Obrigatório) Valor do contrato FLOAT</td>
</tr>
</table>
<p><b>Content-Type</b> application/json</p>
<h4>Exemplo Request</h4>
{
    "nome": "Daiane",
    "email": "teste@teste.com.br",
    "cpf":"21333333333",
    "renda":1000,
    "valor": 20000
}
<h4>Exemplo Response</h4>
{
    "Contrato": {
        "id": 5,
        "valor": 20000.0,
        "status": [
            1,
            "criado"
        ],
        "usuarioId": 13,
        "statusAprovacao": ""
    },
    "User": {
        "id": 13,
        "nome": "Daiane",
        "email": "teste@teste.com.br",
        "cpf": "21333333333",
        "renda": 1000.0,
        "rua": "",
        "numero": 0,
        "bairro": "",
        "cidade": "",
        "estado": "",
        "estadoCivil": "",
        "dataNascimento": "2020-10-14"
    }
}
<p></p>
</br>
<p><b>GET</b> Contrato</p>
<p>api/contrato/id<p>
<p>Requisições PUT e DELETE seguem o mesmo modelo</p>
<h4>Exemplo Response</h4>
{
    "contrato": {
        "id": 1,
        "valor": 300.0,
        "status": 1,
        "usuarioId": 9,
        "statusAprovacao": 1
    },
    "usuario": {
        "id": 9,
        "nome": "Daiane",
        "email": "teste@teste.com.br",
        "cpf": "21333333333",
        "renda": 1000.0,
        "rua": "",
        "numero": 0,
        "bairro": "",
        "cidade": "",
        "estado": "",
        "estadoCivil": "",
        "dataNascimento": "2020-10-13"
    }
}
<p></p>

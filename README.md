# Avaliação Prática do Processo Seletivo BackOffice TI | Raccoon Marketing Digital - Fevereiro de 2023


Orientações
=
Esta atividade tem o intuito de testar os conhecimentos técnicos utilizados para o desenvolvimento de atividades do departamento de BackOffice TI.

Realize os passos descritos neste documento para realizar a entrega adequada do código que soluciona o problema proposto.

Enunciado
=
Os Recursos Humanos (RH) do Grupo Raccoon estão liderando uma iniciativa para centralizar dados dos funcionários.

Para isso, solicitaram ao time de Tecnologia da Informação um script que extraia e transforme os dados de funcionários automaticamente, para facilitar as consultas aos dados pessoais e profissionais.

Realize cada um dos sete passos descritos a partir da próxima página para ajudar o RH a automatizar esse processo.

A partir da página 3 deste documento, você encontrará dicas para a solução de algumas etapas deste processo seletivo.

Considere entregar a solução ainda que não tenha completado todas as etapas.

Script
=
1. Escolha uma linguagem de programação entre Python, Node.js ou JavaScript para desenvolver a solução.

2. Faça uma requisição ao arquivo JSON desenvolvido para retornar os dados de funcionários.

3. O link para obter acesso aos dados dos funcionários é https://storage.googleapis.com/raccoon-humane/psel.json (vide página 3).

4. Ao realizar com sucesso a requisição, ou seja, obtendo um status code igual a 200, você receberá uma lista de objetos, onde cada objeto contém nome, número do CPF, cargo e salário de um funcionário (vide página 4).

5. Faça a validação do número de CPF de cada funcionário, segundo os critérios descritos aqui. Adicione a chave cpf_valido ao objeto do funcionário testado com o valor true para os CPFs válidos e false para os CPFs inválidos (vide página 5).

6. Identifique os cargos de cada um dos funcionários, crie a chave adicional_insalubridade para cada objeto e atribua seu valor seguindo os critérios abaixo (vide página 5):
Assassin        5% do Salário
Batman          10% do Salário
Butler          Não Há Adicional de Insalubridade
Side Kick       15% do Salário
The Chief Demon 12,5% do Salário

7. Imprima os dados completos dos funcionários de toda a empresa acrescidos das chaves cpf_valido e adicional_insalubridade com os valores corretos conforme descritos na página 5.

8. Subir o código no Github em um repositório publico e nos encaminhar o link do repositório.

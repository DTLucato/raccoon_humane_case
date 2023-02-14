import json
import requests
import check_cpf

URL = "https://storage.googleapis.com/raccoon-humane/psel.json"

result_input = requests.get(url=URL)

text_data = json.loads(result_input.text)

if (result_input.status_code == 200):

    json_size = len(text_data)

    result_final = []

    for x in range(json_size):

        nome = text_data[x]["nome"]

        cpf = text_data[x]["cpf"]

        cargo = text_data[x]["cargo"]

        salario = text_data[x]["salario"]

        cpf_invalido = check_cpf.validar_cpf(cpf)

        if (cargo == "Assassin"):
            adicional_insalubridade = round(float(salario) * 0.05, 2)
        elif (cargo == "Batman"):
            adicional_insalubridade = round(float(salario) * 0.10, 2)
        elif (cargo == "Butler"):
            adicional_insalubridade = 0
        elif (cargo == "Side Kick"):
            adicional_insalubridade = round(float(salario) * 0.15, 2)
        elif (cargo == "The Chief Demon"):
            adicional_insalubridade = round(float(salario) * 0.125, 2)

        item_json = {"nome": nome, "cpf": cpf, "cargo": cargo, "salario": salario, "cpf_valido": cpf_invalido,
                     "adicional_insalubridade": adicional_insalubridade}

        result_final.append(item_json)

    result_output = json.dumps(result_final, ensure_ascii=False).encode('utf8')

    print(result_output.decode())

    with open('Resultado.json', 'w', encoding='utf-8') as f:
        f.write(result_output.decode("utf-8"))






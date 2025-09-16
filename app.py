from flask import Flask, render_template, request
from model.Personagem import Personagem
from model.Atributos import Atributos
from model.Raca import Raca
from model.Classe import Classe

app = Flask(__name__)

personagens_criados = []
valores_temp = []  # guarda valores gerados antes da distribuição
dados_temp = {}    # guarda nome, idade, raca, classe antes da distribuição


@app.route("/", methods=["GET", "POST"])
def index():
    global valores_temp, dados_temp

    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        raca_escolha = request.form.get("raca")
        classe_escolha = request.form.get("classe")
        estilo = request.form.get("estilo")

        # Se estamos distribuindo valores (segunda etapa)
        if "atributo_1" in request.form:
            escolhas = [request.form.get(f"atributo_{i}") for i in range(1, 7)]

            # Criar objetos
            p = Personagem()
            r = Raca()
            a = Atributos()
            c = Classe()

            p.nome = dados_temp["nome"]
            p.idade = int(dados_temp["idade"])
            r.escolhaRaca(int(dados_temp["raca"]))
            r.atributosRaca(p.idade)
            c.escolhaClasse(int(dados_temp["classe"]))

            # Distribui valores conforme escolha do usuário
            a.distribuir_valores(escolhas, valores_temp)

            # Salva personagem
            personagens_criados.append({
                "nome": p.nome,
                "idade": p.idade,
                "raca": r.raca,
                "classe": c.tipo,
                "atributos": a.atributos_com_descricoes(),
                "habilidades_raca": r.habilidades,
                "habilidades_classe": c.habilidades
            })

            # Limpa variáveis temporárias
            valores_temp = []
            dados_temp = {}

        else:
            # Primeira etapa: sorteio
            a = Atributos()
            if estilo == "1":
                a.gerar_clássico()

                p = Personagem()
                r = Raca()
                c = Classe()
                p.nome = nome
                p.idade = int(idade)
                r.escolhaRaca(int(raca_escolha))
                r.atributosRaca(p.idade)
                c.escolhaClasse(int(classe_escolha))

                personagens_criados.append({
                    "nome": p.nome,
                    "idade": p.idade,
                    "raca": r.raca,
                    "classe": c.tipo,
                    "atributos": a.atributos_com_descricoes(),
                    "habilidades_raca": r.habilidades,
                    "habilidades_classe": c.habilidades
                })
            else:
                # Gera valores e pede para distribuir no front-end
                if estilo == "2":
                    valores_temp = a.gerar_valores_aventureiro()
                elif estilo == "3":
                    valores_temp = a.gerar_valores_heroico()

                dados_temp = {
                    "nome": nome,
                    "idade": idade,
                    "raca": raca_escolha,
                    "classe": classe_escolha
                }

                return render_template("distribuir.html", valores=valores_temp)

    return render_template("index.html", personagens=personagens_criados)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

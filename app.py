from flask import Flask, render_template, request
from model.Personagem import Personagem
from model.Atributos import Atributos
from model.Raca import Raca
from model.Classe import Classe

app = Flask(__name__)


personagens_criados = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = int(request.form["idade"])
        raca_escolha = int(request.form["raca"])
        classe_escolha = int(request.form["classe"])
        estilo = request.form["estilo"]

        
        p = Personagem()
        r = Raca()
        a = Atributos()
        c = Classe()

        p.nome = nome
        p.idade = idade

        
        r.escolhaRaca(raca_escolha)
        r.atributosRaca(p.idade)
        c.escolhaClasse(classe_escolha)

        
        if estilo == "1":
            a.gerar_clássico()
        elif estilo == "2":
            a.gerar_aventureiro()
        elif estilo == "3":
            a.gerar_heroico()

        p.a = a

        
        personagens_criados.append({
            "nome": p.nome,
            "idade": p.idade,
            "raca": r.raca,
            "classe": c.tipo,
            "atributos": a.AtributosRandom,
            "habilidades_raca": r.habilidades,
            "habilidades_classe": c.habilidades
        })

    return render_template("index.html", personagens=personagens_criados)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

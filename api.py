import flask, json, tensorflow as tf
app = flask.Flask(__name__)
model = tf.keras.models.load_model('sumator.h5')
@app.route("/help")
def help():
    return json.dumps("OLÁ E BEM VINDO. Você esta pronto para pedir para a deusa das IAs fazer um calculo?? Caso sim, apenas escreva /sum/number1/number2/number3/number4! ADIOS")
@app.route("/sum/<n1>/<n2>/<n3>/<n4>")
def sum(n1,n2,n3,n4):
    
    # int(n1), int(n2), int(n3), int(n4)
    a = [n1,n2,n3,n4]
    conta_a_ser_feita = []
    for i in a:
        if not i.isdigit():
            return "VOCÊ É BURRO?!!?!??! COMO OUSAS INSULTAR A INTELIGENCIA ARTIFICIAL COM LETRAR TÃO NÃO NUMÉRICAS?"
        else:
            conta_a_ser_feita.append(int(i))

        

    result_suma = model.predict([conta_a_ser_feita])
    return json.dumps(f"THE AI HAS SPOKEN. A RESPOSTA PELA QUAL PROCURAS ES (aproximadamente) {result_suma[0][0]}")

if __name__ == "__main__":
    app.run(debug=True)
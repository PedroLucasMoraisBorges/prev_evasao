import csv
import codecs
from django.conf import settings
from .models import *

import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "modelo_treinado.pkl")
model = joblib.load(MODEL_PATH)

class CreateDataFromCSV:
    @staticmethod
    def criarCursos(linhas_csv):
        linhas_csv = iter(linhas_csv)
        header = next(linhas_csv)

        if not all(
            [
                ("ID" in header),
                ("ALUNO_BRANCO_AZUL" in header),
                ("COEFICIENTE" in header),
                ("FORMA_INGRESSO" in header),
                ("PERCENTUAL_CARGA_CUMPRIDA" in header),
                ("CH_TOTAL" in header),
                ("CIDADE_DIFERENTE" in header),

                ("SEXO" in header),
                ("ESTADOCIVIL" in header),
                ("IDADE" in header),
                ("TIPO_DE_INSTITUICAO" in header),
                ("RESPONSAVEL_FINANCEIRO" in header),

                ("BOLSA" in header),
                ("DEBITOS_NO_PERIDO" in header),
                ("AV1" in header),
                ("AV2" in header),
                ("ENTREGA1" in header),
                ("ENTREGA2" in header),
                ("ENTREGA3" in header),
                ("ENTREGA4" in header),
                ("ENTREGA5" in header),
                ("ENTREGA6" in header),
                ("AVF" in header),
                ("M_AV1" in header),
                ("M_AV2" in header),
                ("M_TDE" in header),
                ("AVF_COUNT" in header),
                ("FALTA_AT" in header),
                ("M_FALTA_PERIODO" in header),
                ("REPROV_TOT" in header)
            ]
        ):
            return {
                "error": "É necessário que o arquivo para predição contenha as colunas *."
            }
        
        FEATURE_COLUMNS = [
            "ALUNO_BRANCO_AZUL",
            "COEFICIENTE",
            "FORMA_INGRESSO",
            "PERCENTUAL_CARGA_CUMPRIDA",
            "CH_TOTAL",
            "CIDADE_DIFERENTE",
            "SEXO",
            "ESTADOCIVIL",
            "IDADE",
            "TIPO_DE_INSTITUICAO",
            "RESPONSAVEL_FINANCEIRO",
            "BOLSA",
            "DEBITOS_NO_PERIDO",
            "AV1",
            "AV2",
            "ENTREGA1",
            "ENTREGA2",
            "ENTREGA3",
            "ENTREGA4",
            "ENTREGA5",
            "ENTREGA6",
            "AVF",
            "M_AV1",
            "M_AV2",
            "M_TDE",
            "AVF_COUNT",
            "FALTA_AT",
            "M_FALTA_PERIODO",
            "REPROV_TOT"
        ]

        header_indexes = {field: index for index, field in enumerate(header)}

        objs_to_plot = []
        for idx, line in enumerate(linhas_csv, start=1):
            critical_features = []
            features = [
                float(line[header_indexes[col]]) if line[header_indexes[col]] != "" else 0.0
                for col in FEATURE_COLUMNS
            ]
            prediction = model.predict([features])
            prob = getattr(model, "predict_proba", lambda x: None)([features])

            aluno = line[header_indexes["ID"]]
            prediction = int(prediction[0]) if hasattr(prediction[0], "__int__") else str(prediction[0])

            if prediction == 1:
                if float(line[header_indexes["PERCENTUAL_CARGA_CUMPRIDA"]]) < 30:
                    critical_features.append("Percentual de carga cumprida muito baixo")
                if float(line[header_indexes["M_AV1"]]) < 5:
                    critical_features.append("Média da AV1 baixa")
                if float(line[header_indexes["BOLSA"]]) == 0:  
                    critical_features.append("Aluno sem bolsa de estudos")
                if float(line[header_indexes["BOLSA"]]) in [6, 7]:  
                    critical_features.append("Aluno com bolsa 50% ou 60%")
                if float(line[header_indexes["AV1"]]) < 6:   
                    critical_features.append("AV1 com nota baixa")
                if float(line[header_indexes["AVF"]]) > 0:
                    critical_features.append("Aluno ficou de AVF no último período")
                if float(line[header_indexes["DEBITOS_NO_PERIDO"]]) > 1:
                    critical_features.append("Múltiplos débitos no período")
                if float(line[header_indexes["FALTA_AT"]]) > 2:
                    critical_features.append("Frequência baixa")
                if float(line[header_indexes["COEFICIENTE"]]) < 8:
                    critical_features.append("Coeficiente baixo")

   
            objs_to_plot.append({
                "name": aluno,
                "features": critical_features,
                "prediction": prediction,
                "probability": float(prob[0][1]) if prob is not None else None,
                "features" : critical_features
            })

        return objs_to_plot

    @classmethod
    def read_csv(self, file_path):
        print(settings.MEDIA_ROOT)
        print(f"{file_path}")

        if file_path.startswith("/media/"):
            file_path = file_path.replace("/media/", "", 1)

        full_path = os.path.join(settings.MEDIA_ROOT, file_path)


        with codecs.open(full_path, "r", encoding="utf-8") as csv_file:
            file_lines = list(csv.reader(csv_file)) 

        return self.criarCursos(file_lines)

    
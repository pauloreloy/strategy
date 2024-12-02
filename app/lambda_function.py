from decorators.actc_context import actc_strategy
from classes.mapper import Mapper
import json

actc_proc = {
    "codigo_contrato_original": "123456",
    "codigo_contrato_scr": "123",
    "identificador_padronizado_operacoes_credito": "IPOC123456789",
    "indicador_mais_de_um_ipoc_por_contrato": "N",
    "cnpj_base_if_credora_original_contrato": "12345678000100",
    "tipo_ente_consignante": "01",
    "grupo_parcela_normal": 
        {
            "valor_face_parcela": 100,
            "data_primeira_parcela": "10-10-2020"
        }
    ,
    "grupo_parcela_irregular": [
        {
            "valor_face_parcela": 100,
            "data_primeira_parcela": "10-10-2020"
        },
        {
            "valor_face_parcela": 100,
            "data_primeira_parcela": "10-10-2020"
        }
    ],
    "data_contratacao_operacao": "2024-01-15",
    "data_liberacao_novo_recurso": "2024-01-20",
    "data_referencia_saldo_devedor_contabil": "2024-11-01",
    "valor_saldo_devedor_contabil": 150000.75
}


@actc_strategy
def get_actc(actc_type):
    return get_actc(actc_type)

if __name__ == "__main__":
    actc_type = "ACTC103"
    actc = get_actc(actc_type)    
    xml = actc.generate_xml(actc_proc)
    print(xml)
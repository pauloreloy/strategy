from classes.strategies.actc_base import ACTC
import json
import logging
import xmltodict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from typing import List, Optional, TypedDict

class GrupoACTC103ParclNorml(TypedDict):
    NumParcl: int
    DtVencParcl: str
    VlrParcl: float

class GrupoACTC103ParclIrreglr(TypedDict):
    NumParcl: int
    DtVencParcl: str
    VlrParcl: float

class GrupoACTC103FlxPgto(TypedDict):
    TpFlxPgto: str
    Grupo_ACTC103_ParclNorml: Optional[List[GrupoACTC103ParclNorml]]
    Grupo_ACTC103_ParclIrreglr: Optional[List[GrupoACTC103ParclIrreglr]]

class GrupoACTC103PortlddAprovd(TypedDict):
    CodContrtoOr: str
    CodContrtoSCR: str
    IPOC: str
    Ind_MultIPOC: str
    VlrSaldDevdrContb: float
    VlrTxJuros: float
    VlrIOF: float
    QtdDiasCaren: int
    DtUltPgto: str
    DtVencUltParcl: str
    TpPrdCaren: str
    Grupo_ACTC103_FlxPgto: GrupoACTC103FlxPgto
    IOFRecContrtoOrig: Optional[float]
    IOFAlqContrtoOrigBas: float
    IOFAlqContrtoOrigAdc: float
    CanalOperacaoOrigem: str
    CNPJCanalOrigem: str

class GrupoACTC103PortlddRecsd(TypedDict):
    MtvRecusaPortldd: str

class GrupoACTC103PortlddRetd(TypedDict):
    MtvRetenContrto: str
    DtRetenContrto: str
    CNPJCes: Optional[str]

class GrupoACTC103Portldd(TypedDict):
    IdentdPartAdmdo: str
    NUPortlddCTC: str
    NumCtrlIF: str
    Grupo_ACTC103_PortlddAprovd: Optional[GrupoACTC103PortlddAprovd]
    Grupo_ACTC103_PortlddRecsd: Optional[GrupoACTC103PortlddRecsd]
    Grupo_ACTC103_PortlddRetd: Optional[GrupoACTC103PortlddRetd]

class ACTC103(TypedDict):
    Grupo_ACTC103_Portldd: List[GrupoACTC103Portldd]

class ACTC103(ACTC):

    ACTC_GROUP_TAG = "ACTC103"

    @classmethod
    def generate_xml(cls, actc_proc: dict, actc_type: str):
        actc_data = super().map_actc_data(actc_type, actc_proc)
        print(actc_data)

        xml_str = xmltodict.unparse({cls.ACTC_GROUP_TAG: actc_data}, pretty=False)
        xml_str = '\n'.join(xml_str.split('\n')[1:])
        return xml_str


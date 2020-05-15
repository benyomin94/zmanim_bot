from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class GenericData:
    """
    A simple data struct like {'header': str, 'value': str}
    """
    header: str
    value: str


@dataclass
class GenericYomTovData:
    """
    A data class for yom tov with required first day and optional second day and shabbos
    """
    cl_1: GenericData
    cl_2: Optional[GenericData]
    cl_3: Optional[GenericData]
    havdala: GenericData
    date: Optional[GenericData] = None  # todo check none


@dataclass
class GenericYomTov:
    title: str
    data: GenericYomTovData


@dataclass
class GenericHoliday:
    title: str
    date: GenericData

# -------------- DAF YOMI DATA CLASSES -------------- #


@dataclass
class DYData:
    masehet: GenericData
    daf: GenericData


@dataclass
class DafYomi:
    title: str
    data: DYData

# -------------- ROSH HODESH DATA CLASSES -------------- #


@dataclass
class RHData:
    month: GenericData
    n_days: GenericData
    date: GenericData
    molad: GenericData


@dataclass
class RoshHodesh:
    title: str
    data: RHData

# -------------- SHABBOS DATA CLASSES -------------- #


@dataclass
class ShabosData:
    parasha: GenericData
    cl: Optional[GenericData]
    shkia_offset: Optional[str]
    tzeit_kochavim: Optional[GenericData]
    warning: Optional[str]
    error: Optional[str]


@dataclass
class Shabos:
    title: str
    data: ShabosData


# -------------- ZMANIM DATA CLASSES -------------- #


@dataclass
class Zmanim:
    title: str
    date: str
    zmanim: Dict[str, str]

# -------------- FAST DATA CLASSES -------------- #


@dataclass
class FastData:
    start_time: GenericData
    tzeit_kochavim: GenericData
    sba_time: GenericData
    nvr_time: GenericData
    ssk_time: GenericData
    hatzot: Optional[GenericData]


@dataclass
class Fast:
    title: str
    data: FastData


# -------------- YOM KIPPUR DATA CLASSES -------------- #

@dataclass
class YomKippurData:
    date: GenericData
    cl: GenericData
    havdala: GenericData


@dataclass
class YomKippur:
    title: str
    data: YomKippurData


# -------------- SUCCOS DATA CLASSES -------------- #

@dataclass
class SuccosData:
    date: GenericData
    cl_1: GenericData
    cl_2: Optional[GenericData]
    cl_3: Optional[GenericData]
    havdala: GenericData
    hoshana_raba: GenericData


@dataclass
class Succos:
    title: str
    data: SuccosData


# -------------- PESACH DATA CLASSES -------------- #
@dataclass
class PesachData:
    date: GenericData
    part_1: GenericYomTovData
    part_2: GenericYomTovData


@dataclass
class Pesach:
    title: str
    data: PesachData


# -------------- ISRAEL HOLIDAYS DATA CLASSES -------------- #
@dataclass
class IsraelHoliday:
    title: str
    date: GenericData


@dataclass
class IsraelHolidays:
    title: str
    yom_hashoa: IsraelHoliday
    yom_hazikaron: IsraelHoliday
    yom_haatzmaaut: IsraelHoliday
    yom_yerushalaim: IsraelHoliday
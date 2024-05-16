from .constants import TUMAN,RIAL
from phoenix.settings_server import CURRENCY


def to_price(value,unit=CURRENCY):
    # from core.repo import Parameter,ParameterNameEnum
    # (parameter,i)=Parameter.objects.get_or_create(name=ParameterNameEnum.CURRENCY)
    # unit=parameter.value
    # CURRENCY=parameter.value
    if unit==TUMAN:
        pass
    if unit==RIAL and CURRENCY==TUMAN:
        value=value*10
    """converts int to string"""  
    try:
        value=int(value)
        sign=''
        if value<0:
            value=0-value
            sign='- '
        a=separate(value)
        return sign+a+' '+unit
    except:
        return ""


def separate(price):
    
    try:
        price=int(price)
    except:
        return None
    
    if price<1000:
        return str(price)
    else:
        return separate(price/1000)+','+str(price)[-3:]

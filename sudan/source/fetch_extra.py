# Sources complementaires via les clients du depot humanitarian-secondary-data (clone dans ../hsd).
# Lancer : python3 -X utf8 fetch_extra.py   -> ecrit raw/extra/*.json
import sys,json,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','hsd','scripts','clients'))
OUT='raw/extra'
def save(name,fn):
    try:
        d=fn(); json.dump(d,open(f'{OUT}/{name}.json','w'),ensure_ascii=False,default=str); print('OK  ',name,len(d) if hasattr(d,'__len__') else '')
    except Exception as e: print('FAIL',name,type(e).__name__,str(e)[:160])
from hpc_client import HPCClient
from unhcr_client import UNHCRClient
from hapi_client import HAPIClient
from inform_client import *
h=HAPIClient()
save('fts_plans',lambda:HPCClient().get_plans('SDN',max_funded=8))
save('unhcr_origin',lambda:UNHCRClient().get_population(country_origin='SDN'))
save('hapi_needs',lambda:h.get_humanitarian_needs('SDN'))
save('hapi_food_prices',lambda:h.get_food_prices('SDN'))
save('hapi_returnees',lambda:h.get_returnees('SDN'))
save('hapi_funding',lambda:h.get_funding('SDN'))
save('hapi_op_presence',lambda:h.get_op_presence('SDN'))
save('hapi_rainfall',lambda:h.get_rainfall('SDN'))

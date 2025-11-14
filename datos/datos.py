import json

DATOS = {"nombres": ["MERCURIO","VENUS","TIERRA", "MARTE","JUPITER","SATURNO"],
         "puntos" : [{"jugada":"[UNO]", "valor":0, "bandera_uso":True},
                   {"jugada":"[DOS]","valor":0,"bandera_uso":True},
                   {"jugada":"[tRES]","valor":0,"bandera_uso":True},
                   {"jugada":"[CUATRO]","valor":0,"bandera_uso":True},
                   {"jugada":"[CINCO]","valor":0,"bandera_uso":True},
                   {"jugada":"[SEIS]","valor":0,"bandera_uso":True},
                   {"jugada":"[ESCALERA (20)]","valor":0,"bandera_uso":True},
                   {"jugada":"[FULL (30)]","valor":0,"bandera_uso":True},
                   {"jugada":"[POKER (40)]","valor":0,"bandera_uso":True},
                   {"jugada":"[GENERALA (50)]","valor":0,"bandera_uso":True}]}

with open ("archivo.json","w") as archivo:
    json.dump(DATOS,archivo, indent=4)
import json

DATOS = {"nombres": [["MERCURIO",1],["VENUS",2],["TIERRA",3],[ "MARTE",4],["JUPITER",5],["SATURNO",6]],
         "puntos" : [{"jugada":"[UNO]", "valor":0, "bandera_uso":True},
                   {"jugada":"[DOS]","valor":0,"bandera_uso":True},
                   {"jugada":"[TRES]","valor":0,"bandera_uso":True},
                   {"jugada":"[CUATRO]","valor":0,"bandera_uso":True},
                   {"jugada":"[CINCO]","valor":0,"bandera_uso":True},
                   {"jugada":"[SEIS]","valor":0,"bandera_uso":True},
                   {"jugada":"[ESCALERA (20)]","valor":0,"bandera_uso":True},
                   {"jugada":"[FULL (30)]","valor":0,"bandera_uso":True},
                   {"jugada":"[POKER (40)]","valor":0,"bandera_uso":True},
                   {"jugada":"[GENERALA (50)]","valor":0,"bandera_uso":True}]}




with open ("segundo_intento/datos/niveles.json","w") as archivo:
    json.dump(DATOS,archivo, indent=4)
    
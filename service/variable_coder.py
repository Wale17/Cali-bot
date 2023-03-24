
"""Decode the idtype"""
def encode_idtpe(idtype_code):
    try:
        if idtype_code == "CC":
            persona = "Natural"
            tipo_de_documento = "Cedula de ciudadania"
        
        if idtype_code == "TI":
            persona = "Natural"
            tipo_de_documento = "Tarjeta de identidad"

        if idtype_code == "PA":
            persona = "Natural"
            tipo_de_documento = "Pasaporte"

        if idtype_code == "NIT":
            persona = "Juridica"
            tipo_de_documento = "Nit"

        if idtype_code == "CE":
            persona = "Natural"
            tipo_de_documento = "Cedula de extranjeria"
    except:
        raise

    return persona, tipo_de_documento

def big_box_text(persona, document_type, fullname = None, idtype = None, ldnumber = None, FechaDeResoluciónSancionatoria = None, NoComparendoDelCaso = None, NoResoluciónSancionatoria = None, FechaDeComparendo = None, NombreRepresentateLegal = None, TipodeDocumentoRepresentateLegal = None, DocumentoRepresentateLegal = None):
    try:
        if persona == "Natural":
            if document_type.startswith("Derecho de petición"):
                description = "Buen día,\n Yo, {0}, identificado con {1} No. {2} con todo respeto manifiesto a usted que presentó derecho de petición.\n Cordialmente".format(fullname, idtype, ldnumber)
            if document_type.startswith("Caducidad"):
                description = "Buen día,/n Yo, {0}, identificado con {1} No. {2} con todo respeto manifiesto a usted que presentó caducidad contra el\n comparendo No. {3} del {4}.\n Cordialmente.".format(fullname, idtype, ldnumber, NoComparendoDelCaso, FechaDeComparendo)
            if document_type.startswith("Revocatoria"):
                description = "Buen día, \nYo, {0}, identificado con {1} No. {2} con todo respeto manifiesto a usted que presentó revocatoria directa contra la Resolución {3} del {4}. \nCordialmente.".format(fullname, idtype, ldnumber, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria) 
            if document_type == "Prescripción":
                description = "Buenas tardes, \nYo, {0}, identificado con {1} No. {2} con todo respeto manifiesto a usted que presento prescripción contra de la Resolución {3} del {4}. \nCordialmente.".format(fullname, idtype, ldnumber, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
    
        if persona == "Juridica":
            if document_type.startswith("Derecho de petición"):
                description = "Buen día, \nYo, {0}, identificado con {1} No. {2} representante legal de la empresa {3} identificada con Nit No. {4} con todo respeto manifiesto a usted que presentó derecho de petición. \nCordialmente.".format(NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, fullname, ldnumber)
            if document_type.startswith("Caducidad"):
                description = "Buen día, \nYo, {0}, identificado con {1} No. {2} representante legal de la empresa {4} identificada con Nit No. {5} con todo respeto manifiesto a usted que presentó caducidad contra el comparendo No. {6} del  {7}. \nCordialmente.".format(NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, fullname, ldnumber, NoComparendoDelCaso, FechaDeComparendo)
            if document_type.startswith("Revocatoria"):
                description = "Buen día, \nYo, {0}, identificado con {1} No. {2} representante legal de la empresa {3} identificada con Nit No. {4} con todo respeto manifiesto a usted que presentó revocatoria directa contra la Resolución {5} del {6} \nCordialmente.".format(NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, fullname, ldnumber, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
            if document_type == "Prescripción":
                description = "Buenas tardes, \nYo, {0}, identificado con {1} No. {2} representante legal de la empresa {3} identificada con Nit No. {4} con todo respeto manifiesto a usted que presento prescripción contra de la Resolución {5} del {6}. \nCordialmente.".format(NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal, fullname, ldnumber, NoResoluciónSancionatoria, FechaDeResoluciónSancionatoria)
        
        return description
    except:
        raise


def robot_status(api_status):
    try:
        if "data" not in api_status:
            return ""
        data = api_status["data"]
        
        if "status" not in data[0]:
            return ""
        status = data[0]["status"]

        return status
    except:
        raise

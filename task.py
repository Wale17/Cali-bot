"""main bot"""
from handlers import process
from service import variable_coder
from utility import handler_process_utils
from time import sleep
from RPA.Robocorp.WorkItems import WorkItems

workitem = WorkItems()

workitem.get_input_work_item()
"""Varianles"""
url = "https://www.cali.gov.co/participacion/publicaciones/161718/radicacion-de-peticiones-quejas-y-reclamos/"
ldnumber = workitem.get_work_item_variable("idnumber")
FechaDeResoluciónSancionatoria = workitem.get_work_item_variable("FechaDeResolucionSancionatoria") 
NoResoluciónSancionatoria = workitem.get_work_item_variable("NoResolucionSancionatoria")
FechaDeComparendo = workitem.get_work_item_variable("FechaDeComparendo")
NombreRepresentateLegal = workitem.get_work_item_variable("NombreRepresentateLegal")
TipodeDocumentoRepresentateLegal = workitem.get_work_item_variable("TipodeDocumentoRepresentateLegal") 
DocumentoRepresentateLegal = workitem.get_work_item_variable("DocumentoRepresentateLegal")
document_id = workitem.get_work_item_variable("idnumber") 
fullname = workitem.get_work_item_variable("fullname") 
idtype= workitem.get_work_item_variable("idtype")
NoComparendoDelCaso= workitem.get_work_item_variable("NoComparendoDelCaso")
persona, tipo_de_documento = variable_coder.encode_idtpe(idtype) 
idld= workitem.get_work_item_variable("idld")
document_type = workitem.get_work_item_variable("document_type")
ldname = workitem.get_work_item_variable("ldname")


def robot_cali():
    for trial in range(3):
        try:
            process.open_webpage(url)
            process.step_one(fullname, ldnumber, persona)
            process.step_two(ldname)
            process.step_three(persona, idld, ldname, document_type, fullname, idtype, ldnumber, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal)
            api_status = process.update_records_on_zoho(idld)
            robot_status = variable_coder.robot_status(api_status)
            if robot_status == "success":    
                print("Done.")
                break
        except:
            handler_process_utils.handle_error("ROBOT FAILED")
    else:
        workitem.release_input_work_item(state= "FAILED", exception_type= "BUSINESS")
        raise



if __name__ == "__main__":
    robot_cali()
    
    

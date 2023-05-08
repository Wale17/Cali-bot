from RPA.Browser.Selenium import Selenium
from utility import handler_process_utils
from service import handler_process_service, supabase, captcha, variable_coder, zoho_service
from time import sleep
import os


browser = Selenium()

def open_webpage(url):
    if url == "":
        handler_process_utils.raise_error("Please check harcoded url")
    else:
        for trial in range(3):
            try:
                browser.open_available_browser(url)
                if browser.is_element_visible("//select[@id='solicitante']"):
                    break
            except Exception as e:
                handler_process_utils.handle_error(e)
        else:
            handler_process_utils.raise_error(e)
                


def step_one(fullname, idnumber, persona):
    if fullname != "" and idnumber != "":
        try:
            first_name, surname, other_name = handler_process_service.split_fullname(fullname)
            if persona == "Natural":
                browser.select_from_list_by_value("//select[@id='solicitante']", "1")
            if persona == "Juridica":
                browser.select_from_list_by_value("//select[@id='solicitante']", "2")
            browser.input_text("//input[@id='primer-nombre']", first_name)
            browser.input_text("//input[@id='primer-apellido']", surname)
            if not other_name == "":
                browser.input_text("//input[@id='segundo-nombre']", other_name)
            browser.select_from_list_by_value("//select[@id='tipo-identificacion']", "1")
            browser.input_text("//input[@id='numero-identificacion']", idnumber)
            browser.click_button("//button[@id='paso-1-btn-siguiente']")
        except Exception as e:
            handler_process_utils.handle_error(e)
    else:
        ### realease work item as exception since surname is neccessary to fill the form
        handler_process_utils.raise_error(e)

def step_two(ldname):
    if ldname != "":
        try:
            browser.input_text("//input[@id='direccion-residencia']", "CALLE 86 A BIS # 15.12")
            browser.input_text("//input[@id='correo-electronico']", "entidades+{0}@juzto.co".format(ldname))
            browser.input_text("//input[@id='telefono-fijo']", "5140369")
            browser.input_text("//input[@id='telefono-movil']", "3226149157")
            browser.click_button("//button[@id='paso-2-btn-siguiente']")
        except Exception as e:
            handler_process_utils.handle_error(e)
    else:
        ### realease work item as exception since surname is neccessary to fill the form
        handler_process_utils.raise_error(e)
    pass

def step_three(persona, idld, ldname, document_type, NombreTitular, TipodeDocumentoTitular, NoDocumentoTitular, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal):
    if idld != "" and ldname != "":
        try:
            browser.select_from_list_by_value("//select[@id='tipo-solicitud']", "Peticion-2")
            description = variable_coder.big_box_text(persona, document_type, NombreTitular, TipodeDocumentoTitular, NoDocumentoTitular, FechaDeResoluciónSancionatoria, NoComparendoDelCaso, NoResoluciónSancionatoria, FechaDeComparendo, NombreRepresentateLegal, TipodeDocumentoRepresentateLegal, DocumentoRepresentateLegal)
            browser.input_text("//textarea[@id='contenido-solicitud']", description)
            attachment_list = zoho_service.get_attachments(idld)
            attachment_id = zoho_service.get_attachment_id(attachment_list)
            filename = zoho_service.download_attachment(idld, attachment_id, ldname)
            current_dir = os.getcwd()
            filepath = os.path.join(current_dir, filename)
            browser.choose_file("//input[@id='archivo-adjunto']", filepath)
            browser.select_from_list_by_value("//select[@id='correoMsj']", "1")
            browser.click_element("//input[@id='checkbox']")
            captcha_solution = captcha.captcha_cracker()
            browser.execute_javascript('document.getElementById("g-recaptcha-response").innerHTML="{0}";'.format(captcha_solution))
            # sleep(3)
            browser.click_button("//button[@id='paso-3-btn-enviar']")
        except Exception as e:
            handler_process_utils.raise_error(e)

def update_records_on_zoho(idld, ld_name):
    if idld != "":
        browser.wait_until_element_is_visible("//*[@id='radicado']", timeout=200)
        try: 
            radicado_number = browser.get_text("//*[@id='radicado']")
            handler_process_utils.log_message(f"The Radicado for {idld} is {radicado_number}")
            browser.screenshot("//*[@id='respuesta']/div", "EVIDENCIA_" + radicado_number + ".png")
            zoho_service.update_records(idld, radicado_number)
            sleep(5)
            api_result = zoho_service.upload_an_attachment(idld, radicado_number)
            browser.close_browser()
            supabase.insert_filled_ld(idld, radicado_number, ld_name)
            return api_result
        except Exception as e:
            handler_process_utils.raise_error(e)

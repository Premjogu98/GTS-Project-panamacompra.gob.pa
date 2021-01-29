import re
from datetime import datetime
import time
import global_var
from insert_on_databsae import insert_in_Local,create_filename
import sys, os
import urllib.request
import urllib.parse
import string
import html
import requests


# def Translate_close(text_without_translate):
#     String2 = ""
#     try:
#         String2 = str(text_without_translate)
#         url = "https://translate.google.com/m?hl=en&sl=auto&tl=en&ie=UTF-8&prev=_m&q=" + str(String2) + ""
#         response1 = requests.get(str(url))
#         response2 = response1.url
#         user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
#         headers = {'User-Agent': user_agent , }
#         request = urllib.request.Request(response2 , None , headers)  # The assembled request
#         time.sleep(2)
#         response = urllib.request.urlopen(request)
#         htmldata: str = response.read().decode('utf-8')
#         trans_data = re.search(r'(?<=dir="ltr" class="t0">).*?(?=</div>)' , htmldata).group(0)
#         import html
#         trans_data = html.unescape(str(trans_data))
#         return trans_data
#     except:
#         return String2


def scraping_data(get_htmlSource , link, browser):
    a = 0
    while a == 0:
        try:
            # translator = Translator()
            SegFeild = []
            for data in range(45):
                SegFeild.append('')
            global_var.Total += 1
            new_get_htmlSource = get_htmlSource.replace("\n", "")
            new_get_htmlSource: str = new_get_htmlSource.replace(" ng-if=\"!isjson\"" , "")
            #  ===========================================================================================================================================================
            #  ===========================================================================================================================================================
            # E-mail address
            Email = new_get_htmlSource.partition('Correo Electrónico')[2].partition('</tr>')[0].strip()
            Email = Email.partition('<td>')[2].partition('</td>')[0].strip()
            SegFeild[1] = Email
            #  ===========================================================================================================================================================
            # Address
            # Country
            SegFeild[7] ="PA"

            Address = new_get_htmlSource.partition('>Dirección:')[2].partition('</tr>')[0].strip()
            Address = Address.partition('<td>')[2].partition('</td>')[0].strip()
            if Address != "":
                # Address = Translate(Address)
                Address = string.capwords(str(Address))

            Delivery_Province = new_get_htmlSource.partition('>Provincia de Entrega')[2].partition('</tr>')[0].strip()
            Delivery_Province = Delivery_Province.partition('<td>')[2].partition('</td>')[0].strip()
            if Delivery_Province != "":
                Delivery_Province = string.capwords(str(Delivery_Province))
                
           
            
            First_name = new_get_htmlSource.partition('>Nombre:')[2].partition('</tr>')[0].strip()
            First_name = First_name.partition('<td>')[2].partition('</td>')[0].strip()
            if First_name != "":
                # First_name = Translate(First_name)
                First_name = string.capwords(str(First_name))

            Position = new_get_htmlSource.partition('>Cargo:')[2].partition('</tr>')[0].strip()
            Position = Position.partition('<td>')[2].partition('</td>')[0].strip()
            Position = Position.replace(" ", "")
            if Position != "":
                # Position = Translate(Position)
                Position = string.capwords(str(Position))

            Phone = new_get_htmlSource.partition('>Teléfono:')[2].partition('</tr>')[0].strip()
            Phone = Phone.partition('<td>')[2].partition('</td>')[0].strip()

            Email = new_get_htmlSource.partition('>Correo Electrónico')[2].partition('</tr>')[0].strip()
            Email = Email.partition('<td>')[2].partition('</td>')[0].strip()

            Collected_Address = Address.strip() + "<br>\n""Provincia de entrega: " + Delivery_Province.strip() + "<br>\n""Persona de contacto: " + First_name.strip() + "<br>\n""Posición: " + Position.strip() + "<br>\n""Teléfono: " + Phone.strip() + "<br>\n""Correo electrónico: " + Email.strip()
            alladdress2 = str(Collected_Address)
            SegFeild[2] = alladdress2
            #  ===========================================================================================================================================================
        
            #  ===========================================================================================================================================================
            # Customer name
            Purchaser = new_get_htmlSource.partition('>Entidad:')[2].partition('</tr>')[0].strip()
            Purchaser = Purchaser.partition('<td>')[2].partition('</td>')[0].strip().upper()
            if Purchaser != "":
                # Purchaser = Translate(Purchaser)
                SegFeild[12] = Purchaser.strip()

            #  ===========================================================================================================================================================
            # tender_no
            tender_no = new_get_htmlSource.partition('>Número:')[2].partition('</tr>')[0].strip()
            tender_no = tender_no.partition('<td>')[2].partition('</td>')[0].strip()
            if tender_no != "":
                SegFeild[13] = tender_no.strip()

            SegFeild[14] = "2"
            #  ===========================================================================================================================================================

            # Purchase Details

            Name_of_the_Act = new_get_htmlSource.partition('>Nombre del Acto:')[2].partition('</tr>')[0].strip()
            Name_of_the_Act = Name_of_the_Act.partition('<td>')[2].partition('</td>')[0].strip()
            if Name_of_the_Act != "":
                # Name_of_the_Act = Translate(Name_of_the_Act)
                Name_of_the_Act = string.capwords(str(Name_of_the_Act))

            Type_of_Procedure = new_get_htmlSource.partition('>Tipo de Procedimiento:')[2].partition('</tr>')[0].strip()
            Type_of_Procedure = Type_of_Procedure.partition('<td>')[2].partition('</td>')[0].strip()
            if Type_of_Procedure != "":
                # Type_of_Procedure = Translate(Type_of_Procedure)
                Type_of_Procedure = string.capwords(str(Type_of_Procedure))

            Description = new_get_htmlSource.partition('>Descripción:')[2].partition('</tr>')[0].strip()
            Description = Description.partition('<td>')[2].partition('</td>')[0].strip()
            if Description != "":
                # Description = Translate(Description)
                Description = string.capwords(str(Description))

            Publication_date = new_get_htmlSource.partition('>Fecha de Publicación:')[2].partition('</tr>')[0].strip()
            Publication_date = Publication_date.partition('<td>')[2].partition('</td>')[0].strip()

            Date_and_Time_Presentation_of_Proposals = new_get_htmlSource.partition('>Fecha y Hora Presentación de Propuestas:')[2].partition('</tr>')[0].strip()
            Date_and_Time_Presentation_of_Proposals = Date_and_Time_Presentation_of_Proposals.partition('<td>')[2].partition('</td>')[0].strip()

            Proposal_Opening_Date_and_Time = new_get_htmlSource.partition('>Fecha y Hora de Apertura de Propuestas:')[2].partition('</tr>')[0].strip()
            Proposal_Opening_Date_and_Time = Proposal_Opening_Date_and_Time.partition('<td>')[2].partition('</td>')[0].strip()

            Place_of_presentation_of_proposals = new_get_htmlSource.partition('>Lugar de presentación de propuestas:')[2].partition('</tr>')[0].strip()
            Place_of_presentation_of_proposals = Place_of_presentation_of_proposals.partition('<td>')[2].partition('</td>')[0].strip()
            if Place_of_presentation_of_proposals != "":
                # Place_of_presentation_of_proposals = Translate(Place_of_presentation_of_proposals)
                Place_of_presentation_of_proposals = string.capwords(str(Place_of_presentation_of_proposals))

            Remedy_Date = new_get_htmlSource.partition('>Fecha de Subsanación:')[2].partition('</tr>')[0].strip()
            Remedy_Date = Remedy_Date.partition('<td>')[2].partition('</td>')[0].strip()

            Maximum_Date_and_Time_of_Receiving_expressions_of_Interest = new_get_htmlSource.partition('>Fecha y Hora Maxima de Recepción de expresiones de Interes:')[2].partition('</tr>')[0].strip()
            Maximum_Date_and_Time_of_Receiving_expressions_of_Interest = Maximum_Date_and_Time_of_Receiving_expressions_of_Interest.partition('<td>')[2].partition('</td>')[0].strip()

            Reception_Place = new_get_htmlSource.partition('>Lugar de Recepción:')[2].partition('</tr>')[0].strip()
            Reception_Place = Reception_Place.partition('<td>')[2].partition('</td>')[0].strip()
            if Reception_Place != "":
                # Reception_Place = Translate(Reception_Place)
                Reception_Place = string.capwords(str(Reception_Place))

            Reference_Price = new_get_htmlSource.partition('>Precio Referencia:')[2].partition('</tr>')[0].strip()
            Reference_Price = Reference_Price.partition('<td>')[2].partition('</td>')[0].replace(' ','')
            Reference_Price = Reference_Price.replace('B/.','').replace(',','').replace(' ','').strip()
            SegFeild[20] = Reference_Price.strip()

            if str(SegFeild[20]) != "":
                SegFeild[21] = 'PAB'

            Budget_Items = ''
            for Budget_Items in browser.find_elements_by_xpath("//*[@id=\"table_inter_np\"]/tbody"):
                Budget_Items1 = Budget_Items.get_attribute('innerText')
                Budget_Items = Budget_Items1.replace("\n", "")
                if Budget_Items != "":
                    # Budget_Items = Translate(Budget_Items)
                    Budget_Items = string.capwords(str(Budget_Items))

            Type_of_award = new_get_htmlSource.partition('>Modalidad de adjudicación:')[2].partition('</tr>')[0].strip()
            Type_of_award = Type_of_award.partition('<td>')[2].partition('</td>')[0].strip()
            if Type_of_award != "":
                # Type_of_award = Translate(Type_of_award)
                Type_of_award = string.capwords(str(Type_of_award))

            TenderDetails = "Nombre de la ley: " + Name_of_the_Act + "<br>\n""Tipo de procedimiento: " + Type_of_Procedure + "<br>\n""Descripción: " + Description + "<br>\n""Fecha de publicación: " + Publication_date \
                            + "<br>\n""Fecha y hora Presentación de propuestas: " + Date_and_Time_Presentation_of_Proposals + "<br>\n""Fecha y hora de apertura de la propuesta: " + Proposal_Opening_Date_and_Time \
                            + "<br>\n""Lugar de presentación de propuestas: " + Place_of_presentation_of_proposals + "<br>\n""Fecha de remedio: " + Remedy_Date \
                            + "<br>\n""Fecha y hora máximas de recepción de expresiones de interés: " + Maximum_Date_and_Time_of_Receiving_expressions_of_Interest + "<br>\n""Lugar de recepción: " + Reception_Place \
                            + "<br>\n""Precio de referencia: " + Reference_Price + "<br>\n""artidas presupuestarias: " + Budget_Items + "<br>\n""Type_of_award: " + Type_of_award

            SegFeild[18] = TenderDetails.strip()

            Title = re.search(r'(?<=>Nombre del Acto:).*?(?=</tr>)', new_get_htmlSource).group(0)
            Title = re.search(r'(?<=<td>).*?(?=</td>)', Title).group(0)
            if Title != "":
                # Title = Translate(Title)
                SegFeild[19] = string.capwords(str(Title))

            #  ===========================================================================================================================================================

            # Submission Date
            if get_htmlSource.find("Fecha y Hora Presentación de Propuestas:") != -1:
                try:
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=>Fecha y Hora Presentación de Propuestas:).*?(?=</tr>)',new_get_htmlSource).group(0)
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=<td>).*?(?=</td>)',Proposal_Opening_Date_and_Time).group(0)
                    Proposal_Opening_Date_and_Time = str(Proposal_Opening_Date_and_Time[0:10])
                    if Proposal_Opening_Date_and_Time != '':
                        datetime_object = datetime.strptime(Proposal_Opening_Date_and_Time, '%d-%m-%Y')
                        mydate = datetime_object.strftime("%Y-%m-%d")
                        SegFeild[24] = mydate.strip()

                except:
                    SegFeild[24] = ""
            elif get_htmlSource.find("Fecha y Hora Maxima de Recepción de expresiones de Interes:") != -1:
                try:
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=>Fecha y Hora Maxima de Recepción de expresiones de Interes:).*?(?=</tr>)',new_get_htmlSource).group(0)
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=<td>).*?(?=</td>)',Proposal_Opening_Date_and_Time).group(0)
                    Proposal_Opening_Date_and_Time = str(Proposal_Opening_Date_and_Time[0:10])
                    if Proposal_Opening_Date_and_Time != '':
                        datetime_object = datetime.strptime(Proposal_Opening_Date_and_Time, '%d-%m-%Y')
                        mydate = datetime_object.strftime("%Y-%m-%d")
                        SegFeild[24] = mydate.strip()

                except:
                    SegFeild[24] = ""
            elif get_htmlSource.find("Fecha y Hora de Celebración de la Subasta:") != -1:
                try:
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=>Fecha y Hora de Celebración de la Subasta:).*?(?=</tr>)',new_get_htmlSource).group(0)
                    Proposal_Opening_Date_and_Time = re.search(r'(?<=<td>).*?(?=</td>)',Proposal_Opening_Date_and_Time).group(0)
                    Proposal_Opening_Date_and_Time = str(Proposal_Opening_Date_and_Time[0:10])
                    if Proposal_Opening_Date_and_Time != '':
                        datetime_object = datetime.strptime(Proposal_Opening_Date_and_Time, '%d-%m-%Y')
                        mydate = datetime_object.strftime("%Y-%m-%d")
                        SegFeild[24] = mydate.strip()
                except:
                    SegFeild[24] = ""
            else:
                SegFeild[24] = ""
            # doc_cost
            # SegFeild[26] = "0.0"  # earnest_money
            SegFeild[27] = "0"  # Financier
            #  ===========================================================================================================================================================

            SegFeild[28] = link
            #  ===========================================================================================================================================================

            SegFeild[31] = 'panamacompra.gob.pa'
            #  ===========================================================================================================================================================
 
            SegFeild[43] = '' # set_aside
            SegFeild[42] = 'PA'  # project_location

            for SegIndex in range(len(SegFeild)):
                print(SegIndex, end=' ')
                print(SegFeild[SegIndex])
                SegFeild[SegIndex] = html.unescape(str(SegFeild[SegIndex]))
                SegFeild[SegIndex] = str(SegFeild[SegIndex]).replace("'", "''")
            a = 1
            if len(SegFeild[19]) >= 200:
                SegFeild[19] = str(SegFeild[19])[:200] + '...'

            if len(SegFeild[18]) >= 1500:
                SegFeild[18] = str(SegFeild[18])[:1500]+'...'

            check_date(get_htmlSource, SegFeild)

        except Exception as e :
            exc_type , exc_obj , exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e) , "\n" , exc_type , "\n" ,fname , "\n" , exc_tb.tb_lineno)
            a = 0


def check_date(get_htmlSource , SegField):
    deadline = str(SegField[24])
    curdate = datetime.now()
    curdate_str = curdate.strftime("%Y-%m-%d")
    try:
        if deadline != '':
            datetime_object_deadline = datetime.strptime(deadline, '%Y-%m-%d')
            datetime_object_curdate = datetime.strptime(curdate_str, '%Y-%m-%d')
            timedelta_obj = datetime_object_deadline - datetime_object_curdate
            day = timedelta_obj.days
            if day > 0:
                insert_in_Local(get_htmlSource, SegField)
                # print('Insert')
            else:
                print("Expired Tender")
                global_var.expired += 1
        else:
            print("Deadline Not Given")
            global_var.deadline_Not_given += 1
    except Exception as e:
        exc_type , exc_obj , exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error ON : " , sys._getframe().f_code.co_name + "--> " + str(e) , "\n" , exc_type , "\n" , fname , "\n" ,exc_tb.tb_lineno)

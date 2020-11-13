from selenium import webdriver
import time
import global_var
from Scraping_Things import scraping_data
import sys, os
import re
import ctypes
import sys


def choromedriver():
    # File_Location = open("D:\\0 PYTHON EXE SQL CONNECTION & DRIVER PATH\\panamacompra_gob_pa\\Location For Database & Driver.txt" , "r")
    # TXT_File_AllText = File_Location.read()
    # Chromedriver = str(TXT_File_AllText).partition("Driver=")[2].partition("\")")[0].strip()
    # browser = webdriver.Chrome(Chromedriver)
    browser = webdriver.Chrome(executable_path=str('CS:\\chromedriver.exe'))
    browser.maximize_window()

    # browser.get('http://www.panamacompra.gob.pa')
    # time.sleep(4)
    ctypes.windll.user32.MessageBoxW(0, "http://www.panamacompra.gob.pa   NAVIGATE THIS LINK ON CHROME", 'panamacompra.gob.pa', 0)
    time.sleep(4)
    clicking_process(browser)


def clicking_process(browser):
    error = True
    while error == True:
        try:
            for Advance_Search in browser.find_elements_by_xpath("//*[@id=\"navbar-collapse-1\"]/ul/li[5]/a"):
                Advance_Search.click()
                time.sleep(2)
                break
            for select_state in browser.find_elements_by_xpath("//*[@id=\"bam.fields.estado\"]/option[2]"):
                select_state.click()
                time.sleep(2)
                break
            # dateFormat Actual ON site: 17-07-2019
            for Date_from in browser.find_elements_by_xpath("//input[@id='bam.fields.fd']"):
                Date_from.click()
                Date_from.clear()

                From_date = global_var.Fromdate.partition("Date (FROM)")[2].partition("00:")[0].strip()
                # 2019-07-24 # Tender Actual Date Format
                Year = From_date[0:4]
                Month = From_date[5:7]
                Day = From_date[8:10]
                From_date = "" + Day + '-'"" + Month + '-'"" + Year
                Date_from.send_keys(str(From_date))
                time.sleep(1)
                break
            for Date_To in browser.find_elements_by_xpath("//input[@id='bam.fields.fh']"):
                Date_To.click()
                Date_To.clear()
                # Calender From Date 2019-09-17 00:00:00 End
                To_date = global_var.Todate.partition("Date (TO)")[2].partition("00:")[0].strip()
                # 2019-07-24 # Tender Actual Date Format
                Year = To_date[0:4]
                Month = To_date[5:7]
                Day = To_date[8:10]
                To_date = "" + Day + '-'"" + Month + '-'"" + Year
                Date_To.send_keys(str(To_date))
                time.sleep(2)
                break
            time.sleep(2)
            for Search in browser.find_elements_by_xpath("//*[@id=\"busquedaA2\"]/div[9]/div/center/button"):
                Search.click()
                time.sleep(2)
                break
            for dopdown in browser.find_elements_by_xpath('//*[@id="bam.pagina.numPerPage"]/option[3]'):
                dopdown.click()
                break
            NO_Record = ""
            for NO_Record in browser.find_elements_by_xpath("//*[@class=\"table-responsive img-rounded\"]/table/tbody"):
                NO_Record = NO_Record.get_attribute("innerText").strip()
                break
            if 'No hay registro' not in NO_Record:
                for Tenders_Limit in browser.find_elements_by_xpath("//*[@id=\"bam.pagina.numPerPage\"]/option[3]"):
                    Tenders_Limit.click()
                    time.sleep(3)
                    Collect_links(browser)
                    break
            else:
                time.sleep(3)
                print('There is no record found')
                ctypes.windll.user32.MessageBoxW(0, "There is no record found", 'panamacompra.gob.pa', 0)
                browser.close()
                sys.exit()
            error = False
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + ": " + str(e), "\n", exc_type, "\n", fname,"\n", exc_tb.tb_lineno)
            ctypes.windll.user32.MessageBoxW(0, "Error On Advance Search Please Check It", 'panamacompra.gob.pa', 0)
            error = True


def Collect_links(browser):
    link1 = []
    global a
    a = 0
    while a == 0:
        try:
            page_finish = False
            while page_finish == False:
                for tender_links in browser.find_elements_by_xpath('//*[@id="body"]/div/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/a'):
                    browser.execute_script("arguments[0].scrollIntoView();", tender_links)
                    link1.append(tender_links.get_attribute('href'))
                    print(tender_links.get_attribute('href'))
                time.sleep(2)
                for next_page in browser.find_elements_by_xpath('//*[@id="body"]/div/div[2]/div/div/div[2]/div[2]/center/ul/li/a'):
                    next_page_outerHTML = next_page.get_attribute('outerHTML').replace('\n','').strip()
                    next_page_text = next_page.get_attribute('innerText').strip()
                    if '›' in next_page_text:
                        if 'disabled="disabled"' not in next_page_outerHTML:
                            browser.execute_script("arguments[0].scrollIntoView();", next_page)
                            while True:
                                try:
                                    next_page.click()
                                    time.sleep(2)
                                    break
                                except:
                                    print('Error On Pagingation Please check it')
                                    ctypes.windll.user32.MessageBoxW(0, "Error On Pagingation Please check it", 'panamacompra.gob.pa', 0)
                                    time.sleep(3)
                            page_finish = False
                        else:
                            page_finish = True
            for href in link1:
                b = 0
                while b == 0:
                    try:
                        if href != '':
                            browser.refresh()
                            browser.get(href)
                            time.sleep(2)
                            try:
                                for data in browser.find_elements_by_xpath("//*[@id=\"elementToPDF\"]"):
                                    get_htmlSource = data.get_attribute('outerHTML')
                                    get_htmlSource1 = get_htmlSource.replace("<button ng-if=\"!vpcp.param.hiddenBB\" class=\"btn ""btn-default btn-sm\" ng-click=\"vpcp.backbutton("")\">« Volver</button>" , "")

                                    get_htmlSource1 = str(get_htmlSource1).replace('href="/' ,'href="http://www.panamacompra.gob.pa/')
                                    get_htmlSource1 = str(get_htmlSource1).replace('src="/' ,'src="http://www.panamacompra.gob.pa/')
                                    scraping_data(get_htmlSource1 , href , browser)
                                    print(" Total: " + str(len(link1)) + " Duplicate: " + str(global_var.duplicate) + " Expired: " + str(global_var.expired) + " Inserted: " + str(global_var.inserted) + " Deadline Not given: " + str(global_var.deadline_Not_given) + " QC Tenders: " + str(global_var.QC_Tenders),"\n")
                            except:
                                time.sleep(5)
                                for data in browser.find_elements_by_xpath("//*[@id=\"elementToPDF\"]"):
                                    get_htmlSource = data.get_attribute('outerHTML')
                                    get_htmlSource1 = get_htmlSource.replace("<button ng-if=\"!vpcp.param.hiddenBB\" class=\"btn ""btn-default btn-sm\" ng-click=\"vpcp.backbutton("")\">« Volver</button>" , "")
                                    get_htmlSource1 = str(get_htmlSource1).replace('href="/' ,'href="http://www.panamacompra.gob.pa/')
                                    get_htmlSource1 = str(get_htmlSource1).replace('src="/' ,'src="http://www.panamacompra.gob.pa/')
                                    scraping_data(get_htmlSource1 , href , browser)
                        else:
                            pass
                        b = 1
                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print("Error ON : ", sys._getframe().f_code.co_name + ": " + str(e), "\n", exc_type, "\n", fname,"\n", exc_tb.tb_lineno)
                        b = 0
            a = 1
        except Exception as e:
            exc_type , exc_obj , exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : " , sys._getframe().f_code.co_name + ": " + str(e), "\n", exc_type, "\n", fname, "\n", exc_tb.tb_lineno)
            a = 0
    ctypes.windll.user32.MessageBoxW(0, "Total: " + str(global_var.Total) + "\n""Duplicate: " + str(global_var.duplicate) + "\n""Expired: " + str(global_var.expired) + "\n""Inserted: " + str(global_var.inserted) + "\n""Deadline Not given: " + str(global_var.deadline_Not_given) + "\n""QC Tenders: " + str(global_var.QC_Tenders) + "","panamacompra.gob.pa", 1)
    global_var.Process_End()
    browser.close()
    sys.exit()


choromedriver()





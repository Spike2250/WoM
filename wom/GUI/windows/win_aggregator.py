from wom.GUI.windows.omr import (omr_main_menu,
                                 omr_add_new_patient,
                                 # omr_patient_card,
                                 omr_passport_data,
                                 omr_
                                 )
from wom.GUI.windows.bta import (bta_main_menu,
                                 bta_add_new_patient,
                                 bta_patient_card,
                                 bta_passport_data,
                                 bta_obj_status,
                                 bta_neur_status,
                                 bta_diagnosis,
                                 bta_protocol,
                                 # bta_recommends,
                                 bta_discharge_details)
from wom.GUI.windows.FramelessWindow import FramelessWindow
from wom.GUI.windows.test import MainWindow

windows = {
    'Frameless': FramelessWindow,
    'test': MainWindow,
    'omr': {
        'main_menu': omr_main_menu.Ui_MainMenu,
        'add_new_patient': omr_add_new_patient.Ui_AddNewPatient,
        # 'patient_card': omr_patient_card.Ui_PatientCard,
        'passport': 
    },
    'bta': {
        'main_menu': bta_main_menu.Ui_MainMenu,
        'add_new_patient': bta_add_new_patient.Ui_AddNewPatient,
        'patient_card': bta_patient_card.Ui_PatientCard,
        'passport': bta_passport_data.Ui_PatientPassportData,
        'obj_status': bta_obj_status.Ui_Status_objectivus,
        'neur_status': bta_neur_status.Ui_Status_neurology,
        'diagnosis': bta_diagnosis.Ui_Diagnosis,
        'protocol': bta_protocol.Ui_Protocol_BTA,
        # 'recommends': bta_recommends.Ui_Recommends,
        'dis_details': bta_discharge_details.Ui_Discharge_details
    },
    'common': {
        'main_menu': ''
    }
}

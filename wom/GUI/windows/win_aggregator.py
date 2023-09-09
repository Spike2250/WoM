from wom.GUI.windows\
    .FramelessWindow import FramelessWindow
from wom.GUI.windows\
    .omr import (omr_main_menu,
                 omr_add_new_patient,
                 omr_patient_card,
                 omr_appointments_list,
                 omr_mdrk,
                 omr_dynamic)
from wom.GUI.windows\
    .bta import (bta_main_menu,
                 bta_add_new_patient,
                 bta_patient_card,
                 bta_passport_data,
                 bta_obj_status,
                 bta_neur_status,
                 bta_diagnosis,
                 bta_protocol,
                 # bta_recommends,
                 bta_discharge_details)
from wom.GUI.windows\
    .common import (login,
                    registration,
                    main_user_menu,
                    load_arch,
                    passport_data,
                    add_relative,
                    obj_status_adm,
                    obj_status_dis,
                    neur_status,
                    diagnosis,
                    dis_details,
                    icf,
                    lab_data,
                    )
from wom.GUI.windows.test import MainWindow


windows = {
    'Frameless': FramelessWindow,
    'test': MainWindow,
    'omr': {
        'main_menu': omr_main_menu.Ui_MainMenu,
        'add_new_patient': omr_add_new_patient.Ui_AddNewPatient,
        'patient_card': omr_patient_card.Ui_PatientCard,
        'appointments': omr_appointments_list.Ui_Appointments,
        'mdrk': omr_mdrk.Ui_Mdrk,
        'dynamic': omr_dynamic.Ui_Dynamic,
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
        'login': login.Ui_Login,
        'registration': registration.Ui_Registration,
        'main_user_menu': main_user_menu.Ui_User_main_menu,
        'load_arch': load_arch.Ui_load_arch_data,
        'passport': passport_data.Ui_PatientPassportData,
        'add_relative': add_relative.Ui_AddRelative,
        'obj_status_adm': obj_status_adm.Ui_StPrObjectivus_admission,
        'obj_status_dis': obj_status_dis.Ui_StPrObjectivus_discharge,
        'neur_status': neur_status.Ui_StNeurology,
        'diagnosis': diagnosis.Ui_Diagnosis,
        'dis_details': dis_details.Ui_Discharge_details,
        'icf': icf.Ui_icf,
        'lab_data': lab_data.Ui_Laboratory_data,
    }
}

from wom.GUI.windows import (bta_main_menu,
                             bta_add_new_patient,
                             bta_patient_card,
                             bta_passport_data,
                             bta_obj_status,
                             bta_neur_status,
                             bta_diagnosis,
                             bta_protocol,
                             bta_discharge_details
                             )


windows = {
    'bta': {
        'main_menu': bta_main_menu.Ui_MainMenu,
        'add_new_patient': bta_add_new_patient.Ui_AddNewPatient,
        'patient_card': bta_patient_card.Ui_PatientCard,
        'passport': bta_passport_data.Ui_PatientPassportData,
        'obj_status': bta_obj_status.Ui_Status_objectivus,
        'neur_status': bta_neur_status.Ui_Status_neurology,
        'diagnosis': bta_diagnosis.Ui_Diagnosis,
        'protocol': bta_protocol.Ui_Protocol_BTA,
        'dis_details': bta_discharge_details.Ui_Discharge_details
    }
}

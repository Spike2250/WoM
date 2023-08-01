from wom.GUI.windows import (bta_main_menu,
                             bta_add_new_patient,
                             bta_patient_card,
                             bta_passport_data
                             )


windows = {
    'bta': {
        'main_menu': bta_main_menu.Ui_MainMenu,
        'add_new_patient': bta_add_new_patient.Ui_AddNewPatient,
        'patient_card': bta_patient_card.Ui_PatientCard,
        'passport': bta_passport_data.Ui_PatientPassportData,
    }
}

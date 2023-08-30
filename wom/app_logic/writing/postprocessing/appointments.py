from prettytable import PrettyTable


def update_after_appointments(d):
    update_after_drugs_appointments(d)
    update_after_lfk_appointments(d)
    update_after_physio_appointments(d)


def update_after_drugs_appointments(d):
    '''
    '''

    end_string_1 = ''
    for i in range(12):
        end_string_1 += '-'
    end_string_2 = '----------------------------------#'\
                   '-----------------------------------'
    end_list = [end_string_1,
                end_string_1,
                end_string_2]

    # Для инъекционного лн
    sol_table = PrettyTable()
    fields = ["Дата назнач.",
              "Дата отмены",
              "Название препарата, доза, режим дозирования, способ введения"]
    sol_table.field_names = fields

    sol_summary = ''
    sol_row_check = 0

    if len(d['d_sol']) > 0:
        for sol in d['d_sol']:
            sol_i = f"{sol['drug']} {sol['dose']} {sol['DS']}; "
            sol_short = f"{sol['drug']} {sol['dose']}"
            sol_summary += sol_i
            sol_i = sol_i[:-2]
            if len(sol_i) <= 70:
                sol_table.add_rows([[sol['date'], '', sol_i],
                                    end_list, ])
                sol_row_check += 2
            else:
                sol_table.add_rows([[sol['date'], '', sol_short],
                                    ['', '', f"{sol['DS']}"],
                                    end_list, ])
                sol_row_check += 3

    d['лечение_инъекции'] = sol_summary
    while sol_row_check < 15:  # Максимальное количество строк Sol
        sol_row_check += 1
        sol_table.add_row(['', '', ''])
    d['назначение_инъекции'] = f"Парентеральные лекарственные формы:\n"\
                               f"{str(sol_table)}"

    # для энтерального лн
    peros_table = PrettyTable()
    peros_table.field_names = fields
    peros_summary = ''
    peros_row_check = 0

    if len(d['d_tab']) > 0:
        for tab in d['d_tab']:
            tab_i = f"{tab['drug']} {tab['dose']} {tab['DS']}; "
            tab_short = f"{tab['drug']} {tab['dose']}"
            peros_summary += tab_i
            tab_i = tab_i[:-2]
            if len(tab_i) <= 70:
                peros_table.add_rows([[tab['date'], '', tab_i],
                                      end_list, ])
                peros_row_check += 2
            else:
                peros_table.add_rows([[tab['date'], '', tab_short],
                                      ['', '', f"{tab['DS']}"],
                                      end_list, ])
                peros_row_check += 3

    d['лечение_таблетки'] = peros_summary
    while peros_row_check < 43:  # Максимальное количество строк peros
        peros_row_check += 1
        peros_table.add_row(['', '', ''])
    d['назначение_таблетки'] = f"Таблетированные и другие энтеральные "\
                               f"лекарственные формы:\n{str(peros_table)}"
    d['назначение_все'] = f"{d['назначение_инъекции']}\n\n"\
                          f"{d['назначение_таблетки']}"


def update_after_lfk_appointments(d):
    lfk_summary = ''
    for app in d['d_lfk']:
        lfk = f"{app['procedure']} " \
              f"{app['regimen']}; "
        lfk_summary += lfk
    d['лфк'] = lfk_summary


def update_after_physio_appointments(d):
    physio_summary = ''
    for app in d['d_physio']:
        physio = f"{app['procedure']} " \
                 f"{app['place']} " \
                 f"{app['regimen']}; "
        physio_summary += physio
    d['физиотерапия'] = physio_summary

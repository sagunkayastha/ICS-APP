import Tkinter as tk
import ttk
import tkMessageBox
import sys

from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
LARGE_FONT = ("arial", 12, 'bold')
Head_FONT = ("arial", 10, 'bold')
NORMAL_FONT = ("arial", 10)
Ex_FONT=("arial", 15, 'bold')
rd_FONT=("arial", 10, 'bold')
from PIL import ImageFont,Image, ImageDraw
failed = []
failed2 = []
failed3 = []
failed3_2=[]
sailed=[]
add_val=[]
xx=0
zz=0
tt=0
tech_var=[]
score_list= {'Lower_Emission': 0, 'LOW_FUEL_CONSUMPTION': 0, 'FAST_COOKING': 0, 'BUDGET_FRIENDLY': 0, 'MULTIPURPOSE': 0,'DURABILITY':0,
                          'SIMULATNEOUS_COOKING/MULTI-POT_HOLES':0,'EASY_TO_USE':0,'ASTHETIC_APPEAL': 0,'SAFETY':0, 'REGULAR_CLEANING':0,'PORTABILITY': 0}
Final_User_Score=0
Final_Technical_Score=0
page=0
for_write1=[]
for_p = {'Lower_Emission': [0, 0, 0, 0, 0, 0, 0], 'LOW_FUEL_CONSUMPTION': [0, 0,], 'FAST_COOKING': [0, 0, 0],
                      'BUDGET_FRIENDLY': [0, 0,], 'MULTIPURPOSE': [0, 0, 0, 0, 0, 0, 0, 0,], 'DURABILITY': [0, 0, 0, 0, 0, 0, 0, 0,0, 0,0],
                      'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': [0, 0, 0], 'EASY_TO_USE': [0, 0, 0, 0, 0, 0, 0], 'ASTHETIC_APPEAL': [0, 0,],
                      'SAFETY': [0, 0, 0, 0,], 'REGULAR_CLEANING': [0, 0, 0], 'PORTABILITY': [0, 0,0]}
all_total={'Lower_Emission': 100, 'LOW_FUEL_CONSUMPTION': 100, 'FAST_COOKING': 100, 'BUDGET_FRIENDLY': 100, 'MULTIPURPOSE': 100,'DURABILITY':200,
                          'SIMULATNEOUS_COOKING/MULTI-POT_HOLES':150,'EASY_TO_USE':125,'ASTHETIC_APPEAL': 100,'SAFETY':100, 'REGULAR_CLEANING':125,'PORTABILITY': 150}
Percentile = {
            'High_Hill': {'Lower_Emission': 17.08, 'LOW_FUEL_CONSUMPTION': 10.13, 'FAST_COOKING': 13.98, 'BUDGET_FRIENDLY': 7.93, 'MULTIPURPOSE': 10.66, 'DURABILITY': 17.95,
                          'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 12.39, 'EASY_TO_USE': 9.59, 'ASTHETIC_APPEAL': 0.01, 'SAFETY': 0.27, 'REGULAR_CLEANING': 0, 'PORTABILITY': 0},

            'Mid_Hill': {'Lower_Emission': 25.37, 'LOW_FUEL_CONSUMPTION': 14.31, 'FAST_COOKING': 17.14, 'BUDGET_FRIENDLY': 3.84, 'MULTIPURPOSE': 11.87, 'DURABILITY': 13.95,
                         'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 4.05, 'EASY_TO_USE': 8.13, 'ASTHETIC_APPEAL': 0.28, 'SAFETY': 0.44, 'REGULAR_CLEANING': 0.63, 'PORTABILITY': 0},

            'Central_Terai': {'Lower_Emission': 18.06, 'LOW_FUEL_CONSUMPTION': 12.86, 'FAST_COOKING': 16.78, 'BUDGET_FRIENDLY': 8.06, 'MULTIPURPOSE': 7.38, 'DURABILITY': 4.14,
                              'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 17.77, 'EASY_TO_USE': 11.24, 'ASTHETIC_APPEAL': 3.7, 'SAFETY': 0, 'REGULAR_CLEANING': 0, 'PORTABILITY': 0},

            'Western_Terai': {'Lower_Emission': 12.71, 'LOW_FUEL_CONSUMPTION': 11.39, 'FAST_COOKING': 17.36, 'BUDGET_FRIENDLY': 4.57, 'MULTIPURPOSE': 7.21, 'DURABILITY': 22.82,
                              'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 8.06, 'EASY_TO_USE': 14.13, 'ASTHETIC_APPEAL': 0, 'SAFETY': 0, 'REGULAR_CLEANING': 0, 'PORTABILITY': 1.75}
        }
numb=0
def read_files():
    wb=open_workbook('excel_files/Standard_Values.xls')
    cl = []
    fd = []

    ch = [20, 0.039, [41, 979], [1, 8], [8, 16], [0.09, 0.2], 5, 0.42]
    for sheet in wb.sheets():

        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        for row in range(1, number_of_rows):
            value = (sheet.cell(row, 2).value)

            if sheet.name == 'Chimneyless Stove':
                cl.append(value)
            if sheet.name == 'Force Draft Stove':
                fd.append(value)
    return cl,fd

def read_files_ch():
    wb = open_workbook('excel_files/Standard_Values.xls')
    cl = []
    fd = []
    ch1 = []
    ch2 = []
    ch = [20, 0.039, [41, 979], [1, 8], [8, 16], [0.09, 0.2], 5, 0.42]
    sheet = wb.sheet_by_name('Chimney Stove')
    number_of_rows = sheet.nrows
    for row in range(1, number_of_rows):
        ch1.append(sheet.cell(row, 2).value)
        ch2.append(sheet.cell(row, 3).value)

    ch = [ch1[0], ch1[1], [ch1[3], ch2[3]], [ch1[4], ch2[4]], [ch1[5], ch2[5]], [ch1[6], ch2[6]], ch1[8], ch1[9]]
    return ch

def read_files_du(x):
    ch1 = []
    ch2 = []
    wb = open_workbook('excel_files/Standard_Values.xls')
    # du = {'ComCham': [0, 0], 'Grate_Rod': [0, 0,0], 'Grate_plate': [0, 0, 0], 'Top_Plate': [0,0, 0], 'Du': [0, 0]}
    # dur_cl = {'ComCham': [1, 2], 'Grate_Rod': [4, 4, 6], 'Grate_plate': [4, 1, 2], 'Top_Plate': [6, 2, 4], 'Du': [1, 1]}
    sheet = wb.sheet_by_name('Durability')
    number_of_rows = sheet.nrows
    for row in range(1, number_of_rows):
        ch1.append(sheet.cell(row, 2).value)
        ch2.append(sheet.cell(row, 3).value)

    du_1 = {'ComCham': [ch1[1], ch1[2]], 'Grate_Rod': [ch1[6], ch1[7], ch1[8]],
            'Grate_plate': [ch1[10], ch1[11], ch1[12]],
            'Top_Plate': [ch1[14], ch1[15], ch1[16]], 'Du': [1, 1]}
    du_2 = {'ComCham': [ch1[1], ch1[2]], 'Grate_Rod': [ch1[6], ch1[7], ch1[8]],
            'Grate_plate': [ch1[10], ch1[11], ch1[12]],
            'Top_Plate': [ch1[14], ch1[15], ch1[16]], 'Du': [1, 1]}
    print du_1, du_2
    if x == 1:
        return du_1
    if x == 2:
        return du_2
    print du_1, du_2
def write_files(save_filename):
    global for_p, add_val, xx, page,tech_var
    if page==1:
        rb = open_workbook('excel_files/Export_Sample_Chimneyless.xls', formatting_info=True)
    if page==2:
        rb = open_workbook('excel_files/Export_Sample_Force_Draf.xls', formatting_info=True)
    if page==3:
        rb = open_workbook('excel_files/Export_Sample_Chimney.xls', formatting_info=True)

    #Technical

    #user

    r_sheet = rb.sheet_by_index(1)

    number_of_rows = r_sheet.nrows

    i = 0
    c=0
    keyss = []
    keys_counter = 0
    for keys in for_p:
        keyss.append(keys)


    wb = copy(rb)



    t1 = tech_var[0]
    t2=tech_var[1]
    t3=tech_var[2]
    t4=tech_var[3]


    w_sheet = wb.get_sheet(0)
    w_sheet.write(2, 1, t1[0])
    w_sheet.write(3, 1, t1[1])

    if page==1 or page==2:
        w_sheet.write(6, 1, t1[2])
        w_sheet.write(7, 1, t1[3])
        w_sheet.write(8, 1, t1[4])
        w_sheet.write(9, 1, t1[5])

    if page==3:
        w_sheet.write(6, 1, t1[2][0])
        w_sheet.write(6, 2, t1[2][1])
        w_sheet.write(7, 1, t1[3][0])
        w_sheet.write(7, 2, t1[3][1])
        w_sheet.write(8, 1, t1[4][0])
        w_sheet.write(8, 2, t1[4][1])
        w_sheet.write(9, 1, t1[5][0])
        w_sheet.write(9, 2, t1[5][1])



    w_sheet.write(12, 1, t1[6])
    w_sheet.write(13, 1, t1[7])

    if t1[8]==0:
        w_sheet.write(15, 1, 'Metallic Body Cooking and Heating Stove')
        w_sheet.write(16, 1, t1[9])
    if t1[8] == 1:
        w_sheet.write(15, 1, 'Metallic Body Cooking Stove')
        w_sheet.write(16, 1, t1[9])
    if t1[8] == 2:
        w_sheet.write(15, 1, 'Mud/ Composite body Cooking Stove'   )
        w_sheet.write(16, 1, t1[9])

    if t2[0] == 0:
        w_sheet.write(2, 5, t3[0])
    if t2[0] == 1:
        w_sheet.write(3, 5, t3[0])
    if t2[0] == 2:
        w_sheet.write(4, 5, t4[0])

    if t2[1] == 0:
        w_sheet.write(8, 5, t3[1])
    if t2[1] == 1:
        w_sheet.write(9, 5, t3[1])
    if t2[1] == 2:
        w_sheet.write(10, 5, t3[1])

    if t2[2] == 0:
        w_sheet.write(13, 5, t3[2])
    if t2[2] == 1:
        w_sheet.write(14, 5, t3[2])
    if t2[2] == 2:
        w_sheet.write(15, 5, t3[2])

    if t2[3] == 0:
        w_sheet.write(18, 5, t3[3])
    if t2[3] == 1:
        w_sheet.write(18, 5, t3[3])
    if t2[3] == 2:
        w_sheet.write(18, 5, t3[3])
    if t2[3] == 3:
        w_sheet.write(18, 5, t4[1])






    w_sheet = wb.get_sheet(1)
    for i in range(0, len(keyss)):

        while i < number_of_rows:
            value = (r_sheet.cell(i, 0).value).encode('utf-8')

            if value == keyss[keys_counter]:
                # print 'x',value,keyss[keys_counter]
                x = for_p[keyss[keys_counter]]

                for j in range(i, (i + len(x))):
                    t=x[c]

                    w_sheet.write(j + 1, 1, t)
                    c+=1
                    i = i + len(x)
                c=0



            else:
                i += 1

        keys_counter += 1
    c=0
    for row in range(0, 15):
        value = (r_sheet.cell(row, 0).value).encode('utf-8')
        if value == 'Lower_Emission':

            x = for_p['Lower_Emission']

            for j in range(row, (row + len(x))):
                t=x[c]
                w_sheet.write(j + 1, 1, t)

    w_sheet.write(17,1,(30*50/xx))





    wb.save(save_filename+'.xls')


def ccc():
    global all_total,Percentile
    a = {'High_Hill': [], 'Mid_Hill': [], 'Central_Terai': [], 'Western_Terai': []}
    b = ['High_Hill', 'Mid_Hill', 'Central_Terai', 'Western_Terai']
    for i in b:
        x = 0
        for keys in all_total:
            x = x + all_total[keys] * Percentile[i][keys]
        a[i] = (x)
    return a
def Calculation(s, ipx, ipy):


    f = []
    failed_number = []
    read_files()

    cl_standar,fd_standar = read_files()
    saf = [45, 75, 88]

    global page,for_write1,tech_var,failed3_2

    if s == 2:
        page = 1
        cl = cl_standar

    if s == 3:
        page = 2
        cl = fd_standar

    dur_cl = read_files_du(1)
    ip = []

    i_var = [ipy['ComCham'][0].get(), ipy['Grate_Rod'][0].get(), ipy['Grate_plate'][0].get(), ipy['Top_Plate'][0].get()]

    for i in range(0, len(ipx)):
        ip.append(ipx[i].get())
    for_write1.append(ip)
    zpy=[ipy['ComCham'][1].get(),ipy['Grate_Rod'][1].get(),ipy['Grate_plate'][1].get(),ipy['Top_Plate'][1].get()]
    tech_var = [ip, i_var, zpy, [ipy['Du'][0].get(), ipy['Du'][1].get()]]
    if ip[0] < cl[0] or ip[1] > cl[1] or ip[2] > cl[2] or ip[3] > cl[3] or ip[4] > cl[4] or ip[5] > cl[5] or ip[6] > cl[
        6] or ip[7] > cl[7] or ip[9] < saf[ip[8]]:
        f.append('Fail Parameter')

        failed_ones_par(ip, cl, saf)
        score = SCORING_class(ip, ipy)
        score.p()

    else:
        f.append('pass')
        score = SCORING_class(ip, ipy)
        score.p()

    if i_var[0] == 2 and i_var[3] == 3:

        if ipy['ComCham'][1].get() > dur_cl['Du'][0] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][1].get() > \
                dur_cl['Du'][1]:
            f.append('++ ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(), ipy['Top_Plate'][1].get()],
                           [dur_cl['Du'][0], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]], dur_cl['Du'][1]])

        else:
            f.append('pass')
            failed3_2=[]
    if i_var[0] == 2 and i_var[3] != 3:

        if ipy['ComCham'][1].get() > dur_cl['Du'][0] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][1].get() < \
                dur_cl['Top_Plate'][i_var[3]]:
            f.append('+- ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['Du'][0], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Top_Plate'][i_var[3]]])
        else:
            f.append('pass')
            failed3_2 = []
    if i_var[0] != 2 and i_var[3] != 3:

        if ipy['ComCham'][1].get() < dur_cl['ComCham'][i_var[0]] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][
            1].get() < dur_cl['Top_Plate'][i_var[3]]:
            f.append('-- ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['ComCham'][i_var[0]], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Top_Plate'][i_var[3]]])
        else:
            f.append('pass')
            failed3_2 = []
    if i_var[0] != 2 and i_var[3] == 3:

        if ipy['ComCham'][1].get() < dur_cl['ComCham'][i_var[0]] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][
            1].get() > dur_cl['Du'][1]:
            f.append('-+ ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['ComCham'][i_var[0]], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Du'][1]])
        else:
            f.append('pass')
            failed3_2 = []

    return f


def Calculation2(s, ipx, ipy):
    f = []
    global page,tech_var,failed3_2
    page=3
    cl = read_files_ch()

    ip = [ipx[0].get(), ipx[1].get(), [ipx[2][0].get(), ipx[2][1].get()], [ipx[3][0].get(), ipx[3][1].get()], [ipx[4][0].get(), ipx[4][1].get()], [ipx[5][0].get(), ipx[5][1].get()], ipx[6].get(), ipx[7].get(),
          ipx[8].get(), ipx[9].get()]

    saf = [45, 75, 88]
    dur_cl=read_files_du(2)
    dur_cl = {'ComCham': [1, 2], 'Grate_Rod': [4, 4, 6], 'Grate_plate': [4, 1, 2], 'Top_Plate': [6, 2, 4], 'Du': [1, 1]}

    i_var = [ipy['ComCham'][0].get(), ipy['Grate_Rod'][0].get(), ipy['Grate_plate'][0].get(), ipy['Top_Plate'][0].get()]

    #to_send_ip = [ipx[0].get(), ipx[1].get(), ipx[2][1].get(), ipx[3][1].get(), ipx[4][1].get(), ipx[5][1].get(), ipx[6].get(), ipx[7].get(), ipx[8].get(), ipx[9].get()]
    zpy = [ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(), ipy['Top_Plate'][1].get()]
    tech_var = [ip, i_var, zpy, [ipy['Du'][0].get(), ipy['Du'][1].get()]]

    if ip[0] < cl[0] or ip[1] > cl[1] or ip[2][0] > cl[2][0] or ip[2][1] > cl[2][1] or ip[3][0] > cl[3][0] or ip[3][1] > cl[3][1] or ip[4][0] > cl[4][0] or ip[4][1] > cl[4][1] or ip[5] > cl[5] or ip[6] > cl[6] or ip[7] > cl[7] or ip[9] < saf[ip[8]]:
        f.append('fail Parameter')
        score = SCORING_class2(ip, ipy)
        final_score = score.p()

        failed_two_par(ip, cl, saf)


    else:
        f.append('pass')
        score = SCORING_class2(ip, ipy)
        failed3_2 = []
        final_score = score.p()

    if i_var[0] == 2 and i_var[3] == 3:

        if ipy['ComCham'][1].get() > dur_cl['Du'][0] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][1].get() > \
                dur_cl['Du'][1]:
            f.append('++ ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(), ipy['Top_Plate'][1].get()],
                           [dur_cl['Du'][0], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]], dur_cl['Du'][1]])

        else:
            f.append('pass')
            failed3_2 = []
    if i_var[0] == 2 and i_var[3] != 3:

        if ipy['ComCham'][1].get() > dur_cl['Du'][0] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][1].get() < \
                dur_cl['Top_Plate'][i_var[3]]:
            f.append('+- ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['Du'][0], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Top_Plate'][i_var[3]]])
        else:
            f.append('pass')
            failed3_2 = []
    if i_var[0] != 2 and i_var[3] != 3:

        if ipy['ComCham'][1].get() < dur_cl['ComCham'][i_var[0]] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][
            1].get() < dur_cl['Top_Plate'][i_var[3]]:
            f.append('-- ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['ComCham'][i_var[0]], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Top_Plate'][i_var[3]]])
        else:
            f.append('pass')
            failed3_2 = []
    if i_var[0] != 2 and i_var[3] == 3:

        if ipy['ComCham'][1].get() < dur_cl['ComCham'][i_var[0]] or ipy['Grate_Rod'][1].get() < dur_cl['Grate_Rod'][i_var[1]] or ipy['Grate_plate'][1].get() < dur_cl['Grate_plate'][i_var[2]] or ipy['Top_Plate'][
            1].get() > dur_cl['Du'][1]:
            f.append('-+ ovl fail')
            failed_ones_du([ipy['ComCham'][1].get(), ipy['Grate_Rod'][1].get(), ipy['Grate_plate'][1].get(),
                            ipy['Top_Plate'][1].get()],
                           [dur_cl['ComCham'][i_var[0]], dur_cl['Grate_Rod'][i_var[1]], dur_cl['Grate_plate'][i_var[2]],
                            dur_cl['Du'][1]])
        else:
            f.append('pass')
            failed3_2 = []

    return f

def failed_ones_par(ip, cl, saf):
    global failed,sailed
    failed=[]
    if ip[0] < cl[0]:

        failed.append('High Power Thermal Efficiency is less than ' + str(cl[0]))
    if ip[1] > cl[1]:
        failed.append('Specific Fuel Consuption is Higher than ' + str(cl[1]))
    if ip[2] > cl[2]:
        failed.append('High Power PM 2.5 is Higher Than ' + str(cl[2]))
    if ip[3] > cl[3]:
        failed.append('Low Power PM 2.5 is Higher Than ' + str(cl[3]))
    if ip[4] > cl[4]:
        failed.append('High Power CO is Higher Than ' + str(cl[4]))
    if ip[5] > cl[5]:
        failed.append('Low Power CO is Higher Than ' + str(cl[5]))
    if ip[6] > cl[6]:
        failed.append('Indoor Emission PM 2.5 is Higher Than ' + str(cl[6]))
    if ip[7] > cl[7]:
        failed.append('Indoor Emission CO is Higher Than ' + str(cl[7]))
    if ip[9] < saf[ip[8]]:
        failed.append('Safety is less Than ' + str(saf[ip[8]]))
    failed=list(set(failed))


def failed_two_par(ip, cl, saf):
    global failed2, failed
    failed2=[]

    if ip[0] < cl[0]:
        failed2.append('High Power Thermal Efficiency is less than ' + str(cl[0]))
    if ip[1] > cl[1]:
        failed2.append('Specific Fuel Consuption is Higher than ' + str(cl[1]))
    if ip[2][0] > cl[2][0] or ip[2][1] > cl[2][1]:
        failed2.append('High Power PM 2.5 is Higher Than ' + str(cl[2]))

    if ip[3][0] > cl[3][0] or ip[3][1] > cl[3][1]:
        failed2.append('Low Power PM 2.5 is Higher Than ' + str(cl[3]))
    if ip[4][0] > cl[4][0] or ip[4][1] > cl[4][1]:
        failed2.append('High Power CO is Higher Than ' + str(cl[4]))
    if ip[5] > cl[5]:
        failed2.append('Low Power CO is Higher Than ' + str(cl[5]))
    if ip[6] > cl[6]:
        failed2.append('Indoor Emission PM 2.5 is Higher Than ' + str(cl[6]))
    if ip[7] > cl[7]:
        failed2.append('Indoor Emission CO is Higher Than ' + str(cl[7]))
    if ip[9] < saf[ip[8]]:
        failed2.append('Safety is less Than ' + str(saf[ip[8]]))
    failed2= list(set(failed2))


def failed_ones_du(x, y):
    global failed3,failed3_2
    failed3_2=[]
    failed_3=[]
    for i in range(0, len(x)):
        if x[i] < y[i]:
            failed3.append(i)
    failed_3=list(set(failed3))


    for i in failed_3:
        if i==0:
            failed3_2.append('Combustion Chamber Thickness is less than '+str(y[i])+'mm')

        if i==1:
            failed3_2.append('Grate Rod Structure Thickness is less than '+str(y[i])+'mm')
        if i==2:
            failed3_2.append('Plate Structure Thickness is less than '+str(y[i])+'mm')
        if i==3:
            failed3_2.append('Top Plate with Pot riser Thickness is less than '+str(y[i])+'mm')
    print failed3_2


def return_failed():
    global failed

def set_zone(x):
    global zone
    zone=x



class SCORING_class:
    def __init__(self, *args):  # \
        self.score = 0
        self.score2 = 0
        self.ipy = args[1]
        args = list(args[0])
        self.H, self.L, self.H2, self.L2 = args[4], args[5], args[2], args[3]
        self.E = args[0]
        self.LPSC = args[1]
        self.S = args[9]  # --------------------------
        self.I1 = args[7]
        self.I2 = args[6]
        self.chc = args[8]
        self.final_score = 0

        self.i_var = [self.ipy['ComCham'][0].get(), self.ipy['Grate_Rod'][0].get(), self.ipy['Grate_plate'][0].get(),
                      self.ipy['Top_Plate'][0].get()]

    def HP_CO(self):  # 1High Power CO
        r = [0, 8, 9, 11.0, 16]
        rating = [5, 4, 3, 2, 1]
        for i in range(0, len(r) - 1):
            if r[i] < self.H <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H > 16:
            self.score = self.score + 1

    def LP_CO(self):  # 2Low Power CO
        r = [0, 0.09, 0.10, 0.13, 0.20]
        rating = [5, 4, 3, 2, 1]
        score = 0
        for i in range(0, len(r) - 1):
            if r[i] < self.L <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L > 0.20:
            self.score = self.score + 1

    def HP_PM(self):  # 3High Power PM
        r = range(0, 1000, 20)
        rating = range(1, 51)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.H2 <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H2 > 980:
            self.score = self.score + 1

    def LP_PM(self):  # 4Low Power PM
        r = range(0, 10, 1)
        rating = range(1, 11)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.L2 <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L2 > 9:
            self.score = self.score + 1

    def eff(self):  # 5Efficiency
        r = range(0, 75, 5)
        rating = range(1, 16, 1)
        for i in range(0, len(r) - 1):
            if self.E == 0:
                self.score = self.score + 0
                break
            if r[i] <= self.E < r[i + 1]:
                self.score = self.score + rating[i]

        if self.E >= 70:
            self.score = self.score + 15

    def LP_SC(self):  # 6Low Power Specific Consumption
        r = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.039]

        rating = range(1, 9)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.LPSC <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.LPSC > 0.039:
            self.score = self.score + 0

    def Saf(self):  # 7Safety
        r = [100, 95, 85, 75, 45]
        rating = [5, 4, 3, 2, 1]
        for i in range(0, len(r) - 1):
            if r[i] > self.S >= r[i + 1]:
                self.score = self.score + rating[i]

        if self.S < 45 and self.S > 0:

            self.score = self.score + 1
        elif self.S < 1:
            self.score = self.score + 0

    def IE_CO(self):  # 8Indoor_CO
        r = [i / 100.0 for i in range(0, 100, 5)]
        rating = range(1, 21)
        rating.reverse()

        for i in range(0, len(r) - 1):
            if r[i] < self.I1 <= r[i + 1]:
                self.score += rating[i]

        if self.I1 > 0.95:
            self.score = self.score + 1

    def IE_PM(self):
        r = range(0, 50, 5)
        rating = range(1, 11)
        rating.reverse()

        for i in range(0, len(r) - 1):
            if r[i] < self.I2 <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.I2 > 40:
            self.score = self.score + 1

    def du_comcham(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [1, 2, 3, 4, 5]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['ComCham'][1].get() < r[i + 1]:


                    self.score2 = self.score2 + rating[i]

            if self.ipy['ComCham'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [3, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['ComCham'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['ComCham'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            if self.ipy['Du'][0].get() <= 1:
                self.score2 = self.score2 + 5

    def du_graterod(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [6, 7, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

    def du_grateplate(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [6, 7, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [2, 5, 7, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

    def du_topplate(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [3, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [1, 2, 3, 4, 5]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [2, 5, 7, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

        if car == 3:
            if self.ipy['Du'][1].get() <= 1:
                self.score2 = self.score2 + 5

    def calc(self):
        self.HP_CO()

        self.LP_CO()

        self.HP_PM()

        self.LP_PM()

        self.eff()

        self.LP_SC()

        self.Saf()

        self.IE_CO()

        self.IE_PM()

        self.du_comcham(self.i_var[0])
        self.du_graterod(self.i_var[1])
        self.du_grateplate(self.i_var[2])
        self.du_topplate(self.i_var[3])

    def p(self):
        self.calc()
        global Final_Technical_Score
        #print 'Score 1 %f' % self.score
       # print 'Score 2 %f' % self.score2

        s= (self.score + self.score2)
        Final_Technical_Score = 50 / 148.0 * s
        #print 'Final Score Technicla%f' %Final_Technical_Score
class SCORING_class2:

    def __init__(self, *args):  # \
        self.score = 0
        self.score2 = 0
        self.ipy = args[1]
        args = list(args[0])
        self.H, self.L, self.H2, self.L2 = args[4], args[5], args[2], args[3]
        self.E = args[0]
        self.LPSC = args[1]
        self.S = args[9]  # --------------------------
        self.I1 = args[7]
        self.I2 = args[6]
        self.chc = args[8]
        self.final_score = 0
        self.other=list(args[2])
        self.i_var = [self.ipy['ComCham'][0].get(), self.ipy['Grate_Rod'][0].get(), self.ipy['Grate_plate'][0].get(),
                      self.ipy['Top_Plate'][0].get()]

    def HP_CO1(self):  # 1High Power CO
        r = [0, 8, 9, 11.0, 16]
        rating = [5, 4, 3, 2, 1]
        for i in range(0, len(r) - 1):
            if r[i] < self.H[1] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H[1] > 16:
            self.score = self.score + 1
    def HP_CO2(self):  # 1High Power CO
        r = [0, 2, 4, 6, 7]
        rating = [5, 4, 3, 2, 1]
        for i in range(0, len(r) - 1):
            if r[i] < self.H[0] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H[0] > 7 and self.H[0] < 8:
            self.score = self.score + 1



    def LP_CO1(self):  # 2Low Power CO
        r = [0, 0.09, 0.10, 0.13, 0.20]
        rating = [5, 4, 3, 2, 1]
        score = 0
        for i in range(0, len(r) - 1):
            if r[i] < self.L[1] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L[1] > 0.20:
            self.score = self.score + 1
    def LP_CO2(self):  # 2Low Power CO
        r = [0, 0.02, 0.04, 0.06, 0.08]
        rating = [5, 4, 3, 2, 1]
        score = 0
        for i in range(0, len(r)-1):
            if r[i] < self.L[0] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L[0] > 0.08 and self.L[0] <0.09:
            self.score = self.score + 1

    def HP_PM1(self):  # 3High Power PM
        r = range(0, 1000, 20)
        rating = range(1, 51)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.H2[1] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H2[1] > 980:
            self.score = self.score + 1
    def HP_PM2(self):  # 3High Power PM
        r = range(0, 40, 2)
        rating = range(1, 21)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.H2[0] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.H2[0] > 40:
            self.score = self.score + 1

    def LP_PM1(self):  # 4Low Power PM
        r = range(0, 10, 1)
        rating = range(1, 11)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.L2[1] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L2[1] > 9:
            self.score = self.score + 1
    def LP_PM2(self):  # 4Low Power PM
        r = range(0, 10, 1)
        for i in range(0, len(r)):
            r[i] = r[i] / 10.0
        rating = range(1, 11)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.L2[0] <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.L2[0] > 0.9:
            self.score = self.score + 1

    def eff(self):  # 5Efficiency
        r = range(0, 75, 5)
        rating = range(1, 16, 1)
        for i in range(0, len(r) - 1):
            if self.E == 0:
                self.score = self.score + 0
                break
            if r[i] <= self.E < r[i + 1]:
                self.score = self.score + rating[i]

        if self.E >= 70:
            self.score = self.score + 15

    def LP_SC(self):  # 6Low Power Specific Consumption
        r = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.039]

        rating = range(1, 9)
        rating.reverse()
        for i in range(0, len(r) - 1):
            if r[i] < self.LPSC <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.LPSC > 0.039:
            self.score = self.score + 0

    def Saf(self):  # 7Safety
        r = [100, 95, 85, 75, 45]
        rating = [5, 4, 3, 2, 1]
        for i in range(0, len(r) - 1):
            if r[i] > self.S >= r[i + 1]:
                self.score = self.score + rating[i]

        if self.S < 45 and self.S > 0:

            self.score = self.score + 1
        elif self.S < 1:
            self.score = self.score + 0

    def IE_CO(self):  # 8Indoor_CO
        r = [i / 100.0 for i in range(0, 100, 5)]
        rating = range(1, 21)
        rating.reverse()

        for i in range(0, len(r) - 1):
            if r[i] < self.I1 <= r[i + 1]:
                self.score += rating[i]

        if self.I1 > 0.95:
            self.score = self.score + 1

    def IE_PM(self):
        r = range(0, 5)
        rating = range(1, 6)
        rating.reverse()

        for i in range(0, len(r) - 1):
            if r[i] < self.I2 <= r[i + 1]:
                self.score = self.score + rating[i]

        if self.I2 > 4:
            self.score = self.score + 1

    def du_comcham(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [1, 2, 3, 4, 5]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['ComCham'][1].get() < r[i + 1]:

                    self.score2 = self.score2 + rating[i]

            if self.ipy['ComCham'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [3, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['ComCham'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['ComCham'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            if self.ipy['Du'][0].get() <= 1:
                self.score2 = self.score2 + 5

    def du_graterod(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [6, 7, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_Rod'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_Rod'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

    def du_grateplate(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [4, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [6, 7, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [2, 5, 7, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Grate_plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Grate_plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

    def du_topplate(self, car):

        if car == 0:
            rating = [1, 2, 3, 4, 5]
            r = [3, 6, 8, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]
        if car == 1:
            rating = [1, 2, 3, 4, 5]
            r = [1, 2, 3, 4, 5]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

        if car == 2:
            rating = [1, 2, 3, 4, 5]
            r = [2, 5, 7, 9, 10]

            for i in range(0, len(r) - 1):
                if r[i] <= self.ipy['Top_Plate'][1].get() < r[i + 1]:
                    self.score2 = self.score2 + rating[i]

            if self.ipy['Top_Plate'][1].get() >= r[-1]:
                self.score2 = self.score2 + rating[-1]

        if car == 3:
            if self.ipy['Du'][1].get() <= 1:
                self.score2 = self.score2 + 5

    def calc(self):
        self.HP_CO1()
        self.HP_CO2()
        self.LP_CO1()
        self.LP_CO2()
        self.HP_PM1()
        self.HP_PM2()
        self.LP_PM1()
        self.LP_PM2()
        self.eff()

        self.LP_SC()

        self.Saf()

        self.IE_CO()

        self.IE_PM()

        self.du_comcham(self.i_var[0])
        self.du_graterod(self.i_var[1])
        self.du_grateplate(self.i_var[2])
        self.du_topplate(self.i_var[3])

    def p(self):
        self.calc()
        global Final_Technical_Score
       # print 'Score 1 %f' % self.score
        #print 'Score 2 %f' % self.score2
        s = (self.score + self.score2)
        Final_Technical_Score = 50 / 183.0 * s
        print 'Final Score Technical %f' %Final_Technical_Score

class SCORING_class_User:
    def __init__(self):
        self.score_user = 0
        global score_list
        self.xxx=1
        self.whole = {'Lower_Emission': [15, 15, 15, 20, 15, 10, 10], 'LOW_FUEL_CONSUMPTION': [80, 20], 'FAST_COOKING': [30, 20, 0],
                      'BUDGET_FRIENDLY': [0,50], 'MULTIPURPOSE': [25, 15, 10, 10, 5, 10, 10, 15],'DURABILITY':[17.5,5,15,10,7.5,-100,10,10,10,10,5],
                      'SIMULATNEOUS_COOKING/MULTI-POT_HOLES':[50,-50,50],'EASY_TO_USE':[20,20,20,-25,10,10,20],'ASTHETIC_APPEAL':[60,40],
                      'SAFETY':[30,20,20,20],'REGULAR_CLEANING':[50,50,-25],'PORTABILITY':[0,-50,100] }

        self.wholeb = {'Lower_Emission': (15, 15, 15, 20, 15, 10, 10), 'LOW_FUEL_CONSUMPTION': (80, 20), 'FAST_COOKING': (30, 20, 0),
                       'BUDGET_FRIENDLY': (0,50), 'MULTIPURPOSE': (25, 15, 10, 10, 5, 10, 10, 15),'DURABILITY':(17.5,5,15,10,7.5,-100,10,10,10,10,5),
                      'SIMULATNEOUS_COOKING/MULTI-POT_HOLES':(50,-50,50),'EASY_TO_USE':(20,20,20,-25,10,10,20),'ASTHETIC_APPEAL':(60,40),
                       'SAFETY':(30,30,20,20),'REGULAR_CLEANING':(50,50,-25),'PORTABILITY':(0,-50,100) }
        self.all = {'Lower_Emission': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []}, 'LOW_FUEL_CONSUMPTION': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'FAST_COOKING': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'BUDGET_FRIENDLY': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []}, 'MULTIPURPOSE': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []}, 'DURABILITY': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'EASY_TO_USE': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'ASTHETIC_APPEAL': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []} ,'SAFETY': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},
                    'REGULAR_CLEANING': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []},'PORTABILITY': {'score': 0, 'to_exclude': [], 'yes': [], 'no': []}}


        self.percentile = {
            'High_Hill': {'Lower_Emission': 17.08, 'LOW_FUEL_CONSUMPTION': 10.13, 'FAST_COOKING': 13.98, 'BUDGET_FRIENDLY': 7.93, 'MULTIPURPOSE': 10.66, 'DURABILITY': 17.95,
                          'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 12.39, 'EASY_TO_USE': 9.59, 'ASTHETIC_APPEAL': 0.01, 'SAFETY': 0.27, 'REGULAR_CLEANING': 0, 'PORTABILITY': 0},

            'Mid_Hill': {'Lower_Emission': 25.37, 'LOW_FUEL_CONSUMPTION': 14.31, 'FAST_COOKING': 17.14, 'BUDGET_FRIENDLY': 3.84, 'MULTIPURPOSE': 11.87, 'DURABILITY': 13.95,
                         'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 4.05, 'EASY_TO_USE': 8.13, 'ASTHETIC_APPEAL': 0.28, 'SAFETY': 0.44, 'REGULAR_CLEANING': 0.63, 'PORTABILITY': 0},

            'Central_Terai': {'Lower_Emission': 18.06, 'LOW_FUEL_CONSUMPTION': 12.86, 'FAST_COOKING': 16.78, 'BUDGET_FRIENDLY': 8.06, 'MULTIPURPOSE': 7.38, 'DURABILITY': 4.14,
                              'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 17.77, 'EASY_TO_USE': 11.24, 'ASTHETIC_APPEAL': 3.7, 'SAFETY': 0, 'REGULAR_CLEANING': 0, 'PORTABILITY': 0},

            'Western_Terai': {'Lower_Emission': 12.71, 'LOW_FUEL_CONSUMPTION': 11.39, 'FAST_COOKING': 17.36, 'BUDGET_FRIENDLY': 4.57, 'MULTIPURPOSE': 7.21, 'DURABILITY': 22.82,
                              'SIMULATNEOUS_COOKING/MULTI-POT_HOLES': 8.06, 'EASY_TO_USE': 14.13, 'ASTHETIC_APPEAL': 0, 'SAFETY': 0, 'REGULAR_CLEANING': 0, 'PORTABILITY': 1.75}
        }
        self.final_user=dict()
        self.user_total=0

    def for_print(self,x,y,zz):
        global for_p
        if x=='a':
            for_p[zz][y]='Yes'
        if x=='b':
            for_p[zz][y] = 'No'
        if x=='c':
            for_p[zz][y] = 'No Idea'


    def set_x(self, x, y, zz):
        self.b = self.wholeb[zz]
        self.a = self.whole[zz]
        self.for_print(x,y,zz)
        if x == 'a':
            self.a[y] = list(self.b)[y]
            self.all[zz]['yes'] = list((set(self.all[zz]['yes'])) - set([y]))
            self.all[zz]['yes'].append(y)

            self.all[zz]['to_exclude'] = list((set(self.all[zz]['to_exclude'])) - set([y]))

        if x == 'b':

            self.a[y] = 0
            self.all[zz]['yes'] = list(set(self.all[zz]['yes']) - set([y]))
            self.all[zz]['to_exclude'] = list((set(self.all[zz]['to_exclude'])) - set([y]))
            for i in self.all[zz]['yes']:
                self.a[i] = self.b[i]
        if x == 'c':
            self.all[zz]['to_exclude'].append(y)
            self.all[zz]['yes'] = list((set(self.all[zz]['yes'])) - set([y]))
            self.all[zz]['to_exclude']= list(set(self.all[zz]['to_exclude']))


        self.set_v(zz)

    def set_xx(self, x, y, zz):
        self.b = self.wholeb[zz]
        self.a = self.whole[zz]
        self.for_print(x,y,zz)
        if x == 'a':
            self.a[y] = list(self.b)[y]
            self.all[zz]['yes'] = list((set(self.all[zz]['yes'])) - set([y]))
            self.all[zz]['yes'].append(y)

            self.all[zz]['to_exclude'] = list((set(self.all[zz]['to_exclude'])) - set([y]))

        if x == 'b':

            self.a[y] = -(self.a[y])
            self.all[zz]['yes'] = list(set(self.all[zz]['yes']) - set([y]))
            self.all[zz]['to_exclude'] = list((set(self.all[zz]['to_exclude'])) - set([y]))
            for i in self.all[zz]['yes']:
                self.a[i] = self.b[i]
        if x == 'c':
            self.all[zz]['to_exclude'].append(y)
            self.all[zz]['yes'] = list((set(self.all[zz]['yes'])) - set([y]))
            self.all[zz]['to_exclude']= list(set(self.all[zz]['to_exclude']))


        self.set_v(zz)
    def set_v(self,zz):

        global score_list
        self.b = self.wholeb[zz]
        self.score_user = 0
        # print self.a
        ad = 0
        self.temp = 0.0
        next_temp = []
        # print 'se', self.all[zz]['to_exclude']
        # print 'Yes', self.all[zz]['yes']

        for i in self.all[zz]['yes']:
            self.a[i] = self.b[i]
        for i in self.all[zz]['to_exclude']:
            self.temp += self.b[i]
        if self.all[zz]['yes'] == []:
            ad = self.temp / 1
        else:
            ad = self.temp / len(self.all[zz]['yes'])
        # print 'ad', ad
        for i in self.all[zz]['to_exclude']:
            self.a[i] = 0
        # print 'before add', self.a
        for i in self.all[zz]['yes']:
            self.a[i] += ad
        for i in self.all[zz]['to_exclude']:
            self.a[i] = 0
            # print 'after add', self.a
            # print 'sum', sum(self.a)


        self.score_user += sum(self.a)
        # self.a
        self.temp = 0
        print self.score_user
        score_list[zz] = self.score_user




    def zo_ne(self):
        global zone,numb
        self.zone = zone
        numb=ccc()[zone]*0.01
        print numb


    def Budget_calc(self,x, y, zz):
        global add_val

        if x=='a':
            add_val=0

        if x=='b':
            add_val=(50.0/3)
        if x=='c':
            add_val =(100.0/3)
        if x=='d':
            add_val =(150.0/3)
        print add_val

    def F_cook(self,xxx):
        global xx,zz
        if xxx.get()<30:
            xx=50
        else:
            xx=(30/ xxx.get())*50



    def add_2(self):
        global score_list,add_val,xx,zz,tt


        score_list['FAST_COOKING']=score_list['FAST_COOKING']+xx-zz
        zz=xx

        score_list['BUDGET_FRIENDLY']+=add_val-tt
        tt=add_val
        print xx, zz


    def print_all(self):
        global score_list
        self.zo_ne()

        global Final_User_Score,for_p,numb


        self.add_2()

        self.user_total = 0

        for key in score_list:
            self.final_user[key] = score_list[key] * self.percentile[zone][key] *0.01
        self.user_total=0



        for key in self.final_user:

            self.user_total+=self.final_user[key]

        Final_User_Score=50/numb*self.user_total
        print 'Final User Score',Final_User_Score






class ICS_app(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "ICS Rating ")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (NameLogo, HomePage, UserPage, Chimnney_Stove, Chimnneyless_Stove, Force_Draft, Star ,UserP1,UserP2,UserP3,UserP4 ,UserP5, tech_user, Show_Failed,Failed_tech):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(NameLogo)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Star(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global Final_User_Score, Final_Technical_Score



        c = tk.Canvas(self, bg='white', width=700, height=300)
        c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))




        self.c=tk.Canvas(self, bg='white', width=700, height=300)

        txt1 = tk.StringVar()
        asasd = tk.Label(self, text="                   ", font=NORMAL_FONT).grid(row=1, column=0)



        button2 = ttk.Button(self, text='print', command=lambda: self.place())
        button2.grid(row=2, column=1, sticky="nsew")
        button2 = ttk.Button(self, text='Save Input', command=lambda: self.popup())
        button2.grid(row=2, column=2, sticky="nsew")
        button3 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserP5))
        button3.grid(row=3, column=1, sticky="nsew")
        button3 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(HomePage))
        button3.grid(row=3, column=2, sticky="nsew")


    def place(self):
        global Final_User_Score, Final_Technical_Score
        score=83
        #score = Final_User_Score + Final_Technical_Score
        print 'Final Score User = ',Final_User_Score
        print 'Final Score Technical = ',Final_Technical_Score
        print 'Total Score = ',score

        white = (255, 255, 255)
        green = (0, 128, 0)




        if score>=95:
            self.img=tk.PhotoImage(file='images/FIVE_GREEN.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FIVE_GREEN.gif')


        if score>90 and score <=95:
            self.img = tk.PhotoImage(file='images/FIVE_BLUE.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FIVE_BLUE.gif')


        if score>85 and score <=90:
            self.img = tk.PhotoImage(file='images/FIVE_RED.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FIVE_RED.gif')

        if score>80 and score <=85:
            self.img = tk.PhotoImage(file='images/FOUR_GREEN.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FOUR_GREEN.gif')

        if score>75 and score <=80:
            self.img = tk.PhotoImage(file='images/FOUR_BLUE.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FOUR_BLUE.gif')

        if score>70 and score <=75:
            self.img= tk.PhotoImage(file='images/FOUR_RED.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/FOUR_GREEN.gif')

        if score>65 and score <=70:
            self.img = tk.PhotoImage(file='images/THREE_GREEN.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/THREE_GREEN.gif')

        if score>60 and score <=65:
            self.img= tk.PhotoImage(file='images/THREE_BLUE.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/THREE_BLUE.gif')

        if score>55 and score <=60:
            self.img = tk.PhotoImage(file='images/THREE_RED.gif')
            self.img = self.img.subsample(5)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/THREE_GREEN.gif')

        if score<55:
            self.img = tk.PhotoImage(file='images/THREE_RED.gif')
            self.img = self.img.subsample(1)
            self.c.create_image(300, 100, image=self.img)
            self.c.grid(row=0, column=0, padx=(300, 0), pady=(200, 0))
            self.pill('images/THREE_RED.gif')

        txt1 = tk.StringVar()

        x = 'The Total Store is ' + str(Final_Technical_Score + Final_User_Score) + '\n' + \
        'Technical Score ' + str(Final_Technical_Score) + '\n' + \
        'User Score ' + str(Final_User_Score)
        txt1.set(x)

        self.c.create_text(140, 210, fill="darkblue",font="Times 20 bold",
                                text=x)






    def popup(self):
        self.w = popupWindow(self)
        self.wait_window(self.w.top)
        save_filename=self.w.value
        write_files(save_filename)

    def pill(self,x):
        from PIL import Image
        img = Image.open(x, 'r')

        fnt = ImageFont.truetype("arial_narrow_7.ttf", 40)
        img_w, img_h = img.size
        background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        img = img.resize((600, 300), Image.ANTIALIAS)
        # offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
        black = (0, 0, 0)
        offset = (100, 100)
        background.paste(img, offset)
        #background.save('out.png')

        x = 'The Total Store is ' + str(Final_Technical_Score + Final_User_Score) + '\n' + \
            'Technical Score ' + str(Final_Technical_Score) + '\n' + \
            'User Score ' + str(Final_User_Score)
        print 'asdasd'
        draw = ImageDraw.Draw(background)

        draw.text((100, 400), x, black, font=fnt)
        background.save('Result.png')


class NameLogo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="                                                                               ", font=LARGE_FONT)
        label.grid(row=0, column=1)
        var=tk.StringVar()
        v="This labeling system has been developed through parameters provided by the international \n ISO-IWA Tier System and NIBC Standards for Biomass Cookstoves 2016/17. " \
          "\n The stoves need to pass the minimums set by NIBC standards to enter the user acceptance scoring.\n This is a star based and color coded labeling system." \
          "\n\n" \
          "The user aceptance questionnaire and scoring was developed by Centre for Rural Technology,\nNepal in coordination with Alternative Energy Promotion Centre with support from The World Bank\n"
        var.set(v)
        label = tk.Label(self, text="Biomass Cookstove Labeling System", font=Ex_FONT)
        label.grid(row=1, column=2)
        label = tk.Label(self,textvariable=var, font=Head_FONT)
        label.grid(row=2, column=2,sticky=tk.W)
        button1 = ttk.Button(self, text='Enter', command=lambda: controller.show_frame(HomePage))
        button1.grid(row=3, column=2, sticky="ns")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Select the type of ICS", font=LARGE_FONT)
        label.grid(row=0, column=2,pady=10)
        label = tk.Label(self, text="                                                                                                                                 ", font=LARGE_FONT)
        label.grid(row=0, column=0,pady=10)
        button1 = ttk.Button(self, text='Chimney Stove', command=lambda: controller.show_frame(Chimnney_Stove))
        button1.grid(row=1, column=2, sticky="new",pady=5)
        button2 = ttk.Button(self, text='Chimneyless Stove', command=lambda: controller.show_frame(Chimnneyless_Stove))
        button2.grid(row=2, column=2, sticky="nsew",pady=5)
        button3 = ttk.Button(self, text='Forced Draft Stove', command=lambda: controller.show_frame(Force_Draft))
        button3.grid(row=3, column=2, sticky="nsew",pady=5)
        button3 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(NameLogo))
        button3.grid(row=4, column=2, sticky="ns",pady=5)






class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        global zone,page
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="                                                                                                                                 ", font=LARGE_FONT)
        label.grid(row=0, column=0, pady=10)
        label = tk.Label(self, text=" Select the Region  ", font=LARGE_FONT)
        label.grid(row=0, column=2, pady=10)
        button1 = ttk.Button(self, text='High Hill ', command=self.High_Hill).grid(row=1, column=2, sticky="nsew",pady=5)
        button2 = ttk.Button(self, text='Mid Hill ', command=self.Mid_Hill).grid(row=2, column=2, sticky="nsew",pady=5)
        button3 = ttk.Button(self, text='Central Terai', command=self.Central_Terai).grid(row=3, column=2, sticky="nsew",pady=5)
        button4 = ttk.Button(self, text='Western Terai ', command=self.Western_Terai).grid(row=4, column=2, sticky="nsew",pady=5)

        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(HomePage)).grid(row=5, column=2, sticky="nsew",pady=5)

    def High_Hill(self):
        set_zone('High_Hill')

        self.controller.show_frame(UserP1)

    def Mid_Hill(self):
        set_zone('Mid_Hill')
        self.controller.show_frame(UserP1)

    def Central_Terai(self):
        set_zone('Central_Terai')

        self.controller.show_frame(UserP1)

    def Western_Terai(self):
        set_zone('Western_Terai')

        self.controller.show_frame(UserP1)



class Chimnney_Stove(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob=tech_user( parent, controller)
        ##define variables


        self.hp_te, self.sfc, self.te_hp_pmI, self.te_lp_pmI, self.te_hp_coI, \
        self.te_lp_coI, self.ie_pm, self.ie_co = tk.DoubleVar(), tk.DoubleVar(), \
                                                 tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()
        self.te_hp_pmO, self.te_lp_pmO, self.te_hp_coO, self.te_lp_coO = tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()
        self.safety = tk.DoubleVar()
        self.comcham = tk.DoubleVar()
        self.grate_rod = tk.DoubleVar()
        self.grate_plate = tk.DoubleVar()
        self.top_plate = tk.DoubleVar()
        self.comcham_du, self.top_plate_du = tk.DoubleVar(), tk.DoubleVar()
        self.ch_var, self.rod_var, self.plate_var, self.top_var, self.safety_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
        ##Labels
        Lablel_H1 = ttk.Label(self, text="       ", font=LARGE_FONT).grid(row=0, column=0,
                                                                                                       sticky=tk.E)
        Lablel_H1 = ttk.Label(self, text="Thermal Efficiency and Fuel Use     ", font=LARGE_FONT).grid(row=1, column=1,
                                                                                                       sticky=tk.E)
        label1 = ttk.Label(self, text="High Power Thermal Efficiency %      ", font=NORMAL_FONT).grid(row=2, column=1,
                                                                                                      sticky=tk.W)
        label2 = ttk.Label(self, text="Specific Fuel Consumption (MJ/min/L) ", font=NORMAL_FONT).grid(row=3, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H2 = ttk.Label(self, text="Total Emission                      ", font=LARGE_FONT).grid(row=4, column=1,
                                                                                                       sticky=tk.W,
                                                                                                       )

        Lablel_H2a = ttk.Label(self, text="Indoor                     ", font=LARGE_FONT).grid(row=5, column=2, padx=(15, 0))
        Lablel_H2b = ttk.Label(self, text="Outdoor                      ", font=LARGE_FONT).grid(row=5, column=3, padx=(15, 0))
        label3 = ttk.Label(self, text="High Power PM 2.5 (mg/MJd)           ", font=NORMAL_FONT).grid(row=6, column=1,
                                                                                                      sticky=tk.W)
        label4 = ttk.Label(self, text="Low Power PM 2.5 (mg/MJd)            ", font=NORMAL_FONT).grid(row=7, column=1,
                                                                                                      sticky=tk.W)
        label5 = ttk.Label(self, text="High Power CO (g/MJd)                ", font=NORMAL_FONT).grid(row=8, column=1,
                                                                                                      sticky=tk.W)
        label6 = ttk.Label(self, text="Low Power CO (g/MJd)                 ", font=NORMAL_FONT).grid(row=9, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H3 = ttk.Label(self, text="Indoor Emission                   ", font=LARGE_FONT).grid(row=10, column=1,
                                                                                                     sticky=tk.W,
                                                                                                     pady=(10, 0))
        label7 = ttk.Label(self, text="PM 2.5 (mg/min)                      ", font=NORMAL_FONT).grid(row=11, column=1,
                                                                                                      sticky=tk.W)
        label8 = ttk.Label(self, text="CO (mg/min)                          ", font=NORMAL_FONT).grid(row=12, column=1,
                                                                                                      sticky=tk.W)

        labelH3 = tk.Label(self, text="Select Stove Category ", font=LARGE_FONT).grid(row=13, column=1, sticky=tk.W)
        label1 = tk.Label(self, text="Safety Assessment Calculation Value", font=NORMAL_FONT).grid(row=17, column=1,
                                                                                             sticky=tk.W, padx=(16, 0))

        # Entry
        Hp_te = tk.Entry(self, textvariable=self.hp_te).grid(row=2, column=2)
        SFC = tk.Entry(self, textvariable=self.sfc).grid(row=3, column=2)
        SFC = tk.Entry(self, textvariable=self.te_hp_pmI).grid(row=6, column=2, sticky=tk.W)
        SFC = tk.Entry(self, textvariable=self.te_lp_pmI).grid(row=7, column=2, sticky=tk.W)
        SFC = tk.Entry(self, textvariable=self.te_hp_coI).grid(row=8, column=2, sticky=tk.W)
        SFC = tk.Entry(self, textvariable=self.te_lp_coI).grid(row=9, column=2, sticky=tk.W)

        IC_HPPM = tk.Entry(self, textvariable=self.te_hp_pmO).grid(row=6, column=3, sticky=tk.W, padx=(10, 0))
        IC_LPPM = tk.Entry(self, textvariable=self.te_lp_pmO).grid(row=7, column=3, sticky=tk.W, padx=(10, 0))
        IC_TEHPCO = tk.Entry(self, textvariable=self.te_hp_coO).grid(row=8, column=3, sticky=tk.W, padx=(10, 0))
        IC_TElpCO = tk.Entry(self, textvariable=self.te_lp_coO).grid(row=9, column=3, sticky=tk.W, padx=(10, 0))

        SFC = tk.Entry(self, textvariable=self.ie_pm).grid(row=11, column=2)
        SFC = tk.Entry(self, textvariable=self.ie_co).grid(row=12, column=2)

        # Safety

        radio1a = tk.Radiobutton(self, text='Metallic Body Cooking and Heating Stove', value=1, variable=1,
                                 command=lambda: self.set_x(0)).grid(row=14, column=1, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='Metallic Body Cooking Stove            ', value=2, variable=1,
                                 command=lambda: self.set_x(1)).grid(row=15, column=1, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='Mud/ Composite body Cooking Stove      ', value=3, variable=1,
                                 command=lambda: self.set_x(2)).grid(row=16, column=1, sticky=tk.W)
        Safety = tk.Entry(self, textvariable=self.safety).grid(row=17, column=2)

        # Durability



        labelH4 = tk.Label(self, text="            ", font=LARGE_FONT).grid(row=1, column=4, sticky="nsew")
        labelH5 = tk.Label(self, text="Material Durability", font=LARGE_FONT).grid(row=1, column=5, sticky=tk.W)
        labelH6 = tk.Label(self, text="Combustion Camber", font=Head_FONT).grid(row=2, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=4, variable=2,
                                 command=lambda: self.add_box('a', [3, 5])).grid(row=3, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=5, variable=2,
                                 command=lambda: self.add_box('b', [4, 5])).grid(row=4, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Other Material (Durability test)     ', value=6, variable=2,
                                 command=lambda: self.add_box('c', [5, 5])).grid(row=5, column=5, sticky=tk.W)


        labelH6 = tk.Label(self, text="Grate (where applicable)", font=Head_FONT).grid(row=7, column=5, sticky=tk.W,
                                                                                        pady=(10, 0))
        labelH7 = tk.Label(self, text="Rod Structure", font= "arial 10 underline").grid(row=8, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=9, variable=3,
                                 command=lambda: self.add_box('d', [9, 5])).grid(row=9, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=10, variable=3,
                                 command=lambda: self.add_box('e', [10, 5])).grid(row=10, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=11, variable=3,
                                 command=lambda: self.add_box('f', [11, 5])).grid(row=11, column=5, sticky=tk.W)

        labelH9 = tk.Label(self, text="Plate Structure", font="arial 10 underline").grid(row=12, column=5, sticky=tk.W)

        radio1c = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=12, variable=4,
                                 command=lambda: self.add_box('g', [13, 5])).grid(row=13, column=5, sticky=tk.W)
        radio2c = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=13, variable=4,
                                 command=lambda: self.add_box('h', [14, 5])).grid(row=14, column=5, sticky=tk.W)
        radio3c = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=14, variable=4,
                                 command=lambda: self.add_box('i', [15, 5])).grid(row=15, column=5, sticky=tk.W,pady=10)

        labelH12 = tk.Label(self, text="Top Plate with pot riser", font=Head_FONT).grid(row=16, column=5, sticky=tk.W)

        radio1d = tk.Radiobutton(self, text='Cast Iron (thickness in mm)', value=15, variable=5,
                                 command=lambda: self.add_box('j', [17, 5])).grid(row=17, column=5, sticky=tk.W)
        radio2d = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=16, variable=5,
                                 command=lambda: self.add_box('k', [18, 5])).grid(row=18, column=5, sticky=tk.W)
        radio3d = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=17, variable=5,
                                 command=lambda: self.add_box('l', [19, 5])).grid(row=19, column=5, sticky=tk.W)

        radio4d = tk.Radiobutton(self, text='Other Material (Durability test)       ', value=19, variable=5,
                                 command=lambda: self.add_box('m', [20, 5])).grid(row=20, column=5, sticky=tk.W)

        input_var = [self.hp_te, self.sfc, [self.te_hp_pmI, self.te_hp_pmO], [self.te_lp_pmI, self.te_lp_pmO], [self.te_hp_coI, self.te_hp_coO],
                     [self.te_lp_coI, self.te_lp_coO], self.ie_pm, self.ie_co, self.safety_var, self.safety]

        input_var2 = {'ComCham': [self.ch_var, self.comcham], 'Grate_Rod': [self.rod_var, self.grate_rod],
                      'Grate_plate': [self.plate_var, self.grate_plate], 'Top_Plate': [self.top_var, self.top_plate],
                      'Du': [self.comcham_du, self.top_plate_du]}


        labelH5 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=22, column=5, sticky="nsew")
        button = ttk.Button(self, text='Next', command=lambda: ob.final_score_calc(2,3, input_var, input_var2)).grid(row=26,
                                                                                                            column=2)

        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(HomePage)).grid(row=26, column=1)
        #button2 = ttk.Button(self, text='Next Page', command=lambda: final_score_calc()).grid( row=26, column=3)

    def set_x(self, x):

        self.safety_var.set(x)

    def add_box2(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham_du).grid(row=(lit[0] + 1), column=(lit[1]), padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1]), sticky="nwse")

    def add_box3(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.top_plate_du).grid(row=(lit[0] + 1), column=(lit[1] + 1),
                                                                        padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1] + 1), sticky="nwse")

    def no_du(self):
        self.comcham_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")

    def no_du2(self):
        self.top_plate_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=21, column=6, sticky="nwse")

    def add_box(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(0)



        elif v == 'b':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(1)

        elif v == 'c':
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            radio2b = tk.Radiobutton(self, text='Yes', value=7, variable=6,
                                     command=lambda: self.add_box2('a', [5, 6])).grid(row=5, column=6, sticky=tk.W,
                                                                                      padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=8, variable=6,
                                     command=lambda: self.no_du()).grid(row=5, column=7, sticky=tk.W, padx=(10, 0))
            self.ch_var.set(2)
        elif v == 'd':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")

            self.rod_var.set(0)


        elif v == 'e':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] - 1, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] + 1, column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(1)
        elif v == 'f':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(2)
        elif v == 'g':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.plate_var.set(0)

        elif v == 'h':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(1)
        elif v == 'i':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(2)
        elif v == 'j':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 4), column=6, sticky="nwse")
            self.top_var.set(0)

        elif v == 'k':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")

            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            self.top_var.set(1)
        elif v == 'l':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.top_var.set(2)
        elif v == 'm':
            radio2b = tk.Radiobutton(self, text='Yes', value=20, variable=7,
                                     command=lambda: self.add_box3('a', lit)).grid(row=lit[0], column=(lit[1] + 1),
                                                                                   sticky=tk.W, padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=21, variable=7,
                                     command=lambda: self.no_du2()).grid(row=lit[0], column=(lit[1] + 2), sticky=tk.W,
                                                                         padx=(10, 0))
            # ent1 = ttk.Entry(self, textvariable=self.grate).grid(row=lit[0], column=(lit[1]+1))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            self.top_var.set(3)


class Chimnneyless_Stove(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ob = tech_user(parent, controller)
        ##define variables
        self.hp_te, self.sfc, self.te_hp_pm, self.te_lp_pm, self.te_hp_co, \
        self.te_lp_co, self.ie_pm, self.ie_co = tk.DoubleVar(), tk.DoubleVar(), \
                                                tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()
        self.safety = tk.DoubleVar()
        self.comcham = tk.DoubleVar()
        self.grate_rod = tk.DoubleVar()
        self.grate_plate = tk.DoubleVar()
        self.top_plate = tk.DoubleVar()
        self.comcham_du, self.top_plate_du = tk.DoubleVar(), tk.DoubleVar()
        self.ch_var, self.rod_var, self.plate_var, self.top_var, self.safety_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
        ##Labels
        Lablel_H1 = ttk.Label(self, text="       ", font=LARGE_FONT).grid(row=0, column=0,
                                                                          sticky=tk.E)
        Lablel_H1 = ttk.Label(self, text="Thermal Efficiency and Fuel Use     ", font=LARGE_FONT).grid(row=1, column=1,
                                                                                                       sticky=tk.E)
        label1 = ttk.Label(self, text="High Power Thermal Efficiency %      ", font=NORMAL_FONT).grid(row=2, column=1,
                                                                                                      sticky=tk.W)
        label2 = ttk.Label(self, text="Specific Fuel Consumption (MJ/min/L) ", font=NORMAL_FONT).grid(row=3, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H2 = ttk.Label(self, text="Total Emission                      ", font=LARGE_FONT).grid(row=4, column=1,
                                                                                                       sticky=tk.W, pady=(10, 0))
        label3 = ttk.Label(self, text="High Power PM 2.5 (mg/MJd)           ", font=NORMAL_FONT).grid(row=5, column=1,
                                                                                                      sticky=tk.W)
        label4 = ttk.Label(self, text="Low Power PM 2.5 (mg/MJd)            ", font=NORMAL_FONT).grid(row=6, column=1,
                                                                                                      sticky=tk.W)
        label5 = ttk.Label(self, text="High Power CO (g/MJd)               ", font=NORMAL_FONT).grid(row=7, column=1,
                                                                                                      sticky=tk.W)
        label6 = ttk.Label(self, text="Low Power CO (g/MJd)                ", font=NORMAL_FONT).grid(row=8, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H3 = ttk.Label(self, text="Indoor Emission                   ", font=LARGE_FONT).grid(row=9, column=1,
                                                                                                     sticky=tk.W, pady=(10, 0))
        label7 = ttk.Label(self, text="PM 2.5 (mg/min)                      ", font=NORMAL_FONT).grid(row=10, column=1,
                                                                                                      sticky=tk.W)
        label8 = ttk.Label(self, text="CO (mg/min)                          ", font=NORMAL_FONT).grid(row=11, column=1,
                                                                                                      sticky=tk.W)

        labelH3 = tk.Label(self, text="Select Stove Category ", font=LARGE_FONT).grid(row=12, column=1, sticky=tk.W)
        label1 = tk.Label(self, text="Safety Assessment Calculation ", font=NORMAL_FONT).grid(row=16, column=1,
                                                                                             sticky=tk.W, padx=(16, 0))

        # Entry
        Hp_te = tk.Entry(self, textvariable=self.hp_te).grid(row=2, column=2)
        SFC = tk.Entry(self, textvariable=self.sfc).grid(row=3, column=2)
        SFC = tk.Entry(self, textvariable=self.te_hp_pm).grid(row=5, column=2)
        SFC = tk.Entry(self, textvariable=self.te_lp_pm).grid(row=6, column=2)
        SFC = tk.Entry(self, textvariable=self.te_hp_co).grid(row=7, column=2)
        SFC = tk.Entry(self, textvariable=self.te_lp_co).grid(row=8, column=2)
        SFC = tk.Entry(self, textvariable=self.ie_pm).grid(row=10, column=2)
        SFC = tk.Entry(self, textvariable=self.ie_co).grid(row=11, column=2)

        # Safety

        radio1a = tk.Radiobutton(self, text='Metallic Body Cooking and Heating Stove', value=1, variable=1,
                                 command=lambda: self.set_x(0)).grid(row=13, column=1, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='Metallic Body Cooking Stove            ', value=2, variable=1,
                                 command=lambda: self.set_x(1)).grid(row=14, column=1, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='Mud/ Composite body Cooking Stove      ', value=3, variable=1,
                                 command=lambda: self.set_x(2)).grid(row=15, column=1, sticky=tk.W)
        Safety = tk.Entry(self, textvariable=self.safety).grid(row=16, column=2)

        # Durability
        labelH4 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=1, column=4, sticky="nsew")
        labelH5 = tk.Label(self, text="Material Durability", font=LARGE_FONT).grid(row=1, column=5, sticky=tk.W)
        labelH6 = tk.Label(self, text="Combustion Camber", font=Head_FONT).grid(row=2, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=4, variable=2,
                                 command=lambda: self.add_box('a', [3, 5])).grid(row=3, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=5, variable=2,
                                 command=lambda: self.add_box('b', [4, 5])).grid(row=4, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Other Material (Durability test)     ', value=6, variable=2,
                                 command=lambda: self.add_box('c', [5, 5])).grid(row=5, column=5, sticky=tk.W)
        labelH4 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=6, column=6, sticky="nsew")

        labelH6 = tk.Label(self, text="Grate (where applicable)", font=Head_FONT).grid(row=7, column=5, sticky=tk.W, pady=(10, 0))
        labelH7 = tk.Label(self, text="Rod Structure", font="arial 10 underline").grid(row=8, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=9, variable=3,
                                 command=lambda: self.add_box('d', [9, 5])).grid(row=9, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Stainless Steel( thickness in mm)', value=10, variable=3,
                                 command=lambda: self.add_box('e', [10, 5])).grid(row=10, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=11, variable=3,
                                 command=lambda: self.add_box('f', [11, 5])).grid(row=11, column=5, sticky=tk.W)

        labelH9 = tk.Label(self, text="Plate Structure", font="arial 10 underline").grid(row=12, column=5, sticky=tk.W)

        radio1c = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=12, variable=4,
                                 command=lambda: self.add_box('g', [13, 5])).grid(row=13, column=5, sticky=tk.W)
        radio2c = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=13, variable=4,
                                 command=lambda: self.add_box('h', [14, 5])).grid(row=14, column=5, sticky=tk.W)
        radio3c = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=14, variable=4,
                                 command=lambda: self.add_box('i', [15, 5])).grid(row=15, column=5, sticky=tk.W)

        labelH12 = tk.Label(self, text="Top Plate with Pot riser", font=NORMAL_FONT).grid(row=16, column=5, sticky=tk.W)

        radio1d = tk.Radiobutton(self, text='Cast Iron (thickness in mm)', value=15, variable=5,
                                 command=lambda: self.add_box('j', [17, 5])).grid(row=17, column=5, sticky=tk.W)
        radio2d = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=16, variable=5,
                                 command=lambda: self.add_box('k', [18, 5])).grid(row=18, column=5, sticky=tk.W)
        radio3d = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=17, variable=5,
                                 command=lambda: self.add_box('l', [19, 5])).grid(row=19, column=5, sticky=tk.W)

        radio4d = tk.Radiobutton(self, text='Other Material (Durability test)       ', value=19, variable=5,
                                 command=lambda: self.add_box('m', [20, 5])).grid(row=20, column=5, sticky=tk.W)

        input_var = [self.hp_te, self.sfc, self.te_hp_pm, self.te_lp_pm, self.te_hp_co,
                     self.te_lp_co, self.ie_pm, self.ie_co, self.safety_var, self.safety]

        input_var2 = {'ComCham': [self.ch_var, self.comcham], 'Grate_Rod': [self.rod_var, self.grate_rod], 'Grate_plate': [self.plate_var, self.grate_plate], 'Top_Plate': [self.top_var, self.top_plate],
                      'Du': [self.comcham_du, self.top_plate_du]}



        labelH5 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=22, column=6, sticky="nsew")
        button = ttk.Button(self, text='Next', command=lambda: ob.final_score_calc(1, 2, input_var, input_var2)).grid(row=26,
                                                                                                                   column=2)
        # button = ttk.Button(self, text='Next', command=lambda: prinwt(input_var)).grid(row=5, column=12)
        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(HomePage)).grid(row=26, column=1)




    def set_x(self, x):

        self.safety_var.set(x)

    def add_box2(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham_du).grid(row=(lit[0] + 1), column=(lit[1]), padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1]), sticky="nwse")

    def add_box3(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.top_plate_du).grid(row=(lit[0] + 1), column=(lit[1] + 1), padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1] + 1), sticky="nwse")

    def no_du(self):
        self.comcham_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
    def no_du2(self):
        self.comcham_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=21, column=6, sticky="nwse")
    def add_box(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(0)



        elif v == 'b':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(1)

        elif v == 'c':
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            radio2b = tk.Radiobutton(self, text='Yes', value=7, variable=7,
                                     command=lambda: self.add_box2('a', [5, 6])).grid(row=5, column=6, sticky=tk.W, padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=8, variable=7,
                                     command=lambda: self.no_du()).grid(row=5, column=7, sticky=tk.W, padx=(10, 0))
            self.ch_var.set(2)
        elif v == 'd':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.rod_var.set(0)


        elif v == 'e':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] - 1, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] + 1, column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(1)
        elif v == 'f':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(2)
        elif v == 'g':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.plate_var.set(0)

        elif v == 'h':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(1)
        elif v == 'i':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(2)
        elif v == 'j':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 4), column=6, sticky="nwse")
            self.top_var.set(0)

        elif v == 'k':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")

            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            self.top_var.set(1)
        elif v == 'l':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.top_var.set(2)
        elif v == 'm':
            radio2b = tk.Radiobutton(self, text='Yes', value=20, variable=7,
                                     command=lambda: self.add_box3('a', lit)).grid(row=lit[0], column=(lit[1] + 1), sticky=tk.W, padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=21, variable=7,
                                     command=lambda: self.no_du2()).grid(row=lit[0], column=(lit[1] + 2), sticky=tk.W, padx=(10, 0))
            # ent1 = ttk.Entry(self, textvariable=self.grate).grid(row=lit[0], column=(lit[1]+1))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            self.top_var.set(3)


class Force_Draft(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob = tech_user(parent, controller)
        ##define variables

        self.hp_te, self.sfc, self.te_hp_pm, self.te_lp_pm, self.te_hp_co, \
        self.te_lp_co, self.ie_pm, self.ie_co = tk.DoubleVar(), tk.DoubleVar(), \
                                                tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()
        self.safety = tk.DoubleVar()
        self.comcham = tk.DoubleVar()
        self.grate_rod = tk.DoubleVar()
        self.grate_plate = tk.DoubleVar()
        self.top_plate = tk.DoubleVar()
        self.comcham_du, self.top_plate_du = tk.DoubleVar(), tk.DoubleVar()
        self.ch_var, self.rod_var, self.plate_var, self.top_var, self.safety_var = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
        ##Labels
        Lablel_H1 = ttk.Label(self, text="       ", font=LARGE_FONT).grid(row=0, column=0,
                                                                          sticky=tk.E)
        Lablel_H1 = ttk.Label(self, text="Thermal Efficiency and Fuel Use     ", font=LARGE_FONT).grid(row=1, column=1,
                                                                                                       sticky=tk.E)
        label1 = ttk.Label(self, text="High Power Thermal Efficiency %      ", font=NORMAL_FONT).grid(row=2, column=1,
                                                                                                      sticky=tk.W)
        label2 = ttk.Label(self, text="Specific Fuel Consumption (MJ/min/L) ", font=NORMAL_FONT).grid(row=3, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H2 = ttk.Label(self, text="Total Emission                      ", font=LARGE_FONT).grid(row=4, column=1,
                                                                                                       sticky=tk.W, pady=(10, 0))
        label3 = ttk.Label(self, text="High Power PM 2.5 (mg/MJd)           ", font=NORMAL_FONT).grid(row=5, column=1,
                                                                                                      sticky=tk.W)
        label4 = ttk.Label(self, text="Low Power PM 2.5 (mg/MJd)            ", font=NORMAL_FONT).grid(row=6, column=1,
                                                                                                      sticky=tk.W)
        label5 = ttk.Label(self, text="High Power CO (g/MJd)                ", font=NORMAL_FONT).grid(row=7, column=1,
                                                                                                      sticky=tk.W)
        label6 = ttk.Label(self, text="Low Power CO (g/MJd)                 ", font=NORMAL_FONT).grid(row=8, column=1,
                                                                                                      sticky=tk.W)

        Lablel_H3 = ttk.Label(self, text="Indoor Emission                   ", font=LARGE_FONT).grid(row=9, column=1,
                                                                                                     sticky=tk.W, pady=(10, 0))
        label7 = ttk.Label(self, text="PM 2.5 (mg/min)                      ", font=NORMAL_FONT).grid(row=10, column=1,
                                                                                                      sticky=tk.W)
        label8 = ttk.Label(self, text="CO (mg/min)                          ", font=NORMAL_FONT).grid(row=11, column=1,
                                                                                                      sticky=tk.W)

        labelH3 = tk.Label(self, text="Select Stove Category ", font=LARGE_FONT).grid(row=12, column=1, sticky=tk.W)
        label1 = tk.Label(self, text="Safety Assessment Calculation", font=NORMAL_FONT).grid(row=16, column=1,
                                                                                             sticky=tk.W, padx=(16, 0))

        # Entry
        Hp_te = tk.Entry(self, textvariable=self.hp_te).grid(row=2, column=2)
        SFC = tk.Entry(self, textvariable=self.sfc).grid(row=3, column=2)
        SFC = tk.Entry(self, textvariable=self.te_hp_pm).grid(row=5, column=2)
        SFC = tk.Entry(self, textvariable=self.te_lp_pm).grid(row=6, column=2)
        SFC = tk.Entry(self, textvariable=self.te_hp_co).grid(row=7, column=2)
        SFC = tk.Entry(self, textvariable=self.te_lp_co).grid(row=8, column=2)
        SFC = tk.Entry(self, textvariable=self.ie_pm).grid(row=10, column=2)
        SFC = tk.Entry(self, textvariable=self.ie_co).grid(row=11, column=2)

        # Safety

        radio1a = tk.Radiobutton(self, text='Metallic Body Cooking and Heating Stove', value=1, variable=1,
                                 command=lambda: self.set_x(0)).grid(row=13, column=1, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='Metallic Body Cooking Stove            ', value=2, variable=1,
                                 command=lambda: self.set_x(1)).grid(row=14, column=1, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='Mud/ Composite body Cooking Stove      ', value=3, variable=1,
                                 command=lambda: self.set_x(2)).grid(row=15, column=1, sticky=tk.W)
        Safety = tk.Entry(self, textvariable=self.safety).grid(row=16, column=2)

        # Durability
        labelH4 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=1, column=4, sticky="nsew")
        labelH5 = tk.Label(self, text="Material Durability", font=LARGE_FONT).grid(row=1, column=5, sticky=tk.W)
        labelH6 = tk.Label(self, text="Commbustion Camber", font=Head_FONT).grid(row=2, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=4, variable=2,
                                 command=lambda: self.add_box('a', [3, 5])).grid(row=3, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=5, variable=2,
                                 command=lambda: self.add_box('b', [4, 5])).grid(row=4, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Other Material ((Durability test)       ', value=6, variable=2,
                                 command=lambda: self.add_box('c', [5, 5])).grid(row=5, column=5, sticky=tk.W)
        labelH4 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=6, column=6, sticky="nsew")

        labelH6 = tk.Label(self, text="Grate (where applicable)", font=Head_FONT).grid(row=7, column=5, sticky=tk.W, pady=(10, 0))
        labelH7 = tk.Label(self, text="Rod Structure", font="arial 10 underline").grid(row=8, column=5, sticky=tk.W)

        radio1b = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=9, variable=3,
                                 command=lambda: self.add_box('d', [9, 5])).grid(row=9, column=5, sticky=tk.W)
        radio2b = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=10, variable=3,
                                 command=lambda: self.add_box('e', [10, 5])).grid(row=10, column=5, sticky=tk.W)
        radio3b = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=11, variable=3,
                                 command=lambda: self.add_box('f', [11, 5])).grid(row=11, column=5, sticky=tk.W)

        labelH9 = tk.Label(self, text="Plate Structure", font="arial 10 underline").grid(row=12, column=5, sticky=tk.W)

        radio1c = tk.Radiobutton(self, text='Cast Iron Structure (thickness in mm)', value=12, variable=4,
                                 command=lambda: self.add_box('g', [13, 5])).grid(row=13, column=5, sticky=tk.W)
        radio2c = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=13, variable=4,
                                 command=lambda: self.add_box('h', [14, 5])).grid(row=14, column=5, sticky=tk.W)
        radio3c = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=14, variable=4,
                                 command=lambda: self.add_box('i', [15, 5])).grid(row=15, column=5, sticky=tk.W)

        labelH12 = tk.Label(self, text="Top Plate with pot riser", font=Head_FONT).grid(row=16, column=5, sticky=tk.W)

        radio1d = tk.Radiobutton(self, text='Cast Iron (thickness in mm)', value=15, variable=5,
                                 command=lambda: self.add_box('j', [17, 5])).grid(row=17, column=5, sticky=tk.W)
        radio2d = tk.Radiobutton(self, text='Stainless Steel (thickness in mm)', value=16, variable=5,
                                 command=lambda: self.add_box('k', [18, 5])).grid(row=18, column=5, sticky=tk.W)
        radio3d = tk.Radiobutton(self, text='Mild Steel (thickness in mm)', value=17, variable=5,
                                 command=lambda: self.add_box('l', [19, 5])).grid(row=19, column=5, sticky=tk.W)

        radio4d = tk.Radiobutton(self, text='Other Material (Durability test)       ', value=19, variable=5,
                                 command=lambda: self.add_box('m', [20, 5])).grid(row=20, column=5, sticky=tk.W)

        input_var = [self.hp_te, self.sfc, self.te_hp_pm, self.te_lp_pm, self.te_hp_co,
                     self.te_lp_co, self.ie_pm, self.ie_co, self.safety_var, self.safety]

        input_var2 = {'ComCham': [self.ch_var, self.comcham], 'Grate_Rod': [self.rod_var, self.grate_rod],
                      'Grate_plate': [self.plate_var, self.grate_plate], 'Top_Plate': [self.top_var, self.top_plate],
                      'Du': [self.comcham_du, self.top_plate_du]}


        labelH5 = tk.Label(self, text="                      ", font=LARGE_FONT).grid(row=22, column=5, sticky="nsew")
        button = ttk.Button(self, text='Next', command=lambda: ob.final_score_calc(1, 3, input_var, input_var2)).grid(row=26,
                                                                                                                   column=2)
        # button = ttk.Button(self, text='Next', command=lambda: prinwt(input_var)).grid(row=5, column=12)
        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(HomePage)).grid(row=26, column=1)


    def set_x(self, x):

        self.safety_var.set(x)

    def add_box2(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham_du).grid(row=(lit[0] + 1), column=(lit[1]), padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1]), sticky="nwse")

    def add_box3(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.top_plate_du).grid(row=(lit[0] + 1), column=(lit[1] + 1), padx=(10, 0))

        if v == 'b':
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=(lit[1] + 1), sticky="nwse")

    def no_du(self):
        self.comcham_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
    def no_du2(self):
        self.comcham_du.set(100)
        lab1 = ttk.Label(self, text='          ').grid(row=21, column=6, sticky="nwse")
    def add_box(self, v, lit):
        if v == 'a':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(0)



        elif v == 'b':
            ent1 = ttk.Entry(self, textvariable=self.comcham).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=5, column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=6, column=6, sticky="nwse")
            self.ch_var.set(1)

        elif v == 'c':
            lab1 = ttk.Label(self, text='          ').grid(row=3, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=4, column=6, sticky="nwse")
            radio2b = tk.Radiobutton(self, text='Yes', value=7, variable=7,
                                     command=lambda: self.add_box2('a', [5, 6])).grid(row=5, column=6, sticky=tk.W, padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=8, variable=7,
                                     command=lambda: self.no_du()).grid(row=5, column=7, sticky=tk.W, padx=(10, 0))
            self.ch_var.set(2)
        elif v == 'd':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.rod_var.set(0)


        elif v == 'e':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] - 1, column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=lit[0] + 1, column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(1)
        elif v == 'f':

            ent1 = ttk.Entry(self, textvariable=self.grate_rod).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.rod_var.set(2)
        elif v == 'g':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.plate_var.set(0)

        elif v == 'h':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(1)
        elif v == 'i':

            ent1 = ttk.Entry(self, textvariable=self.grate_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            # lab1 = ttk.Label(self, text='          ').grid(row=5, column=6, sticky="nwse")
            self.plate_var.set(2)
        elif v == 'j':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 4), column=6, sticky="nwse")
            self.top_var.set(0)

        elif v == 'k':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")

            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 3), column=6, sticky="nwse")
            self.top_var.set(1)
        elif v == 'l':

            ent1 = ttk.Entry(self, textvariable=self.top_plate).grid(row=lit[0], column=(lit[1] + 1), padx=(10, 0))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 1), column=7, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] + 2), column=6, sticky="nwse")
            self.top_var.set(2)
        elif v == 'm':
            radio2b = tk.Radiobutton(self, text='Yes', value=20, variable=7,
                                     command=lambda: self.add_box3('a', lit)).grid(row=lit[0], column=(lit[1] + 1), sticky=tk.W, padx=(10, 0))
            radio3b = tk.Radiobutton(self, text='No     ', value=21, variable=7,
                                     command=lambda: self.no_du2()).grid(row=lit[0], column=(lit[1] + 2), sticky=tk.W, padx=(10, 0))
            # ent1 = ttk.Entry(self, textvariable=self.grate).grid(row=lit[0], column=(lit[1]+1))
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 3), column=6, sticky="nwse")
            lab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 2), column=6, sticky="nwse")
            ab1 = ttk.Label(self, text='          ').grid(row=(lit[0] - 1), column=6, sticky="nwse")
            self.top_var.set(3)


class Show_Failed(tk.Frame):
    global failed,failed2,failed3_2
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        w=tk.Text(self,state=tk.NORMAL,width=10,height=10)
        for i in failed:
            w.insert(tk.INSERT,i)
            w.insert(tk.INSERT, '\n')

        w.grid(row=0,column=0)

        button2 = ttk.Button(self, text='Next Page', command=lambda: controller.show_frame(Chimnneyless_Stove)).grid(     row=26, column=3)

class tech_user(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global failed3_2

    def final_score_calc(self,x, s, ipx, ipy):
        global Final_User_Score, Final_Technical_Score
        if x == 1:
            f=Calculation(s, ipx, ipy)
            print ' -----------',f
            if f==['pass','pass']:
                self.controller.show_frame(UserPage)
            else:
                self.controller.show_frame(Failed_tech)
        elif x == 2:
            f = Calculation2(s, ipx, ipy)
            print 'f -----------', f
            if f == ['pass', 'pass']:
                self.controller.show_frame(UserPage)
            else:
                self.controller.show_frame(Failed_tech)

class Failed_tech(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        text= tk.Text(self)

        text.grid(row=0,column=0)
        button3 = ttk.Button(self, text='Show Failed', command=lambda: self.show_f()).grid(row=5, column=2, sticky="nsew")
        button3 = ttk.Button(self, text='Clear', command=lambda: self.clear()).grid(row=7, column=2, sticky="nsew")
        button2 = ttk.Button(self, text='Back', command=lambda: self.back()).grid(row=6, column=2, sticky="nsew")



    def back(self):
        global page
        if page==1:
            self.controller.show_frame(Chimnneyless_Stove)

        elif page==2:
            self.controller.show_frame(Force_Draft)
        elif page==3:
            self.controller.show_frame(Chimnney_Stove)

    def show_f(self):
        global failed,failed3_2,failed2



        if page==1 or page==2:

            f_failed = failed + failed3_2
            print f_failed
            text = tk.Text(self)
            for x in f_failed:
                text.insert(tk.END, x + '\n')
            text.grid(row=0, column=0)

        if page==3:

            f_failed = failed2 + failed3_2

            text = tk.Text(self)
            for x in f_failed:
                text.insert(tk.END, x + '\n')
            text.grid(row=0, column=0)

    def clear(self):
        text = tk.Text(self)
        text.grid(row=0, column=0)

    def popup(self):
        self.w = popupWindow(self)
        self.wait_window(self.w.top)
        save_filename=self.w.value
        write_files(save_filename)



class Passed_all(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class popupWindow(object):
    def __init__(self, master):
        self.e=tk.StringVar()
        top = self.top = tk.Toplevel(master)
        self.l = tk.Label(top, text="Enter File Name")
        self.l.pack()
        e = tk.Entry(top, textvariable=self.e).pack()

        self.b = tk.Button(top, text='Ok', command=self.cleanup)
        self.b.pack()
        top.geometry("200x100+500+500")

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()





class UserP1(tk.Frame):
    def __init__(self, parent, controller):
        ob=SCORING_class_User()
        tk.Frame.__init__(self, parent)
        self.min=tk.DoubleVar()
        self.controller = controller

        Lablel_B = ttk.Label(self, text="     ", font=LARGE_FONT).grid(row=0, column=0, sticky=tk.W,pady=(0, 5))
        Lablel_H1 = ttk.Label(self, text="Lower Emission     ", font=LARGE_FONT).grid(row=1, column=1, sticky=tk.W, pady=(0, 5))
        Lablel_01 = ttk.Label(self, text="1. Emits Less Smoke     ", font=NORMAL_FONT).grid(row=2, column=1, sticky=tk.W)
        Lablel_02 = ttk.Label(self, text="2. Eyes water less. "
                                         "Can remain in kitchen longer     ", font=NORMAL_FONT).grid(row=3, column=1, sticky=tk.W)
        Lablel_03 = ttk.Label(self, text="3. Even children can comfortably stay in kitchen while cooking", font=NORMAL_FONT).grid(row=4, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="4. Reduced smoke related health problems:  ", font=NORMAL_FONT).grid(row=5, column=1, sticky=tk.W)
        Lablel_044 = ttk.Label(self, text="    Irritation, headaches, chest pain, cough, etc.", font=NORMAL_FONT).grid(row=6, column=1, sticky=tk.W)
        Lablel_05 = ttk.Label(self, text="5. Clean breathable and healthier environment in kitchen", font=NORMAL_FONT).grid(row=7, column=1, sticky=tk.W)
        Lablel_06 = ttk.Label(self, text="6. Pot remains cleaner     ", font=NORMAL_FONT).grid(row=8, column=1, sticky=tk.W)
        Lablel_07 = ttk.Label(self, text="7. The house and clothes remain cleaner", font=NORMAL_FONT).grid(row=9, column=1, sticky=tk.W)

        Lablel_H2 = ttk.Label(self, text="Low Fuel Consumption", font=LARGE_FONT).grid(row=10, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_11 = ttk.Label(self, text="1. Saves fuel     ", font=NORMAL_FONT).grid(row=11, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="2. Eyes water less. ", font=NORMAL_FONT).grid(row=12, column=1, sticky=tk.W)

        Lablel_H3 = ttk.Label(self, text="Fast Cooking", font=LARGE_FONT).grid(row=13, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_11 = ttk.Label(self, text="1. Regular food cooks faster.", font=NORMAL_FONT).grid(row=14, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="2. Occasional dishes cook faster as well.", font=NORMAL_FONT).grid(row=15, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="3. Time to cook meal for family of 5 members (Full course meal of Dal, Bhat and Tarakari)", font=NORMAL_FONT).grid(row=16, column=1, sticky=tk.W)

        Lablel_H4 = ttk.Label(self, text="Budget Friendly", font=LARGE_FONT).grid(row=17, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_11 = ttk.Label(self, text="1. What do you feel about price of the stove? ", font=NORMAL_FONT).grid(row=18, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="2. Pellets: Having used the pellet based technology,", font=NORMAL_FONT).grid(row=19, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="   Are you ready for spending some money on processed fuel for cooking?", font=NORMAL_FONT).grid(row=20, column=1, sticky=tk.W)



        # radio 1
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=100, command=lambda: ob.set_x('a', 0, 'Lower_Emission')).grid(row=2, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=100, command=lambda: ob.set_x('b', 0, 'Lower_Emission')).grid(row=2, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=100, command=lambda: ob.set_x('c', 0, 'Lower_Emission')).grid(row=2, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=101, command=lambda: ob.set_x('a', 1, 'Lower_Emission')).grid(row=3, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=101, command=lambda: ob.set_x('b', 1, 'Lower_Emission')).grid(row=3, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=101, command=lambda: ob.set_x('c', 1, 'Lower_Emission')).grid(row=3, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=102, command=lambda: ob.set_x('a', 2, 'Lower_Emission')).grid(row=4, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=102, command=lambda: ob.set_x('b', 2, 'Lower_Emission')).grid(row=4, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=102, command=lambda: ob.set_x('c', 2, 'Lower_Emission')).grid(row=4, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=103, command=lambda: ob.set_x('a', 3, 'Lower_Emission')).grid(row=5, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=103, command=lambda: ob.set_x('b', 3, 'Lower_Emission')).grid(row=5, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=103, command=lambda: ob.set_x('c', 3, 'Lower_Emission')).grid(row=5, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=104, command=lambda: ob.set_x('a', 4, 'Lower_Emission')).grid(row=7, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=104, command=lambda: ob.set_x('b', 4, 'Lower_Emission')).grid(row=7, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=104, command=lambda: ob.set_x('c', 4, 'Lower_Emission')).grid(row=7, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=105, command=lambda: ob.set_x('a', 5, 'Lower_Emission')).grid(row=8, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=105, command=lambda: ob.set_x('b', 5, 'Lower_Emission')).grid(row=8, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=105, command=lambda: ob.set_x('c', 5, 'Lower_Emission')).grid(row=8, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=106, command=lambda: ob.set_x('a', 6, 'Lower_Emission')).grid(row=9, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=106, command=lambda: ob.set_x('b', 6, 'Lower_Emission')).grid(row=9, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=106, command=lambda: ob.set_x('c', 6, 'Lower_Emission')).grid(row=9, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=107, command=lambda: ob.set_x('a', 0, 'LOW_FUEL_CONSUMPTION')).grid(row=11, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=107, command=lambda: ob.set_x('b', 0, 'LOW_FUEL_CONSUMPTION')).grid(row=11, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=107, command=lambda: ob.set_x('c', 0, 'LOW_FUEL_CONSUMPTION')).grid(row=11, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=108, command=lambda: ob.set_x('a', 1, 'LOW_FUEL_CONSUMPTION')).grid(row=12, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=108, command=lambda: ob.set_x('b', 1, 'LOW_FUEL_CONSUMPTION')).grid(row=12, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=108, command=lambda: ob.set_x('c', 1, 'LOW_FUEL_CONSUMPTION')).grid(row=12, column=5, sticky=tk.W)


        #fast cooking
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=109, command=lambda: ob.set_x('a', 0, 'FAST_COOKING')).grid(row=14, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=109, command=lambda: ob.set_x('b', 0, 'FAST_COOKING')).grid(row=14, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=109, command=lambda: ob.set_x('c', 0, 'FAST_COOKING')).grid(row=14, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=110, command=lambda: ob.set_x('a', 1, 'FAST_COOKING')).grid(row=15, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=110, command=lambda: ob.set_x('b', 1, 'FAST_COOKING')).grid(row=15, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=110, command=lambda: ob.set_x('c', 1, 'FAST_COOKING')).grid(row=15, column=5, sticky=tk.W)

        enty=tk.Entry(self, textvariable=self.min).grid(row=16, column=3)




        #BUDGET_FRIENDLY
        radio1a = tk.Radiobutton(self, text='Highly Expensive', value=1, variable=111, command=lambda: ob.Budget_calc('a', 0, 'BUDGET_FRIENDLY')).grid(row=18, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='Slightly Expensive', value=2, variable=111, command=lambda: ob.Budget_calc('b', 0, 'BUDGET_FRIENDLY')).grid(row=18, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='Optimum value for money', value=3, variable=111, command=lambda: ob.Budget_calc('c', 0, 'BUDGET_FRIENDLY')).grid(row=18, column=5, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='More value than the cost', value=4, variable=111, command=lambda: ob.Budget_calc('d', 0, 'BUDGET_FRIENDLY')).grid(row=18, column=6, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=112, command=lambda: ob.set_x('a', 1, 'BUDGET_FRIENDLY')).grid(row=19, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=112, command=lambda: ob.set_x('b', 1, 'BUDGET_FRIENDLY')).grid(row=19, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=112, command=lambda: ob.set_x('c', 1, 'BUDGET_FRIENDLY')).grid(row=19, column=5, sticky=tk.W)

        Lablel_12 = ttk.Label(self, text="   ", font=NORMAL_FONT).grid(row=25, column=1, sticky=tk.W,pady=(10,10))
        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserPage))
        button2.grid(row=2214, column=3)
        button2 = ttk.Button(self, text='Next', command=lambda: self.next1())
        button2.grid(row=2214, column=4)

    def next1(self):
        self.controller.show_frame(UserP2)
        ob = SCORING_class_User()
        ob.F_cook(self.min)



class UserP2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob = SCORING_class_User()
        tk.Frame.__init__(self, parent)


        Lablel_B = ttk.Label(self, text="     ", font=LARGE_FONT).grid(row=0, column=0, sticky=tk.W,
                                                                       pady=(0, 5))
        Lablel_H5 = ttk.Label(self, text="Multipurpose", font=LARGE_FONT).grid(row=21, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_11 = ttk.Label(self, text="1. Meets regular human meal cooking (Dal, Bhat, Tarkari, Roti, Dhindo)", font=NORMAL_FONT).grid(row=22, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="2. Meets regular animal feed cooking? ", font=NORMAL_FONT).grid(row=23, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="   (applicable for Eco-Chula XXL and XXXL only)", font=NORMAL_FONT).grid(row=24, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="3. Meets occasional dishes during festivals? (Perception)", font=NORMAL_FONT).grid(row=25, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="4. Meets cooking needs for occasional increase in member?  ", font=NORMAL_FONT).grid(row=26, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="   not more than (1.5 times the family size)", font=NORMAL_FONT).grid(row=27, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="5. Brewing for family (Not for commercial/occasional festivals?", font=NORMAL_FONT).grid(row=28, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    Only small amount) (Perception based)", font=NORMAL_FONT).grid(row=29, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="6. Boiling water for family?", font=NORMAL_FONT).grid(row=30, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="7. Space heating for winter?", font=NORMAL_FONT).grid(row=31, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="8. Suitable for my regular cooking pot size?", font=NORMAL_FONT).grid(row=32, column=1, sticky=tk.W)

        # MUltipurpose
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=113, command=lambda: ob.set_x('a', 0, 'MULTIPURPOSE')).grid(row=22, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=113, command=lambda: ob.set_x('b', 0, 'MULTIPURPOSE')).grid(row=22, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=113, command=lambda: ob.set_x('c', 0, 'MULTIPURPOSE')).grid(row=22, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=114, command=lambda: ob.set_x('a', 1, 'MULTIPURPOSE')).grid(row=23, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=114, command=lambda: ob.set_x('b', 1, 'MULTIPURPOSE')).grid(row=23, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=114, command=lambda: ob.set_x('c', 1, 'MULTIPURPOSE')).grid(row=23, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=115, command=lambda: ob.set_x('a', 2, 'MULTIPURPOSE')).grid(row=25, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=115, command=lambda: ob.set_x('b', 2, 'MULTIPURPOSE')).grid(row=25, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=115, command=lambda: ob.set_x('c', 2, 'MULTIPURPOSE')).grid(row=25, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=116, command=lambda: ob.set_x('a', 3, 'MULTIPURPOSE')).grid(row=26, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=116, command=lambda: ob.set_x('b', 3, 'MULTIPURPOSE')).grid(row=26, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=116, command=lambda: ob.set_x('c', 3, 'MULTIPURPOSE')).grid(row=26, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=117, command=lambda: ob.set_x('a', 4, 'MULTIPURPOSE')).grid(row=28, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=117, command=lambda: ob.set_x('b', 4, 'MULTIPURPOSE')).grid(row=28, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=117, command=lambda: ob.set_x('c', 4, 'MULTIPURPOSE')).grid(row=28, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=118, command=lambda: ob.set_x('a', 5, 'MULTIPURPOSE')).grid(row=30, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=118, command=lambda: ob.set_x('b', 5, 'MULTIPURPOSE')).grid(row=30, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=118, command=lambda: ob.set_x('c', 5, 'MULTIPURPOSE')).grid(row=30, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=119, command=lambda: ob.set_x('a', 6, 'MULTIPURPOSE')).grid(row=31, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=119, command=lambda: ob.set_x('b', 6, 'MULTIPURPOSE')).grid(row=31, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=119, command=lambda: ob.set_x('c', 6, 'MULTIPURPOSE')).grid(row=31, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=120, command=lambda: ob.set_x('a', 7, 'MULTIPURPOSE')).grid(row=32, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=120, command=lambda: ob.set_x('b', 7, 'MULTIPURPOSE')).grid(row=32, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=120, command=lambda: ob.set_x('c', 7, 'MULTIPURPOSE')).grid(row=32, column=5, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="   ", font=NORMAL_FONT).grid(row=35, column=1, sticky=tk.W, pady=(10, 10))
        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserP1))
        button2.grid(row=2214, column=3)
        button2 = ttk.Button(self, text='Next', command=lambda: controller.show_frame(UserP3))
        button2.grid(row=2214, column=5)


class UserP3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob = SCORING_class_User()
        Lablel_B = ttk.Label(self, text="     ", font=LARGE_FONT).grid(row=0, column=0, sticky=tk.W,
                                                                       pady=(0, 5))
        Lablel_H1 = ttk.Label(self, text="Durability    ", font=LARGE_FONT).grid(row=1, column=1, sticky=tk.W, pady=(0, 5))
        Lablel_01 = ttk.Label(self, text="1. Does the stove come with limited time warranty?", font=NORMAL_FONT).grid(row=2, column=1, sticky=tk.W)

        Lablel_03 = ttk.Label(self, text="2. Stove is robust and feels durable?", font=NORMAL_FONT).grid(row=5, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="3. Accessories are robust and feel durable ?", font=NORMAL_FONT).grid(row=6, column=1, sticky=tk.W)

        Lablel_05 = ttk.Label(self, text="4. Connections and Wire are managed well and seems durable?", font=NORMAL_FONT).grid(row=7, column=1, sticky=tk.W)
        Lablel_06 = ttk.Label(self, text="5. Stove and/or accessories are damaged during the course ", font=NORMAL_FONT).grid(row=8, column=1, sticky=tk.W)
        Lablel_07 = ttk.Label(self, text="    of use. Not working", font=NORMAL_FONT).grid(row=9, column=1, sticky=tk.W)
        Lablel_07 = ttk.Label(self, text="6. Stove is installed properly. Enough guidance has been ", font=NORMAL_FONT).grid(row=10, column=1, sticky=tk.W)
        Lablel_08 = ttk.Label(self, text="    given regarding the setting of the stove and required", font=NORMAL_FONT).grid(row=11, column=1, sticky=tk.W)
        Lablel_08 = ttk.Label(self, text="    ventilation /chimney setting?", font=NORMAL_FONT).grid(row=12, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="7. Does the stove come with any sort of User Manual on how ", font=NORMAL_FONT).grid(row=13, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="    to use with different types of fuel and regular different", font=NORMAL_FONT).grid(row=14, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    types of fuel and regular cleaning and maintenance guide?", font=NORMAL_FONT).grid(row=15, column=1, sticky=tk.W)

        Lablel_H3 = ttk.Label(self, text="8. Was the User Manual helpful?", font=NORMAL_FONT).grid(row=16, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="9. Can do replacement of basic parts at own house by ", font=NORMAL_FONT).grid(row=17, column=1, sticky=tk.W, padx=(0, 5))
        Lablel_12 = ttk.Label(self, text="     purchasing or fabricating damaged parts?", font=NORMAL_FONT).grid(row=18, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="10. Can be replaced by trained technician available? ", font=NORMAL_FONT).grid(row=19, column=1, sticky=tk.W)

        # radio 1
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=121, command=lambda: self.box_add('a', 0, 'DURABILITY', ob)).grid(row=2, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=121, command=lambda: self.box_add('b', 0, 'DURABILITY', ob)).grid(row=2, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=121, command=lambda: self.box_add('c', 0, 'DURABILITY', ob)).grid(row=2, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=123, command=lambda: ob.set_x('a', 2, 'DURABILITY')).grid(row=5, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=123, command=lambda: ob.set_x('b', 2, 'DURABILITY')).grid(row=5, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=123, command=lambda: ob.set_x('c', 2, 'DURABILITY')).grid(row=5, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=124, command=lambda: ob.set_x('a', 3, 'DURABILITY')).grid(row=6, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=124, command=lambda: ob.set_x('b', 3, 'DURABILITY')).grid(row=6, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=124, command=lambda: ob.set_x('c', 3, 'DURABILITY')).grid(row=6, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=125, command=lambda: ob.set_x('a', 4, 'DURABILITY')).grid(row=7, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=125, command=lambda: ob.set_x('b', 4, 'DURABILITY')).grid(row=7, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=125, command=lambda: ob.set_x('c', 4, 'DURABILITY')).grid(row=7, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=126, command=lambda: ob.set_xx('a', 5, 'DURABILITY')).grid(row=8, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=126, command=lambda: ob.set_xx('b', 5, 'DURABILITY')).grid(row=8, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=126, command=lambda: ob.set.xx('c', 5, 'DURABILITY')).grid(row=8, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=127, command=lambda: ob.set_x('a', 6, 'DURABILITY')).grid(row=10, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=127, command=lambda: ob.set_x('b', 6, 'DURABILITY')).grid(row=10, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=127, command=lambda: ob.set_x('c', 6, 'DURABILITY')).grid(row=10, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=128, command=lambda: ob.set_x('a', 7, 'DURABILITY')).grid(row=13, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=128, command=lambda: ob.set_x('b', 7, 'DURABILITY')).grid(row=13, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=128, command=lambda: ob.set_x('c', 7, 'DURABILITY')).grid(row=13, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=129, command=lambda: ob.set_x('a', 8, 'DURABILITY')).grid(row=16, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=129, command=lambda: ob.set_x('b', 8, 'DURABILITY')).grid(row=16, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=129, command=lambda: ob.set_x('c', 8, 'DURABILITY')).grid(row=16, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=130, command=lambda: ob.set_x('a', 9, 'DURABILITY')).grid(row=17, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=130, command=lambda: ob.set_x('b', 9, 'DURABILITY')).grid(row=17, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=130, command=lambda: ob.set_x('c', 9, 'DURABILITY')).grid(row=17, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=131, command=lambda: ob.set_x('a', 10, 'DURABILITY')).grid(row=19, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=131, command=lambda: ob.set_x('b', 10, 'DURABILITY')).grid(row=19, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=131, command=lambda: ob.set_x('c', 10, 'DURABILITY')).grid(row=19, column=5, sticky=tk.W)

        Lablel_12 = ttk.Label(self, text="   ", font=NORMAL_FONT).grid(row=35, column=1, sticky=tk.W, pady=(10, 10))
        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserP2))
        button2.grid(row=2214, column=3)
        button2 = ttk.Button(self, text='Next', command=lambda: controller.show_frame(UserP4))
        button2.grid(row=2214, column=5)

    def box_add(self,x,y,zz,ob):
        if zz == 'DURABILITY' and y == 0 and x == 'a':

            Lablel_02 = ttk.Label(self, text="  - Having given limited time warranty, do you feel good/reliable if you were to ", font=NORMAL_FONT).grid(row=3, column=1, sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="    purchase the new stove compared to other locally manufactured stoves?  ", font=NORMAL_FONT).grid(row=4, column=1, sticky=tk.W)
            radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=30123, command=lambda: self.box_add('a', 1, 'DURABILITY', ob)).grid(row=3, column=3, sticky=tk.W)
            radio2a = tk.Radiobutton(self, text='No', value=2, variable=30123, command=lambda: self.box_add('b', 1, 'DURABILITY', ob)).grid(row=3, column=4, sticky=tk.W)
            radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=30123, command=lambda: self.box_add('b', 1, 'DURABILITY', ob)).grid(row=3, column=5, sticky=tk.W)

        elif zz == 'DURABILITY' and y == 0 and x == 'b':

            Lablel_02 = ttk.Label(self, text="                                                                                                                                 ", font=NORMAL_FONT).grid(row=3, column=1,columnspan = 2, sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="                                                                                                                                ", font=NORMAL_FONT).grid(row=4, column=1,columnspan = 2, sticky=tk.W)
            Lablel_02 = ttk.Label(self, text="                                        ", font=NORMAL_FONT).grid(row=3, column=3, columnspan=2,sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="                                     ", font=NORMAL_FONT).grid(row=3, column=4, columnspan=2,sticky=tk.W)
            Lablel_02 = ttk.Label(self, text="                                ", font=NORMAL_FONT).grid(row=3, column=5, columnspan=2, sticky=tk.W)


        elif zz == 'DURABILITY' and y == 0 and x == 'c':

            Lablel_02 = ttk.Label(self, text="                                                                                                                  ", font=NORMAL_FONT).grid(row=3, column=1, columnspan=2,sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="                                                                                                             ", font=NORMAL_FONT).grid(row=4, column=1, columnspan=2, sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="        ", font=NORMAL_FONT).grid(row=3, column=4, columnspan=2, sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="        ", font=NORMAL_FONT).grid(row=3, column=4, columnspan=2, sticky=tk.W)
            Lablel_02 = ttk.Label(self, text="             ", font=NORMAL_FONT).grid(row=3, column=5, columnspan=2, sticky=tk.W)
        ob.set_x(x, y, zz)

class UserP4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob = SCORING_class_User()
        Lablel_B = ttk.Label(self, text="     ", font=LARGE_FONT).grid(row=0, column=0, sticky=tk.W,
                                                                       pady=(0, 5))



        Lablel_H2 = ttk.Label(self, text="Simultaneous Cooking/ Multi-Pot Holes ", font=LARGE_FONT).grid(row=21, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_H4 = ttk.Label(self, text="1. Can cook two dishes at the same time?", font=NORMAL_FONT).grid(row=22, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="2. Have the current stove usage affected your daily practice", font=NORMAL_FONT).grid(row=23, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    of simultaneous cooking in negative way?", font=NORMAL_FONT).grid(row=24, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="3. Like the new features at the cost of simultaneous cooking?", font=NORMAL_FONT).grid(row=25, column=1, sticky=tk.W)

        Lablel_H5 = ttk.Label(self, text="EASY TO USE", font=LARGE_FONT).grid(row=26, column=1, sticky=tk.W, pady=(10, 5))
        Lablel_11 = ttk.Label(self, text="1. Easy to start fire?", font=NORMAL_FONT).grid(row=27, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="2. Do not have to keep adding fuel, so no need to stay?" , font=NORMAL_FONT).grid(row=28, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    in kitchen for longer time? ", font=NORMAL_FONT).grid(row=29, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="3. Once lit, fire does not go out easily so no need to" , font=NORMAL_FONT).grid(row=30, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    monitor and hence can multitask?", font=NORMAL_FONT).grid(row=31, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="4. Does the need of pellets bother you after having ", font=NORMAL_FONT).grid(row=32, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="    experienced the clean cooking?", font=NORMAL_FONT).grid(row=33, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="5. Can use fan while starting so no need to blow on ", font=NORMAL_FONT).grid(row=34, column=1, sticky=tk.W)
        Lablel_11 = ttk.Label(self, text="    the fire initially?", font=NORMAL_FONT).grid(row=35, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="6. Easy to clean out ashes?", font=NORMAL_FONT).grid(row=36, column=1, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="7. Right height for cooking?", font=NORMAL_FONT).grid(row=37, column=1, sticky=tk.W)




        #radio2
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=132, command=lambda: ob.set_x('a',0, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=22, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=132, command=lambda: ob.set_x('b', 0, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=22, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=132, command=lambda: ob.set_x('c', 0, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=22, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=133, command=lambda: ob.set_xx('a', 1, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=23, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=133, command=lambda: ob.set_xx('b', 1, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=23, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=133, command=lambda: ob.set_xx('c', 1, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=23, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=134, command=lambda: ob.set_x('a', 2, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=25, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=134, command=lambda: ob.set_x('b', 2, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=25, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=134, command=lambda: ob.set_x('c', 2, 'SIMULATNEOUS_COOKING/MULTI-POT_HOLES')).grid(row=25, column=5, sticky=tk.W)

        #EASY_TO_USE
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=135, command=lambda: ob.set_x('a', 0, 'EASY_TO_USE')).grid(row=27, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=135, command=lambda: ob.set_x('b', 0, 'EASY_TO_USE')).grid(row=27, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=135, command=lambda: ob.set_x('c', 0, 'EASY_TO_USE')).grid(row=27, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=136, command=lambda: ob.set_x('a', 1, 'EASY_TO_USE')).grid(row=28, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=136, command=lambda: ob.set_x('b', 1, 'EASY_TO_USE')).grid(row=28, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=136, command=lambda: ob.set_x('c', 1, 'EASY_TO_USE')).grid(row=28, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=137, command=lambda: ob.set_x('a', 2, 'EASY_TO_USE')).grid(row=30, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=137, command=lambda: ob.set_x('b', 2, 'EASY_TO_USE')).grid(row=30, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=137, command=lambda: ob.set_x('c', 2, 'EASY_TO_USE')).grid(row=30, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=138, command=lambda: ob.set_xx('a', 3, 'EASY_TO_USE')).grid(row=32, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=138, command=lambda: ob.set_xx('b', 3, 'EASY_TO_USE')).grid(row=32, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=138, command=lambda: ob.set_xx('c', 3, 'EASY_TO_USE')).grid(row=32, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=139, command=lambda: ob.set_x('a', 4, 'EASY_TO_USE')).grid(row=34, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=139, command=lambda: ob.set_x('b', 4, 'EASY_TO_USE')).grid(row=34, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=139, command=lambda: ob.set_x('c', 4, 'EASY_TO_USE')).grid(row=34, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=140, command=lambda: ob.set_x('a', 5, 'EASY_TO_USE')).grid(row=36, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=140, command=lambda: ob.set_x('b', 5, 'EASY_TO_USE')).grid(row=36, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=140, command=lambda: ob.set_x('c', 5, 'EASY_TO_USE')).grid(row=36, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=141, command=lambda: ob.set_x('a',6, 'EASY_TO_USE')).grid(row=37, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=141, command=lambda: ob.set_x('b', 6, 'EASY_TO_USE')).grid(row=37, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=141, command=lambda: ob.set_x('c', 6, 'EASY_TO_USE')).grid(row=37, column=5, sticky=tk.W)
        Lablel_12 = ttk.Label(self, text="   ", font=NORMAL_FONT).grid(row=45, column=1, sticky=tk.W, pady=(10, 10))

        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserP3))
        button2.grid(row=2214, column=3)
        button2 = ttk.Button(self, text='Next', command=lambda: controller.show_frame(UserP5))
        button2.grid(row=2214, column=5)


class UserP5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ob=SCORING_class_User()
        self.controller = controller
        Lablel_B = ttk.Label(self, text="     ", font=LARGE_FONT).grid(row=0, column=0, sticky=tk.W,
                                                                       pady=(0, 5))
        Lablel_H1 = ttk.Label(self, text=" Asthetic Appeal  ", font=LARGE_FONT).grid(row=1, column=1, sticky=tk.W, pady=(0, 5))
        Lablel_01 = ttk.Label(self, text="1. Looks attractive", font=NORMAL_FONT).grid(row=2, column=1, sticky=tk.W)
        Lablel_01 = ttk.Label(self, text="2. Other people are impressed and it makes you feel happy/proud", font=NORMAL_FONT).grid(row=3, column=1, sticky=tk.W)


        Lablel_03 = ttk.Label(self, text="Safety", font=LARGE_FONT).grid(row=4, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="1. No burn risks for children accidentally touching the outside ", font=NORMAL_FONT).grid(row=5, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="surface. Can keep children with us while cooking?   ", font=NORMAL_FONT).grid(row=6, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="2. Stove frequent touching surfaces is warm so no burn risks?", font=NORMAL_FONT).grid(row=7, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="3. Stove is stable.", font=NORMAL_FONT).grid(row=8, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="4. Reduced risk of burning while adding/changing fuel batch?", font=NORMAL_FONT).grid(row=9, column=1, sticky=tk.W)

        Lablel_03 = ttk.Label(self, text="Regular Cleaning", font=LARGE_FONT).grid(row=10, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="1. Regular cleaning is easier?", font=NORMAL_FONT).grid(row=11, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="2. Reduced frequency and time of cleaning of stoves and accessories?", font=NORMAL_FONT).grid(row=12, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="3. Difficult to clean out ashes from interior parts while cleaning?", font=NORMAL_FONT).grid(row=13, column=1, sticky=tk.W)

        Lablel_03 = ttk.Label(self, text="Portability", font=LARGE_FONT).grid(row=14, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="1. Is portability a necessary feature for your household?", font=NORMAL_FONT).grid(row=15, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="2. If Yes, (concerning your need of portability) does it bother in ", font=NORMAL_FONT).grid(row=16, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="    your daily cooking practice while using the new stove?", font=NORMAL_FONT).grid(row=17, column=1, sticky=tk.W)
        Lablel_04 = ttk.Label(self, text="3. Light and Portable. Can even change stove location in regular basis?", font=NORMAL_FONT).grid(row=18, column=1, sticky=tk.W)

        # radio 1
        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=142, command=lambda: ob.set_x('a', 0, 'ASTHETIC_APPEAL')).grid(row=2, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=142, command=lambda: ob.set_x('b', 0, 'ASTHETIC_APPEAL')).grid(row=2, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=142, command=lambda: ob.set_x('c', 0, 'ASTHETIC_APPEAL')).grid(row=2, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=143, command=lambda: ob.set_x('a', 1, 'ASTHETIC_APPEAL')).grid(row=3, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=143, command=lambda: ob.set_x('b', 1, 'ASTHETIC_APPEAL')).grid(row=3, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=143, command=lambda: ob.set_x('c', 1, 'ASTHETIC_APPEAL')).grid(row=3, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=144, command=lambda: ob.set_x('a', 0, 'SAFETY')).grid(row=5, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=144, command=lambda: ob.set_x('b', 0, 'SAFETY')).grid(row=5, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=144, command=lambda: ob.set_x('c', 0, 'SAFETY')).grid(row=5, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=145, command=lambda: ob.set_x('a', 1, 'SAFETY')).grid(row=7, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=145, command=lambda: ob.set_x('b',1, 'SAFETY')).grid(row=7, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=145, command=lambda: ob.set_x('c', 1, 'SAFETY')).grid(row=7, column=5, sticky=tk.W)


        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=146, command=lambda: ob.set_x('a', 2, 'SAFETY')).grid(row=8, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=146, command=lambda: ob.set_x('b', 2, 'SAFETY')).grid(row=8, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=146, command=lambda: ob.set_x('c', 2, 'SAFETY')).grid(row=8, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=147, command=lambda: ob.set_x('a', 1, 'SAFETY')).grid(row=9, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=147, command=lambda: ob.set_x('b', 1, 'SAFETY')).grid(row=9, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=147, command=lambda: ob.set_x('c', 1, 'SAFETY')).grid(row=9, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=148, command=lambda: ob.set_x('a', 0, 'REGULAR_CLEANING')).grid(row=11, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=148, command=lambda: ob.set_x('b', 0, 'REGULAR_CLEANING')).grid(row=11, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=148, command=lambda: ob.set_x('c', 0, 'REGULAR_CLEANING')).grid(row=11, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=149, command=lambda: ob.set_x('a', 1, 'REGULAR_CLEANING')).grid(row=12, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=149, command=lambda: ob.set_x('b', 1, 'REGULAR_CLEANING')).grid(row=12, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=149, command=lambda: ob.set_x('c', 1, 'REGULAR_CLEANING')).grid(row=12, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=150, command=lambda: ob.set_xx('a', 2, 'REGULAR_CLEANING')).grid(row=13, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=150, command=lambda: ob.set_xx('b', 2, 'REGULAR_CLEANING')).grid(row=13, column=4, sticky=tk.W)
        radio3a = tk.Radiobutton(self, text='No Idea', value=3, variable=150, command=lambda: ob.set_xx('c', 2, 'REGULAR_CLEANING')).grid(row=13, column=5, sticky=tk.W)

        radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=151, command=lambda: self.box_add('a', 0, 'PORTABILITY', ob)).grid(row=15, column=3, sticky=tk.W)
        radio2a = tk.Radiobutton(self, text='No', value=2, variable=151, command=lambda: self.box_add('b', 0, 'PORTABILITY', ob)).grid(row=15, column=4, sticky=tk.W)





        button2 = ttk.Button(self, text='Back', command=lambda: controller.show_frame(UserP4))
        button2.grid(row=2214, column=3, sticky="nsew")
        button2 = ttk.Button(self, text='Next', command=lambda: self.next1())
        button2.grid(row=2214, column=5, sticky="nsew")

    def box_add(self, x, y, zz, ob):
        if zz == 'PORTABILITY' and y == 0 and x == 'a':
            radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=52, command=lambda: ob.set_xx('a', 0, 'PORTABILITY')).grid(row=16, column=3, sticky=tk.W)
            radio2a = tk.Radiobutton(self, text='No', value=2, variable=52, command=lambda: ob.set_xx('b', 0, 'PORTABILITY')).grid(row=16, column=4, sticky=tk.W)

            radio1a = tk.Radiobutton(self, text='Yes', value=1, variable=12, command=lambda: ob.set_x('a', 2, 'PORTABILITY')).grid(row=18, column=3, sticky=tk.W)
            radio2a = tk.Radiobutton(self, text='No', value=2, variable=12, command=lambda: ob.set_x('b', 2, 'PORTABILITY')).grid(row=18, column=4, sticky=tk.W)


        if zz == 'PORTABILITY' and y == 0 and x == 'b':
            Lablel_02 = ttk.Label(self, text="          ", font=NORMAL_FONT).grid(row=16, column=3, columnspan=2,
                                                                                                                                                                                          sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="          ", font=NORMAL_FONT).grid(row=16, column=4, columnspan=2,
                                                                                                                                                                                     sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="          ", font=NORMAL_FONT).grid(row=18, column=3, columnspan=2, sticky=tk.W)
            Lablel_03 = ttk.Label(self, text="          ", font=NORMAL_FONT).grid(row=18, column=4, columnspan=2, sticky=tk.W)


    def next1(self):
        self.controller.show_frame(Star)
        ob = SCORING_class_User()
        ob.print_all()







app = ICS_app()
#app.geometry('1024x768')


w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))

app.mainloop()

##Chimney_Stove = {'HP_TE': '>=20', 'SFC': '<=0.039',
##                 'TE_HP_P.M': ['<=41', '<=979'], 'TE_LP_P.M': ['<=1', '<=8'],
##                 'TE_HP_CO': ['<=8', '<=16'], 'TE_LP_CO': ['<=0.09', '<0.20'],
##                 'IE_PM': '<=5', 'IE_CO': '<=0.42'}
##Chimneyless_Stove = {'HP_TE': '>=25', 'SFC': '<=0.039',
##                     'TE_HP_P.M': '<=513', 'TE_LP_P.M': '<=4',
##                     'TE_HP_CO': '<=10', 'TE_LP_CO': '<0.0.09',
##                     'IE_PM': '<=40', 'IE_CO': '<=0.49'}
##
##Force_Draft_Stove = {'HP_TE': '>=35', 'SFC': '<=0.039',
##                     'TE_HP_P.M': '<=386', 'TE_LP_P.M': '<=4',
##                     'TE_HP_CO': '<=8', 'TE_LP_CO': '<0.0.09', 'IE_PM': '<=30',
##                     'IE_CO': '<=0.42'}
##Safety_assessment={Metallic body:>=45,'
##Percentile= {'High_Hill': [17.08,10.13,13.98,7.93,10.66,17.95,12.39,9.59,0.01,0.27,0.00,0.00],'Mid_Hill':[25.37,14.31,17.14,3.84,11.87,13.95,4.05,8.13,0.28,0.44,0.63,0.00]
##,'Central_Terai':[18.06,12.86,16.78,8.06,7.38,4.14,17.77,11.24,3.70,0.00,0.00,0.00],'Western Terai':[12.71,11.39,17.36,4.57,7.21,22.82,8.06,14.13,0.00,0.00,0.00,1.75]}
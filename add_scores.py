# List of all the contraceptives
import ast
import pandas as pd
contraceptives = ['condoms', 'internal_condoms', 'cervical_cap', 'FAM', 
                  'arm_implant', 'copper_iud', 'hormonal_iud', 'patch', 
                  'combo_pill', 'mini_pill', 'ring', 'shot', 'sterilizatoin', 'spermicide/vaginal_cream',
                  'withdrawal'] 

# Method Data list containing the correlations of contraceptices with various decision factors
method_data = [
    ['condoms', 1, 1, 1, 0.5, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0],
    ['internal condoms', 1, 1, 1, 0.5, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0.5, 0],
    ['cervical cap', 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0],
    ['FAM', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    ['arm implant', 1, 1, 0, 1, 1, -1, 0, 0, 0, 0, 1, 0, 1, 1, 1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    ['copper IUD', 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0],
    ['hormonal IUD', 1, 1, 0, 1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 1, -1, -1, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 0, 1, -1, 1, 0],
    ['patch', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 0, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['combo pill', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 0, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['mini pill', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 0, 1, 0, 1, 0, 1, -1, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 0, 1, 0, 0.5, 0],
    ['ring', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 1, 1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 0.5, -1],
    ['shot', 1, 1, 0, 0.5, 1, -1, 0, 0, 0, 0, 1, 0, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['sterilization', 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    ['spermicide/vaginal gel', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['withdrawal', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]
]

# Similar list in which the values get changed based on the user's answers. 
method_data_1 = [
    ['condoms', 1, 1, 1, 0.5, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0],
    ['internal condoms', 1, 1, 1, 0.5, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0.5, 0],
    ['cervical cap', 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0],
    ['FAM', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    ['arm implant', 1, 1, 0, 1, 1, -1, 0, 0, 0, 0, 1, 0, 1, 1, 1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    ['copper IUD', 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0],
    ['hormonal IUD', 1, 1, 0, 1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 1, -1, -1, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 0, 1, -1, 1, 0],
    ['patch', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 0, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['combo pill', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 0, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['mini pill', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 0, 1, 0, 1, 0, 1, -1, -1, 0, 0, 0, -1, 0, 0, 1, 1, 0, 0, 1, 0, 0.5, 0],
    ['ring', 1, 1, 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 1, 1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 0.5, -1],
    ['shot', 1, 1, 0, 0.5, 1, -1, 0, 0, 0, 0, 1, 0, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 0, 0.5, -1],
    ['sterilization', 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    ['spermicide/vaginal gel', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['withdrawal', 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]
]


# Choices available to users for all the pages
experience_with_method = [None, "negative", "neutral", "positive"]

user_method_again = ["no", "yes", "dont_know"]

cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 
management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 
weight_maintain = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
maintainence = ['daily', 'weekly', 'monthly', 'yearly']
willingness_of_partner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]

sti_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones = [None, 'progestin', 'estrogen_and_or_progestin']
willingess_to_insert_into_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingness_to_seek_consultion = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingess_to_undergo_procedure = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 

medical_conditions = [
    'acne', 'anxiety', 'depression', 'hypertension', 'blood_clots', 'CHFCAD', 
    'breast', 'smoker', 'migraine', 'PCOS', 'endo', 'top_gender_dysphoria', 
    'top_surgery', 'bottom_gender_dysphoria_periods', 'bottom_gender_dysphoria_vaginal_insertion', 
    'gender_dysphoria_pregnancy', 'HRT'
]


severity = ['mild', 'moderate', 'severe']

medical_history = ['migraine_with_aura', 
                   'smoker', 
                   'hypertension',
                   'blood_clots',
                   'CHF or CAD',
                   'PCOS',
                   'endometriosis',
                   'breast_cancer',
                   'hrt',
                   'top_surgery']

# Function that applies a score based on the user's answer and the index of the column
def apply_score(factor, user_ans):
    for i in range(len(method_data)):
        method_data_1[i][factor] = method_data[i][factor] * user_ans

# This function applies the multipliers to correlations for medical conditions page
def med_cond_score(a, b):
    for i in range(len(method_data)):
        # user has condition and method worsens conditions
        if method_data[i][a] < 0:
            method_data_1[i][a] = method_data[i][a] * b
        
        # user has condition and method betters conditions
        elif method_data[i][a] > 0:
            method_data_1[i][a] = method_data[i][a] * 3

method_experience = {}

# This function takes user input and applies the scores to the arrays
def get_user_input(array_csv):
    method_index = 0
    
    method_experience = {}
    for method in contraceptives:
        if method in array_csv[0]:
            used = 'yes'
        else:
            used = 'no'
        if used == "yes":
            experience = array_csv[1]
            consider_again = array_csv[2]  
            method_experience[method] = {"used": used, "experience": experience, "consider_again": consider_again}
            if experience == "negative":
                method_data_1[method_index][1] = method_data[method_index][1] * -8
            elif experience == "positive":
                method_data_1[method_index][1] = method_data[method_index][1] * 8
            else:
                method_data_1[method_index][1] = method_data[method_index][1] * 0
            
            if consider_again == "yes":
                method_data_1[method_index][2] = method_data[method_index][2] * 3
            elif consider_again == "no":
                method_data_1[method_index][2] = method_data[method_index][2] * -100
            else:
                method_data[method_index][2] = method_data[method_index][2] * 0

        else:
            method_experience[method] = {"used": used}
            method_data_1[method_index][1] = method_data[method_index][1] * 0
            method_data_1[method_index][2] = method_data[method_index][2] * 0
        method_index += 1

    preferences = ["Cost Effectiveness", "Pregnancy Prevention", "Management of Period and Side Effects",
                   "Low Chance of Weight Gain/Loss", "Maintenance of Birth Control", 
                   "Partner's Willingness to Participate in Contraception"]
    
    personal_preferences = {}

    for preference in preferences:
        if preference == "Cost Effectiveness":
            ceff_ans = array_csv[3]
            if ceff_ans == "v_unp":
                apply_score(3, -3)
            elif ceff_ans == "unp":
                apply_score(3, -2)
            elif ceff_ans == "sl_unp":
                apply_score(3, -1)
            elif ceff_ans == "neutral":
                apply_score(3, 0)
            elif ceff_ans == "sl_imp":
                apply_score(3, 1)
            elif ceff_ans == "imp":
                apply_score(3, 2)
            else:
                apply_score(3, 3)
        
        elif preference == "Pregnancy Prevention":
            pp_ans = array_csv[4] 
            if pp_ans == "v_unp":
                apply_score(4, -3)
            elif pp_ans == "unp":
                apply_score(4, -2)
            elif pp_ans == "sl_unp":
                apply_score(4, -1)
            elif pp_ans == "neutral":
                apply_score(4, 0)
            elif pp_ans == "sl_imp":
                apply_score(4, 1)
            elif pp_ans == "imp":
                apply_score(4, 2)
            else:
                apply_score(4, 3)
    
        elif preference == "Management of Period and Side Effects":
            mpse_ans = array_csv[5] 
            if mpse_ans == "v_unp":
                apply_score(5, -3)
            elif mpse_ans == "unp":
                apply_score(5, -2)
            elif mpse_ans == "sl_unp":
                apply_score(5, -1)
            elif mpse_ans == "neutral":
                apply_score(5, 0)
            elif mpse_ans == "sl_imp":
                apply_score(5, 1)
            elif mpse_ans == "imp":
                apply_score(5, 2)
            else:
                apply_score(5, 3)
    
        elif preference == "Low Chance of Weight Gain/Loss":
            lwgl_ans = array_csv[6]
            if lwgl_ans == "v_unp":
                apply_score(6, -3)
            elif lwgl_ans == "unp":
                apply_score(6, -2)
            elif lwgl_ans == "sl_unp":
                apply_score(6, -1)
            elif lwgl_ans == "neutral":
                apply_score(6, 0)
            elif lwgl_ans == "sl_imp":
                apply_score(6, 1)
            elif lwgl_ans == "imp":
                apply_score(6, 2)
            else:
                apply_score(6, 3) 
            
        elif preference == "Maintenance of Birth Control":
            mbc_ans = array_csv[7]
            if mbc_ans == 'daily':
                method_data_1[0][7] = 3

                method_data_1[1][7] = 3

                method_data_1[2][7] = 3

                method_data_1[3][7] = 3

                method_data_1[8][7] = 3

                method_data_1[9][7] = 3

                method_data_1[13][7] = 3

                method_data_1[14][7] = 3
            
            elif mbc_ans == 'weekly':
                method_data_1[7][7] = 3

            elif mbc_ans == 'monthly':

                method_data_1[10][7] = 3
                
                method_data_1[11][7] = 3
            
            else:
                method_data_1[4][7] = 3

                method_data_1[5][7] = 3

                method_data_1[6][7] = 3
        
        elif preference == "Partner's Willingness to Participate in Contraception":
            pwpc_ans = array_csv[8]
            if pwpc_ans == "v_unp":
                apply_score(8, -3)
            elif pwpc_ans == "unp":
                apply_score(8, -2)
            elif pwpc_ans == "sl_unp":
                apply_score(8, -1)
            elif pwpc_ans == "neutral":
                apply_score(8, 0)
            elif pwpc_ans == "sl_imp":
                apply_score(8, 1)
            elif pwpc_ans == "imp":
                apply_score(8, 2)
            else:
                apply_score(8, 3)


            
        else:
            pass

    medical_preferences = ["STI Prevention", "Hormones Used", "Willing to Insert Foreign Object Into Vagina",
                           "Willing to Seek Consultation by a Medical Professional", 
                           "Willing to Undergo a Medical Procedure"]
    
    medical_pref = {}
    for preference in medical_preferences:
        if preference == "STI Prevention":
            sti_ans = array_csv[9]
            if sti_ans == "v_unp":
                apply_score(9, -3)
            elif sti_ans == "unp":
                apply_score(9, -2)
            elif sti_ans == "sl_unp":
                apply_score(9, -1)
            elif sti_ans == "neutral":
                apply_score(9, 0)
            elif sti_ans == "sl_imp":
                apply_score(9, 1)
            elif sti_ans == "imp":
                apply_score(9, 2)
            else:
                apply_score(9, 3)
        elif preference == "Hormones Used":
            horm_ans = array_csv[10]
            value = None
            if horm_ans == 'estrogen_and_or_progestin':
                value = 4
            elif horm_ans == 'progestin':
                value = 2
            elif horm_ans == 'none':
                value = 1
            
            i = 0
            while i < 15:
                if ((method_data[i][10] == 1 and method_data[i][11] == 1) and value == 4):
                    apply_score(10, 1.5)
                    apply_score(11, 1.5)
                elif ((method_data[i][10] == 1 or method_data[i][11] == 1) and value ==4):
                    apply_score(10, 3)
                    apply_score(11, 3)
                elif ((method_data[i][10] == 1 and method_data[i][11] == 0) and value == 3):
                    apply_score(10, 3)
                elif ((method_data[i][10] == 0 and method_data[i][11] == 1) and value == 2):
                    apply_score(11, 3)
                elif ((method_data[i][10] == 0 and method_data[i][11] == 0) and value == 1):
                    method_data_1[i][10] = 3
                    method_data_1[i][11] = 3
                else:
                    method_data_1[i][10] = 0
                    method_data_1[i][11] = 0
                i += 1

        elif preference == "Willing to Insert Foreign Object Into Vagina":
            insert_vag_ans = array_csv[11]
            if insert_vag_ans == "v_unp":
                apply_score(12, -3)
            elif insert_vag_ans == "unp":
                apply_score(12, -2)
            elif insert_vag_ans == "sl_unp":
                apply_score(12, -1)
            elif insert_vag_ans == "neutral":
                apply_score(12, 0)
            elif insert_vag_ans == "sl_imp":
                apply_score(12, 1)
            elif insert_vag_ans == "imp":
                apply_score(12, 2)
            else:
                apply_score(12, 3)
        elif preference == "Willing to Seek Consultation by a Medical Professional":
            med_prof_ans = array_csv[12]
            if med_prof_ans == "v_unp":
                apply_score(13, -3)
            elif med_prof_ans == "unp":
                apply_score(13, -2)
            elif med_prof_ans == "sl_unp":
                apply_score(13, -1)
            elif med_prof_ans == "neutral":
                apply_score(13, 0)
            elif med_prof_ans == "sl_imp":
                apply_score(13, 1)
            elif med_prof_ans == "imp":
                apply_score(13, 2)
            else:
                apply_score(13, 3)
        elif preference ==  "Willing to Undergo a Medical Procedure":
            med_proc_ans = array_csv[13]
            if med_proc_ans == "v_unp":
                apply_score(14, -3)
            elif med_proc_ans == "unp":
                apply_score(14, -2)
            elif med_proc_ans == "sl_unp":
                apply_score(14, -1)
            elif med_proc_ans == "neutral":
                apply_score(14, 0)
            elif med_proc_ans == "sl_imp":
                apply_score(14, 1)
            elif med_proc_ans == "imp":
                apply_score(14, 2)
            else:
                apply_score(14, 3) 

        else:
            pass
    
    # medical_conditions = ['acne', 'anxiety', 'depression', 'top_gender_dsyphoria', 
                     # 'bottom_gender_dysphoria_periods', 'bottom_gender_dysphoria_vaginal_insertion',
                     # 'gender_dysphoria_pregnancy'] 
   
    anxiety_exists = None
    depression_exists = None
    for condition in medical_conditions:
        
        if condition in array_csv[14] or condition in array_csv[16]:
            condition_exists = "yes"
        else:
            condition_exists = "no"
        if condition_exists == "yes":
            if condition == "acne":
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(15, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(15, 25)
                else:
                    med_cond_score(15, 50)
            elif condition == "anxiety":
                anxiety_exists = True
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(16, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(16, 25)
                else:
                    med_cond_score(16, 50)
            elif condition == "depression":
                depression_exists = True
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(17, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(17, 25)
                else:
                    med_cond_score(17, 50)
            elif condition == "hypertension":
                med_cond_score(18, 100)
            
            elif condition == "blood_clots":
                med_cond_score(19, 100)
            elif condition == "CHFCAD":
                med_cond_score(20, 100)
            elif condition == "breast":
                med_cond_score(21, 100)
            elif condition == "smoker":
                med_cond_score(22, 100)
            elif condition == "migraine":
                med_cond_score(23, 100)
            elif condition == "PCOS":
                med_cond_score(24, 100)
            elif condition == "endo":
                med_cond_score(25, 100)

            elif condition == "top_gender_dysphoria":
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(26, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(26, 25)
                else:
                    med_cond_score(26, 50)
            
            elif condition == "top_surgery":
                med_cond_score(27, 100)
            elif condition == "bottom_gender_dysphoria_periods":
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(28, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(28, 25)
                else:
                    med_cond_score(28, 50)
            elif condition == "bottom_gender_dysphoria_vaginal_insertion":
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(29, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(29, 25)
                else:
                    med_cond_score(29, 50)
            elif condition == "gender_dysphoria_pregnancy":
                condition_sev = array_csv[15]
                if condition_sev == 'mild':
                    med_cond_score(30, 15)
                elif condition_sev == 'moderate':
                    med_cond_score(30, 25)
                else:
                    med_cond_score(30, 50)
            elif condition == "HRT":
                med_cond_score(31, 100)
        else:
            if condition == 'acne':
                apply_score(15, 0)
            elif condition == 'anxiety':
                apply_score(16, 0)
            elif condition == 'depression':
                apply_score(17, 0)
            elif condition == 'hypertension':
                apply_score(18, 0)
            elif condition == 'blood_clots':
                apply_score(19, 0)
            elif condition == 'CHFCAD':
                apply_score(20, 0)
            elif condition == 'breast':
                apply_score(21, 0)
            elif condition == 'smoker':
                apply_score(22, 0)
            elif condition == 'migraine':
                apply_score(23, 0)
            elif condition == 'PCOS':
                apply_score(24, 0)
            elif condition == 'endo':
                apply_score(25, 0)
            elif condition == 'top_gender_dysphoria':
                apply_score(26, 0)
            elif condition == 'top_surgery':
                apply_score(27, 0)
            elif condition == 'bottom_gender_dysphoria_periods':
                apply_score(28, 0)
            elif condition == 'bottom_gender_dysphoria_vaginal_insertion':
                apply_score(29, 0)
            elif condition == 'gender_dysphoria_pregnancy':
                apply_score(30, 0)
            elif condition == 'HRT':
                apply_score(31, 0)
    if anxiety_exists and depression_exists:

        for method in method_data_1:
            if method[17] < 0:
                method[17] *= 0.5
            elif method[17] > 0:
                pass
            else:
                pass

            if method[16] < 0:
                method[16] *= 0.5
            elif method[16] > 0:
                pass
            else:
                pass



df = pd.read_csv('contraceptive_combinations.csv', header=None)

# Store each column in a variable
column1 = df.iloc[0].to_list()
print(column1)
# Getting user input
arr = column1
get_user_input(arr)
#print(method_data_1)

# Summing up all the values in the array and adding the data to an array named sums
sums = []
for contraceptive in method_data_1:
    # Calculate the sum of the values (excluding the first element which is the name)
    total = sum(contraceptive[1:])
    # Append the sum to the sums list
    sums.append((contraceptive[0], total))


# Sorting the final scores in reverse order
sums.sort(key=lambda x:x[1], reverse=True)

# print(method_data_1)
# Printing out the results
for i in sums:
    print(i)
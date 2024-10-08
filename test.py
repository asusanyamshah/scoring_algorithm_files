import pandas as pd
from return_scores import get_user_input

# Define the arrays
contraceptives = [['condoms'], ['internal_condoms'], ['cervical_cap'], ['FAM'], 
                  ['arm_implant'], ['copper_iud'], ['hormonal_iud'], ['patch'], 
                  ['combo_pill'], ['mini_pill'], ['ring'], ['shot'], ['sterilization'], 
                  ['spermicide/vaginal_cream'], ['withdrawal']]

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

experience_with_method = ["negative", "neutral", "positive"]
user_method_again = ["no", "yes", "dont_know"]

cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
weight_maintain = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
maintainence = ['daily', 'weekly', 'monthly', 'yearly']
willingness_of_partner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]

sti_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones = ['none', 'progestin', 'estrogen_and_or_progestin']
willingess_to_insert_into_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingness_to_seek_consultion = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingess_to_undergo_procedure = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]

medical_conditions = [['none'], ['acne'], ['anxiety'], ['depression'],
                      ['top_gender_dysphoria'], 
                      ['bottom_gender_dysphoria_periods'], ['bottom_gender_dysphoria_vaginal_insertion'], 
                      ['gender_dysphoria_pregnancy']]

medical_history = [['migraine_with_aura'], ['smoker'], ['hypertension'], ['blood_clots'], 
                   ['CHF or CAD'], ['PCOS'], ['endometriosis'], ['breast_cancer'], 
                   ['hrt'], ['top_surgery']]

severity = ['mild', 'moderate', 'severe']

headers = ["contraceptive", "exp", "again", "cost", "preg", "manage", "weight", "maint", "partner", "sti", "hormone", "insert", "consult", "procedure", "condition", "sev", "history"]
column_names = []
for i in headers:
    column_names.append(i.upper())
# Function to generate combinations and write to Excel

def generate_combinations_to_excel(filename):
    with open(filename, 'w') as f:
        row = 0
        
        for contraceptive in contraceptives:
            for exp in experience_with_method:
                for again in user_method_again:
                    for cost in cost_effectiveness:
                        for preg in pregnancy_prevention:
                            for manage in management:
                                for weight in weight_maintain:
                                    for maint in maintainence:
                                        for partner in willingness_of_partner:
                                            for sti in sti_prevention:
                                                for hormone in hormones:
                                                    for insert in willingess_to_insert_into_vagina:
                                                        for consult in willingness_to_seek_consultion:
                                                            for procedure in willingess_to_undergo_procedure:
                                                                for condition in medical_conditions:
                                                                    for sev in severity:
                                                                        for history in medical_history:
                                                                            data = [contraceptive, exp, again, cost, preg, manage, weight, maint, partner,
                                                                                    sti, hormone, insert, consult, procedure, condition, sev, history]
                                                                            scores = get_user_input(data)
                                                                            data.append(scores)
                                                                            df = pd.DataFrame([data])
                                                                            df.to_csv(f, index=False, header=False)
                                                                            row += 1
                                                                            
                                                                            # Write in batches of 10000 rows
                                                                            '''
                                                                            if row % 100000 == 0:
                                                                                return
                                                                                print(f"Processed {row} combinations")
                                                                            '''

    print(f"All combinations written to {filename}")

# Generate combinations and write to Excel
generate_combinations_to_excel('contraceptive_combinations.csv')
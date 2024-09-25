import itertools

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Basic function used in this code:

'''
1. itertools.permutations(array, number): It will take an array, and a number as an input. 
It will generate all the possible perutations of that array of length n. Some values may be duplicated for example:
(a, b)
(b, a)

2. itertoold.combinations(array, number): It will take an array, and a number as an input. 
It will generate all the possible combinations of that array of length n. The only difference between this function and the permutations 
function is that values are not duplicated here. 
If there is (a, b), there won't be (b, a)

3. itertools.product(array1, array2, .....): It will take multiple arrays, and will calculate all the permutations of the combinations of
array1, array2, array3, ......
In other words, it calculates the cartesian product of the inputs. 
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Method history combinations
contraceptives = ['condoms', 'internal_condoms', 'cervical_cap', 'FAM', 
                  'arm_implant', 'copper_iud', 'hormonal_iud', 'patch', 
                  'combo_pill', 'mini_pill', 'ring', 'shot', 'sterilization', 
                  'spermicide/vaginal_cream', 'withdrawal']

# Create a new list to store all combinations
all_combinations = []

# Generate and add combinations
for i in range(1, len(contraceptives) + 1):
    combinations = list(itertools.combinations(contraceptives, i))
    for combo in combinations:
        all_combinations.append(list(combo))

experience_with_method = [None, "negative", "neutral", "positive"]

user_method_again = ["no", "yes", "dont_know"]

method_history_prod = []
for comb in all_combinations:
    prod = list(itertools.product(comb, user_method_again, experience_with_method))
    method_history_prod.append(prod)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Personal Preferances combinations
cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 
management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 
weight_maintain = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
maintainence = ['daily', 'weekly', 'monthly', 'yearly']
willingness_of_partner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]

personal_pref_combinations = list(itertools.product(cost_effectiveness, pregnancy_prevention, management, weight_maintain, maintainence, willingness_of_partner))


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Medical Preferences combinations
sti_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones = [None, 'progestin', 'estrogen_and_or_progestin']
willingess_to_insert_into_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingness_to_seek_consultion = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
willingess_to_undergo_procedure = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"] 

medical_pref_combinations = list(itertools.product(sti_prevention, hormones, willingess_to_insert_into_vagina, willingness_to_seek_consultion, willingess_to_undergo_procedure))

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Medical Conditions combinations
medical_conditions = ['None',
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

medical_conditions_all = []
for i in range(1, len(medical_history) + 1):
    combinations = list(itertools.combinations(medical_conditions, i))
    for combo in combinations:
        medical_conditions_all.append(list(combo))

product_all = list(itertools.product(medical_conditions_all, severity, medical_history))



# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Total combinations

all_combinations = list(itertools.product(method_history_prod, personal_pref_combinations, medical_pref_combinations, product_all))
import pandas as pd
import itertools

# Data for permutations
contraceptives = [['ring']]
cost_effectiveness = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
pregnancy_prevention = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
management_of_periods = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
weight_management = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
hormones_used = ['ep', 'p', 'none']
willingness_vagina = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
medical_practitioner = ['v_unp', 'unp', 'sl_unp', 'neutral', 'sl_imp', 'imp', "v_imp"]
acne = ['no', 'mild', 'moderate', 'severe']
anxiety = ['no', 'mild', 'moderate', 'severe']
depression = ['no', 'mild', 'moderate', 'severe']
hyper = ['no', 'yes']
bclots = ['no', 'yes']
chf_cad = ['no', 'yes']
breast = ['no', 'yes']
smoker = ['no', 'yes']
migraine = ['no', 'yes']
pcos = ['no', 'yes']
endmt = ['no', 'yes']
tgd = ['no', 'mild', 'moderate', 'severe']
ts = ['no', 'yes']
bgdper = ['no', 'mild', 'moderate', 'severe']
gd_vaginal_insertion = ['no', 'mild', 'moderate', 'severe']
gdp = ['no', 'mild', 'moderate', 'severe']
hrt = ['no', 'yes']

# Generate all combinations using itertools
all_options = list(itertools.product(
    contraceptives, cost_effectiveness, management_of_periods, weight_management, hormones_used,
    willingness_vagina, medical_practitioner, acne, anxiety, depression, hyper, bclots, chf_cad, breast,smoker, migraine
    ,pcos, endmt, tgd,
    ts, bgdper, gd_vaginal_insertion, gdp, hrt
))

print("Done")

'''
# ['ring', 1, 0.5, 1, -1, 0, 0, 0, 1, 1, 1, 1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 0.5, -1],
def scoring_ring(arr):
    ring_score = 3
    if arr[1] == "v_unp":
        ring_score -= 3
    elif arr[1] == "unp":
        ring_score -= 2
    elif arr[1] == "sl_unp":
        ring_score -= 1
    elif arr[1] == "neutral":
        pass
    elif arr[1] == "sl_imp":
        ring_score += 1
    elif arr[1] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    if arr[2] == "v_unp":
        ring_score -= 1.5
    elif arr[2] == "unp":
        ring_score -= 1
    elif arr[2] == "sl_unp":
        ring_score -= 0.5
    elif arr[2] == "neutral":
        pass
    elif arr[2] == "sl_imp":
        ring_score += 0.5
    elif arr[2] == "imp":
        ring_score += 1
    else:
        ring_score += 1.5
    
    if arr[3] == "v_unp":
        ring_score -= 3
    elif arr[3] == "unp":
        ring_score -= 2
    elif arr[3] == "sl_unp":
        ring_score -= 1
    elif arr[3] == "neutral":
        pass
    elif arr[3] == "sl_imp":
        ring_score += 1
    elif arr[3] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    if arr[4] == "v_unp":
        ring_score += 3
    elif arr[4] == "unp":
        ring_score += 2
    elif arr[4] == "sl_unp":
        ring_score += 1
    elif arr[4] == "neutral":
        pass
    elif arr[4] == "sl_imp":
        ring_score -= 1
    elif arr[4] == "imp":
        ring_score -= 2
    else:
        ring_score -= 3
    
    if arr[6] == "v_unp":
        ring_score -= 3
    elif arr[6] == "unp":
        ring_score -= 2
    elif arr[6] == "sl_unp":
        ring_score -= 1
    elif arr[6] == "neutral":
        pass
    elif arr[6] == "sl_imp":
        ring_score += 1
    elif arr[6] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    if arr[5] == 'ep':
        ring_score += 3
    
    if arr[7] == "v_unp":
        ring_score -= 3 
    elif arr[7] == "unp":
        ring_score -= 2
    elif arr[7] == "sl_unp":
        ring_score -= 1
    elif arr[7] == "neutral":
        pass
    elif arr[7] == "sl_imp":
        ring_score += 1
    elif arr[7] == "imp":
        ring_score += 2
    else:
        ring_score += 3
    
    if arr[8] == 'no':
        pass
    elif arr[8] == 'mild' or arr[8] == 'moderate' or arr[8] == 'severe':
        ring_score += 3
    
    if arr[9] == 'no':
        pass
    elif arr[9] == 'mild':
        ring_score -= 15
    elif arr[9] == 'moderate':
        ring_score -= 25
    else:
        ring_score -= 50
    
    if arr[10] == 'no':
        pass
    
    elif arr[10] == 'mild':
        ring_score -= 10

    
    
    


num = 0
for i in all_options:
    score = scoring_ring(i)
    all_options[num] = all_options[num] + (score, )

df = pd.DataFrame(all_options)
df.to_csv('ring_combinations.csv', index=False, header=False)
'''
import pandas as pd

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

questions_condoms = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5, 
    "Partner's Willingness": 1, "STI Prevention": 1, 
    "Gender Dysphoria Pregnancy": 0.5
}

questions_internal_condoms = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5,
    "Prevents STI": 1, "Vaginal Insertion": 1,
    "Bottom gender dysphoria vaginal insertion": -1, "Bottom gender dysphoria pregnancy": 0.5
}

questions_cervical_cap = {
    "Cost Effectiveness": 1, "Vaginal insertion": 1,
    "Seeking consultation": 1, "Bottom gender dysphoria vaginal insertion": -1, 
    "Bottom gender dysphoria pregnancy": -1 
}

questions_fam = {
    "Cost Effectiveness": 1, "Partner's Willingness": 1,
    "Bottom gender dysphoria pregnancy": -1
}

questions_arm_implant = {
    "Pregnancy Prevention": 1,
    "Lessens Periods": 1, "Maintains Weight": -1,
    "Progestogen": 1,
    "Seeking Consultation": 1, "Medical Procedure Required": 1,
    "Acne": 1, "Anxiety": -1, "Depression": -1,
    "Bottom gender dysphoria period": 1, "Bottom Gender dysphoria pregnancy": 1
}

questions_copper_iud = {
    "Pregnancy Prevention": 1,
    "Vaginal Insertion": 1, "Seeking Consultation": 1,
    "Medical Procedure Required": 1, "Bottom gender dysphoria period": -1,
    "Bottom gender dysphoria vaginal Insertion": -1, "Bottom Gender dysphoria pregnancy": 1
}

questions_hormonal_iud = {
    "Pregnancy Prevention": 1,
    "Lessens Periods": 1, "Maintains Weight": -1,
    "Progestogen": 1, 
    "Vaginal Insertion": 1, "Seeking Consultation": 1,
    "Medical Procedure Required": 1,
    "Acne": -1, "Anxiety": -1, "Depression": -1,
    "History of Breast cancer": -1, "PCOS": 1,
    "Endometriosis": 1, "Bottom gender dysphoria period": 1,
    "Bottom gender dysphoria vaginal Insertion": -1, "Bottom Gender dysphoria pregnancy": 1
}

questions_patch = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5,
    "Lessens Periods": 1, "Maintains Weight": -1,
     "Hormones Used: Estrogen": 1,
    "Hormones Used: Progestogen": 1,
    "Seeking Consultation": 1, "Acne": -1,
    "Anxiety": -1, "Depression": -1, "Hypertension": -1,
    "Blood Clots": -1, "History of CHF or CAD": -1,
    "History of Breast cancer": -1, "Smoker over 35 years old": -1,
    "Migraine with aura": -1, "PCOS": 1, "Endometriosis": 1,
    "Top Gender Dysphoria": -1, "Top Surgery": -1,
    "Bottom gender dysphoria period": 1, "Bottom Gender dysphoria pregnancy": 0.5,
    "HRT": -1
}

questions_combo_pill = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5,
    "Lessens Periods": 1, "Maintains Weight": -1,
    "Hormones Used: Estrogen": 1,
    "Hormones Used: Progestogen": 1, "Seeking Consultation": 1,
    "Acne": -1, "Anxiety": -1,
    "Depression": -1, "Hypertension": -1,
    "Blood Clots": -1, "History of CHF or CAD": -1,
    "History of Breast cancer": -1, "Smoker over 35 years old": -1,
    "Migraine with aura": -1, "PCOS": 1, "Endometriosis": 1,
    "Bottom gender dysphoria period": 1, "Bottom Gender dysphoria pregnancy": 0.5,
    "HRT": -1
}

questions_mini_pill = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5,
    "Lessens Periods": 1, "Maintains Weight": -1,
     "Hormones Used: Progestogen": 1, "Seeking Consultation": 1, 
     "Acne": 1, "Anxiety": -1, "Depression": -1,
    "History of Breast cancer": -1, "PCOS": 1,
    "Endometriosis": 1, "Bottom gender dysphoria period": 1,
    "Bottom Gender dysphoria pregnancy": 0.5
}

questions_ring = {
    "Cost Effectiveness": 1, "Pregnancy Prevention": 0.5,
    "Lessens Periods": 1, "Maintains Weight": -1,
    "Hormones Used: Estrogen": 1, "Hormones Used: Progestogen": 1,
    "Vaginal Insertion": 1, "Seeking Consultation": 1,
    "Acne": 1, "Anxiety": -1, "Depression": -1,
    "Hypertension": -1, "Blood Clots": -1, "History of CHF or CAD": -1,
    "History of Breast cancer": -1, "Smoker over 35 years old": -1,
    "Migraine with aura": -1, "PCOS": 1, "Endometriosis": 1,
    "Top gender dysphoria": -1, "Top Surgery": -1,
    "Bottom gender dysphoria period": 1, "Bottom gender dysphoria vaginal Insertion": -1,
    "Bottom Gender dysphoria pregnancy": 0.5, "HRT": -1
}

questions_shot = {
    "Pregnancy Prevention": 0.5,
    "Lessens Periods": 1, "Maintains Weight": -1,
    "Hormones Used: Progestogen": 1, "Seeking Consultation": 1, 
    "Medical Procedure Required": 1, "Acne": 1,
    "Anxiety": -1, "Depression": -1, "Hypertension": -1,
    "Blood Clots": -1, "History of CHF or CAD": -1,
    "History of Breast cancer": -1, "Smoker over 35 years old": -1,
    "Migraine with aura": -1, "PCOS": 1, "Endometriosis": 1,
    "Top gender dysphoria": -1, "Top surgery": -1,
    "Bottom gender dysphoria period": 1, "Bottom Gender dysphoria pregnancy": 0.5,
    "HRT": -1
}

questions_sterilization = {
    "Pregnancy Prevention": 1, "Lessens Periods": 1,
    "Seeking Consultation": 1, "Medical Procedure Required": 1,
    "PCOS": 1, "Endometriosis": 1, "Bottom gender dysphoria period": 1,
    "Bottom Gender dysphoria pregnancy": 1
}

questions_spermicide_vaginal_gel = {
    "Cost Effectiveness": 1, "Partner's Willingness": 1, 
    "Vaginal Insertion": 1,
    
}

questions_withdrawal = {
    "Cost Effectiveness": 1, "Partner's Willingness": 1,
    "Bottom Gender dysphoria pregnancy": -1
}

# Create a dictionary to store all the questions for each method
all_questions = {
    'condoms': questions_condoms,
    'internal condoms': questions_internal_condoms,
    'cervical cap': questions_cervical_cap,
    'FAM': questions_fam,
    'arm implant': questions_arm_implant,
    'copper IUD': questions_copper_iud,
    'hormonal IUD': questions_hormonal_iud,
    'patch': questions_patch,
    'combo pill': questions_combo_pill,
    'mini pill': questions_mini_pill,
    'ring': questions_ring,
    'shot': questions_shot,
    'sterilization': questions_sterilization,
    'spermicide/vaginal gel': questions_spermicide_vaginal_gel,
    'withdrawal': questions_withdrawal
}

columns = ['Method', 'Previously Used', 'Good or Bad experience', 'Cost Effectiveness', 
           'Pregnancy Prevention', 'Lessens Periods', 'Maintains Weight', 'Maintenance', 
           'Willingness', 'Prevents STI', 'Hormones Used: Estrogen', 'Hormones Used: Progestogen', 
           'Vaginal Insertion', 'Seeking Consultation', 'Medical Procedure Required', 
           'Acne', 'Anxiety', 'Depression', 'Hypertension', 'Blood Clots', 'History of CHF or CAD', 
           'History of Breast cancer', 'Smoker over 35 years old', 'Migraine with aura', 
           'PCOS', 'Endometriosis', 'Top Gender dysphoria', 'Top surgery', 
           'Bottom gender dysphoria period', 'Bottom gender dysphoria vaginal Insertion', 
           'Bottom Gender dysphoria pregnancy', 'HRT']


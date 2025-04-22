from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define network structure
model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

# Define CPDs
cpd_disease = TabularCPD(
    variable='Disease', variable_card=2,
    values=[[0.3], [0.7]],
    state_names={'Disease': ['Flu', 'Cold']}
)

cpd_fever = TabularCPD(
    variable='Fever', variable_card=2,
    values=[
        [0.9, 0.5],  # P(Fever=Yes | Disease)
        [0.1, 0.5]   # P(Fever=No | Disease)
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fever': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_cough = TabularCPD(
    variable='Cough', variable_card=2,
    values=[
        [0.8, 0.6],  # P(Cough=Yes | Disease)
        [0.2, 0.4]   # P(Cough=No | Disease)
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Cough': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_fatigue = TabularCPD(
    variable='Fatigue', variable_card=2,
    values=[
        [0.7, 0.3],  # P(Fatigue=Yes | Disease)
        [0.3, 0.7]   # P(Fatigue=No | Disease)
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fatigue': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

cpd_chills = TabularCPD(
    variable='Chills', variable_card=2,
    values=[
        [0.6, 0.4],  # P(Chills=Yes | Disease)
        [0.4, 0.6]   # P(Chills=No | Disease)
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Chills': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

# Add CPDs to model
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)

# Verify model
assert model.check_model()

# Perform inference
infer = VariableElimination(model)

# Inference Task 1: P(Disease | Fever=Yes, Cough=Yes)
result1 = infer.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print("P(Disease | Fever=Yes, Cough=Yes):")
print(result1)

# Inference Task 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
result2 = infer.query(variables=['Disease'], evidence={
    'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'
})
print("\nP(Disease | Fever=Yes, Cough=Yes, Chills=Yes):")
print(result2)

# Inference Task 3: P(Fatigue=Yes | Disease=Flu)
# This is directly from the CPD:
print("\nP(Fatigue=Yes | Disease=Flu): 0.7")

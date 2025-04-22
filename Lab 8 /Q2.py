from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_intelligence = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'Intelligence': ['High', 'Low']}
)

cpd_studyhours = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

cpd_difficulty = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'Difficulty': ['Hard', 'Easy']}
)

cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        # A, B, C
        [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.4, 0.3],
        [0.08, 0.15, 0.2, 0.25, 0.3, 0.3, 0.3, 0.3],
        [0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.3, 0.4],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],
        [0.05, 0.20, 0.50],
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

assert model.check_model()

# noinspection PyTypeChecker
infer = VariableElimination(model)

query1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
print("\nP(Pass | StudyHours=Sufficient, Difficulty=Hard):\n", query1)

query2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass': 'Yes'}
)
print("\nP(Intelligence = High | Pass=Yes):\n", query2)

def get_patient_health(inputs):
    # Define your rules for patient health here
    if inputs['fever'] > 100:
        if inputs['cough'] == 'yes':
            if inputs['breathing'] == 'difficult':
                return 'critical'
            else:
                if inputs['fatigue'] == 'yes':
                    if inputs['nausea'] == 'yes':
                        return 'unhealthy'
                    else:
                        return 'caution'
                else:
                    return 'mild'
        else:
            return 'unknown'
    else:
        return 'healthy'

# Prompt user for input
print('Enter patient symptoms:')
fever = float(input('Fever (in Fahrenheit): '))
cough = input('Cough (yes/no): ')
breathing = input('Breathing (normal/difficult): ')
fatigue = input('Fatigue (yes/no): ')
nausea = input('Nausea/vomiting (yes/no): ')
headache = input('Headache (yes/no): ')
sore_throat = input('Sore throat (yes/no): ')

# Create input data dictionary
input_data = {
    'fever': fever,
    'cough': cough,
    'breathing': breathing,
    'fatigue': fatigue,
    'nausea': nausea,
    'headache': headache,
    'sore_throat': sore_throat
}

# Get health status for patient
patient_health = get_patient_health(input_data)

# Print health status
if patient_health == 'healthy':
    print('Patient health: Healthy')
elif patient_health == 'unknown':
    print('Patient health: Unknown')
else:
    print('Patient health: Potentially {} - seek medical advice'.format(patient_health))

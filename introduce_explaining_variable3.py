# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    technique = time * temperature * pressure * COOKED_CONSTANT
    if desired_state == 'well-done' and technique >= WELL_DONE:
        print('Well Done')
        return True
    if desired_state == 'medium' and technique >= MEDIUM:
        print('medium')
        return True
    return False

well_done = 'well-done'
is_cookeding_criteria_satisfied(10,900000,5,well_done)
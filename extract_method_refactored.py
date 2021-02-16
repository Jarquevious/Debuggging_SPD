import math 


def create_grades_list():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
        
    return grade_list

def calculate_mean():
    
    # Calculate the mean and standard deviation of the grades
    sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    mean = sum / len(grade_list)
    return mean 

def calculate_standard_deviation():
    
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    mean = calculate_mean()
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd
 
def print_grade_stats():
    mean = calculate_mean()
    sd = calculate_standard_deviation()
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

grade_list = create_grades_list()
print_grade_stats()


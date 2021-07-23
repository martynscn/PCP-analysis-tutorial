# importing modulesneccesary libraries
import os
import load_dataset_module as dataset
import importlib
import csv
activity_features = dataset.Activity_Features()


def mean(activity_data):
    'function for computing the mean of each sensor readings'
    for keys in activity_data:
        mean_orientation_Xi = sum(activity_data[keys][:3]) / len(activity_data[keys][:3])
        mean_rotation_Xi = sum(activity_data[keys][3:6]) / len(activity_data[keys][3:6])
        mean_accelerometer_Xi = sum(activity_data[keys][6:9]) / len(activity_data[keys][6:9])
        mean_gyroscope_Xi = sum(activity_data[keys][9:12]) / len(activity_data[keys][9:12])
        mean_magnetic_Xi = sum(activity_data[keys][12:15]) / len(activity_data[keys][12:15])
        
        activity_features[keys].update({'id':keys, 'orMean':mean_orientation_Xi, 'rMean':mean_rotation_Xi, 'accMean':mean_accelerometer_Xi,
        'gMean':mean_gyroscope_Xi,'MagMean':mean_magnetic_Xi,'Activity':activity_data[keys][-1]})       # Here -1 is the Last column
    return activity_features

def variance(activity_data):
    'function for computing the variance of each sensor readings'
    for keys in activity_data:
        mean_orientation_Xi = sum(activity_data[keys][:3]) / len(activity_data[keys][:3])
        mean_rotation_Xi = sum(activity_data[keys][3:6]) / len(activity_data[keys][3:6])
        mean_accelerometer_Xi = sum(activity_data[keys][6:9]) / len(activity_data[keys][6:9])
        mean_gyroscope_Xi = sum(activity_data[keys][9:12]) / len(activity_data[keys][9:12])
        mean_magnetic_Xi = sum(activity_data[keys][12:15]) / len(activity_data[keys][12:15]) 
        
        var_orientation = sum([(x - mean_orientation_Xi) **2 for x in activity_data[keys][:3]]) / len(activity_data[keys][:3])
        var_rotation = sum([(x - mean_rotation_Xi) **2 for x in activity_data[keys][3:6]]) / len(activity_data[keys][3:6])
        var_accelerometer = sum([(x - mean_accelerometer_Xi) **2 for x in activity_data[keys][6:9]]) / len(activity_data[keys][6:9])
        var_gyroscope = sum([(x - mean_gyroscope_Xi) **2 for x in activity_data[keys][9:12]]) / len(activity_data[keys][9:12])
        var_magnetic = sum([(x - mean_magnetic_Xi) **2 for x in activity_data[keys][12:15]]) / len(activity_data[keys][12:15])
        
        activity_features[keys].update({'id':keys, 'orVar':var_orientation, 'rVar':var_rotation, 'accVar':var_accelerometer,
        'gVar':var_gyroscope,'MagVar':var_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features

def std_deviation(activity_data):
    'function for computing the standard deviation of each sensor readings'
    for keys in activity_data:    
        mean_orientation_Xi = sum(activity_data[keys][:3]) / len(activity_data[keys][:3])
        mean_rotation_Xi = sum(activity_data[keys][3:6]) / len(activity_data[keys][3:6])
        mean_accelerometer_Xi = sum(activity_data[keys][6:9]) / len(activity_data[keys][6:9])
        mean_gyroscope_Xi = sum(activity_data[keys][9:12]) / len(activity_data[keys][9:12])
        mean_magnetic_Xi = sum(activity_data[keys][12:15]) / len(activity_data[keys][12:15]) 
        
        std_orientation = (sum([(x - mean_orientation_Xi) **2 for x in activity_data[keys][:3]]) / len(activity_data[keys][:3])) ** 0.5
        std_rotation = (sum([(x - mean_rotation_Xi) **2 for x in activity_data[keys][3:6]]) / len(activity_data[keys][3:6])) ** 0.5
        std_accelerometer = (sum([(x - mean_accelerometer_Xi) **2 for x in activity_data[keys][6:9]]) / len(activity_data[keys][6:9])) ** 0.5
        std_gyroscope = (sum([(x - mean_gyroscope_Xi) **2 for x in activity_data[keys][9:12]]) / len(activity_data[keys][9:12])) ** 0.5
        std_magnetic = (sum([(x - mean_magnetic_Xi) **2 for x in activity_data[keys][12:15]]) / len(activity_data[keys][12:15])) ** 0.5
        
        activity_features[keys].update({'id':keys, 'orStd':std_orientation, 'rStd':std_rotation, 'accStd':std_accelerometer,
        'gStd':std_gyroscope,'MagStd':std_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features

def root_ms(activity_data):
    'function for computing the root mean square of each sensor readings'
    for keys in activity_data:
        rms_orientation = (sum([x**2 for x in activity_data[keys][:3]]) / len(activity_data[keys][:3])) ** 0.5       # [x**2 for x in a_list] is called list comprehension
        rms_rotation = (sum([x**2 for x in activity_data[keys][3:6]]) / len(activity_data[keys][3:6])) ** 0.5
        rms_accelerometer = (sum([x**2 for x in activity_data[keys][6:9]]) / len(activity_data[keys][6:9])) ** 0.5
        rms_gyroscope = (sum([x**2 for x in activity_data[keys][9:12]]) / len(activity_data[keys][9:12])) ** 0.5
        rms_magnetic = (sum([x**2 for x in activity_data[keys][12:15]]) / len(activity_data[keys][12:15])) ** 0.5
        
        activity_features[keys].update({'id':keys, 'orRms':rms_orientation, 'rRms':rms_rotation, 'accRms':rms_accelerometer,
        'gRms':rms_gyroscope,'MagRms':rms_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features

def sum_squares(activity_data):
    'function for computing the sum of square of each sensor readings'
    for keys in activity_data:
        mean_orientation_Xi = sum(activity_data[keys][:3]) / len(activity_data[keys][:3])
        mean_rotation_Xi = sum(activity_data[keys][3:6]) / len(activity_data[keys][3:6])
        mean_accelerometer_Xi = sum(activity_data[keys][6:9]) / len(activity_data[keys][6:9])
        mean_gyroscope_Xi = sum(activity_data[keys][9:12]) / len(activity_data[keys][9:12])
        mean_magnetic_Xi = sum(activity_data[keys][12:15]) / len(activity_data[keys][12:15]) 
        
        sos_orientation = sum([(x - mean_orientation_Xi) **2 for x in activity_data[keys][:3]])
        sos_rotation = sum([(x - mean_rotation_Xi) **2 for x in activity_data[keys][3:6]])
        sos_accelerometer = sum([(x - mean_accelerometer_Xi) **2 for x in activity_data[keys][6:9]]) 
        sos_gyroscope = sum([(x - mean_gyroscope_Xi) **2 for x in activity_data[keys][9:12]])
        sos_magnetic = sum([(x - mean_magnetic_Xi) **2 for x in activity_data[keys][12:15]])
        
        activity_features[keys].update({'id':keys, 'orSos':sos_orientation, 'rSos':sos_rotation, 'accSos':sos_accelerometer,
        'gSos':sos_gyroscope,'MagSos':sos_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features
def median(activity_data):
    'function for computing the median of each sensor readings'
    # since our no of observations is an odd number
    for keys in activity_data:
        #sorting respective featues in an ascending order
        activity_data[keys][:3].sort()
        activity_data[keys][3:6].sort()
        activity_data[keys][6:9].sort()
        activity_data[keys][9:12].sort()
        activity_data[keys][12:15].sort()

        med_orientation = activity_data[keys][:3] [int(((len(activity_data[keys][:3]) + 1) / 2)) -1  ]      # We subtract 1 (-1) because python is zero indexed
        med_rotation = activity_data[keys][3:6] [int(((len(activity_data[keys][3:6]) + 1) / 2)) -1 ]
        med_accelerometer = activity_data[keys][6:9] [int(((len(activity_data[keys][6:9]) + 1) / 2)) -1 ]
        med_gyroscope = activity_data[keys][9:12] [int(((len(activity_data[keys][9:12]) + 1) / 2)) -1 ]
        med_magnetic = activity_data[keys][12:15] [int(((len(activity_data[keys][12:15]) + 1) / 2)) -1 ]
        
        activity_features[keys].update({'id':keys, 'orMedian':med_orientation, 'rMedian':med_rotation, 'accMedian':med_accelerometer,
        'gMedian':med_gyroscope,'MagMedian':med_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features

# The zero crosssing is the point where the sign of the values of our observed variables/parameter changes sign from positive to negative or vice versa.
def zero_crossing(activity_data):
    'function for computing the zero crossing of each sensor readings'
    for keys in activity_data:
        or_zcross = sum(1 for ind, val in enumerate(activity_data[keys][:3]) if (ind+1 < len(activity_data[keys][:3]))
            if activity_data[keys][:3][ind] * activity_data[keys][:3][ind+1]<0)
        r_zcross = sum(1 for ind, val in enumerate(activity_data[keys][3:6]) if (ind+1 < len(activity_data[keys][3:6]))
            if activity_data[keys][:3][ind] * activity_data[keys][3:6][ind+1]<0)
        acc_zcross = sum(1 for ind, val in enumerate(activity_data[keys][6:9]) if (ind+1 < len(activity_data[keys][6:9]))
            if activity_data[keys][:3][ind] * activity_data[keys][6:9][ind+1]<0)
        g_zcross = sum(1 for ind, val in enumerate(activity_data[keys][9:12]) if (ind+1 < len(activity_data[keys][9:12]))
            if activity_data[keys][:3][ind] * activity_data[keys][9:12][ind+1]<0)
        m_zcross = sum(1 for ind, val in enumerate(activity_data[keys][12:15]) if (ind+1 < len(activity_data[keys][12:15]))
            if activity_data[keys][:3][ind] * activity_data[keys][12:15][ind+1]<0)
        
        activity_features[keys].update({'id':keys, 'orZcross':or_zcross, 'rZcross':r_zcross, 'accZcross':acc_zcross,
        'gZcross':g_zcross,'MagZcross':m_zcross,'Activity':activity_data[keys][-1]})
    return activity_features


def covariance(activity_data):
    'function for computing the covariance of each sensor readings'
    # note that we have only one set of observations and no other set of observations to find our covariance against
    # COV(X,X) = VAR(X)\
    for keys in activity_data:
        mean_orientation_Xi = sum(activity_data[keys][:3]) / len(activity_data[keys][:3])
        mean_rotation_Xi = sum(activity_data[keys][3:6]) / len(activity_data[keys][3:6])
        mean_accelerometer_Xi = sum(activity_data[keys][6:9]) / len(activity_data[keys][6:9])
        mean_gyroscope_Xi = sum(activity_data[keys][9:12]) / len(activity_data[keys][9:12])
        mean_magnetic_Xi = sum(activity_data[keys][12:15]) / len(activity_data[keys][12:15]) 
        
        cov_orientation = sum([(x - mean_orientation_Xi) **2 for x in activity_data[keys][:3]]) / len(activity_data[keys][:3])
        cov_rotation = sum([(x - mean_rotation_Xi) **2 for x in activity_data[keys][3:6]]) / len(activity_data[keys][3:6])
        cov_accelerometer = sum([(x - mean_accelerometer_Xi) **2 for x in activity_data[keys][6:9]]) / len(activity_data[keys][6:9])
        cov_gyroscope = sum([(x - mean_gyroscope_Xi) **2 for x in activity_data[keys][9:12]]) / len(activity_data[keys][9:12])
        cov_magnetic = sum([(x - mean_magnetic_Xi) **2 for x in activity_data[keys][12:15]]) / len(activity_data[keys][12:15])
        
        activity_features[keys].update({'id':keys,'orCov':cov_orientation, 'rCov':cov_rotation, 'accCov':cov_accelerometer,
        'gCov':cov_gyroscope,'MagCov':cov_magnetic,'Activity':activity_data[keys][-1]})
    return activity_features 
    
def write_csv(no,activity_data):
    'function for writing out computed features to a csv file'
    print('Computing features...\n')
    if os.path.exists('extracted_features') == False: # checks if directory exists before creating it
        os.mkdir('extracted_features') # creating a directory to put the new csv files in
    else:
        pass
    os.chdir('extracted_features') # changing into the directory
    if no  == '1':
        features = mean(activity_data)
        csv_columns = ['id','orMean','rMean','accMean','gMean','MagMean', 'Activity']
        csv_filename = 'mean_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '2':
        features = variance(activity_data)
        csv_columns = ['id','orVar','rVar','accVar','gVar','MagVar', 'Activity']
        csv_filename = 'variance_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '3':
        features = median(activity_data)
        csv_columns = ['id','orMedian','rMedian','accMedian','gMedian','MagMedian', 'Activity']
        csv_filename = 'median_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '4':
        features = std_deviation(activity_data)
        csv_columns = ['id','orStd','rStd','accStd','gStd','MagStd', 'Activity']
        csv_filename = 'std_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '5':
        features = root_ms(activity_data)
        csv_columns = ['id','orRms','rRms','accRms','gRms','MagRms', 'Activity']
        csv_filename = 'root_mean_square_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '6':
        features = zero_crossing(activity_data)
        csv_columns = ['id','orZcross','rZcross','accZcross','gZcross','MagZcross', 'Activity']
        csv_filename = 'zerocrossing_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '7':
        features = sum_squares(activity_data)
        csv_columns = ['id','orSos','rSos','accSos','gSos','MagSos', 'Activity']
        csv_filename = 'sum_squares_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    elif no == '8':
        features = covariance(activity_data)
        csv_columns = ['id','orCov','rCov','accCov','gCov','MagCov', 'Activity']
        csv_filename = 'covariance_features.csv'
        hold_list = []
        try:
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for keys in features:
                    values = features[keys]
                    hold_list.append(values)
                for data in hold_list:
                    writer.writerow(data)
                    #print(data) 
        except IOError:
            print("I/O error")
    else:
        raise Exception('Wrong value given')
    print('Feature completed.Check extracted_features folder')

import csv
import calendar
import pandas as pd
import numpy as np
import validation as v
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

def get_random_rows(data_array, fraction=0.05, random_state=None):
    """
    Lấy một phần ngẫu nhiên của mảng NumPy.

    Parameters:
        data_array (np.ndarray): Mảng NumPy chứa dữ liệu.
        fraction (float): Tỷ lệ phần trăm dữ liệu muốn lấy ngẫu nhiên. Mặc định là 0.05 (5%).
        random_state (int): Số ngẫu nhiên dùng để điều khiển quá trình lựa chọn. Mặc định là None.

    Returns:
        np.ndarray: Mảng con chứa 5% hàng dữ liệu được chọn ngẫu nhiên.
    """
    # Đặt hạt ngẫu nhiên (random seed) nếu cần thiết
    if random_state is not None:
        np.random.seed(random_state)

    # Tính số lượng hàng dữ liệu muốn lấy
    num_rows_to_sample = int(fraction * data_array.shape[0])

    # Lấy các chỉ số ngẫu nhiên của hàng dữ liệu
    sampled_indices = np.random.choice(data_array.shape[0], num_rows_to_sample, replace=False)

    # Sử dụng các chỉ số để trích xuất các hàng dữ liệu
    sampled_data = data_array[sampled_indices]

    return sampled_data

def save_data(data,file_name,choice):

    data = pd.DataFrame(data, columns=['id','age', 'job', 'marital','education','default','balance','housing','loan',
                                                  'contact','day','month','duration','campaign','pdays', 'previous', 'poutcome','y','probability'])
    print(choice)
    if choice == 'yes':
        data = data[data['y'] == 'yes']

    # Save DataFrame to a CSV file with a custom delimiter
    data.to_csv(file_name+'.csv', sep=';', index=False)  # Set index=False if you don't want to save the index
    data.to_excel(file_name+'.xlsx', index=False,engine='openpyxl')

def data_from_csv(file):
    with open(file) as f:
        sep = v.check_csv_separator(file)
        df = pd.read_csv(f,sep=sep)
        return df

def search_from_csv(df,col,txt):
    if col not in df.columns:

        return None

    if txt == '':
        return df

    txt = str(txt)
    results = df[df[col].astype(str).str.lower().str.contains(txt)]

    return results

def samples_0_1_values(df):
    yes = len(df[df['y'] == 'yes'])
    no = len(df[df['y'] == 'no'])
    return str(len(df)),str(yes),str(no)

def loan(df):
    yes_count = (df['loan'] == 'yes').sum()

    yes_count_with_loan_1 = df.loc[(df['loan'] == 'yes') & (df['y'] == 'yes'), 'y'].count()

    no_count_with_loan_1 = df.loc[(df['loan'] == 'yes') & (df['y'] == 'no'), 'y'].count()

    return (yes_count,yes_count_with_loan_1,no_count_with_loan_1)

def pred_data_label(data_numpyArr):
    df = pd.DataFrame(data_numpyArr, columns=['age', 'job', 'marital','education','default','balance' ,'housing','loan',
                                                  'contact','day','month','duration','campaign','pdays', 'previous', 'poutcome'])
    convert = {
        "job": {"blue-collar": 0, "management": 1, "technician": 2, "admin.": 3, "services": 4, "retired": 5,
                "self-employed": 6, "entrepreneur": 7, "unemployed": 8, "housemaid": 9, "student": 10,
                 "unknown": 11},
        "marital": {"married": 0, "single": 1, "divorced": 2, "unknown":3},
        "education": {"secondary": 0, "tertiary": 1, "primary": 2, "unknown": 3},
        "default": {"no": 0, "yes": 1,"unknown": 2},
        "housing": {"no": 0, "yes": 1,"unknown": 2},
        "loan": {"no": 0, "yes": 1,"unknown": 2},
        "contact": {"cellular": 0, "unknown": 1, "telephone": 2},
        "month": {"may": 1, "jul": 2, "aug": 3, "jun": 4, "nov": 5, "apr": 6, "feb": 7, "jan": 8, "oct": 9,
                    "sep": 10, "mar": 11, "dec": 12,"unknown":13},
        "poutcome": {"unknown": 0, "failure": 1, "other": 2, "success": 3}
    }
    # Xử lý cột job
    job_unique = df['job'].unique()
    for uni in job_unique:
        if uni not in convert['job']:
            max_value = max(convert['job'].values())
            convert['job'][uni] = max_value + 1

    # Xử lý cột education
    education_unique = df['education'].unique()
    for uni in education_unique:
        if uni not in convert['education']:
            max_value = max(convert['education'].values())
            convert['education'][uni] = max_value + 1

    # Xử lý cột contact
    contact_unique = df['contact'].unique()
    for uni in contact_unique:
        if uni not in convert['contact']:
            max_value = max(convert['contact'].values())
            convert['contact'][uni] = max_value + 1

    df = df.replace(convert)
    return df

def des_data_label(data_numpyArr):
    df = pd.DataFrame(data_numpyArr, columns=['age', 'job', 'marital','education','default','balance' ,'housing','loan',
                                                  'contact','day','month','duration','campaign','pdays', 'previous', 'poutcome','y'])
    convert = {
        "job": {"blue-collar": 0, "management": 1, "technician": 2, "admin.": 3, "services": 4, "retired": 5,
                "self-employed": 6, "entrepreneur": 7, "unemployed": 8, "housemaid": 9, "student": 10,
                 "unknown": 11},
        "marital": {"married": 0, "single": 1, "divorced": 2, "unknown":3},
        "education": {"secondary": 0, "tertiary": 1, "primary": 2, "unknown": 3},
        "default": {"no": 0, "yes": 1,"unknown": 2},
        "housing": {"no": 0, "yes": 1,"unknown": 2},
        "loan": {"no": 0, "yes": 1,"unknown": 2},
        "contact": {"cellular": 0, "unknown": 1, "telephone": 2},
        "month": {"may": 1, "jul": 2, "aug": 3, "jun": 4, "nov": 5, "apr": 6, "feb": 7, "jan": 8, "oct": 9,
                    "sep": 10, "mar": 11, "dec": 12,"unknown": 13},
        "poutcome": {"unknown": 0, "failure": 1, "other": 2, "success": 3},
        "y": {'yes': 1, 'no': 0}
    }
    # Xử lý cột job
    job_unique = df['job'].unique()
    for uni in job_unique:
        if uni not in convert['job']:
            max_value = max(convert['job'].values())
            convert['job'][uni] = max_value + 1

    # Xử lý cột education
    education_unique = df['education'].unique()
    for uni in education_unique:
        if uni not in convert['education']:
            max_value = max(convert['education'].values())
            convert['education'][uni] = max_value + 1

    # Xử lý cột contact
    contact_unique = df['contact'].unique()
    for uni in contact_unique:
        if uni not in convert['contact']:
            max_value = max(convert['contact'].values())
            convert['contact'][uni] = max_value + 1

    df = df.replace(convert)
    return df

def calculate_min_median_max(data_frame):
    data = np.array(data_frame)
    min_value = np.min(data)
    first_quartile = np.percentile(data, 25)
    median = np.median(data)
    third_quartile = np.percentile(data, 75)
    max_value = np.max(data)

    return [min_value, first_quartile, median, third_quartile, max_value]

def education(data):
    data_education_y = data[data['y'] != 'no'][['education', 'y']]
    primary_education_y = data_education_y.loc[(data_education_y['education'] == 'primary'),'y'].count()
    secondary_education_y = data_education_y.loc[(data_education_y['education'] == 'secondary'),'y'].count()
    tertiary_education_y = data_education_y.loc[(data_education_y['education'] == 'tertiary'),'y'].count()
    unknown_education_y = data_education_y.loc[(data_education_y['education'] == 'unknown'),'y'].count()
    return (primary_education_y,secondary_education_y,tertiary_education_y,unknown_education_y)

def month_y(data):
    data_month_y = data[data['y'] != 'no'][['month', 'y']]
    jan_month_1 = data_month_y.loc[(data_month_y['month'] == 'jan'),'y'].count()
    feb_month_2 = data_month_y.loc[(data_month_y['month'] == 'feb'),'y'].count()
    mar_month_3 = data_month_y.loc[(data_month_y['month'] == 'mar'),'y'].count()
    apr_month_4 = data_month_y.loc[(data_month_y['month'] == 'apr'),'y'].count()
    may_month_5 = data_month_y.loc[(data_month_y['month'] == 'may'),'y'].count()
    jun_month_6 = data_month_y.loc[(data_month_y['month'] == 'jun'),'y'].count()
    jul_month_7 = data_month_y.loc[(data_month_y['month'] == 'jul'),'y'].count()
    aug_month_8 = data_month_y.loc[(data_month_y['month'] == 'aug'),'y'].count()
    sep_month_9 = data_month_y.loc[(data_month_y['month'] == 'sep'),'y'].count()
    oct_month_10 = data_month_y.loc[(data_month_y['month'] == 'oct'),'y'].count()
    nov_month_11 = data_month_y.loc[(data_month_y['month'] == 'nov'),'y'].count()
    dec_month_12 = data_month_y.loc[(data_month_y['month'] == 'dec'),'y'].count()

    return(jan_month_1,feb_month_2,mar_month_3,apr_month_4,may_month_5,jun_month_6,
           jul_month_7,aug_month_8,sep_month_9,oct_month_10,nov_month_11,dec_month_12)

def top3_corr(data):
    corr_matrix = data.corr()
    correlation_with_y = corr_matrix['y'].drop('y')

    top_3_correlated_features = correlation_with_y.abs().nlargest(3)
    fea = []
    value = []
    for feature, correlation_value in top_3_correlated_features.items():
        fea.append(feature)
        value.append(correlation_value)

    return (fea, value)

def concat_X_prdy(X, y):
    # Check if the dimensions match
    if len(X) != len(y):

        return None
    # Concatenate y_pred to X_test
    X['y'] = y
    return X

def concat_X_prob(X, y):
    # Check if the dimensions match
    if len(X) != len(y):

        return None
    # Concatenate y_pred to X_test
    X['probability'] = y
    return X

def job_age_y_chat(df):
    # Filter out rows with 'y' column not equal to 'no'
    data_job_y = df[df['y'] != 'no'][['job', 'age']]

    # Define age bins
    age_bins = [16, 25, 30, 35, 45, 55, 65, 100]
    age_labels = ['16-24', '25-29', '30-34', '35-44', '45-54', '55-64', '65-100']

    # Use pd.cut to categorize ages
    data_job_y['age_group'] = pd.cut(data_job_y['age'], bins=age_bins, labels=age_labels, right=True)

    # Group by 'job' and 'age_group' and count the occurrences
    counts = data_job_y.groupby(['job', 'age_group']).size().unstack(fill_value=0)

    # Convert the counts DataFrame to a dictionary
    counts_dict = counts.to_dict(orient='index')

    return counts_dict

def data_from_excel(filename):
    data = pd.read_excel(filename)
    return data

def calculate_monthly(data, col):
    # Lấy các cột cần thiết và nhóm theo tháng
    data_duration_y = data[[col, 'month']]
    result_month_duration = data_duration_y.groupby(['month']).sum()

    month_durations = []
    for month in range(1, 13):
        month_name = calendar.month_abbr[month].lower()  # Chuyển tháng từ số sang chữ viết tắt

        if month_name in result_month_duration.index:
            month_duration = result_month_duration.loc[month_name, col]
        else:
            # Nếu không có dữ liệu cho tháng đó, sử dụng giá trị mặc định (0 hoặc chuỗi trống)
            month_duration = 0 if data[col].dtype != 'object' else ''

        month_durations.append(month_duration)

    return tuple(month_durations)

def preprocess(df):
    # Lấy số lượng mẫu cho các lớp 'yes' và 'no' từ hàm `samples_0_1_values`
    yes_no = samples_0_1_values(df)
    total_samples = int(yes_no[0])  # Tổng số mẫu
    yes_count = int(yes_no[1])  # Số lượng mẫu lớp 'yes'
    no_count = int(yes_no[2])  # Số lượng mẫu lớp 'no'

    # Tính tỷ lệ giữa số lượng mẫu của 'yes' và tổng số mẫu
    ratio_yes = yes_count / total_samples

    # Tính tỷ lệ giữa số lượng mẫu của 'no' và tổng số mẫu
    ratio_no = no_count / total_samples

    # Tính 10% tổng số mẫu
    ten_percent_total = int(total_samples / 10)

    # Lấy dữ liệu X (các cột trừ cột 'y') và y (cột 'y')
    X = df.drop(columns=['y'])
    y = df['y']

    # Biến để lưu trữ dữ liệu đã được resample
    X_resampled = X
    y_resampled = y

    # Xử lý mất cân bằng dữ liệu
    if ratio_yes < 0.25:
        # Mục tiêu số lượng mẫu cho 'yes' và 'no' dựa trên 10% tổng số mẫu
        target_yes_count = ten_percent_total * 3
        target_no_count = ten_percent_total * 7

        # Undersampling lớp 'no' để đạt mục tiêu
        undersampler = RandomUnderSampler(sampling_strategy={'no': target_no_count}, random_state=42)
        X_resampled, y_resampled = undersampler.fit_resample(X, y)

        # Oversampling lớp 'yes' để đạt mục tiêu
        oversampler = RandomOverSampler(sampling_strategy={'yes': target_yes_count}, random_state=42)
        X_resampled, y_resampled = oversampler.fit_resample(X_resampled, y_resampled)

    elif ratio_no < 0.25:
        # Mục tiêu số lượng mẫu cho 'yes' và 'no' dựa trên 10% tổng số mẫu
        target_yes_count = ten_percent_total * 7
        target_no_count = ten_percent_total * 3

        # Undersampling lớp 'yes' để đạt mục tiêu
        undersampler = RandomUnderSampler(sampling_strategy={'yes': target_yes_count}, random_state=42)
        X_resampled, y_resampled = undersampler.fit_resample(X, y)

        # Oversampling lớp 'no' để đạt mục tiêu
        oversampler = RandomOverSampler(sampling_strategy={'no': target_no_count}, random_state=42)
        X_resampled, y_resampled = oversampler.fit_resample(X_resampled, y_resampled)

    # Kết hợp lại dữ liệu đã resample
    df_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name='y')], axis=1)

    return df_resampled

def clear_null_predict(df,id_column):
    int_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    # Loại bỏ các hàng chứa giá trị null
    df_cleaned = df.dropna(axis=0).copy()  # Sử dụng .copy() để tạo bản sao độc lập
    filtered_id_column = id_column.loc[df_cleaned.index]
    for col in int_columns:
        df_cleaned[col] = df_cleaned[col].astype(int)

    return df_cleaned,filtered_id_column

def clear_null_design(df):
    int_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    # Loại bỏ các hàng chứa giá trị null
    df_cleaned = df.dropna(axis=0).copy()  # Sử dụng .copy() để tạo bản sao độc lập
    for col in int_columns:
        df_cleaned[col] = df_cleaned[col].astype(int)

    return df_cleaned

if __name__ == "__main__":
    import time
    raw_data = data_from_excel('data/predict_test.xlsx')
    raw_data['id'] = ''
    id_column = raw_data['id'].astype(str)
    data = raw_data.drop(columns=['id'])
    data = clear_null_predict(raw_data,id_column)
    data = v.check_value(data[0], 'predict')
    if data is None:
        print('Not oke')


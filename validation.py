import os
import pandas as pd
from openpyxl import load_workbook

def check_csv_separator(filename):
    """
    Kiểm tra xem tệp CSV có dấu phân cách là dấu phẩy (',') hay dấu chấm phẩy (';').

    filename: Đường dẫn đến tệp CSV cần kiểm tra.

    Trả về:
    - 'comma' nếu dấu phân cách là dấu phẩy (',').
    - 'semicolon' nếu dấu phân cách là dấu chấm phẩy (';').
    - None nếu không thể xác định được dấu phân cách.
    """
    # Đọc dòng đầu tiên của tệp CSV
    with open(filename, 'r') as file:
        first_line = file.readline()

    # Tách dòng đầu tiên bằng dấu phẩy và dấu chấm phẩy
    comma_split = first_line.split(',')
    semicolon_split = first_line.split(';')

    # Kiểm tra số lượng phần tử sau khi tách
    if len(comma_split) > len(semicolon_split):
        return ','
    elif len(semicolon_split) > len(comma_split):
        return ';'
    else:
        return None

def file_valid(file):
    return os.path.exists(file)

def file_check_label(tp,df):
    df_label = df.columns
    label = ['age', 'job', 'marital', 'education', "default", "balance", "housing", "loan", "contact", "day",
                "month", "duration", "campaign", "pdays", "previous", "poutcome", "y"]
    num = len(label) if tp == 'design' else len(label) - 1

    if len(df_label) != num:
        return None

    for i in range(num):
        if df_label[i].lower() != label[i]:
            return None

    return df

def check_value(df,tp):
    if len(df) <100 and tp =='design':
        return None
    if len(df) == 0 and tp =='predict':
        return None
    if not check_integer_columns(df):
        print('integer')
        return None
    if check_age_column(df):
        print('age')
        return None
    if check_day_column(df):
        print('day')
        return None
    if check_campaign_column(df):
        print('campaign')
        return None
    if check_previous_column(df):
        print('previous')
        return None
    if check_pdays_column(df):
        print('p_days')
        return None
    if check_duration_column(df):
        print('duration')
        return None

    if not check_all_columns_for_outliers(df, tp):
        print('outlier')
        return None
    return df

def find_columns_with_only_nulls(df):
    """
    Tìm các cột trong DataFrame chỉ chứa giá trị null.

    df: DataFrame chứa dữ liệu.

    Trả về danh sách các tên cột chỉ chứa giá trị null.
    """
    # Tạo một danh sách lưu trữ các tên cột chỉ chứa giá trị null
    columns_with_only_nulls = []

    # Duyệt qua từng cột trong DataFrame
    for column in df.columns:
        # Kiểm tra xem tất cả các giá trị trong cột có phải là null không
        if df[column].isnull().all():
            # Nếu tất cả các giá trị trong cột đều là null, thêm tên cột vào danh sách
            columns_with_only_nulls.append(column)

    # Trả về danh sách các tên cột chỉ chứa giá trị null
    return columns_with_only_nulls

def find_null_columns(df):
    """
    Kiểm tra xem cột nào trong DataFrame chứa giá trị null.

    df: DataFrame chứa dữ liệu.

    Trả về danh sách các cột chứa giá trị null.
    """
    # Tìm các cột có giá trị null
    null_columns = df.columns[df.isnull().any()].tolist()

    # Trả về danh sách các cột chứa giá trị null
    return null_columns

def fill_nulls_based_on_type(df, numeric_fill_value="average", string_fill_value="unknown"):
    """
    Thay thế các giá trị null trong DataFrame dựa trên loại dữ liệu của cột.

    df: DataFrame chứa dữ liệu.
    numeric_fill_value: Giá trị để thay thế giá trị null trong các cột chứa dữ liệu kiểu số.
                        Mặc định là "average", nghĩa là sử dụng giá trị trung bình của cột.
    string_fill_value: Giá trị mặc định để thay thế giá trị null trong các cột chứa dữ liệu kiểu chuỗi.
                       Mặc định là "unknown".

    Trả về DataFrame đã được thay thế giá trị null.
    """
    for column in df.columns:
        # Kiểm tra kiểu dữ liệu của cột
        if df[column].dtype in [int, float]:  # Các kiểu dữ liệu số
            # Thay thế các giá trị null bằng giá trị trung bình của cột
            avg_value = df[column].mean()
            df[column] = df[column].fillna(avg_value).astype(int)
        elif df[column].dtype == object:  # Kiểu dữ liệu chuỗi (string)
            # Thay thế các giá trị null bằng giá trị mặc định (unknown)
            df[column] = df[column].fillna(string_fill_value)

    # Trả về DataFrame đã được thay thế giá trị null
    return df

def check_column_values(df, column_name, allowed_values):
    """
    Kiểm tra xem một cột trong DataFrame chỉ chứa các giá trị hợp lệ từ allowed_values.

    df: DataFrame chứa dữ liệu.
    column_name: Tên của cột cần kiểm tra.
    allowed_values: Tập hợp giá trị hợp lệ được xác định.

    Trả về True nếu cột chỉ chứa các giá trị hợp lệ, ngược lại trả về False.
    """
    allowed_values_set = set(allowed_values.values())  # Chuyển các giá trị thành một tập hợp
    return df[column_name].isin(allowed_values_set).all()

def check_all_columns_for_outliers(df,type):
    """
    Kiểm tra các cột của DataFrame xem có giá trị ngoại lai so với giá trị hợp lệ đã cung cấp hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu không có giá trị ngoại lai trong bất kỳ cột nào, ngược lại trả về False.
    """
    # Danh sách các cột và giá trị hợp lệ của chúng
    columns_and_allowed_values = {
        'marital': {"married", "single", "divorced", "unknown"},
        'default': {"no", "yes", "unknown"},
        'housing': {"no", "yes", "unknown"},
        'loan': {"no", "yes", "unknown"},
        'poutcome': {"unknown", "failure", "other", "success"},
        'month': {"may", "jul", "aug", "jun", "nov", "apr", "feb", "jan", "oct", "sep",
                  "mar", "dec","unknown"},
    }
    if type == 'design':
        columns_and_allowed_values['y'] = {'yes', 'no'}
    # Kiểm tra từng cột
    for column_name, allowed_values in columns_and_allowed_values.items():
        # Sử dụng phương thức .isin() để kiểm tra xem cột có chỉ chứa các giá trị hợp lệ không
        if not df[column_name].isin(allowed_values).all():
            # Nếu có giá trị ngoại lai, trả về False
            return False
    # Nếu không có cột nào có giá trị ngoại lai, trả về True
    return True

def check_integer_columns(df):
    # Danh sách các cột cần kiểm tra
    columns_to_check = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

    # Kiểm tra xem tất cả các cột trong danh sách có chứa toàn bộ các giá trị số nguyên hay không
    return all(is_integer_column(df, column) for column in columns_to_check)

def is_integer_column(df, column_name):
    # Sử dụng apply() để kiểm tra xem tất cả các giá trị trong cột là số nguyên hay không
    return df[column_name].apply(lambda x: isinstance(x, int)).all()

def check_age_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['age'] < 16 | (df['age'] >= 118)]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_day_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['day'] < 1 | (df['day'] > 31)]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_campaign_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['campaign'] < 1 ]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_duration_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['duration'] < 0 ]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_previous_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['previous'] < 0 ]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_pdays_column(df):
    """
    Kiểm tra xem cột 'age' trong DataFrame có giá trị nhỏ hơn 16 hay không.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu có giá trị nhỏ hơn 16 trong cột 'age', ngược lại trả về False.
    """
    # Lọc cột 'age' để kiểm tra xem có giá trị nào nhỏ hơn 16 không
    age_below_16 = df[df['pdays'] < -1 ]

    # Nếu có bất kỳ giá trị nào nhỏ hơn 16 trong cột 'age', trả về True
    if not age_below_16.empty:
        return True

    # Nếu không có giá trị nào nhỏ hơn 16, trả về False
    return False

def check_day_column_2(df):
    """
    Kiểm tra tính hợp lệ của giá trị 'day' trong cột 'day' và giá trị 'month' trong cột 'month' của DataFrame.

    df: DataFrame chứa dữ liệu.

    Trả về True nếu tất cả các giá trị trong cột 'day' và 'month' hợp lệ, ngược lại trả về False.
    """
    # Dictionary chứa số ngày tối đa trong mỗi tháng
    days_in_month = {
        'jan': 31, 'feb': 29, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30,
        'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31
    }

    # Kiểm tra tính hợp lệ của giá trị 'day' dựa trên 'month'
    for index, row in df.iterrows():
        month = row['month'].lower()  # Lấy giá trị tháng
        day = row['day']  # Lấy giá trị ngày

        # Lấy số ngày tối đa trong tháng tương ứng
        max_days = days_in_month.get(month, 0)

        # Kiểm tra tính hợp lệ của giá trị ngày
        if not (1 <= day <= max_days):
            return False

    # Nếu tất cả các giá trị 'day' và 'month' hợp lệ, trả về True
    return True

if __name__ == "__main__":
    #df = pd.read_excel('data/test_2.xlsx')
    #### check file - check du du lieu - check cot bi null - check gia tri null - fill null - check value
    data = file_check_label('design', 'data/test_2.xlsx','.xlsx')
    print(data)

    if len(data) < 100:
        print('len<100')
    if find_columns_with_only_nulls(data):
        print('col nul')

    col_num = find_null_columns(data)
    if col_num:
        decision = input('avg or cancel')
        if decision == 'cancel':
            print('cancl')
        else:
            data = fill_nulls_based_on_type(data)

    data = check_value(data, 'design')

    if data is None:
        print('none')
    print(data)


import math
def clean_value(value, column):
    if(column==0):
        try:
            cleaned_value = float(value.replace('Rs.', '').replace(',', '').strip())
            cleaned_value *= 100
        except ValueError:
            cleaned_value = 0.0  
        return cleaned_value
    elif (column==1):
        try:
            if (value=='No discount'):
                cleaned_value = 0
            else:
                cleaned_value = float(value.replace('%', '').replace('Off', '').strip())
        except ValueError:
            cleaned_value = 0.0  
        return cleaned_value
    elif (column==2):
        cleaned_value = value.replace('sold', '').strip()
    
        try:
            if value=='No rating':
                cleaned_value=0
            elif cleaned_value.endswith('K'):
                cleaned_value = float(cleaned_value[:-1]) * 1000  
            else:
                cleaned_value = float(cleaned_value)
        except ValueError:
            cleaned_value = 0.0
        cleaned_value = math.floor(cleaned_value)
        return cleaned_value
    elif (column==3):
        try:
            if (value=='Not sold'):
                cleaned_value = 0
            else:
                cleaned_value = int(value)
        except ValueError:
            cleaned_value = 0.0  
        return cleaned_value
    else:
        return value
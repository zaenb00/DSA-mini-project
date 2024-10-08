import math
def normal (value, column):
    if(column==0):
        if isinstance (value,str):
            try:
                normal_value = float(value.replace('Rs.', '').replace(',', '').strip())
                normal_value *= 100
            except ValueError:
                normal_value = 0.0  
        else:
            normal_value = 0
        return normal_value
    elif (column==1):
        if isinstance (value,str):
            try:
                if (value=='No discount'):
                    normal_value = 0
                else:
                    normal_value = float(value.replace('%', '').replace('Off', '').strip())
            except ValueError:
                normal_value = 0.0
        else:
            normal_value = 0
        return normal_value
    elif (column==2):
        
        normal_value = value
        if isinstance(normal_value,str):
            try:
                if value=='No rating':
                    normal_value=0
                elif normal_value.endswith('K'):
                    normal_value = float(normal_value[:-1]) * 1000  
                else:
                    normal_value = float(normal_value)
            except ValueError:
                normal_value = 0.0
            normal_value = math.floor(normal_value)
        
        return normal_value
    elif (column==3):
        if isinstance (value,str):
            try:
                if (value=='Not sold'):
                    normal_value = 0
                else:
                    normal_value = value.replace('sold', '').strip()
                    if normal_value.endswith('K'):
                        normal_value = float(normal_value[:-1]) * 1000  
                    normal_value = float(normal_value)
            except ValueError:
                normal_value = 0.0  
        else:
            normal_value = value
        return normal_value
    else:
        return value
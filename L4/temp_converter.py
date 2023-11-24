def celsius_to_fahr(temp_celsius):
    return 9/5 * temp_celsius + 32


def kelvins_to_celsius(temp_kelvins):
    return temp_kelvins - 273.15


def kelvins_to_fahr(temp_kelvins):
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr


def temp_calculator(temp_k, convert_to):
    """
    Function for converting temperature in Kelvins 
    to Celsius or Fahrenheit.

    Parameters
    ----------
    temp_k: <numerical>
        Temperature in Kelvins
    convert_to: <str>
        Target temperature that can be either
        Celsius ('C') or Fahrenheit ('F').
        Supported values: 'C' | 'F'
    
    Returns
    -------
    <float>
        Converted temperature.
    """

    
    # Check if user wants the temperature in Celsius
    if convert_to == 'C':
        # Convert value to Celsius using kelvins_to_celsius()
        converted_temp = kelvins_to_celsius(temp_kelvins=temp_k)
    elif convert_to == 'F':
        # Convert value to Fahrenheit using kelvins_to_fahr()
        converted_temp = kelvins_to_fahr(temp_kelvins=temp_k)
    return converted_temp
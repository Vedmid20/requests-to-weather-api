import sys, os
from src.CurrentWeather import CurrentWeather
from src.Forecast import Forecast


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

if __name__ == '__main__':
    lst = [CurrentWeather(), Forecast()]
    [print(i.parsing()) for i in lst]

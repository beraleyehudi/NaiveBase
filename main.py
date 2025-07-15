from numpy.ma.extras import average
import statistics

from manager import Manager
from UI.prints import Prints
from classifier import Classifier
from cleaner import Cleaner
from coach import Coach
from UI.prints import Prints
from receprtor import Receptor
from tester import Tester


if __name__ == '__main__':
    # Manager.start(r'table\health_generated.csv')
    csv = r'table\health_generated.csv'
    df = Cleaner(Receptor(csv).df).df
    results = []

    for i in range(10):
        result =  Tester(df, df.columns[-1]).teke_test()
        results.append(result)
        # print(f'{result}%')

    print(f'average: {average(results)} | max: {max(results)} | min: {min(results)} | median:{statistics.median(results)}')


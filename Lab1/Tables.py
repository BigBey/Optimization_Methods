# draw tables using pandas
import math
from Lab1 import Functions as f
import Lab1.Methods.DihotomiaMethod as dihotomia
import Lab1.Methods.GoldenRatioMethod as goldenratio
import Lab1.Methods.FibonacciMethod as fibonacci
import Lab1.Methods.ParabolaMethod as parabola

count_of_functions = 5
intervals = [(-0.5, 0.5), (6.0, 9.9), (0.0, 2 * math.pi), (0.0, 1.0), (0.5, 2.5)]


# tables for Dihotomia method

print('Tables for Dihotomia Method:')

for i in range(count_of_functions):
    print(dihotomia.dihotomiaMethodGetTable(f.getFunc(i+1), 0.000001, intervals[i][0], intervals[i][1])[1])

print('Tables for Golden Ratio Method:')

for i in range(count_of_functions):
    print(goldenratio.goldenRatioMethodGetTable(f.getFunc(i+1), 0.000001, intervals[i][0], intervals[i][1])[1])

print('Tables for Fibonacci Method:')

for i in range(count_of_functions):
    print(fibonacci.fibonacciMethodGetTable(f.getFunc(i + 1), 30, intervals[i][0],
                                                              intervals[i][1])[1])

print('Tables for Parabola Method:')

for i in range(count_of_functions):
    print(parabola.parabolaMethodGetTable(f.getFunc(i + 1), 0.000001, intervals[i][0],
                                                              intervals[i][1])[1])

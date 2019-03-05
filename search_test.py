
import binarysearch_iter
import binarysearch_rec
sample_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 20, 21, 23, 31, 34, 35, 41, 45, 46, 48, 51, 53, 54, 55, 56, 57, 61, 63, 65, 67, 68, 74, 76, 78, 79, 84, 87, 96, 97, 98, 99, 132, 145, 154, 163, 165, 235, 468, 513, 534, 641, 651, 654, 684, 687, 711, 763, 774, 860, 864, 871, 898, 2314, 3541, 3554, 5341, 5413, 5754, 6465, 6474, 6587, 7891, 8641, 8685, 9487, 64131, 798612, 878941, 687431464154]
print('Length of Sample list = ', len(sample_array))
# testing binarysearch interative method
print('\n\n#Binary Search iterative method')

print('*key = 5')
print('Index = ', binarysearch_iter.binarysearch_iter(sample_array, 5) )

print('*key = 30')
print('Index = ', binarysearch_iter.binarysearch_iter(sample_array, 30) )

print('*key = 0')
print('Index = ', binarysearch_iter.binarysearch_iter(sample_array, 0) )

print('*key = 687431464154')
print('Index = ', binarysearch_iter.binarysearch_iter(sample_array, 687431464154) )

print('*key = 235')
print('Index = ', binarysearch_iter.binarysearch_iter(sample_array, 235) )

print('#')


# testing binarysearch recursive method
print('\n\n#Binary Search recursive method')

print('*key = 5')
print('Index = ', binarysearch_rec.binarysearch_rec(sample_array, 5) )

print('*key = 30')
print('Index = ', binarysearch_rec.binarysearch_rec(sample_array, 30) )

print('*key = 0')
print('Index = ', binarysearch_rec.binarysearch_rec(sample_array, 0) )

print('*key = 687431464154')
print('Index = ', binarysearch_rec.binarysearch_rec(sample_array, 687431464154) )

print('*key = 235')
print('Index = ', binarysearch_rec.binarysearch_rec(sample_array, 235) )

print('#')

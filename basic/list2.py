#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  nums_no_runs = []
  for index, num in enumerate(nums):
    if ((0 == index)
        or (nums[index-1] != num)):
      nums_no_runs.append(num)

  return nums_no_runs


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  """
  Unforunately list.pop(0) is not constant time with the standard python list implementation.
  Use pop(-1) to remove the endmost elements from each list, building a solution list which is backwards.
  Then use reversed() to put the result back in the correct order.
  This solution works in linear time, but is more ugly.
  """

  merged_list = []
  list_merge_length = (len(list1) + len(list2))

  for index in range(0, list_merge_length):
    if (0 == len(list1)):
      merged_list.append(list2.pop(-1))
    elif (0 == len(list2)):
      merged_list.append(list1.pop(-1))
    elif list1[-1] >= list2[-1]:
      merged_list.append(list1.pop(-1))
    else:
      merged_list.append(list2.pop(-1))

  # reversed() returns an iterator, use list(reversed()) to return a list
  return list(reversed(merged_list))



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()

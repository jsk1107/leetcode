# -*- coding: utf-8 -*-
# Author: jsk1107

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        if not n:
            return []

        res = [[0 for _ in range(n)] for _ in range(n)]

        top, right, bottom, left = 0, n - 1, n - 1, 0
        num = 1

        while num <= n ** 2:

            if top == right:
                mid = n // 2
                res[mid][mid] = num
                return res

            for i in range(left, right):
                res[top][i] = num
                num += 1

            for i in range(top, bottom):
                res[i][right] = num
                num += 1

            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][left] = num
                num += 1

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return res

if __name__ == '__main__':
    n = 5
    solution = Solution()
    output = solution.generateMatrix(n)
    print(output)

"""

"""

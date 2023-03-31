#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def insertion_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for i in range(1, len(target_list_)):
        if target_list_[i] < target_list_

    return target_list_


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-1000, 9999) for a in range(length)]
print(list_to_sort)

sorted_ = insertion_sort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort)

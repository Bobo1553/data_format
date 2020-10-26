# -*- encoding: utf -*-
"""
Create on 2020/10/17 16:17
@author: Xiao Yijia
"""




def main():
    student_tuples = [
        (16, 15, 'A'),
        (16, 12, 'C'),
        (12, 15, 'D'),
        (19, 11, 'A'),
        (20, 12, 'E'),
    ]
    student_tuples.sort(key=lambda x: (x[0], x[1]))
    print(student_tuples)


if __name__ == '__main__':
    main()

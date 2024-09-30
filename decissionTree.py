from sklearn import tree

# bước 1: thu thập dữ liệu
# bước 2 : XỬ lí dữ liệu
# bước 3: Xây dựng model
# bước 4 Dự đoán kết quả

my_tree = tree.DecisionTreeClassifier()
# feature=[['nhe','tb','tb','nhieu'],
#          ['nang','thap','cao','it'],
#          ['nhe','thap','cao','it'],
#          ['nang','cao','cao','tb'],
#          ['nhe','cao','cao','nhieu'],
#          ['tb','thap','tb','nhieu'],
#          ['tb','tb','tb','it'],
#          ['nang','thap','thap','nhieu']
#          ]

# Quy uoc
# Name      | Value
# nhe       | 1
# thap      | 2
# tb        | 3
# cao       | 4
# nang      | 5
# it        | 6
# nhieu     | 7

feature =[[1, 3, 3, 7],
         [5, 2, 4, 6],
         [1, 2, 4, 6],
         [5, 4, 4, 3],
         [1, 4, 4, 7],
         [3, 2, 3, 7],
         [3, 3, 3, 6],
         [5, 2, 2, 7]]

label = [0, 1, 1, 0, 0, 0, 0, 1]
result = my_tree.fit(feature,label)
kq = result.predict([[1, 4, 3, 6], [1, 4, 3, 7]])
print(kq)



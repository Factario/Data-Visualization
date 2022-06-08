import matplotlib.pyplot as plt
import numpy as np


col_count = 3
bar_width = .1

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

kr = plt.bar(index, korea_scores, bar_width,
             label='Korea')
ca = plt.bar(index + bar_width, canada_scores, bar_width,
             label='Canada')
ch = plt.bar(index + 0.2, china_scores, bar_width,
             label='China')
fr = plt.bar(index + 0.3, france_scores, bar_width,
             label='France')


def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height*1.05,
                 '%d' % int(height),
                 ha='center', va='bottom')

CreateLabels(kr)
CreateLabels(ca)
CreateLabels(ch)
CreateLabels(fr)

plt.ylabel('Mean score in PISA 2012')
plt.xlabel('Subjects')
plt.title('Test Scores by Coutnry')

plt.xticks(index + .3 / 2, ('Mathematics', 'Reading', 'Science'))
plt.legend(frameon=False, bbox_to_anchor=(1,1))
plt.grid(True)

plt.show()
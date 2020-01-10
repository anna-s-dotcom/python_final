import pandas as pd
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Window(QWidget):
    def __init__(self, x, y, name, filename):
        super().__init__()

        fig = plt.figure()
        canvas = FigureCanvas(fig)

        ax = canvas.figure.add_subplot(111)
        ax.bar(x, y, label = name)
        ax.legend()
        # ax.set_xticks(x)
        import time
        # fig.savefig('graph' + str(time.time()) + '.png')
        fig.savefig(filename)

        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)

        self.show()

df = pd.read_csv('data/names.csv')

start = 1995
end = 1997
name = 'Bruce'

s_start = df['Year'] >= start
s_end = df['Year'] <= end

s_years = s_start & s_end

df_years = df[s_years].copy()
df_final = df_years[df_years['Name'] == name].copy()

s_counts = df_final.groupby('Year')['Count'].sum()

# print(s_counts)

app = QApplication(sys.argv)
window = Window(s_counts.index, s_counts.values, name, 'between')
app.exec()

#############################################
# 2

state = 'NY'
name = 'Bruce'

# df_sn = df[(df['State'] == state) & (df['Name'] == name)].copy()
#
# s_count = df_sn.groupby('Year')['Count'].sum()


##############################################

s_sn = df.groupby(['State', 'Name', 'Year'])['Count'].sum()

# print(s_sn)
# print(s_sn[state, name])
s_count = s_sn[state, name].copy()

window = Window(s_count.index, s_count.values, name, 'State')
app.exec()

import sys
from csvProcessor import display_csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class CountPlotWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        if self.data == None:
            self.data = display_csv("Feeding Dashboard data.csv")
        self.df = pd.DataFrame.from_dict(self.data)
        self.initUI()

    def initUI(self):
        print(self.df)
        layout = QVBoxLayout()

        # Create Matplotlib figure and axis
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Generate sample categorical data
        categories = np.random.choice(["A", "B", "C", "D"], size=100)

        # Create count plot using seaborn
        sns.countplot(x='referral', data=self.df, palette="coolwarm")
        self.ax.set_title("Referral Vs Non-Referral Count")

        layout.addWidget(self.canvas)
        self.setLayout(layout)
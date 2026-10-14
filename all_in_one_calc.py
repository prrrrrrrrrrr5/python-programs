import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTabWidget, QComboBox, QGridLayout
)
from PyQt6.QtCore import Qt

# ===== Styles =====
LIGHT_STYLE = """
QWidget {
    background: qlineargradient(x1:0 y1:0, x2:1 y2:1,
        stop:0 #f7faff, stop:1 #e9efff);
    font-family: Inter, Roboto, Arial;
    color: #222;
}
QLineEdit, QComboBox, QPushButton {
    border-radius: 10px;
    padding: 8px;
    font-size: 14px;
}
QLineEdit, QComboBox {
    background: white;
    border: 1px solid #aaa;
}
QPushButton {
    background: qlineargradient(x1:0 y1:0, x2:0 y2:1,
        stop:0 #4facfe, stop:1 #00f2fe);
    color: white;
    min-height: 36px;
}
QPushButton:pressed {
    background: qlineargradient(x1:0 y1:0, x2:0 y2:1,
        stop:0 #38a6f3, stop:1 #00d3df);
}
QTabBar::tab {
    padding: 8px;
    border-radius: 10px;
}
QTabBar::tab:selected {
    background: rgba(0,0,0,0.08);
}
QGroupBox { border: none; }
"""

DARK_STYLE = """
QWidget {
    background: #1e1e1e;
    font-family: Inter, Roboto, Arial;
    color: #eee;
}
QLineEdit, QComboBox, QPushButton {
    border-radius: 10px;
    padding: 8px;
    font-size: 14px;
}
QLineEdit, QComboBox {
    background: #2a2a2a;
    border: 1px solid #555;
    color: #eee;
}
QPushButton {
    background: qlineargradient(x1:0 y1:0, x2:0 y2:1,
        stop:0 #ff7e5f, stop:1 #feb47b);
    color: black;
    min-height: 36px;
}
QPushButton:pressed {
    background: qlineargradient(x1:0 y1:0, x2:0 y2:1,
        stop:0 #e36b52, stop:1 #eaa868);
}
QTabBar::tab {
    padding: 8px;
    border-radius: 10px;
    color: #eee;
}
QTabBar::tab:selected {
    background: rgba(255,255,255,0.1);
}
QGroupBox { border: none; }
"""

# ===== Main Window =====
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.setWindowTitle("All-in-One Calculator & Converter")
        self.setMinimumSize(820, 560)
        self.setStyleSheet(LIGHT_STYLE)
        self._build_ui()

    def _build_ui(self):
        tabs = QTabWidget()
        tabs.addTab(self._calculator_tab(), "Calculator")
        tabs.addTab(self._geometry2d_tab(), "2D Geometry")
        tabs.addTab(self._geometry3d_tab(), "3D Geometry")
        tabs.addTab(self._converter_tab(), "Converters")

        main = QWidget()
        main_layout = QVBoxLayout()

        # Header with toggle
        header_layout = QHBoxLayout()
        header_label = QLabel("All-in-One Calculator • 2D/3D • Currency & Unit Converters")
        header_label.setStyleSheet("font-size:20px; font-weight:700; padding:6px;")
        toggle_btn = QPushButton("🌙 Dark Mode")
        toggle_btn.clicked.connect(self.toggle_theme)
        header_layout.addWidget(header_label)
        header_layout.addStretch()
        header_layout.addWidget(toggle_btn)

        main_layout.addLayout(header_layout)
        main_layout.addWidget(tabs)
        main.setLayout(main_layout)
        self.setCentralWidget(main)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.setStyleSheet(DARK_STYLE)
        else:
            self.setStyleSheet(LIGHT_STYLE)

    # ===== Tabs =====
    def _calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.calc_input = QLineEdit()
        self.calc_input.setPlaceholderText("Enter expression (e.g., 2+3*math.sin(1))")
        self.calc_result = QLabel("Result: ")
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self._calculate)

        layout.addWidget(self.calc_input)
        layout.addWidget(calc_btn)
        layout.addWidget(self.calc_result)
        tab.setLayout(layout)
        return tab

    def _calculate(self):
        try:
            expr = self.calc_input.text()
            result = eval(expr, {"math": math, "__builtins__": {}})
            self.calc_result.setText(f"Result: {result}")
        except Exception as e:
            self.calc_result.setText(f"Error: {e}")

    def _geometry2d_tab(self):
        tab = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Shape:"), 0, 0)
        self.shape_2d = QComboBox()
        self.shape_2d.addItems(["Circle", "Rectangle", "Triangle"])
        layout.addWidget(self.shape_2d, 0, 1)

        layout.addWidget(QLabel("Dimension 1:"), 1, 0)
        self.dim1_2d = QLineEdit()
        layout.addWidget(self.dim1_2d, 1, 1)

        layout.addWidget(QLabel("Dimension 2:"), 2, 0)
        self.dim2_2d = QLineEdit()
        layout.addWidget(self.dim2_2d, 2, 1)

        self.result_2d = QLabel("Area: -")
        calc_btn = QPushButton("Calculate Area")
        calc_btn.clicked.connect(self._calc_area_2d)

        layout.addWidget(calc_btn, 3, 0, 1, 2)
        layout.addWidget(self.result_2d, 4, 0, 1, 2)

        tab.setLayout(layout)
        return tab

    def _calc_area_2d(self):
        try:
            shape = self.shape_2d.currentText()
            d1 = float(self.dim1_2d.text())
            d2 = float(self.dim2_2d.text() or 0)
            if shape == "Circle":
                area = math.pi * d1 ** 2
            elif shape == "Rectangle":
                area = d1 * d2
            elif shape == "Triangle":
                area = 0.5 * d1 * d2
            else:
                area = 0
            self.result_2d.setText(f"Area: {area}")
        except:
            self.result_2d.setText("Error")

    def _geometry3d_tab(self):
        tab = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Shape:"), 0, 0)
        self.shape_3d = QComboBox()
        self.shape_3d.addItems(["Sphere", "Cube", "Cylinder"])
        layout.addWidget(self.shape_3d, 0, 1)

        layout.addWidget(QLabel("Dimension 1:"), 1, 0)
        self.dim1_3d = QLineEdit()
        layout.addWidget(self.dim1_3d, 1, 1)

        layout.addWidget(QLabel("Dimension 2:"), 2, 0)
        self.dim2_3d = QLineEdit()
        layout.addWidget(self.dim2_3d, 2, 1)

        self.result_3d = QLabel("Volume: -")
        calc_btn = QPushButton("Calculate Volume")
        calc_btn.clicked.connect(self._calc_vol_3d)

        layout.addWidget(calc_btn, 3, 0, 1, 2)
        layout.addWidget(self.result_3d, 4, 0, 1, 2)

        tab.setLayout(layout)
        return tab

    def _calc_vol_3d(self):
        try:
            shape = self.shape_3d.currentText()
            d1 = float(self.dim1_3d.text())
            d2 = float(self.dim2_3d.text() or 0)
            if shape == "Sphere":
                vol = (4/3) * math.pi * d1 ** 3
            elif shape == "Cube":
                vol = d1 ** 3
            elif shape == "Cylinder":
                vol = math.pi * d1 ** 2 * d2
            else:
                vol = 0
            self.result_3d.setText(f"Volume: {vol}")
        except:
            self.result_3d.setText("Error")

    def _converter_tab(self):
        tab = QWidget()
        layout = QGridLayout()

        # Currency converter (static example)
        layout.addWidget(QLabel("Currency (USD→EUR):"), 0, 0)
        self.curr_usd = QLineEdit()
        layout.addWidget(self.curr_usd, 0, 1)
        btn_curr = QPushButton("Convert")
        btn_curr.clicked.connect(self._convert_currency)
        self.curr_result = QLabel("EUR: -")
        layout.addWidget(btn_curr, 0, 2)
        layout.addWidget(self.curr_result, 0, 3)

        # Length converter
        layout.addWidget(QLabel("Length (meters→feet):"), 1, 0)
        self.len_m = QLineEdit()
        layout.addWidget(self.len_m, 1, 1)
        btn_len = QPushButton("Convert")
        btn_len.clicked.connect(self._convert_length)
        self.len_result = QLabel("Feet: -")
        layout.addWidget(btn_len, 1, 2)
        layout.addWidget(self.len_result, 1, 3)

        tab.setLayout(layout)
        return tab

    def _convert_currency(self):
        try:
            usd = float(self.curr_usd.text())
            eur = usd * 0.92  # example static rate
            self.curr_result.setText(f"EUR: {eur}")
        except:
            self.curr_result.setText("Error")

    def _convert_length(self):
        try:
            meters = float(self.len_m.text())
            feet = meters * 3.28084
            self.len_result.setText(f"Feet: {feet}")
        except:
            self.len_result.setText("Error")

# ===== Run App =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

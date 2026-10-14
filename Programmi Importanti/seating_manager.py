import sys
import random
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QMessageBox, QFileDialog,
    QGridLayout, QComboBox, QSpinBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtPrintSupport import QPrinter


# -------------------- Seat Button --------------------
class SeatButton(QPushButton):
    def __init__(self, row, col, parent=None):
        super().__init__("", parent)
        self.row = row
        self.col = col
        self.active = False
        self.student = None
        self.update_style()

    def toggle_active(self):
        self.active = not self.active
        if not self.active:
            self.student = None
            self.setText("")
        self.update_style()

    def update_style(self):
        if self.active:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #2E7D32;
                    border-radius: 8px;
                    border: 1px solid #1B5E20;
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #388E3C;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #424242;
                    border-radius: 8px;
                    border: 1px solid #212121;
                    color: #BDBDBD;
                }
                QPushButton:hover {
                    background-color: #616161;
                }
            """)


# -------------------- Main Window --------------------
class SeatingMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestione Aula - Seating Manager")
        self.resize(1100, 750)

        self.rows = 6
        self.cols = 6
        self.students = []
        self.student_prefs = {}
        self.seat_buttons = []

        self._build_ui()
        self.apply_dark_theme()

    # ---------- UI ----------
    def _build_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout(main_widget)

        # Pannello laterale
        side_panel = QWidget()
        side_layout = QVBoxLayout(side_panel)

        # ---- input studenti ----
        side_layout.addWidget(QLabel("Inserisci studenti:"))
        self.students_edit = QTextEdit()
        self.students_edit.setPlaceholderText("Mario\nLuigi [nondavanti]\nAnna [nondietro]")
        side_layout.addWidget(self.students_edit)

        self.confirm_btn = QPushButton("Conferma studenti")
        self.confirm_btn.clicked.connect(self.confirm_students)
        side_layout.addWidget(self.confirm_btn)

        # ---- impostazioni griglia ----
        side_layout.addWidget(QLabel("Configura griglia:"))
        row_layout = QHBoxLayout()
        row_layout.addWidget(QLabel("Righe:"))
        self.rows_spin = QSpinBox()
        self.rows_spin.setRange(1, 20)
        self.rows_spin.setValue(self.rows)
        row_layout.addWidget(self.rows_spin)
        side_layout.addLayout(row_layout)

        col_layout = QHBoxLayout()
        col_layout.addWidget(QLabel("Colonne:"))
        self.cols_spin = QSpinBox()
        self.cols_spin.setRange(1, 20)
        self.cols_spin.setValue(self.cols)
        col_layout.addWidget(self.cols_spin)
        side_layout.addLayout(col_layout)

        self.apply_grid_btn = QPushButton("Applica griglia")
        self.apply_grid_btn.clicked.connect(self.apply_grid_size)
        side_layout.addWidget(self.apply_grid_btn)

        # ---- direzione davanti ----
        side_layout.addWidget(QLabel("Davanti:"))
        self.front_selector = QComboBox()
        self.front_selector.addItems(["Sopra", "Sotto"])
        side_layout.addWidget(self.front_selector)

        # ---- azioni ----
        self.random_btn = QPushButton("Randomizza")
        self.random_btn.clicked.connect(self.randomize_seating)
        side_layout.addWidget(self.random_btn)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_all)
        side_layout.addWidget(self.reset_btn)

        self.save_btn = QPushButton("Salva JSON")
        self.save_btn.clicked.connect(self.save_to_file)
        side_layout.addWidget(self.save_btn)

        self.load_btn = QPushButton("Carica JSON")
        self.load_btn.clicked.connect(self.load_from_file)
        side_layout.addWidget(self.load_btn)

        self.export_pdf_btn = QPushButton("Esporta PDF")
        self.export_pdf_btn.clicked.connect(self.export_pdf)
        side_layout.addWidget(self.export_pdf_btn)

        self.export_img_btn = QPushButton("Esporta Immagine (PNG/JPEG)")
        self.export_img_btn.clicked.connect(self.export_image)
        side_layout.addWidget(self.export_img_btn)

        side_layout.addStretch()
        layout.addWidget(side_panel, 2)

        # Griglia
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(5)
        layout.addWidget(self.grid_widget, 5)

        self.build_grid(self.rows, self.cols)

    def build_grid(self, rows, cols):
        # clear
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.seat_buttons.clear()
        for r in range(rows):
            for c in range(cols):
                seat = SeatButton(r, c)
                seat.clicked.connect(seat.toggle_active)
                self.grid_layout.addWidget(seat, r, c)
                self.seat_buttons.append(seat)

    def apply_grid_size(self):
        self.rows = self.rows_spin.value()
        self.cols = self.cols_spin.value()
        self.build_grid(self.rows, self.cols)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #303030;
            }
            QLabel {
                color: #FFFFFF;
                font-weight: bold;
            }
            QTextEdit {
                background-color: #424242;
                color: #FFFFFF;
                border: 1px solid #616161;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #1976D2;
                border-radius: 8px;
                color: white;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #2196F3;
            }
        """)

    # ---------- Students ----------
    def confirm_students(self):
        text = self.students_edit.toPlainText().strip()
        self.students = []
        self.student_prefs = {}
        if not text:
            return
        raw = [x.strip() for part in text.split("\n") for x in part.split(",")]
        for item in raw:
            if not item:
                continue
            name = item
            prefs = {}
            if "[nondavanti]" in item.lower():
                name = name.replace("[nondavanti]", "").strip()
                prefs["nondavanti"] = True
            if "[nondietro]" in item.lower():
                name = name.replace("[nondietro]", "").strip()
                prefs["nondietro"] = True
            self.students.append(name)
            if prefs:
                self.student_prefs[name] = prefs
        QMessageBox.information(self, "Confermato", f"{len(self.students)} studenti caricati.")

    # ---------- Randomize ----------
    def randomize_seating(self):
        active_seats = [s for s in self.seat_buttons if s.active]
        if len(self.students) > len(active_seats):
            QMessageBox.critical(self, "Errore", "Troppi studenti rispetto ai banchi attivi!")
            return

        # davanti/dietro
        if self.front_selector.currentText() == "Sopra":
            front_row = 0
            back_row = self.rows - 1
        else:
            front_row = self.rows - 1
            back_row = 0

        for s in active_seats:
            s.student = None
            s.setText("")

        shuffled = self.students[:]
        random.shuffle(shuffled)

        for student in shuffled:
            prefs = self.student_prefs.get(student, {})
            possible_seats = []
            for seat in active_seats:
                if seat.student is not None:
                    continue
                if prefs.get("nondavanti") and seat.row == front_row:
                    continue
                if prefs.get("nondietro") and seat.row == back_row:
                    continue
                possible_seats.append(seat)

            if not possible_seats:
                QMessageBox.critical(self, "Errore",
                                     f"Impossibile assegnare posto a {student} rispettando i vincoli.")
                return

            seat = random.choice(possible_seats)
            seat.student = student
            seat.setText(student)

    # ---------- Reset ----------
    def reset_all(self):
        self.students = []
        self.student_prefs = {}
        self.students_edit.clear()
        self.rows = 6
        self.cols = 6
        self.rows_spin.setValue(self.rows)
        self.cols_spin.setValue(self.cols)
        self.build_grid(self.rows, self.cols)

        for seat in self.seat_buttons:
            seat.active = False
            seat.student = None
            seat.setText("")
            seat.update_style()

        QMessageBox.information(self, "Reset", "Tutto è stato resettato.")

    # ---------- Save / Load ----------
    def save_to_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Salva disposizione", "", "JSON Files (*.json)")
        if not filename:
            return
        data = {
            "rows": self.rows,
            "cols": self.cols,
            "students": self.students,
            "prefs": self.student_prefs,
            "seats": [
                {"row": s.row, "col": s.col, "active": s.active, "student": s.student}
                for s in self.seat_buttons
            ]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Carica disposizione", "", "JSON Files (*.json)")
        if not filename:
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.rows = data.get("rows", 6)
        self.cols = data.get("cols", 6)
        self.rows_spin.setValue(self.rows)
        self.cols_spin.setValue(self.cols)
        self.build_grid(self.rows, self.cols)
        self.students = data.get("students", [])
        self.student_prefs = data.get("prefs", {})

        for seat_info in data.get("seats", []):
            for s in self.seat_buttons:
                if s.row == seat_info["row"] and s.col == seat_info["col"]:
                    s.active = seat_info["active"]
                    s.student = seat_info["student"]
                    s.setText(s.student if s.student else "")
                    s.update_style()

    # ---------- Export ----------
    def export_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Esporta PDF", "", "PDF Files (*.pdf)")
        if not filename:
            return
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QPainter(printer)
        self.grid_widget.render(painter)
        painter.end()

    def export_image(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Esporta Immagine", "", "PNG Files (*.png);;JPEG Files (*.jpg)")
        if not filename:
            return
        pixmap = self.grid_widget.grab()
        pixmap.save(filename)


# -------------------- Run --------------------
def main():
    app = QApplication(sys.argv)
    window = SeatingMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

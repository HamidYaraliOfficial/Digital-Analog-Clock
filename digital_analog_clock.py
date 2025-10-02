import sys
import math
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,
    QPushButton, QTextEdit, QLabel, QStyleFactory, QTabWidget, QGridLayout,
    QScrollArea, QMenuBar, QMenu, QFileDialog, QMessageBox, QLineEdit, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QIcon, QPalette, QColor, QFont, QPainter, QPen, QBrush
import json
from pathlib import Path
import pytz

# Developed by Hamid Yarali
# GitHub: https://github.com/HamidYaraliOfficial
# Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==
# Telegram: @Hamid_Yarali

class ClockWidget(QWidget):
    def __init__(self, timezone, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.time = datetime.now()
        self.timezone = pytz.timezone(timezone)

    def set_timezone(self, timezone):
        self.timezone = pytz.timezone(timezone)
        self.update()

    def update_time(self):
        self.time = datetime.now(self.timezone)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        size = min(self.width(), self.height())
        center = self.rect().center()
        radius = size // 2 - 15

        # Draw clock face
        painter.setPen(QPen(QColor(0, 0, 0), 2))
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawEllipse(center, radius, radius)

        # Draw hour markers
        for i in range(12):
            angle = i * 30 * math.pi / 180
            x1 = center.x() + (radius - 8) * math.cos(angle)
            y1 = center.y() + (radius - 8) * math.sin(angle)
            x2 = center.x() + radius * math.cos(angle)
            y2 = center.y() + radius * math.sin(angle)
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Draw minute markers
        for i in range(60):
            if i % 5 != 0:
                angle = i * 6 * math.pi / 180
                x1 = center.x() + (radius - 4) * math.cos(angle)
                y1 = center.y() + (radius - 4) * math.sin(angle)
                x2 = center.x() + radius * math.cos(angle)
                y2 = center.y() + radius * math.sin(angle)
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Draw hour hand
        hour = self.time.hour % 12 + self.time.minute / 60
        hour_angle = (hour * 30) * math.pi / 180
        hour_x = center.x() + (radius - 40) * math.cos(hour_angle)
        hour_y = center.y() + (radius - 40) * math.sin(hour_angle)
        painter.setPen(QPen(QColor(0, 0, 0), 5))
        painter.drawLine(center.x(), center.y(), int(hour_x), int(hour_y))

        # Draw minute hand
        minute = self.time.minute + self.time.second / 60
        minute_angle = minute * 6 * math.pi / 180
        minute_x = center.x() + (radius - 25) * math.cos(minute_angle)
        minute_y = center.y() + (radius - 25) * math.sin(minute_angle)
        painter.setPen(QPen(QColor(0, 0, 0), 3))
        painter.drawLine(center.x(), center.y(), int(minute_x), int(minute_y))

        # Draw second hand
        second = self.time.second
        second_angle = second * 6 * math.pi / 180
        second_x = center.x() + (radius - 15) * math.cos(second_angle)
        second_y = center.y() + (radius - 15) * math.sin(second_angle)
        painter.setPen(QPen(QColor(200, 0, 0), 2))
        painter.drawLine(center.x(), center.y(), int(second_x), int(second_y))

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital & Analog Clock")
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowIcon(QIcon('icon.ico'))  # Assuming an icon file exists
        
        # Language and theme settings
        self.current_lang = 'en'
        self.current_theme = 'Windows'
        self.time_format = '24'
        self.timezones = ['Asia/Tehran']  # Default with Iran
        self.clocks = []
        self.history = []
        self.load_history()
        
        # Language dictionaries
        self.texts = {
            'en': {
                'title': 'Digital & Analog Clock',
                'timezone_label': 'Select Timezone:',
                'add_timezone_btn': 'Add Timezone',
                'remove_timezone_btn': 'Remove Selected',
                'format_label': 'Time Format:',
                'digital_label': 'Digital Clocks:',
                'analog_label': 'Analog Clocks:',
                'history_tab': 'Time Check History',
                'settings_tab': 'Settings',
                'language_label': 'Language:',
                'theme_label': 'Theme:',
                'clear_history': 'Clear History',
                'status_idle': 'Displaying current time...',
                'status_updated': 'Time updated: {time}',
                'status_added': 'Timezone {tz} added',
                'status_removed': 'Timezone {tz} removed',
                'history_time': 'Time',
                'history_timezone': 'Timezone',
                'history_date': 'Date',
                'save_history': 'Save History to File',
                'apply': 'Apply',
                'file_menu': 'File',
                'exit_action': 'Exit',
                'about': 'About',
                'about_text': 'Digital & Analog Clock\nVersion 1.0\nDeveloped by Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': 'Copy Time',
                'format_12': '12-Hour',
                'format_24': '24-Hour'
            },
            'fa': {
                'title': 'ساعت دیجیتال و عقربه‌ای',
                'timezone_label': 'انتخاب منطقه زمانی:',
                'add_timezone_btn': 'افزودن منطقه زمانی',
                'remove_timezone_btn': 'حذف انتخاب‌شده',
                'format_label': 'فرمت زمان:',
                'digital_label': 'ساعت‌های دیجیتال:',
                'analog_label': 'ساعت‌های عقربه‌ای:',
                'history_tab': 'تاریخچه بررسی زمان',
                'settings_tab': 'تنظیمات',
                'language_label': 'زبان:',
                'theme_label': 'تم:',
                'clear_history': 'پاک کردن تاریخچه',
                'status_idle': 'نمایش زمان کنونی...',
                'status_updated': 'زمان به‌روزرسانی شد: {time}',
                'status_added': 'منطقه زمانی {tz} اضافه شد',
                'status_removed': 'منطقه زمانی {tz} حذف شد',
                'history_time': 'زمان',
                'history_timezone': 'منطقه زمانی',
                'history_date': 'تاریخ',
                'save_history': 'ذخیره تاریخچه در فایل',
                'apply': 'اعمال',
                'file_menu': 'فایل',
                'exit_action': 'خروج',
                'about': 'درباره',
                'about_text': 'ساعت دیجیتال و عقربه‌ای\nنسخه 1.0\nتوسعه‌یافته توسط حمید یارعلی\nگیت‌هاب: https://github.com/HamidYaraliOfficial\nاینستاگرام: https://www.instagram.com/hamidyaraliofficial\nتلگرام: @Hamid_Yarali',
                'copy_btn': 'کپی زمان',
                'format_12': '12 ساعته',
                'format_24': '24 ساعته'
            },
            'zh': {
                'title': '数字与模拟时钟',
                'timezone_label': '选择时区：',
                'add_timezone_btn': '添加时区',
                'remove_timezone_btn': '移除选定',
                'format_label': '时间格式：',
                'digital_label': '数字时钟：',
                'analog_label': '模拟时钟：',
                'history_tab': '时间检查历史',
                'settings_tab': '设置',
                'language_label': '语言：',
                'theme_label': '主题：',
                'clear_history': '清除历史记录',
                'status_idle': '显示当前时间...',
                'status_updated': '时间已更新：{time}',
                'status_added': '已添加时区 {tz}',
                'status_removed': '已移除时区 {tz}',
                'history_time': '时间',
                'history_timezone': '时区',
                'history_date': '日期',
                'save_history': '将历史记录保存到文件',
                'apply': '应用',
                'file_menu': '文件',
                'exit_action': '退出',
                'about': '关于',
                'about_text': '数字与模拟时钟\n版本 1.0\n由 Hamid Yarali 开发\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': '复制时间',
                'format_12': '12小时制',
                'format_24': '24小时制'
            },
            'ru': {
                'title': 'Цифровые и аналоговые часы',
                'timezone_label': 'Часовой пояс:',
                'add_timezone_btn': 'Добавить часовой пояс',
                'remove_timezone_btn': 'Удалить выбранный',
                'format_label': 'Формат времени:',
                'digital_label': 'Цифровые часы:',
                'analog_label': 'Аналоговые часы:',
                'history_tab': 'История проверки времени',
                'settings_tab': 'Настройки',
                'language_label': 'Язык:',
                'theme_label': 'Тема:',
                'clear_history': 'Очистить историю',
                'status_idle': 'Отображение текущего времени...',
                'status_updated': 'Время обновлено: {time}',
                'status_added': 'Часовой пояс {tz} добавлен',
                'status_removed': 'Часовой пояс {tz} удален',
                'history_time': 'Время',
                'history_timezone': 'Часовой пояс',
                'history_date': 'Дата',
                'save_history': 'Сохранить историю в файл',
                'apply': 'Применить',
                'file_menu': 'Файл',
                'exit_action': 'Выход',
                'about': 'О программе',
                'about_text': 'Цифровые и аналоговые часы\nВерсия 1.0\nРазработано Hamid Yarali\nGitHub: https://github.com/HamidYaraliOfficial\nInstagram: https://www.instagram.com/hamidyaraliofficial\nTelegram: @Hamid_Yarali',
                'copy_btn': 'Копировать время',
                'format_12': '12-часовой',
                'format_24': '24-часовой'
            }
        }

        # Theme dictionaries
        self.themes = {
            'Windows': {
                'background': QColor(245, 245, 245),
                'text': QColor(0, 0, 0),
                'button': QColor(230, 230, 230),
                'button_text': QColor(0, 0, 0),
                'button_hover': QColor(200, 200, 200),
                'accent': QColor(0, 120, 212),
                'border': QColor(180, 180, 180),
                'header': QColor(220, 220, 220)
            },
            'Dark': {
                'background': QColor(32, 32, 32),
                'text': QColor(230, 230, 230),
                'button': QColor(50, 50, 50),
                'button_text': QColor(230, 230, 230),
                'button_hover': QColor(70, 70, 70),
                'accent': QColor(0, 120, 212),
                'border': QColor(80, 80, 80),
                'header': QColor(40, 40, 40)
            },
            'Red': {
                'background': QColor(255, 235, 235),
                'text': QColor(80, 0, 0),
                'button': QColor(255, 200, 200),
                'button_text': QColor(80, 0, 0),
                'button_hover': QColor(255, 180, 180),
                'accent': QColor(200, 0, 0),
                'border': QColor(220, 150, 150),
                'header': QColor(255, 220, 220)
            },
            'Blue': {
                'background': QColor(235, 245, 255),
                'text': QColor(0, 0, 80),
                'button': QColor(200, 220, 255),
                'button_text': QColor(0, 0, 80),
                'button_hover': QColor(180, 200, 255),
                'accent': QColor(0, 0, 200),
                'border': QColor(150, 180, 220),
                'header': QColor(220, 235, 255)
            }
        }

        # Initialize UI
        self.init_ui()
        self.apply_theme(self.current_theme)
        self.update_texts()

        # Timer for updating clocks
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clocks)
        self.timer.start(1000)

    def init_ui(self):
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Menu bar
        self.menu_bar = QMenuBar()
        self.file_menu = QMenu(self.texts['en']['file_menu'])
        self.exit_action = self.file_menu.addAction(self.texts['en']['exit_action'])
        self.exit_action.triggered.connect(self.close)
        self.about_action = self.file_menu.addAction(self.texts['en']['about'])
        self.about_action.triggered.connect(self.show_about)
        self.menu_bar.addMenu(self.file_menu)
        self.main_layout.addWidget(self.menu_bar)

        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
            QTabBar::tab {
                padding: 10px 20px;
                margin-right: 5px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                background: rgba(0, 0, 0, 0.05);
                color: black;
            }
            QTabBar::tab:selected {
                background: rgba(0, 120, 212, 0.3);
                font-weight: bold;
                color: black;
            }
        """)
        self.main_layout.addWidget(self.tabs)

        # Clock tab
        self.clock_tab = QWidget()
        self.clock_layout = QVBoxLayout(self.clock_tab)
        self.clock_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.clock_layout.setSpacing(10)

        # Timezone selection
        self.timezone_label = QLabel()
        self.timezone_label.setFont(QFont("Segoe UI", 12))
        self.timezone_combo = QComboBox()
        self.timezone_combo.addItems(pytz.common_timezones)
        self.timezone_combo.setCurrentText('Asia/Tehran')
        self.timezone_combo.setFixedHeight(40)
        self.timezone_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        # Add/Remove timezone buttons
        self.add_timezone_btn = QPushButton()
        self.add_timezone_btn.setFixedHeight(40)
        self.add_timezone_btn.setFont(QFont("Segoe UI", 12))
        self.add_timezone_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.add_timezone_btn.clicked.connect(self.add_timezone)

        self.remove_timezone_btn = QPushButton()
        self.remove_timezone_btn.setFixedHeight(40)
        self.remove_timezone_btn.setFont(QFont("Segoe UI", 12))
        self.remove_timezone_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(200, 0, 0, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(200, 0, 0, 1.0);
            }
        """)
        self.remove_timezone_btn.clicked.connect(self.remove_timezone)

        # Time format selection
        self.format_label = QLabel()
        self.format_label.setFont(QFont("Segoe UI", 12))
        self.format_combo = QComboBox()
        self.format_combo.addItems([self.texts['en']['format_12'], self.texts['en']['format_24']])
        self.format_combo.setFixedHeight(40)
        self.format_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.format_combo.currentIndexChanged.connect(self.change_format)

        # Timezone list
        self.timezone_list = QListWidget()
        self.timezone_list.setFixedHeight(100)
        self.timezone_list.setStyleSheet("""
            QListWidget {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)
        for tz in self.timezones:
            self.timezone_list.addItem(tz)

        # Digital clocks
        self.digital_label = QLabel()
        self.digital_label.setFont(QFont("Segoe UI", 12))
        self.digital_container = QWidget()
        self.digital_layout = QGridLayout(self.digital_container)
        self.digital_layout.setSpacing(10)

        # Analog clocks
        self.analog_label = QLabel()
        self.analog_label.setFont(QFont("Segoe UI", 12))
        self.analog_container = QWidget()
        self.analog_layout = QGridLayout(self.analog_container)
        self.analog_layout.setSpacing(10)

        # Copy button
        self.copy_btn = QPushButton()
        self.copy_btn.setFixedHeight(40)
        self.copy_btn.setFont(QFont("Segoe UI", 12))
        self.copy_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.copy_btn.clicked.connect(self.copy_to_clipboard)

        # Status text
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setFixedHeight(100)
        self.status_text.setStyleSheet("""
            QTextEdit {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
        """)

        # Layout for clock tab
        timezone_layout = QHBoxLayout()
        timezone_layout.addWidget(self.timezone_combo)
        timezone_layout.addWidget(self.add_timezone_btn)
        timezone_layout.addWidget(self.remove_timezone_btn)

        self.clock_layout.addWidget(self.timezone_label)
        self.clock_layout.addLayout(timezone_layout)
        self.clock_layout.addWidget(self.timezone_list)
        self.clock_layout.addWidget(self.format_label)
        self.clock_layout.addWidget(self.format_combo)
        self.clock_layout.addWidget(self.digital_label)
        self.clock_layout.addWidget(self.digital_container)
        self.clock_layout.addWidget(self.analog_label)
        self.clock_layout.addWidget(self.analog_container)
        self.clock_layout.addWidget(self.copy_btn)
        self.clock_layout.addWidget(self.status_text)

        # History tab
        self.history_tab = QWidget()
        self.history_layout = QVBoxLayout(self.history_tab)
        self.history_scroll = QScrollArea()
        self.history_scroll.setWidgetResizable(True)
        self.history_content = QWidget()
        self.history_grid = QGridLayout(self.history_content)
        self.history_grid.setSpacing(10)
        self.history_scroll.setWidget(self.history_content)
        self.history_scroll.setStyleSheet("""
            QScrollArea {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.95);
            }
        """)
        self.clear_history_btn = QPushButton()
        self.clear_history_btn.setFixedHeight(40)
        self.clear_history_btn.setFont(QFont("Segoe UI", 12))
        self.clear_history_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(200, 0, 0, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(200, 0, 0, 1.0);
            }
        """)
        self.clear_history_btn.clicked.connect(self.clear_history)
        self.save_history_btn = QPushButton()
        self.save_history_btn.setFixedHeight(40)
        self.save_history_btn.setFont(QFont("Segoe UI", 12))
        self.save_history_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.save_history_btn.clicked.connect(self.save_history_to_file)
        self.history_layout.addWidget(self.history_scroll)
        self.history_layout.addWidget(self.clear_history_btn)
        self.history_layout.addWidget(self.save_history_btn)

        # Settings tab
        self.settings_tab = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_tab)
        self.settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.settings_layout.setSpacing(10)

        self.language_label = QLabel()
        self.language_label.setFont(QFont("Segoe UI", 12))
        self.language_combo = QComboBox()
        self.language_combo.addItems(['English', 'فارسی', '中文', 'Русский'])
        self.language_combo.setFixedHeight(40)
        self.language_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.language_combo.currentIndexChanged.connect(self.change_language)

        self.theme_label = QLabel()
        self.theme_label.setFont(QFont("Segoe UI", 12))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Windows', 'Dark', 'Red', 'Blue'])
        self.theme_combo.setFixedHeight(40)
        self.theme_combo.setStyleSheet("""
            QComboBox {
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 0.95);
                color: black;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        self.apply_btn = QPushButton()
        self.apply_btn.setFixedHeight(40)
        self.apply_btn.setFont(QFont("Segoe UI", 12))
        self.apply_btn.setStyleSheet("""
            QPushButton {
                border-radius: 8px;
                font-size: 14px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                background: rgba(0, 120, 212, 0.8);
                color: white;
            }
            QPushButton:hover {
                background: rgba(0, 120, 212, 1.0);
            }
        """)
        self.apply_btn.clicked.connect(self.apply_settings)

        self.settings_layout.addWidget(self.language_label)
        self.settings_layout.addWidget(self.language_combo)
        self.settings_layout.addWidget(self.theme_label)
        self.settings_layout.addWidget(self.theme_combo)
        self.settings_layout.addWidget(self.apply_btn)
        self.settings_layout.addStretch()

        # Add tabs
        self.tabs.addTab(self.clock_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.history_tab, self.texts['en']['history_tab'])
        self.tabs.addTab(self.settings_tab, self.texts['en']['settings_tab'])

        # Initialize clocks
        self.update_clocks_ui()
        self.update_clocks()

    def apply_theme(self, theme_name):
        palette = QPalette()
        theme = self.themes.get(theme_name, self.themes['Windows'])
        palette.setColor(QPalette.ColorRole.Window, theme['background'])
        palette.setColor(QPalette.ColorRole.WindowText, theme['text'])
        palette.setColor(QPalette.ColorRole.Button, theme['button'])
        palette.setColor(QPalette.ColorRole.ButtonText, theme['button_text'])
        palette.setColor(QPalette.ColorRole.Highlight, theme['accent'])
        palette.setColor(QPalette.ColorRole.Base, theme['background'])
        palette.setColor(QPalette.ColorRole.AlternateBase, theme['header'])
        palette.setColor(QPalette.ColorRole.Text, theme['text'])
        self.setPalette(palette)
        self.setStyle(QStyleFactory.create('WindowsVista' if theme_name == 'Windows' else 'Fusion'))

    def update_texts(self):
        lang = self.current_lang
        self.setWindowTitle(self.texts[lang]['title'])
        self.timezone_label.setText(self.texts[lang]['timezone_label'])
        self.add_timezone_btn.setText(self.texts[lang]['add_timezone_btn'])
        self.remove_timezone_btn.setText(self.texts[lang]['remove_timezone_btn'])
        self.format_label.setText(self.texts[lang]['format_label'])
        self.digital_label.setText(self.texts[lang]['digital_label'])
        self.analog_label.setText(self.texts[lang]['analog_label'])
        self.copy_btn.setText(self.texts[lang]['copy_btn'])
        self.status_text.setText(self.texts[lang]['status_idle'])
        self.clear_history_btn.setText(self.texts[lang]['clear_history'])
        self.save_history_btn.setText(self.texts[lang]['save_history'])
        self.language_label.setText(self.texts[lang]['language_label'])
        self.theme_label.setText(self.texts[lang]['theme_label'])
        self.apply_btn.setText(self.texts[lang]['apply'])
        self.file_menu.setTitle(self.texts[lang]['file_menu'])
        self.exit_action.setText(self.texts[lang]['exit_action'])
        self.about_action.setText(self.texts[lang]['about'])
        self.tabs.setTabText(0, self.texts[lang]['history_tab'])
        self.tabs.setTabText(1, self.texts[lang]['history_tab'])
        self.tabs.setTabText(2, self.texts[lang]['settings_tab'])

        # Update format combo
        current_format = self.format_combo.currentText()
        self.format_combo.clear()
        self.format_combo.addItems([self.texts[lang]['format_12'], self.texts[lang]['format_24']])
        if current_format:
            index = 0 if current_format == self.texts['en']['format_12'] else 1
            self.format_combo.setCurrentIndex(index)

        # Set text alignment
        alignment = Qt.AlignmentFlag.AlignRight if lang == 'fa' else Qt.AlignmentFlag.AlignLeft
        self.timezone_label.setAlignment(alignment)
        self.format_label.setAlignment(alignment)
        self.digital_label.setAlignment(alignment)
        self.analog_label.setAlignment(alignment)
        self.language_label.setAlignment(alignment)
        self.theme_label.setAlignment(alignment)

    def change_language(self, index):
        langs = ['en', 'fa', 'zh', 'ru']
        self.current_lang = langs[index]
        self.update_texts()
        self.update_history_ui()
        self.update_clocks()

    def change_theme(self, index):
        themes = ['Windows', 'Dark', 'Red', 'Blue']
        self.current_theme = themes[index]
        self.apply_theme(self.current_theme)

    def change_format(self, index):
        self.time_format = '12' if index == 0 else '24'
        self.update_clocks()

    def apply_settings(self):
        self.update_texts()
        self.apply_theme(self.current_theme)
        self.update_clocks()

    def show_about(self):
        QMessageBox.information(self, self.texts[self.current_lang]['about'], 
                               self.texts[self.current_lang]['about_text'])

    def add_timezone(self):
        timezone = self.timezone_combo.currentText()
        if timezone not in self.timezones:
            self.timezones.append(timezone)
            self.timezone_list.addItem(timezone)
            self.update_clocks_ui()
            self.status_text.setText(self.texts[self.current_lang]['status_added'].format(tz=timezone))
            self.add_to_history(timezone)

    def remove_timezone(self):
        selected = self.timezone_list.currentItem()
        if selected and len(self.timezones) > 1:  # Keep at least one timezone
            timezone = selected.text()
            self.timezones.remove(timezone)
            self.timezone_list.takeItem(self.timezone_list.row(selected))
            self.update_clocks_ui()
            self.status_text.setText(self.texts[self.current_lang]['status_removed'].format(tz=timezone))
            self.add_to_history(timezone, removed=True)

    def update_clocks_ui(self):
        # Clear existing clocks
        for i in reversed(range(self.digital_layout.count())):
            self.digital_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.analog_layout.count())):
            self.analog_layout.itemAt(i).widget().setParent(None)
        self.clocks = []

        # Add new clocks
        for i, tz in enumerate(self.timezones):
            # Digital clock
            digital_display = QLineEdit()
            digital_display.setReadOnly(True)
            digital_display.setFixedHeight(40)
            digital_display.setStyleSheet("""
                QLineEdit {
                    border-radius: 8px;
                    padding: 8px;
                    font-size: 14px;
                    border: 1px solid rgba(0, 0, 0, 0.2);
                    background: rgba(255, 255, 255, 0.95);
                    color: black;
                }
            """)
            digital_label = QLabel(tz)
            digital_label.setFont(QFont("Segoe UI", 10))
            digital_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.digital_layout.addWidget(digital_label, i * 2, 0)
            self.digital_layout.addWidget(digital_display, i * 2 + 1, 0)

            # Analog clock
            analog_clock = ClockWidget(tz)
            self.analog_layout.addWidget(analog_clock, i // 2, i % 2)
            analog_label = QLabel(tz)
            analog_label.setFont(QFont("Segoe UI", 10))
            analog_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.analog_layout.addWidget(analog_label, (i // 2) + 1, i % 2)

            self.clocks.append((digital_display, analog_clock))

        self.update_clocks()

    def update_clocks(self):
        for i, (digital_display, analog_clock) in enumerate(self.clocks):
            timezone = pytz.timezone(self.timezones[i])
            current_time = datetime.now(timezone)
            format_str = "%I:%M:%S %p" if self.time_format == '12' else "%H:%M:%S"
            time_str = current_time.strftime(format_str)
            digital_display.setText(time_str)
            analog_clock.update_time()
        self.status_text.setText(self.texts[self.current_lang]['status_updated'].format(time=datetime.now(pytz.timezone(self.timezones[0])).strftime(format_str)))

    def copy_to_clipboard(self):
        times = [digital.text() + f" ({tz})" for digital, _ in self.clocks for tz in self.timezones]
        if times:
            QApplication.clipboard().setText("\n".join(times))
            self.status_text.setText(self.texts[self.current_lang]['status_updated'].format(time="Times copied to clipboard"))

    def add_to_history(self, timezone, removed=False):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i, tz in enumerate(self.timezones):
            current_time = datetime.now(pytz.timezone(tz))
            format_str = "%I:%M:%S %p" if self.time_format == '12' else "%H:%M:%S"
            time_str = current_time.strftime(format_str)
            self.history.append({
                'time': time_str,
                'timezone': tz,
                'date': timestamp,
                'action': 'Removed' if removed and tz == timezone else 'Added' if tz == timezone else 'Updated'
            })
        self.save_history()
        self.update_history_ui()

    def save_history(self):
        with open('clock_history.json', 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def load_history(self):
        try:
            with open('clock_history.json', 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = []

    def save_history_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, self.texts[self.current_lang]['save_history'], "", "JSON Files (*.json)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=4)
            self.status_text.setText(self.texts[self.current_lang]['status_updated'].format(time="History saved to file"))

    def update_history_ui(self):
        # Clear existing widgets
        for i in reversed(range(self.history_grid.count())):
            self.history_grid.itemAt(i).widget().setParent(None)

        # Add headers
        headers = [
            self.texts[self.current_lang]['history_time'],
            self.texts[self.current_lang]['history_timezone'],
            self.texts[self.current_lang]['history_date'],
            'Action'
        ]
        for col, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: black;")
            label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            self.history_grid.addWidget(label, 0, col)

        # Add history items
        for row, item in enumerate(self.history, 1):
            time_label = QLabel(item['time'])
            timezone_label = QLabel(item['timezone'])
            date_label = QLabel(item['date'])
            action_label = QLabel(item['action'])
            
            for label in [time_label, timezone_label, date_label, action_label]:
                label.setStyleSheet("font-size: 12px; padding: 5px; border-bottom: 1px solid rgba(0, 0, 0, 0.1); color: black;")
                label.setWordWrap(True)
                label.setAlignment(Qt.AlignmentFlag.AlignRight if self.current_lang == 'fa' else Qt.AlignmentFlag.AlignLeft)
            
            self.history_grid.addWidget(time_label, row, 0)
            self.history_grid.addWidget(timezone_label, row, 1)
            self.history_grid.addWidget(date_label, row, 2)
            self.history_grid.addWidget(action_label, row, 3)

    def clear_history(self):
        self.history = []
        self.save_history()
        self.update_history_ui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = DigitalClock()
    window.show()
    sys.exit(app.exec())
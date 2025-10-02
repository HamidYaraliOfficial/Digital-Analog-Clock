# Digital & Analog Clock

## English

### Overview
The **Digital & Analog Clock** is a versatile desktop application built using Python and PyQt6, designed to display both digital and analog clocks for multiple timezones simultaneously. It includes a user-friendly interface with support for multiple languages, customizable themes, and a history log of timezone changes. The application is perfect for users who need to track time across different regions, with a default inclusion of the Asia/Tehran timezone.

### Features
- **Multi-Timezone Support**: Display multiple digital and analog clocks for different timezones.
- **Customizable Time Format**: Switch between 12-hour and 24-hour time formats.
- **Themed Interface**: Choose from four themes (Windows, Dark, Red, Blue) for a personalized experience.
- **Multilingual Interface**: Supports English, Persian, Chinese, and Russian languages.
- **History Log**: Tracks timezone additions, removals, and updates with timestamps.
- **Copy to Clipboard**: Easily copy the displayed time for all timezones.
- **Save History**: Export the history log to a JSON file for record-keeping.

### Requirements
- Python 3.9 or higher
- PyQt6
- pytz
- A compatible operating system (Windows, macOS, Linux)

### Installation
1. Ensure Python is installed on your system.
2. Install the required dependencies:
   ```bash
   pip install PyQt6 pytz
   ```
3. Download or clone the repository to your local machine.
4. Run the application:
   ```bash
   python digital_analog_clock.py
   ```

### Usage
- **Add Timezones**: Select a timezone from the dropdown and click "Add Timezone" to display its digital and analog clocks.
- **Remove Timezones**: Select a timezone from the list and click "Remove Selected" to remove it (at least one timezone must remain).
- **Change Time Format**: Use the dropdown to switch between 12-hour and 24-hour formats.
- **Change Language/Theme**: Navigate to the Settings tab to select a language or theme, then click "Apply".
- **View History**: Check the History tab to see a log of timezone changes.
- **Copy Time**: Click the "Copy Time" button to copy all displayed times to the clipboard.
- **Save History**: Use the "Save History to File" button to export the history log as a JSON file.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgments
Developed by Hamid Yarali.

---

# ساعت دیجیتال و عقربه‌ای

## فارسی

### معرفی
**ساعت دیجیتال و عقربه‌ای** یک برنامه دسکتاپ چندمنظوره است که با استفاده از پایتون و PyQt6 توسعه یافته و برای نمایش همزمان ساعت‌های دیجیتال و عقربه‌ای برای چندین منطقه زمانی طراحی شده است. این برنامه دارای رابط کاربری ساده و جذابی است که از چندین زبان، تم‌های قابل تنظیم و ثبت تاریخچه تغییرات منطقه زمانی پشتیبانی می‌کند. این برنامه برای کاربرانی که نیاز به پیگیری زمان در مناطق مختلف دارند، با گنجاندن پیش‌فرض منطقه زمانی آسیا/تهران، بسیار مناسب است.

### ویژگی‌ها
- **پشتیبانی از چندین منطقه زمانی**: نمایش چندین ساعت دیجیتال و عقربه‌ای برای مناطق زمانی مختلف.
- **فرمت زمان قابل تنظیم**: امکان انتخاب بین فرمت ۱۲ ساعته و ۲۴ ساعته.
- **رابط کاربری با تم‌های متنوع**: انتخاب از میان چهار تم (ویندوز، تیره، قرمز، آبی) برای تجربه‌ای شخصی‌سازی‌شده.
- **رابط چندزبانه**: پشتیبانی از زبان‌های انگلیسی، فارسی، چینی و روسی.
- **ثبت تاریخچه**: ثبت افزودن، حذف و به‌روزرسانی مناطق زمانی با زمان‌بندی.
- **کپی به کلیپ‌بورد**: کپی آسان زمان‌های نمایش داده شده برای تمام مناطق زمانی.
- **ذخیره تاریخچه**: امکان ذخیره تاریخچه به‌صورت فایل JSON برای نگهداری سوابق.

### پیش‌نیازها
- پایتون نسخه ۳.۹ یا بالاتر
- PyQt6
- pytz
- سیستم‌عامل سازگار (ویندوز، مک‌اواس، لینوکس)

### نصب
1. اطمینان حاصل کنید که پایتون روی سیستم شما نصب است.
2. وابستگی‌های مورد نیاز را نصب کنید:
   ```bash
   pip install PyQt6 pytz
   ```
3. مخزن را دانلود کنید یا به سیستم خود منتقل کنید.
4. برنامه را اجرا کنید:
   ```bash
   python digital_analog_clock.py
   ```

### نحوه استفاده
- **افزودن منطقه زمانی**: یک منطقه زمانی را از منوی کشویی انتخاب کنید و روی «افزودن منطقه زمانی» کلیک کنید تا ساعت دیجیتال و عقربه‌ای آن نمایش داده شود.
- **حذف منطقه زمانی**: یک منطقه زمانی را از لیست انتخاب کنید و روی «حذف انتخاب‌شده» کلیک کنید (حداقل یک منطقه زمانی باید باقی بماند).
- **تغییر فرمت زمان**: از منوی کشویی برای تغییر بین فرمت ۱۲ ساعته و ۲۴ ساعته استفاده کنید.
- **تغییر زبان/تم**: به تب تنظیمات بروید، زبان یا تم را انتخاب کنید و روی «اعمال» کلیک کنید.
- **مشاهده تاریخچه**: به تب تاریخچه بروید تا فهرست تغییرات منطقه زمانی را ببینید.
- **کپی زمان**: روی دکمه «کپی زمان» کلیک کنید تا تمام زمان‌های نمایش داده شده به کلیپ‌بورد کپی شوند.
- **ذخیره تاریخچه**: از دکمه «ذخیره تاریخچه در فایل» برای ذخیره تاریخچه به‌صورت فایل JSON استفاده کنید.

### مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر فایل `LICENSE` را ببینید.

### تقدیر
توسعه‌یافته توسط حمید یارعلی.

---

# 数字与模拟时钟

## 中文

### 概述
**数字与模拟时钟** 是一款使用 Python 和 PyQt6 开发的桌面应用程序，旨在同时显示多个时区的数字和模拟时钟。它具有用户友好的界面，支持多种语言、可自定义主题以及时区更改的历史记录。该应用程序非常适合需要跟踪不同地区时间的用户，默认包含亚洲/德黑兰时区。

### 功能
- **多时区支持**：显示不同时区的多个数字和模拟时钟。
- **可自定义时间格式**：在12小时制和24小时制之间切换。
- **主题化界面**：提供四种主题（Windows、深色、红色、蓝色）以实现个性化体验。
- **多语言界面**：支持英语、波斯语、中文和俄语。
- **历史记录**：记录时区的添加、删除和更新，并带有时间戳。
- **复制到剪贴板**：轻松复制所有显示的时区时间。
- **保存历史记录**：将历史记录导出为 JSON 文件以便记录保存。

### 系统要求
- Python 3.9 或更高版本
- PyQt6
- pytz
- 兼容的操作系统（Windows、macOS、Linux）

### 安装
1. 确保系统中已安装 Python。
2. 安装所需的依赖项：
   ```bash
   pip install PyQt6 pytz
   ```
3. 下载或传输存储库到本地计算机。
4. 运行应用程序：
   ```bash
   python digital_analog_clock.py
   ```

### 使用方法
- **添加时区**：从下拉菜单中选择一个时区，然后点击“添加时区”以显示其数字和模拟时钟。
- **移除时区**：从列表中选择一个时区，然后点击“移除选定”以删除（至少保留一个时区）。
- **更改时间格式**：使用下拉菜单在12小时制和24小时制之间切换。
- **更改语言/主题**：导航到设置选项卡，选择语言或主题，然后点击“应用”。
- **查看历史记录**：在历史记录选项卡中查看时区更改的日志。
- **复制时间**：点击“复制时间”按钮将所有显示的时间复制到剪贴板。
- **保存历史记录**：使用“将历史记录保存到文件”按钮将历史记录导出为 JSON 文件。

### 许可
该项目基于 MIT 许可证发布。详情请见 `LICENSE` 文件。

### 致谢
由 Hamid Yarali 开发。
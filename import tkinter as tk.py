import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def generate_schedule_gui():
    regions_input = entry_regions.get()
    start_date_str = entry_start.get()
    end_date_str = entry_end.get()
    hour_str = entry_hour.get()

    try:
        regions = [r.strip() for r in regions_input.split(",")]
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        outage_hour = int(hour_str)
    except Exception as e:
        messagebox.showerror("خطا", "ورودی‌ها را به‌درستی وارد کنید.\nمثلاً: 2025-07-20")
        return

    if start_date > end_date:
        messagebox.showerror("خطا", "تاریخ شروع باید قبل از تاریخ پایان باشد.")
        return

    result = ""
    current_date = start_date
    region_index = 0

    while current_date <= end_date:
        region = regions[region_index % len(regions)]
        result += f"{current_date.strftime('%Y-%m-%d')} → منطقه {region} از ساعت {outage_hour}:00 تا {outage_hour + 2}:00 خاموشی دارد.\n"
        current_date += timedelta(days=2)  # یک‌روز در میان
        region_index += 1

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# طراحی رابط گرافیکی
root = tk.Tk()
root.title("برنامه‌ریز خاموشی برق")

tk.Label(root, text="مناطق (مثلاً: A, B, C):").pack()
entry_regions = tk.Entry(root, width=40)
entry_regions.pack()

tk.Label(root, text="تاریخ شروع (YYYY-MM-DD):").pack()
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="تاریخ پایان (YYYY-MM-DD):").pack()
entry_end = tk.Entry(root)
entry_end.pack()

tk.Label(root, text="ساعت شروع خاموشی (مثلاً: 14):").pack()
entry_hour = tk.Entry(root)
entry_hour.pack()

tk.Button(root, text="تولید برنامه خاموشی", command=generate_schedule_gui).pack(pady=10)
text_output = tk.Text(root, height=15, width=60)
text_output.pack()  # اضافه کردن pack برای نمایش ویجت
root.mainloop()

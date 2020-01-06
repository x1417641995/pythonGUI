import tkinter as tk
import math

window = tk.Tk()
# 設定視窗標題、大小和背景顏色
window.title('BMI App')
window.geometry('800x600')
window.configure(background='white')
header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()




#

def calculate_bmi_number():
    height = float(height_entry.get())
    #print(bmi_value)
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height/100, 2), 2)
    print(bmi_value)
    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    # 將計算結果更新到 result_label 文字內容
    result_label.configure(text=result)
def get_bmi_status_description(bmi_value):
    
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'
    
# 以下為 height_frame 群組
height_frame = tk.Frame(window)
# 向上對齊父元件
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（cm）')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

# 以下為 weight_frame 群組
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

    
result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算')
calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)
calculate_btn.pack()

# 運行主程式
window.mainloop()
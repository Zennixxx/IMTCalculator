import customtkinter as ctk
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор ІМТ')
        self.geometry('600x550')
        self.resizable(False, False)
        self.configure(fg_color='#2E3759')

        ctk.CTkLabel(self, text='Розрахуємо індекс маси тіла', font=('Poppins', 18)).pack(pady=20)

        self.weight = 30
        self.height = 100
        self.imt = 0
        self.gender = ''
        self.advices = {
            '1': 'Виражений дефіцит маси тіла. Рекомендується звернутися до лікаря.',
            '2': 'Недостатня маса тіла. Рекомендується звернутися до лікаря.',
            '3': 'Норма',
            '4': 'Надлишкова маса тіла. Рекомендується звернутися до лікаря.',
            '5': 'Ожиріння. Рекомендується звернутися до лікаря.',
        }



        self.weight_frame1 = ctk.CTkFrame(self, fg_color='#38426A', corner_radius=10)
        self.weight_frame1.pack(pady=10)

        ctk.CTkLabel(self.weight_frame1, text='Вага (кг):', font=('Poppins', 16)).pack(side='left', padx=10)

        self.weight_frame2 = ctk.CTkFrame(self.weight_frame1, fg_color='#3F4B79', corner_radius=10)
        self.weight_frame2.pack(side='right', padx=5)

        self.weight_label = ctk.CTkLabel(self.weight_frame2, text=self.weight, font=('Poppins', 16))
        self.weight_label.pack(pady=10, padx=15)

        self.weight_scale = ctk.CTkSlider(self, from_=30, to=200, number_of_steps=170, width=250,
                                            fg_color='#3F4B79', progress_color='#38426A', button_color='#4F5C8D', button_hover_color='#38426A')
        self.weight_scale.set(self.weight)
        self.weight_scale.pack(pady=5)



        self.height_frame1 = ctk.CTkFrame(self, fg_color='#38426A', corner_radius=10)
        self.height_frame1.pack(pady=10)

        ctk.CTkLabel(self.height_frame1, text='Зріст (см):', font=('Poppins', 16)).pack(side='left', padx=10)

        self.height_frame2 = ctk.CTkFrame(self.height_frame1, fg_color='#3F4B79', corner_radius=10)
        self.height_frame2.pack(side='right', padx=(0, 6))

        self.height_label = ctk.CTkLabel(self.height_frame2, text=self.height, font=('Poppins', 16))
        self.height_label.pack(pady=10, padx=15)

        self.height_scale = ctk.CTkSlider(self, from_=100, to=220, number_of_steps=120, width=250,
                                            fg_color='#3F4B79', progress_color='#38426A', button_color='#4F5C8D', button_hover_color='#38426A')
        self.height_scale.set(self.height)
        self.height_scale.pack(pady=5)
        
        

        ctk.CTkLabel(self, text='Ваша стать:', font=('Poppins', 16)).pack(pady=(20, 5))

        self.gender_frame = ctk.CTkFrame(self, fg_color='transparent', corner_radius=10)
        self.gender_frame.pack(pady=5)

        self.male_button = ctk.CTkButton(self.gender_frame, text='Чоловіча', command=self.male_button_click,
                                            fg_color='#3A4A90', hover_color='#313f7d', font=('Poppins', 16), width=100, height=40)
        self.male_button.pack(side='left', padx=2)

        self.female_button = ctk.CTkButton(self.gender_frame, text='Жіноча', command=self.female_button_click,
                                            fg_color='#7C3EA0', hover_color='#5f2f7a', font=('Poppins', 16), width=100, height=40)
        self.female_button.pack(side='right', padx=2)



        self.result_frame = ctk.CTkFrame(self, fg_color='transparent', corner_radius=10, width=300, height=100)
        self.result_frame.pack(pady=30)

        self.imt_text_frame = ctk.CTkFrame(self.result_frame, fg_color='#38426A', corner_radius=10, width=70, height=40)
        self.imt_text_frame.pack(padx=(0, 0), side='left')

        self.imt_frame = ctk.CTkFrame(self.result_frame, fg_color='#3F4B79', corner_radius=10, width=120, height=55)
        self.imt_frame.pack(padx=(0, 0), side='left')

        self.advice_frame = ctk.CTkFrame(self.result_frame, fg_color='#38426A', corner_radius=10, height=40)
        self.advice_frame.pack(padx=(0, 0), side='left')

        self.imt_label = ctk.CTkLabel(self.imt_text_frame, text='ІМТ:', font=('Poppins', 16))
        self.imt_label.pack(pady=5, padx=15)

        self.imt_value_label = ctk.CTkLabel(self.imt_frame, text='0', font=('Poppins', 16))
        self.imt_value_label.pack(pady=10, padx=15)

        self.advice_label = ctk.CTkLabel(self.advice_frame, text='', font=('Poppins', 16), wraplength=250, justify='left')
        self.advice_label.pack(pady=5, padx=15)

        self.calculate_button = ctk.CTkButton(self, text='Розрахувати', command=self.calc_imt,
                                                fg_color='#3A4A90', hover_color='#313f7d', font=('Poppins', 16), width=100, height=40)
        self.calculate_button.pack(pady=5)

        self.weight_scale.configure(command=self.update_weight_label)
        self.height_scale.configure(command=self.update_height_label)




    def male_button_click(self):
        self.male_button.configure(fg_color='#313f7d')
        self.female_button.configure(fg_color='#7C3EA0')
        self.gender = 'male'

    def female_button_click(self):
        self.female_button.configure(fg_color='#5f2f7a')
        self.male_button.configure(fg_color='#3A4A90')
        self.gender = 'female'

    def update_weight_label(self, value):
        self.weight = int(value)
        self.weight_label.configure(text=self.weight)
        
        # if self.weight == 0 or self.height == 0:
        #     return
        # else:
        #     self.calc_imt()
    def update_height_label(self, value):
        self.height = int(value)
        self.height_label.configure(text=self.height)
        
        # if self.weight == 0 or self.height == 0:
        #     return
        # else:
        #     self.calc_imt()

    def calc_imt(self):
        if self.height == 0 or self.weight == 0:
            messagebox.showerror('Помилка', 'Будь ласка, введіть коректні дані.')
            return
        self.imt = self.weight / ((self.height / 100) ** 2)
        self.imt_value_label.configure(text=f'{self.imt:.2f}')

        if self.imt < 16:
            self.advice_label.configure(text=self.advices['1'])
        elif 16 <= self.imt < 18.5:
            self.advice_label.configure(text=self.advices['2'])
        elif 18.5 <= self.imt < 25:
            self.advice_label.configure(text=self.advices['3'])
        elif 25 <= self.imt < 30:
            self.advice_label.configure(text=self.advices['4'])
        else:
            self.advice_label.configure(text=self.advices['5'])

if __name__ == '__main__':
    app = App()
    app.mainloop()

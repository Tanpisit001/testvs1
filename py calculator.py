import customtkinter as ctk

# ตั้งค่าธีม
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("380x550")
        self.root.resizable(False, False)

        self.expression = ""

        # หน้าจอแสดงผล
        self.display = ctk.CTkEntry(
            root,
            width=340,
            height=70,
            font=("Arial", 28),
            justify="right"
        )
        self.display.pack(pady=20)

        # ปุ่มต่างๆ
        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row in buttons:
            frame = ctk.CTkFrame(root, fg_color="transparent")
            frame.pack(pady=5)

            for btn in row:
                width = 75
                if btn == "0":
                    width = 160

                button = ctk.CTkButton(
                    frame,
                    text=btn,
                    width=width,
                    height=60,
                    font=("Arial", 22, "bold"),
                    command=lambda x=btn: self.click(x)
                )
                button.pack(side="left", padx=5)

    def click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, "end")
                self.display.insert("end", result)
                self.expression = result
            except:
                self.display.delete(0, "end")
                self.display.insert("end", "Error")
                self.expression = ""

        elif value == "C":
            self.expression = ""
            self.display.delete(0, "end")

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.display.delete(0, "end")
            self.display.insert("end", self.expression)

        else:
            self.expression += value
            self.display.delete(0, "end")
            self.display.insert("end", self.expression)


if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculator(root)
    root.mainloop()
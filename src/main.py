import tkinter as tk                  # Tkinter GUI 라이브러리 불러오기
from tkinter import messagebox        # 오류 메시지 창을 띄우기 위해 messagebox 사용

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCalc")     # 윈도우 제목 설정
        self.root.geometry("300x400") # 윈도우 크기 설정
        self.root.resizable(False, False) # 창 크기 조절 비활성화

        self.expression = ""          # 계산식 문자열 저장용 변수

        # 입력창(엔트리 위젯) 생성
        self.entry = tk.Entry(
            root, font=("Arial", 20), bd=10, relief="sunken", justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
        self.entry.focus_set()

        # Enter 키를 누르면 결과 계산 함수 실행
        self.root.bind("<Return>", self.calculate_result)
        self.entry.bind("<Return>", self.calculate_result)
        self.entry.bind("<KP_Enter>", self.calculate_result)

        # 버튼 배열 정의: (텍스트, 행 위치, 열 위치)
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
            ('C',5,0), ('(',5,1), (')',5,2), ('Exit',5,3)
        ]

        # 버튼 생성 및 배치
        for (text, r, c) in buttons:
            action = lambda x=text: self.on_click(x)   # 각 버튼 클릭 시 on_click 호출
            tk.Button(
                root, text=text, width=6, height=2, font=("Arial", 14),
                command=action
            ).grid(row=r, column=c, padx=5, pady=5)

        # 행/열 크기 조정 (Grid가 화면 전체에 꽉 차도록)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_click(self, char):
        """버튼 클릭 시 동작"""
        if char == "=":
            self.calculate_result()   # '=' 버튼이면 결과 계산
        elif char == "C":
            self.entry.delete(0, tk.END)  # 'C' 버튼이면 입력창 비우기
            self.expression = ""          # 저장된 수식도 초기화
        elif char == "Exit":
            self.root.quit()              # 'Exit' 버튼이면 프로그램 종료
        else:
            self.expression += str(char)  # 버튼 값(숫자/연산자)을 수식에 추가
            self.entry.delete(0, tk.END)  # 기존 입력창 지우기
            self.entry.insert(tk.END, self.expression)  # 현재 수식 표시

    def calculate_result(self, event=None):
        """결과 계산 (Enter 키나 '=' 버튼 눌렀을 때 실행)"""
        try:
            current_text = self.entry.get() # 입력창에 입력된 텍스트
            expression_text = current_text if current_text != "" else self.expression
            # 입력창에 입력된 텍스트가 비어있으면 저장된 수식 사용
            # 입력창에 입력된 텍스트가 비어있지 않으면 입력된 텍스트 사용
            
            result = str(eval(expression_text))     # eval()로 문자열 계산
            self.entry.delete(0, tk.END)            # 입력창 비우기
            self.entry.insert(tk.END, result)       # 결과 표시
            self.expression = result                # expression 업데이트
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")  # 잘못된 수식일 경우 에러창
            self.entry.delete(0, tk.END)            # 입력창 비우기
            self.expression = ""                    # expression 초기화

if __name__ == "__main__":
    root = tk.Tk()              # Tkinter 기본 윈도우 생성
    calc = Calculator(root)     # Calculator 클래스 객체 생성
    root.mainloop()             # 이벤트 루프 실행 (창이 닫힐 때까지 대기)

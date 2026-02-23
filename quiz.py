import tkinter as tk
from tkinter import font
import random
import time

# ─── Question Bank ───────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Core Processor Utility", "Central Program Uploader"],
        "answer": "Central Processing Unit",
        "category": "Hardware"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "define", "function"],
        "answer": "def",
        "category": "Python"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["HyperText Markup Language", "High Tech Modern Language", "HyperText Modern Links", "Hyper Transfer Markup Layer"],
        "answer": "HyperText Markup Language",
        "category": "Web"
    },
    {
        "question": "Which data structure follows LIFO order?",
        "options": ["Queue", "Array", "Stack", "Linked List"],
        "answer": "Stack",
        "category": "Data Structures"
    },
    {
        "question": "What is the output of: print(type(42))?",
        "options": ["<class 'str'>", "<class 'float'>", "<class 'int'>", "<class 'num'>"],
        "answer": "<class 'int'>",
        "category": "Python"
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": ["List", "Dictionary", "Array", "Tuple"],
        "answer": "Array",
        "category": "Python"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["Simple Query Language", "Structured Query Language", "Standard Query Logic", "Sequential Query Layer"],
        "answer": "Structured Query Language",
        "category": "Database"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#",
        "category": "Python"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
        "answer": "O(log n)",
        "category": "Algorithms"
    },
    {
        "question": "Which company developed the Android operating system?",
        "options": ["Apple", "Microsoft", "Google", "Samsung"],
        "answer": "Google",
        "category": "General"
    },
    {
        "question": "What does OOP stand for?",
        "options": ["Object Oriented Programming", "Open Object Processing", "Ordered Output Procedure", "Object Oriented Protocol"],
        "answer": "Object Oriented Programming",
        "category": "Programming"
    },
    {
        "question": "Which of the following is a primary key property?",
        "options": ["Can be NULL", "Must be unique", "Can repeat", "Optional field"],
        "answer": "Must be unique",
        "category": "Database"
    },
    {
        "question": "What does 'git commit' do?",
        "options": ["Uploads code to GitHub", "Saves changes to local repository", "Creates a new branch", "Merges branches"],
        "answer": "Saves changes to local repository",
        "category": "Git"
    },
    {
        "question": "Which Python method adds an element to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()",
        "category": "Python"
    },
    {
        "question": "What is the full form of GUI?",
        "options": ["General User Interface", "Graphical User Interface", "Global Unified Interface", "Graphical Unix Interface"],
        "answer": "Graphical User Interface",
        "category": "General"
    },
]

# ─── Color Palette ────────────────────────────────────────────────────────────
NAVY       = "#0a1628"
NAVY_MID   = "#112040"
NAVY_LIGHT = "#1a3055"
GOLD       = "#c9a84c"
GOLD_LIGHT = "#e8c97a"
WHITE      = "#ffffff"
MUTED      = "#8a9bb5"
GREEN      = "#2ecc71"
RED        = "#e74c3c"
CARD_BG    = "#0f1e3a"


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sanjay's Quiz App")
        self.root.geometry("820x600")
        self.root.resizable(False, False)
        self.root.configure(bg=NAVY)

        # State
        self.questions = random.sample(QUESTIONS, 10)
        self.current_q = 0
        self.score = 0
        self.selected = tk.StringVar()
        self.answered = False
        self.timer_running = False
        self.time_left = 20
        self.timer_id = None

        # Fonts
        self.font_title  = font.Font(family="Georgia", size=22, weight="bold")
        self.font_sub    = font.Font(family="Georgia", size=13, weight="bold")
        self.font_body   = font.Font(family="Helvetica", size=11)
        self.font_opt    = font.Font(family="Helvetica", size=11)
        self.font_btn    = font.Font(family="Helvetica", size=11, weight="bold")
        self.font_mono   = font.Font(family="Courier", size=10)
        self.font_small  = font.Font(family="Helvetica", size=9)

        self.show_welcome()

    # ── Welcome Screen ────────────────────────────────────────────────────────
    def show_welcome(self):
        self.clear()

        # Background canvas with decorative lines
        canvas = tk.Canvas(self.root, width=820, height=600, bg=NAVY, highlightthickness=0)
        canvas.place(x=0, y=0)
        for i in range(0, 820, 60):
            canvas.create_line(i, 0, i, 600, fill="#0d1f3a", width=1)
        for i in range(0, 600, 60):
            canvas.create_line(0, i, 820, i, fill="#0d1f3a", width=1)
        canvas.create_rectangle(0, 0, 820, 4, fill=GOLD, outline="")
        canvas.create_rectangle(0, 596, 820, 600, fill=GOLD, outline="")

        # Center frame
        frame = tk.Frame(self.root, bg=CARD_BG, bd=0, relief="flat")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=560, height=380)

        # Gold border effect
        border = tk.Frame(self.root, bg=GOLD)
        border.place(relx=0.5, rely=0.5, anchor="center", width=564, height=384)
        frame.lift()

        tk.Label(frame, text="// QUIZ APP", bg=CARD_BG, fg=GOLD,
                 font=self.font_mono).pack(pady=(30, 4))

        tk.Label(frame, text="Test Your Knowledge", bg=CARD_BG, fg=WHITE,
                 font=self.font_title).pack(pady=(0, 6))

        tk.Label(frame, text="10 Questions  ·  Multiple Choice  ·  20 sec per question",
                 bg=CARD_BG, fg=MUTED, font=self.font_small).pack()

        # Divider
        tk.Frame(frame, bg=GOLD, height=1, width=400).pack(pady=20)

        # Topics
        topics_frame = tk.Frame(frame, bg=CARD_BG)
        topics_frame.pack()
        topics = ["Python", "Data Structures", "Databases", "Web", "Git", "General"]
        for i, t in enumerate(topics):
            tk.Label(topics_frame, text=t, bg=NAVY_LIGHT, fg=GOLD_LIGHT,
                     font=self.font_small, padx=10, pady=4,
                     relief="flat").grid(row=0, column=i, padx=4)

        tk.Frame(frame, bg=GOLD, height=1, width=400).pack(pady=20)

        # Start button
        start_btn = tk.Button(
            frame, text="START QUIZ  ▶",
            font=self.font_btn, bg=GOLD, fg=NAVY,
            activebackground=GOLD_LIGHT, activeforeground=NAVY,
            bd=0, padx=30, pady=12, cursor="hand2",
            command=self.start_quiz
        )
        start_btn.pack()

        tk.Label(frame, text="Built by Vadla Sanjay Kumar",
                 bg=CARD_BG, fg=MUTED, font=self.font_small).pack(pady=(20, 0))

    # ── Quiz Screen ───────────────────────────────────────────────────────────
    def start_quiz(self):
        self.current_q = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear()
        self.answered = False
        self.selected.set("")
        self.time_left = 20

        q_data = self.questions[self.current_q]

        # Top bar
        topbar = tk.Frame(self.root, bg=NAVY_MID, height=56)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        tk.Label(topbar, text="// QUIZ APP", bg=NAVY_MID, fg=GOLD,
                 font=self.font_mono).pack(side="left", padx=20, pady=16)

        # Score
        tk.Label(topbar, text=f"Score: {self.score}", bg=NAVY_MID, fg=GOLD_LIGHT,
                 font=self.font_btn).pack(side="right", padx=20, pady=16)

        # Progress bar
        prog_frame = tk.Frame(self.root, bg=NAVY_MID, height=6)
        prog_frame.pack(fill="x")
        prog_fill = tk.Frame(prog_frame, bg=GOLD, height=6)
        prog_fill.place(x=0, y=0, width=int(820 * (self.current_q / 10)))

        # Main content
        content = tk.Frame(self.root, bg=NAVY, padx=50, pady=20)
        content.pack(fill="both", expand=True)

        # Question meta row
        meta_row = tk.Frame(content, bg=NAVY)
        meta_row.pack(fill="x", pady=(10, 0))

        tk.Label(meta_row,
                 text=f"Question {self.current_q + 1} of 10",
                 bg=NAVY, fg=MUTED, font=self.font_small).pack(side="left")

        tk.Label(meta_row,
                 text=f"[ {q_data['category']} ]",
                 bg=NAVY_LIGHT, fg=GOLD, font=self.font_small,
                 padx=8, pady=3).pack(side="right")

        # Timer
        self.timer_label = tk.Label(meta_row, text=f"⏱ {self.time_left}s",
                                    bg=NAVY, fg=WHITE, font=self.font_btn)
        self.timer_label.pack(side="right", padx=16)

        # Gold accent line
        tk.Frame(content, bg=GOLD, height=2).pack(fill="x", pady=(8, 0))

        # Question text
        q_frame = tk.Frame(content, bg=CARD_BG, padx=24, pady=20)
        q_frame.pack(fill="x", pady=16)

        tk.Label(q_frame, text=q_data["question"],
                 bg=CARD_BG, fg=WHITE, font=self.font_sub,
                 wraplength=680, justify="left", anchor="w").pack(fill="x")

        # Options
        self.option_btns = []
        opts = q_data["options"][:]
        random.shuffle(opts)

        for opt in opts:
            btn_frame = tk.Frame(content, bg=NAVY, pady=4)
            btn_frame.pack(fill="x")

            btn = tk.Button(
                btn_frame, text=f"  {opt}",
                font=self.font_opt,
                bg=NAVY_MID, fg=WHITE,
                activebackground=NAVY_LIGHT,
                activeforeground=WHITE,
                anchor="w", bd=0, padx=16, pady=12,
                cursor="hand2", relief="flat",
                command=lambda o=opt, b=btn_frame: self.select_answer(o, b, q_data["answer"])
            )
            btn.pack(fill="x")

            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=NAVY_LIGHT))
            btn.bind("<Leave>", lambda e, b=btn, bf=btn_frame: b.config(
                bg=bf.winfo_children()[0].cget("bg") if bf.winfo_children() else NAVY_MID
            ))

            self.option_btns.append((btn_frame, btn, opt))

        # Next button (hidden until answered)
        self.next_btn = tk.Button(
            content,
            text="NEXT  →" if self.current_q < 9 else "SEE RESULTS  →",
            font=self.font_btn, bg=GOLD, fg=NAVY,
            activebackground=GOLD_LIGHT, bd=0,
            padx=24, pady=10, cursor="hand2",
            command=self.next_question
        )

        # Start timer
        self.start_timer(q_data["answer"])

    def start_timer(self, correct):
        self.timer_running = True
        self._tick(correct)

    def _tick(self, correct):
        if not self.timer_running:
            return
        if self.time_left <= 0:
            self.timer_running = False
            if not self.answered:
                self.answered = True
                self.highlight_answer(None, correct)
                self.next_btn.pack(anchor="e", pady=(8, 0))
            return
        color = WHITE if self.time_left > 8 else ("#e67e22" if self.time_left > 4 else RED)
        self.timer_label.config(text=f"⏱ {self.time_left}s", fg=color)
        self.time_left -= 1
        self.timer_id = self.root.after(1000, lambda: self._tick(correct))

    def select_answer(self, chosen, btn_frame, correct):
        if self.answered:
            return
        self.answered = True
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        if chosen == correct:
            self.score += 1

        self.highlight_answer(chosen, correct)
        self.next_btn.pack(anchor="e", pady=(8, 0))

    def highlight_answer(self, chosen, correct):
        for bf, btn, opt in self.option_btns:
            btn.unbind("<Enter>")
            btn.unbind("<Leave>")
            btn.config(cursor="arrow")
            if opt == correct:
                btn.config(bg=GREEN, fg=WHITE)
                bf.config(bg=GREEN)
            elif opt == chosen and chosen != correct:
                btn.config(bg=RED, fg=WHITE)
                bf.config(bg=RED)
            else:
                btn.config(bg=NAVY_MID, fg=MUTED)

    def next_question(self):
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.current_q += 1
        if self.current_q < 10:
            self.show_question()
        else:
            self.show_results()

    # ── Results Screen ────────────────────────────────────────────────────────
    def show_results(self):
        self.clear()

        canvas = tk.Canvas(self.root, width=820, height=600, bg=NAVY, highlightthickness=0)
        canvas.place(x=0, y=0)
        for i in range(0, 820, 60):
            canvas.create_line(i, 0, i, 600, fill="#0d1f3a", width=1)
        for i in range(0, 600, 60):
            canvas.create_line(0, i, 820, i, fill="#0d1f3a", width=1)
        canvas.create_rectangle(0, 0, 820, 4, fill=GOLD, outline="")
        canvas.create_rectangle(0, 596, 820, 600, fill=GOLD, outline="")

        frame = tk.Frame(self.root, bg=CARD_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=560, height=400)

        border = tk.Frame(self.root, bg=GOLD)
        border.place(relx=0.5, rely=0.5, anchor="center", width=564, height=404)
        frame.lift()

        pct = int((self.score / 10) * 100)

        if pct == 100:
            grade, grade_color, msg = "PERFECT!", GOLD, "Outstanding! Flawless performance 🏆"
        elif pct >= 80:
            grade, grade_color, msg = "EXCELLENT", GREEN, "Great job! You really know your stuff 🎉"
        elif pct >= 60:
            grade, grade_color, msg = "GOOD", GOLD_LIGHT, "Solid effort! Keep pushing forward 💪"
        elif pct >= 40:
            grade, grade_color, msg = "AVERAGE", "#e67e22", "Not bad! A bit more practice will help 📚"
        else:
            grade, grade_color, msg = "KEEP TRYING", RED, "Don't give up — every expert was once a beginner 🌱"

        tk.Label(frame, text="// RESULTS", bg=CARD_BG, fg=GOLD,
                 font=self.font_mono).pack(pady=(28, 4))

        tk.Label(frame, text=grade, bg=CARD_BG, fg=grade_color,
                 font=font.Font(family="Georgia", size=28, weight="bold")).pack()

        tk.Frame(frame, bg=GOLD, height=1, width=400).pack(pady=14)

        # Score display
        score_frame = tk.Frame(frame, bg=NAVY_MID, padx=30, pady=14)
        score_frame.pack()

        tk.Label(score_frame,
                 text=f"{self.score}  /  10",
                 bg=NAVY_MID, fg=WHITE,
                 font=font.Font(family="Georgia", size=32, weight="bold")).pack()

        tk.Label(score_frame, text=f"{pct}% Correct",
                 bg=NAVY_MID, fg=MUTED, font=self.font_small).pack()

        tk.Frame(frame, bg=GOLD, height=1, width=400).pack(pady=14)

        tk.Label(frame, text=msg, bg=CARD_BG, fg=WHITE,
                 font=self.font_body, wraplength=460).pack(pady=(0, 18))

        # Buttons
        btn_row = tk.Frame(frame, bg=CARD_BG)
        btn_row.pack()

        tk.Button(
            btn_row, text="PLAY AGAIN  ↺",
            font=self.font_btn, bg=GOLD, fg=NAVY,
            activebackground=GOLD_LIGHT, bd=0,
            padx=20, pady=10, cursor="hand2",
            command=self.restart
        ).pack(side="left", padx=8)

        tk.Button(
            btn_row, text="QUIT",
            font=self.font_btn, bg=NAVY_MID, fg=MUTED,
            activebackground=NAVY_LIGHT, bd=0,
            padx=20, pady=10, cursor="hand2",
            command=self.root.destroy
        ).pack(side="left", padx=8)

    def restart(self):
        self.questions = random.sample(QUESTIONS, 10)
        self.current_q = 0
        self.score = 0
        self.show_question()

    # ── Utility ───────────────────────────────────────────────────────────────
    def clear(self):
        self.timer_running = False
        if hasattr(self, "timer_id") and self.timer_id:
            self.root.after_cancel(self.timer_id)
        for widget in self.root.winfo_children():
            widget.destroy()


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

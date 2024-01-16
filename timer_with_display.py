import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Display")

        self.output_text = ScrolledText(root, width=40, height=20, wrap=tk.WORD)
        self.output_text.pack(padx=10, pady=10)

        self.global_timer_id = None
        self.countdown_timer_id = None
        self.stopwatch_start_time = None

        self.global_timer_running = False
        self.countdown_timer_running = False
        self.stopwatch_running = False

        self.create_widgets()

    def create_widgets(self):
        start_global_button = tk.Button(self.root, text="Start Global Timer", command=self.start_global_timer)
        start_global_button.pack()

        stop_global_button = tk.Button(self.root, text="Stop Global Timer", command=self.stop_global_timer)
        stop_global_button.pack()

        start_countdown_button = tk.Button(self.root, text="Start Countdown Timer", command=self.start_countdown_timer)
        start_countdown_button.pack()

        stop_countdown_button = tk.Button(self.root, text="Stop Countdown Timer", command=self.stop_countdown_timer)
        stop_countdown_button.pack()

        start_stopwatch_button = tk.Button(self.root, text="Start Stopwatch", command=self.start_stopwatch)
        start_stopwatch_button.pack()

        stop_stopwatch_button = tk.Button(self.root, text="Stop Stopwatch", command=self.stop_stopwatch)
        stop_stopwatch_button.pack()

        reset_stopwatch_button = tk.Button(self.root, text = "Reset Stopwatch", command = self.reset_stopwatch)
        reset_stopwatch_button.pack()

    def start_global_timer(self):
        if not self.global_timer_running and not self.countdown_timer_running and not self.stopwatch_running:
            self.global_timer_id = self.root.after(0, self.update_global_timer)
            self.global_timer_running = True

    def stop_global_timer(self):
        if self.global_timer_running:
            self.root.after_cancel(self.global_timer_id)
            self.global_timer_running = False

    def update_global_timer(self):
        global_time = time.time()
        self.output_text.insert(tk.END, f"Global Timer: {global_time}\n")
        self.output_text.yview(tk.END)
        self.global_timer_id = self.root.after(1000, self.update_global_timer)

    def start_countdown_timer(self):
        if not self.global_timer_running and not self.countdown_timer_running and not self.stopwatch_running:
            self.countdown_timer_id = self.root.after(0, lambda: self.update_countdown_timer(60))
            self.countdown_timer_running = True

    def stop_countdown_timer(self):
        if self.countdown_timer_running:
            self.root.after_cancel(self.countdown_timer_id)
            self.countdown_timer_running = False

    def update_countdown_timer(self, seconds):
        if seconds > 0:
            self.output_text.insert(tk.END, f"Countdown Timer: {seconds}\n")
            self.output_text.yview(tk.END)
            self.countdown_timer_id = self.root.after(1000, lambda: self.update_countdown_timer(seconds - 1))
        else:
            self.output_text.insert(tk.END, "Countdown Timer: Time's up!\n")
            self.output_text.yview(tk.END)
            self.countdown_timer_running = False

    def start_stopwatch(self):
        if not self.global_timer_running and not self.countdown_timer_running:
            if not self.stopwatch_running:
                if hasattr(self, 'stopwatch_pause_time'):
                    self.stopwatch_offset += time.time() - self.stopwatch_pause_time
                else:
                    self.stopwatch_start_time = time.time()
                    self.stopwatch_offset = 0
                self.stop_stopwatch()
                self.update_stopwatch()
                self.stopwatch_id = self.root.after(100, self.update_stopwatch)
                self.stopwatch_running = True
            else:
                self.stopwatch_start_time = time.time() - self.stopwatch_offset
                self.stopwatch_id = self.root.after(100, self.update_stopwatch)

    def stop_stopwatch(self):
        if self.stopwatch_running:
            self.root.after_cancel(self.stopwatch_id)
            self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stop_stopwatch()
        self.output_text.delete(1.0, tk.END)
        self.stopwatch_start_time = time.time()
        self.stopwatch_offset = 0
        self.update_stopwatch()

    def update_stopwatch(self):
        if self.stopwatch_running:
            elapsed_time = time.time() - self.stopwatch_start_time + self.stopwatch_offset
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Stopwatch: Elapsed time: {elapsed_time:.4f} seconds\n")
            self.output_text.yview(tk.END)
            self.stopwatch_id = self.root.after(100, self.update_stopwatch)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

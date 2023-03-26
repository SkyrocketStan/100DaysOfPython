import time
import tkinter as tk


class TypingSpeedTest:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Typing Speed Test")
        self.root_window.geometry("600x400")
        self.start_time = 0
        self.correct_words = 0
        self.total_words = 0

        # Text to type
        self.text = "The quick brown fox jumps over the lazy dog."
        self.words = self.text.split()

        # Create widgets
        default_font = ("Helvetica", 14)
        self.text_label = tk.Label(self.root_window, text=self.text, font=default_font)
        self.text_label.pack(pady=20)

        self.input_entry = tk.Entry(self.root_window, font=default_font)
        self.input_entry.pack(pady=20)

        self.start_button = tk.Button(self.root_window, text="Start", font=default_font, command=self.start_test)
        self.start_button.pack(pady=20)

        self.result_label = tk.Label(self.root_window, text="", font=default_font)
        self.result_label.pack(pady=20)

        self.root_window.bind("<Return>", self.check_input)

    def start_test(self):
        self.start_button.config(state=tk.DISABLED)
        self.input_entry.config(state=tk.NORMAL)
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

        self.start_time = time.time()
        self.correct_words = 0
        self.total_words = 0

    def check_input(self, _):
        input_words = self.input_entry.get().split()
        self.total_words += len(input_words)

        for i in range(min(len(input_words), len(self.words))):
            if input_words[i] == self.words[i]:
                self.correct_words += 1

        if len(input_words) >= len(self.words):
            self.show_results()

    def show_results(self):
        self.input_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

        accuracy = round(self.correct_words / self.total_words * 100, 2)
        elapsed_time = time.time() - self.start_time
        wpm = round(self.total_words / elapsed_time * 60)

        self.result_label.config(text=f"Accuracy: {accuracy}%\nWPM: {wpm}")


def main():
    root_window = tk.Tk()
    TypingSpeedTest(root_window)
    root_window.mainloop()


if __name__ == "__main__":
    main()

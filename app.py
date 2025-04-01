import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import scrolledtext

# Download necessary NLTK data (first time only)
nltk.download('vader_lexicon')

class SentimentAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis Tool")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")
        
        # Initialize the VADER sentiment analyzer
        self.analyzer = SentimentIntensityAnalyzer()
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Sentiment Analysis", 
                              font=("Arial", 16, "bold"), bg="#f5f5f5")
        title_label.pack(pady=10)
        
        # Input area
        input_frame = tk.Frame(self.root, bg="#f5f5f5")
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        input_label = tk.Label(input_frame, text="Enter text to analyze:", 
                              font=("Arial", 10), bg="#f5f5f5")
        input_label.pack(anchor="w")
        
        self.text_input = scrolledtext.ScrolledText(input_frame, 
                                                  width=60, height=8, 
                                                  font=("Arial", 10))
        self.text_input.pack(pady=5)
        
        # Analyze button
        analyze_button = tk.Button(input_frame, text="Analyze Sentiment", 
                                  command=self.analyze_sentiment,
                                  bg="#4CAF50", fg="white",
                                  font=("Arial", 10, "bold"), padx=10)
        analyze_button.pack(pady=10)
        
        # Results area
        results_frame = tk.Frame(self.root, bg="#f5f5f5")
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        results_label = tk.Label(results_frame, text="Results:", 
                               font=("Arial", 10), bg="#f5f5f5")
        results_label.pack(anchor="w")
        
        self.result_display = tk.Label(results_frame, text="", 
                                     font=("Arial", 12), bg="white",
                                     wraplength=550, height=5, anchor="w",
                                     justify="left", bd=1, relief="solid")
        self.result_display.pack(fill="both", expand=True, pady=5)
    
    def analyze_sentiment(self):
        # Get text from input area
        text = self.text_input.get("1.0", "end-1c").strip()
        
        if not text:
            self.result_display.config(text="Please enter some text to analyze.")
            return
        
        # Analyze sentiment using VADER
        sentiment_scores = self.analyzer.polarity_scores(text)
        
        # Determine overall sentiment
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            sentiment = "Positive"
            color = "#4CAF50"  # Green
        elif compound_score <= -0.05:
            sentiment = "Negative"
            color = "#F44336"  # Red
        else:
            sentiment = "Neutral"
            color = "#2196F3"  # Blue
        
        # Display results
        result_text = f"Overall Sentiment: {sentiment} (Score: {compound_score:.2f})\n\n"
        result_text += f"Positive: {sentiment_scores['pos']:.2f}, "
        result_text += f"Negative: {sentiment_scores['neg']:.2f}, "
        result_text += f"Neutral: {sentiment_scores['neu']:.2f}"
        
        self.result_display.config(text=result_text, bg=color, fg="white")

def main():
    root = tk.Tk()
    app = SentimentAnalysisApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
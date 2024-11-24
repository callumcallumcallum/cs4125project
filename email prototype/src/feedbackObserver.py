class FeedbackObserver:
 def notify(self, email, feedback):
     pass

class SpamFeedbackLogger(FeedbackObserver):
 def notify(self, email, feedback):
     print(f"Logging feedback: Email '{email}' marked as {feedback}.")

class RetrainingHandler(FeedbackObserver):
 def notify(self, email, feedback):
     print(f"Email '{email}' feedback received for model retraining: {feedback}.")

class FeedbackManager:
 def __init__(self):
     self.observers = []

 def add_observer(self, observer):
     self.observers.append(observer)

 def report_feedback(self, email, feedback):
     for observer in self.observers:
         observer.notify(email, feedback)

def submit_feedback(feedback_manager):
    email = input("Enter the email content: ")
    feedback = input("Enter the feedback (e.g., 'spam', 'not spam'): ")
    feedback_manager.report_feedback(email, feedback)
    print("Feedback submitted successfully.")
         


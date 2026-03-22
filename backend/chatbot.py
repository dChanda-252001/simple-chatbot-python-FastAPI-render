def get_response(role, message):
    message = message.lower()

    if role == "general":
        if "hello" in message or "hi" in message:
            return "Hello! How can I assist you today?"
        elif "good morning" in message:
            return "Good morning! Hope you have a great day ahead."
        elif "good evening" in message:
            return "Good evening! How can I help you?"
        elif "what is your name" in message or "your name" in message:
            return "I am your chatbot assistant."
        elif "who created you" in message:
            return "I was created by a developer to assist users."
        elif "what can you do" in message:
            return "I can answer your questions and provide basic assistance."
        elif "are you human" in message:
            return "No, I am a computer program designed to help you."
        elif "how are you" in message:
            return "I am just a bot, but I am functioning perfectly!"
        elif "what are you doing" in message:
            return "I am here waiting to assist you."
        elif "can you help me" in message:
            return "Of course! Tell me what you need."
        elif "thank you" in message or "thanks" in message:
            return "You're welcome!"
        elif "what is ai" in message:
            return "AI stands for Artificial Intelligence."
        elif "machine learning" in message:
            return "Machine learning is a subset of AI where systems learn from data."
        elif "python" in message:
            return "Python is a popular programming language."
        elif "joke" in message:
            return "Why did the computer get cold? Because it forgot to close Windows!"
        elif "time" in message:
            return "I cannot access real-time data, please check your device clock."
        elif "date" in message or "day" in message:
            return "Please check your system date for accurate information."
        else:
            return "Sorry, I don't understand."

    elif role == "medical":
        if "fever" in message:
            return "Take rest, drink fluids, and monitor your temperature."
        elif "reduce fever" in message:
            return "Stay hydrated and take rest. You may take paracetamol if needed."
        elif "headache" in message:
            return "Headache may be due to stress or dehydration. Try relaxing."
        elif "cause headache" in message:
            return "Common causes include stress, dehydration, and lack of sleep."
        elif "cold" in message:
            return "Drink warm fluids and take proper rest."
        elif "cough" in message:
            return "Stay hydrated and try warm drinks like honey water."
        elif "immunity" in message:
            return "Eat healthy, exercise regularly, and sleep well."
        elif "water" in message:
            return "Drink around 2–3 liters of water daily."
        elif "sleep" in message:
            return "Adults need around 7–9 hours of sleep."
        elif "healthy diet" in message:
            return "Eat fruits, vegetables, and avoid processed food."
        elif "junk food" in message:
            return "Excess junk food can harm your health."
        elif "diabetes" in message:
            return "Diabetes is a condition with high blood sugar levels."
        elif "symptoms of diabetes" in message:
            return "Frequent urination, thirst, fatigue, and blurred vision."
        elif "blood pressure" in message:
            return "It refers to the force of blood against artery walls."
        elif "stress" in message:
            return "Try relaxation techniques like meditation and exercise."
        elif "chest pain" in message:
            return "Chest pain can be serious. Seek immediate medical attention."
        elif "when should i see a doctor" in message:
            return "If symptoms are severe or persistent, consult a doctor."
        elif "paracetamol" in message:
            return "It is used to reduce fever and relieve mild pain."
        elif "medicine without prescription" in message:
            return "Always consult a doctor before taking medicines."
        else:
            return "I am not sure. Please consult a doctor for proper medical advice."

    elif role == "student":
        if "study" in message:
            return "Create a study plan and follow it regularly."
        elif "how to start studying" in message:
            return "Start with small goals and a clear plan."
        elif "hours should i study" in message:
            return "4–6 focused hours daily is effective."
        elif "concentrate" in message:
            return "Study in a distraction-free environment."
        elif "best way to study" in message:
            return "Use notes, revision, and practice questions."
        elif "exam" in message:
            return "Start early and revise regularly."
        elif "score good marks" in message:
            return "Understand concepts and practice consistently."
        elif "before exam" in message:
            return "Revise key points and avoid new topics."
        elif "exam stress" in message:
            return "Stay calm, sleep well, and avoid panic."
        elif "time management" in message:
            return "Make a timetable and prioritize tasks."
        elif "procrastination" in message:
            return "Break tasks into smaller parts and start."
        elif "consistent" in message:
            return "Follow a routine and track progress."
        elif "programming language" in message:
            return "Start with Python as it is beginner-friendly."
        elif "coding" in message:
            return "Practice daily and solve coding problems."
        elif "skills" in message:
            return "Focus on communication and problem-solving skills."
        elif "career" in message:
            return "Explore your interests before choosing a career."
        elif "lazy" in message:
            return "Start small and build momentum."
        elif "motivation" in message:
            return "Set goals and remind yourself why you started."
        elif "focus" in message:
            return "Take short breaks and restart fresh."
        elif "remember" in message:
            return "Revise regularly and use notes."
        elif "revision" in message:
            return "Spaced repetition works best."
        elif "college" in message:
            return "Balance your schedule wisely."
        elif "attendance" in message:
            return "Stay disciplined and attend regularly."
        else:
            return "Focus and stay consistent."

    return "Invalid role."
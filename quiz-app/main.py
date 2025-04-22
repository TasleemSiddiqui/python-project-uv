import streamlit as st
import time

st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan", 
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

# Initialize session state variables
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.answered_questions = []
    st.session_state.show_results = False

# Show results when all questions are answered
if st.session_state.current_question_index >= len(questions):
    if not st.session_state.show_results:
        st.session_state.show_results = True
    
    st.subheader("Quiz Complete! 🎉")
    st.write(f"Your Score: {st.session_state.score}/{len(questions)}")
    
    # Show detailed results
    st.subheader("Detailed Results:")
    for idx, result in enumerate(st.session_state.answered_questions):
        with st.expander(f"Question {idx + 1}"):
            st.write(f"Q: {result['question']}")
            st.write(f"Your answer: {result['selected']}")
            st.write(f"Correct answer: {result['correct']}")
            if result['selected'] == result['correct']:
                st.success("✅ Correct")
            else:
                st.error("❌ Incorrect")
    
    if st.button("Restart Quiz"):
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.answered_questions = []
        st.session_state.show_results = False
        st.rerun()

else:
    # Show current question
    question = questions[st.session_state.current_question_index]
    st.subheader(question["question"])
    selected_option = st.radio("Choose your answer", question["options"], key=f"answer_{st.session_state.current_question_index}")

    if st.button("Submit Answer"):
        # Record answer and update score
        is_correct = selected_option == question["answer"]
        if is_correct:
            st.session_state.score += 1
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect! The correct answer is " + question["answer"])
        
        # Store question result
        st.session_state.answered_questions.append({
            "question": question["question"],
            "selected": selected_option,
            "correct": question["answer"]
        })
        
        time.sleep(1)
        st.session_state.current_question_index += 1
        st.rerun()
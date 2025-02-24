document.addEventListener("DOMContentLoaded", function() {
    // Dark Mode Toggle 
    const darkModeToggle = document.getElementById("darkModeToggle");
    if (darkModeToggle) {
        if (localStorage.getItem("darkMode") === "enabled") {
            document.body.classList.add("dark");
            darkModeToggle.textContent = "Light Mode";
        }
        darkModeToggle.addEventListener("click", function() {
            document.body.classList.toggle("dark");
            if (document.body.classList.contains("dark")) {
                localStorage.setItem("darkMode", "enabled");
                darkModeToggle.textContent = "Light Mode";
            } else {
                localStorage.setItem("darkMode", "disabled");
                darkModeToggle.textContent = "Dark Mode";
            }
        });
    }

    // Hamburger Menu 
    const hamburger = document.getElementById("hamburger");
    const navLinks = document.getElementById("navLinks");

    if (hamburger && navLinks) {
        hamburger.addEventListener("click", function() {
            navLinks.classList.toggle("active");
        });
    }

    // Form Submission for "Start Interview" on index.html 
    const scheduleForm = document.getElementById("scheduleForm");
    if (scheduleForm) {
        scheduleForm.addEventListener("submit", function(event) {
            event.preventDefault();
            const profile = document.getElementById("profile").value;
            const experience = document.getElementById("experience").value;
            // Adjust profile value if necessary (e.g., "Devops" to "DevOps")
            const adjustedProfile = (profile.toLowerCase() === "devops") ? "DevOps" : profile;
            localStorage.setItem("profile", adjustedProfile);
            localStorage.setItem("experience", experience);
            window.location.href = "interview.html";
        });
    }

    // Setup Page (interview.html) 
    let mediaStream = null;
    const setupVideoPreview = document.getElementById("videoPreview");
    if (setupVideoPreview && navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true, audio: true })
            .then(function(stream) {
                setupVideoPreview.srcObject = stream;
                mediaStream = stream;
                setupVideoPreview.muted = true; // Ensure no feedback on setup page 
            })
            .catch(function(err) {
                console.error("Error accessing media devices:", err);
                alert("Could not access camera/microphone. Please ensure permissions are granted.");
            });
    }

    const micTestButton = document.getElementById("micTestButton");
    const micLevel = document.getElementById("micLevel");
    if (micTestButton && micLevel) {
        micTestButton.addEventListener("click", function() {
            micLevel.classList.add("active");
            setTimeout(() => micLevel.classList.remove("active"), 2000);
        });
    }

    const startInterviewButton = document.getElementById("startInterviewButton");
    if (startInterviewButton) {
        startInterviewButton.addEventListener("click", function() {
            window.location.href = "interview_main.html";
        });
    }

    // Interview Page (interview_main.html)
    const interviewVideoPreview = document.getElementById("videoPreview");
    if (interviewVideoPreview && navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true, audio: true })
            .then(function(stream) {
                interviewVideoPreview.srcObject = stream;
                mediaStream = stream;
                interviewVideoPreview.muted = true; // Mute to prevent feedback 
            })
            .catch(function(err) {
                console.error("Error accessing media devices:", err);
            });
    }

    // Declare questions as a let variable so it can be overridden
    let questions = [
        "Tell me about yourself.",
        "What is your greatest strength?",
        "Describe a challenge you faced and how you overcame it.",
        "Why do you want this job?",
        "Where do you see yourself in 5 years?"
    ];
    let currentQuestionIndex = 0;

    function speakText(text) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.volume = 1;
        utterance.pitch = 1.2;
        utterance.rate = 1;
        speechSynthesis.speak(utterance);
    }

    function updateProgress() {
        const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
        document.getElementById("progressFill").style.width = progress + "%";
    }

    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            const questionBox = document.getElementById("questionBox");
            questionBox.textContent = currentQuestion;
            speakText(currentQuestion);
            updateProgress();
            const nextQuestionBtn = document.getElementById("nextQuestionBtn");
            const endInterviewBtn = document.getElementById("endInterviewBtn");
            if (currentQuestionIndex === questions.length - 1) {
                nextQuestionBtn.style.display = "none";
                endInterviewBtn.style.display = "inline-block";
            } else {
                nextQuestionBtn.style.display = "inline-block";
                endInterviewBtn.style.display = "none";
            }
        }
    }

    const nextQuestionBtn = document.getElementById("nextQuestionBtn");
    if (nextQuestionBtn) {
        nextQuestionBtn.addEventListener("click", function() {
            currentQuestionIndex++;
            displayQuestion();
        });
    }

    const endInterviewBtn = document.getElementById("endInterviewBtn");
    if (endInterviewBtn) {
        endInterviewBtn.addEventListener("click", function() {
            if (mediaStream) {
                mediaStream.getTracks().forEach(track => track.stop());
            }
            window.location.href = "result.html";
        });
    }

    // Fetch questions from backend if on interview_main.html
    if (document.getElementById("questionBox")) {
        const storedProfile = localStorage.getItem("profile");
        const storedExperience = localStorage.getItem("experience");
        if (storedProfile && storedExperience) {
            fetch("http://localhost:8000/get-questions/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    profile: storedProfile,
                    experience: storedExperience
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data && data.questions && Array.isArray(data.questions)) {
                    questions = data.questions;
                }
                currentQuestionIndex = 0;
                displayQuestion();
            })
            .catch(error => {
                console.error("Error fetching questions:", error);
                displayQuestion();
            });
        } else {
            displayQuestion();
        }
    }

    // Result page: Attach event for home button 
    const homeButton = document.getElementById("homeButton");
    if (homeButton) {
        homeButton.addEventListener("click", function() {
            window.location.href = "index.html";
        });
    }

    // Initialize testimonial carousel 
    function initTestimonialCarousel() {
        const carousel = document.getElementById("testimonialCarousel");
        if (!carousel) return;
        const testimonials = carousel.getElementsByClassName("testimonial-item");
        let currentIndex = 0;

        for (let i = 0; i < testimonials.length; i++) {
            testimonials[i].style.display = "none";
        }
        testimonials[0].style.display = "block";

        setInterval(function() {
            testimonials[currentIndex].style.display = "none";
            currentIndex = (currentIndex + 1) % testimonials.length;
            testimonials[currentIndex].style.display = "block";
        }, 4000);
    }

    initTestimonialCarousel();
});

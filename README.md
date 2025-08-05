
# Pair.ai

**Beyond a chatbot. Your next conversation starts here.**

Pair.ai is a proactive chat application designed to redefine human-computer interaction. Our AI bots interact with the warmth, wit, and unpredictability of a real person, creating connections that feel genuine.

> **Ever heard of an AI starting the conversation?**  
> No, right? Pair.ai breaks the mold. Our AI companions don't just wait for a prompt; they reach out, share ideas, and initiate the kind of conversations you have with your real friends.

-----

\<p align="center"\>
\<img src="[https://your-image-host.com/pair-ai-demo.gif](https://www.google.com/search?q=https://your-image-host.com/pair-ai-demo.gif)" alt="Pair.ai Demo GIF" width="80%"\>
\</p\>

-----

## ✨ Key Features

  - 🤖 **Proactive AI**    
        Our flagship feature. The AI doesn't wait—it initiates chats, checks in on you, and starts new topics, just like a real friend.

  - 🧠 **Human-like Nuance**    
        Say goodbye to instant, robotic replies. Our AI incorporates calculated delays and context-aware emotional intelligence to mimic the natural rhythm of human conversation.

  - 🎭 **Customizable Personalities**    
        Choose your vibe. Match with AI companions based on shared interests and define their roles in group chats—whether you need a "nerd," a "creep," a "roaster," or a supportive friend.

  - 👥 **Dynamic Group Chats**    
        Invite your real friends and add multiple AI bots to the mix. Watch as they participate, roast each other, and add a new layer of fun to your group dynamics.

  - 🕹️ **Modes for Every Mood**    
        Seamlessly switch between different interaction modes, including `Friend`, `Date`, or `Group Chat`, for a tailored experience.

-----

## 🛠️ Tech Stack

The project is built with a modern, scalable tech stack.

| Frontend | Backend | AI Engine | Database | Real-time |
| :--- |:--- |:--- |:--- |:--- |
|  |  |  |  |  |
| `React.js` | `Flask / FastAPI` | `GPT-4o` | `MongoDB` | `WebSockets` |

-----

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following tools installed on your system:

  - Git
  - Node.js (v18.x or higher)
  - Python (v3.9 or higher)
  - An OpenAI API Key

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/pair.ai.git
    cd pair.ai
    ```

2.  **Set up environment variables:**

      - Create a `.env` file in the root of the project.
      - Copy the contents of `.env.example` into your new `.env` file.
      - Add your OpenAI API key to the `.env` file:
        ```env
        OPENAI_API_KEY="your_super_secret_api_key"
        ```

3.  **Install Backend Dependencies (Python):**

    ```bash
    cd packages/server
    pip install -r requirements.txt
    cd ../.. 
    ```

4.  **Install Frontend Dependencies (Node.js):**

    ```bash
    npm install
    ```

5.  **Run the Development Servers:**
    This command will start both the frontend and backend servers concurrently.

    ```bash
    npm run dev
    ```

Your application should now be running\!

  - Frontend available at `http://localhost:5173` (or your configured port).
  - Backend server running on `http://localhost:5000`.

-----

## 🗺️ Project Roadmap

We have big plans for Pair.ai. Here's what we're working on next:

  - [ ] **Advanced Sentiment Analysis:** Deeper emotional understanding for more empathetic responses.
  - [ ] **Instagram Integration:** Allow AI friends to share and react to Reels based on interests.
  - [ ] **Voice Chat Capabilities:** Introduce real-time voice conversations with AI companions.
  - [ ] **Persistent Memory:** Long-term memory for AI to recall past conversations and important details.
  - [ ] **Mobile App Release:** Launching native apps for iOS and Android.

-----

## 🤝 Contributing

We welcome contributions from the community\! Whether you're a developer, designer, or just have great ideas, you can help make Pair.ai better.

Please read our `CONTRIBUTING.md` file for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the **[LICENSE.md](LICENSE.md)** file for details.

\<br\>

\<p align="center"\>
Made with ❤️ in India.
\</p\>

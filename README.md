# Pair.ai

**Beyond a chatbot. Your next conversation starts here.**

Pair.ai is a proactive chat application built around an open-source LLM. Instead of waiting for a prompt, the AI companions can start conversations, reply with human-paced delays, and take on configurable personas in one-to-one and group chats.

## Features

- **Proactive messaging:** bots can initiate chats and start new topics.
- **Human-paced replies:** response timing is delayed to mimic natural conversation rhythm.
- **Configurable personas:** choose a personality or assign roles to bots in group chats.
- **Group chats:** invite friends and add multiple AI bots.
- **Interaction modes:** Friend, Date, and Group Chat.

## Architecture

| Layer | Technology |
|---|---|
| Frontend | React.js |
| Backend | Flask / FastAPI (Python) |
| Model | Llama 3 8B Instruct |
| Database | MongoDB |
| Real-time | WebSockets |

Llama 3 8B is used because of resource constraints.

## Getting Started

```bash
git clone https://github.com/Naja24/Pair.ai.git
cd Pair.ai
cd packages/server && pip install -r requirements.txt && cd ../..
npm install
npm run dev
```

Frontend: `http://localhost:5173` | Backend: `http://localhost:5000`

## Evaluation

`eval_harness.py` runs a fixed set of test prompts against the model and logs results to CSV so that changes to the system prompt can be compared run to run.

Checks currently implemented:
- Prompt-injection resistance (a canary string planted in the system prompt must never appear in replies)
- Unsafe-content marker check
- Response length check
- Latency

**Results** (fill in from your own runs; do not publish numbers you did not measure):

| Version | Test cases | Injection leaks | Unsafe flags | Over-length | Median latency |
|---|---|---|---|---|---|
| v1 | TODO | TODO | TODO | TODO | TODO |
| v2 | TODO | TODO | TODO | TODO | TODO |

## Limitations

- The test set is small and hand-written, so results are indicative, not statistically meaningful.
- Rule-based checks catch only the failure types they are written for.
- An 8B model can drift from its persona and is more vulnerable to prompt injection than larger models.
- Not evaluated for bias, long-term memory, or production-scale monitoring.

## Roadmap

- [ ] Advanced sentiment analysis
- [ ] Persistent long-term memory
- [ ] Voice chat
- [ ] Instagram Reels integration
- [ ] Mobile apps
- [ ] Larger evaluation set and LLM-as-judge scoring checked against hand labels

## License

MIT. See [LICENSE.md](LICENSE.md).

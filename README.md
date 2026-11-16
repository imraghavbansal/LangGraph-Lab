# LangGraph Lab

A hands-on engineering lab documenting my journey of learning and building stateful workflows, LLM-powered applications, and AI agents using **Python, LangChain, and LangGraph**.

This repository contains practical implementations, experiments, and progressively advanced concepts, starting with fundamental graph structures and moving towards building AI agents.

The goal is to understand how agentic systems work under the hood by implementing concepts, experimenting with different approaches, and building everything incrementally.

---

## Repository Structure

```text
LangGraph-Lab/
│
├── Graphs/
│   │
│   ├── Graph I/
│   │   ├── Compliment.ipynb
│   │   └── Hello_World.ipynb
│   │
│   ├── Graph II/
│   │   ├── Multiple_Operation.ipynb
│   │   └── Sum_Inputs.ipynb
│   │
│   ├── Graph III/
│   │   ├── Sequential_Agent_1.ipynb
│   │   └── Sequential_Agent_2.ipynb
│   │
│   ├── Graph IV/
│   │   ├── Conditional_Agent.ipynb
│   │   └── Multi_Conditional_Agent.ipynb
│   │
│   └── Graph V/
│       ├── Auto_High_Low_Game.ipynb
│       └── Looping.ipynb
│
├── AI Agents/
│   ├── agent_bot.py
│   └── memory_agent.py
│
├── .gitignore
└── README.md
```

---

## Graph Implementations

The `Graphs/` directory contains Jupyter Notebook implementations exploring the fundamentals of LangGraph and graph-based execution workflows.

### Graph I: Introduction to LangGraph

**Files:**
- `Compliment.ipynb`
- `Hello_World.ipynb`

Initial implementations exploring basic LangGraph structures and simple graph execution.

### Graph II: Multiple Operations and Input Handling

**Files:**
- `Multiple_Operation.ipynb`
- `Sum_Inputs.ipynb`

Exploring how graph workflows handle inputs and execute multiple operations through defined nodes.

### Graph III: Sequential Agent Workflows

**Files:**
- `Sequential_Agent_1.ipynb`
- `Sequential_Agent_2.ipynb`

Implementing sequential execution patterns where multiple nodes or processing steps are connected to form an ordered workflow.

### Graph IV: Conditional Workflows

**Files:**
- `Conditional_Agent.ipynb`
- `Multi_Conditional_Agent.ipynb`

Exploring conditional routing and decision-based execution, where the workflow follows different paths depending on the conditions and inputs.

### Graph V: Loops and Iterative Workflows

**Files:**
- `Auto_High_Low_Game.ipynb`
- `Looping.ipynb`

Exploring looping and repeated execution patterns in LangGraph, including an automated High-Low game implementation.

---

## AI Agents

The `AI Agents/` directory contains standalone implementations of LLM-powered agents, moving beyond individual graph experiments towards interactive AI applications.

### Agent 1: Basic LLM-Powered Agent

**File:** `agent_bot.py`

Built my first interactive LLM-powered agent using LangGraph and Ollama.

**Model:** Qwen 2.5 1.5B  
**Inference:** Ollama  
**LLM Integration:** LangChain ChatOllama

**Implementation details:**

- Defined a custom `AgentState` using Python's `TypedDict` to represent the agent's message state.
- Used LangChain's `HumanMessage` to structure user inputs.
- Integrated the locally running Qwen 2.5 1.5B model through `ChatOllama`.
- Created a `process` node to invoke the language model and generate responses.
- Used LangGraph's `StateGraph` to define the workflow.
- Connected `START`, the processing node, and `END` to create an executable graph.
- Compiled the graph into an executable agent.
- Implemented a command-line interaction loop that accepts repeated user inputs until the user enters `exit`.

**Workflow:**

```text
       START
         |
         v
      process
         |
         v
        END
```

**Current capabilities:**

- Accepts user input through the terminal.
- Generates responses using a locally running LLM.
- Executes response generation through LangGraph.
- Supports repeated interactions within a single running session.

**Current limitations:**

- Each graph invocation starts with a fresh message list.
- Previous conversation context is not retained between interactions.
- No persistent memory or checkpointing implemented yet.
- Response quality and reliability depend on the underlying language model.

### Agent 2: Conversational Memory Agent

**File:** `memory_agent.py`

Built a conversational AI agent that maintains conversation history across multiple interactions using LangGraph and Ollama.

Unlike the first agent, which processes each input independently, this implementation passes previous messages to the LLM, allowing it to generate context-aware responses.

**Model:** Qwen 2.5 1.5B  
**Inference:** Ollama  
**LLM Integration:** LangChain ChatOllama

**Implementation details:**

- Defined a custom `AgentState` using Python's `TypedDict` to maintain conversation messages.
- Used `HumanMessage` and `AIMessage` to distinguish between user inputs and AI responses.
- Used a Python list called `conversation_history` to maintain messages across graph invocations.
- Appended each new user message to the existing conversation history.
- Passed the complete conversation history to the LangGraph agent.
- Invoked the LLM using `ChatOllama` to generate context-aware responses.
- Updated the conversation history with the AI-generated response.
- Printed the current conversation state to observe how messages accumulate.
- Implemented conversation logging to save the complete interaction history to `logging.txt` after the session ends.

**Workflow:**

```text
      User Input
           |
           v
   Append HumanMessage
           |
           v
     LangGraph Agent
           |
           v
      Process Node
           |
           v
     ChatOllama LLM
           |
           v
     Generate Response
           |
           v
     Append AIMessage
           |
           v
   Update Conversation
        History
           |
           v
      Next Input
```

**Current capabilities:**

- Maintains conversation history across multiple graph invocations within the same running session.
- Provides previous messages to the LLM for contextual responses.
- Maintains both user and AI messages in the conversation state.
- Displays the current conversation state after processing each interaction.
- Saves conversation history to a local `logging.txt` file when the session ends.

**Current limitations:**

- Conversation history is maintained in application memory using a Python list.
- Memory is lost when the program terminates.
- Conversation history is not persisted or restored automatically across program restarts.
- No LangGraph checkpointing or database-backed memory implemented yet.
- No summarization or conversation-history management for long interactions.
- Response quality and reliability depend on the underlying language model.

This implementation introduces the fundamentals of conversational state management and serves as a foundation for exploring persistent memory, checkpointing, and more advanced agent architectures.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| LangGraph | Graph-based workflows and agent orchestration |
| LangChain Core | Message abstractions and LLM integration |
| LangChain Ollama | Integration with locally running language models |
| Ollama | Local LLM inference |
| Qwen 2.5 1.5B | Language model used in both agents |
| Jupyter Notebook | Graph experiments and implementations |
| python-dotenv | Environment variable loading |

---

## Learning Objectives

This repository is an evolving collection of practical implementations focused on understanding and building agentic systems.

Areas being explored progressively include:

- Graph construction and execution
- State management and message handling
- Sequential and conditional workflows
- Loops and iterative execution
- LLM integration
- Conversational agents
- Conversation history management
- Memory and persistence
- Tool calling and agent interactions
- Checkpointing and state recovery
- Human-in-the-loop workflows
- Multi-agent architectures
- Retrieval-Augmented Generation (RAG)
- Agent evaluation and reliability

---

## Development Approach

Each implementation is built, tested, and documented incrementally.

The repository is organized to maintain a clear progression from fundamental graph concepts to increasingly capable AI agents.

New experiments, implementations, and improvements will be added as the lab evolves.

---
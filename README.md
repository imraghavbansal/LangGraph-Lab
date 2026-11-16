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
│   └── agent_bot.py
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

### Agent 1: LLM-Powered Conversational Bot

**File:** `agent_bot.py`

Built my first interactive LLM-powered bot using LangGraph and Ollama.

**Model:** Qwen 2.5:1.5B or Qwen 2.5:3B
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

**Current workflow:**

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
- Executes the response generation workflow through LangGraph.
- Supports repeated interactions within a single running session.

**Current limitations:**
- Conversation context is not maintained across separate graph invocations.
- No persistent memory or checkpointing implemented yet.
- Response quality and reliability depend on the underlying language model.

This implementation serves as the starting point for exploring more advanced agent capabilities.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| LangGraph | Graph-based workflows and agent orchestration |
| LangChain | LLM integration and message abstractions |
| Ollama | Local LLM inference |
| Qwen 2.5 1.5B | Language model used in the first agent |
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
- Memory and persistence
- Tool calling and agent interactions
- More advanced agentic workflows

---

## Development Approach

Each implementation is built, tested, and documented incrementally.

The repository is organized to maintain a clear progression from fundamental graph concepts to increasingly capable AI agents.

New experiments, implementations, and improvements will be added as the lab evolves.

---

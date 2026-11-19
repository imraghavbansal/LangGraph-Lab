# LangGraph Lab

A hands-on engineering lab documenting my journey of learning and building stateful workflows, LLM-powered applications and AI agents using **Python, LangChain and LangGraph**.

This repository contains practical implementations, experiments and progressively advanced concepts, starting with fundamental graph structures and moving towards building LLM-powered agents capable of maintaining conversational context, using tools and interacting with external systems.

<<<<<<< HEAD
=======
The goal is to understand how agentic systems work under the hood by implementing concepts, experimenting with different approaches and building everything incrementally.

>>>>>>> 4aef170 (feat(agents): add tool-driven document drafting agent)
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
│   ├── memory_agent.py
│   ├── ReAct.py
│   └── Drafter.py
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

Initial implementations exploring basic LangGraph structures, nodes, edges and simple graph execution.

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

Exploring conditional routing and decision-based execution, where the workflow follows different paths depending on conditions and inputs.

### Graph V: Loops and Iterative Workflows

**Files:**
- `Auto_High_Low_Game.ipynb`
- `Looping.ipynb`

Exploring looping and repeated execution patterns in LangGraph, including an automated High-Low game implementation.

---

## AI Agents

The `AI Agents/` directory contains standalone implementations of LLM-powered agents, progressively introducing conversational context, tool calling, graph-based control flow and document operations.

All four agents currently use **Qwen 2.5 1.5B** through Ollama and LangChain's `ChatOllama` integration.

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
- Connected `START`, the processing node and `END` to create an executable graph.
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
- No persistent memory or checkpointing implemented.
- Response quality and reliability depend on the underlying language model.

This implementation introduces the fundamentals of integrating an LLM into a LangGraph workflow.

---

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
      ChatOllama
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
- No LangGraph checkpointing or database-backed memory implemented.
- No summarization or conversation-history management for long interactions.
- Response quality and reliability depend on the underlying language model.

This implementation introduces conversational state management and serves as a foundation for exploring persistent memory and checkpointing.

---

### Agent 3: ReAct Agent (Reasoning and Acting)

**File:** `ReAct.py`

Built a ReAct (Reasoning and Acting) agent using LangGraph, LangChain and Ollama.

Unlike the previous agents, this implementation allows the LLM to interact with tools, select appropriate operations and use their execution results to continue processing.

**Model:** Qwen 2.5 1.5B  
**Inference:** Ollama  
**LLM Integration:** LangChain ChatOllama

**Implementation details:**

- Defined a custom `AgentState` using Python's `TypedDict` to manage messages.
- Used `Annotated` with LangGraph's `add_messages` reducer to manage message state updates.
- Used `BaseMessage` to represent different types of messages in the conversation.
- Created mathematical tools using LangChain's `@tool` decorator:
  - `add`: Adds two numbers.
  - `subtract`: Subtracts one number from another.
  - `multiply`: Multiplies two numbers.
- Used `bind_tools()` to make the available tools accessible to the LLM.
- Created a `model_call` node to invoke the LLM with system instructions and conversation messages.
- Used LangGraph's prebuilt `ToolNode` to execute tool calls requested by the model.
- Implemented a `should_continue` function to check whether the LLM requested a tool call.
- Used conditional edges to route execution either to the tools node or `END`.
- Connected the tools node back to the LLM node, creating a cyclic execution workflow.
- Used `ToolMessage` to pass tool execution results back to the LLM.
- Implemented streaming with `stream()` and `stream_mode="values"` to observe graph state updates during execution.

**Workflow:**

```text
          START
            |
            v
         our_agent
            |
            v
      should_continue
            |
       +----+----+
       |         |
   Tool Calls   No Tool Calls
       |         |
       v         v
     tools       END
       |
       v
  Tool Results
       |
       v
    our_agent
       |
       v
   Check Again
```

**Example execution:**

Input:

```text
Add 4 + 12 and then multiply the result by 4
and then subtract 64 from that result.
```

The agent uses its available mathematical tools to perform the operations:

```text
Addition:        4 + 12 = 16
Multiplication:  16 * 4 = 64
Subtraction:     64 - 64 = 0
```

**Final result:** `0`

**Current capabilities:**

- Accepts mathematical queries through the graph input.
- Uses an LLM with access to multiple mathematical tools.
- Allows the model to decide when tools are required.
- Executes requested tools through LangGraph's `ToolNode`.
- Uses conditional routing to determine the next execution step.
- Supports cyclic execution between the LLM and tool nodes.
- Passes tool execution results back to the LLM.
- Streams graph state updates during execution.

**Current limitations:**

- Currently implements only three mathematical tools.
- Tool selection depends on the language model's tool-calling capabilities.
- No persistent memory or checkpointing implemented.
- No human approval mechanism for tool execution.
- No advanced tool error handling or retry strategy implemented.

This implementation introduces the ReAct pattern and demonstrates how LLMs can interact with external tools through graph-based orchestration.

---

### Agent 4: Drafter (Tool-Driven Document Writing Agent)

**File:** `Drafter.py`

Built a document-writing AI agent using LangGraph, LangChain and Ollama.

Drafter is designed to help users create, modify and save text documents through natural language instructions.

Unlike the previous agents, this implementation introduces document-specific tools that allow the LLM to modify application data and perform local file operations.

**Model:** Qwen 2.5 1.5B  
**Inference:** Ollama  
**LLM Integration:** LangChain ChatOllama

**Implementation details:**

- Defined a custom `AgentState` using Python's `TypedDict`.
- Used `Annotated` with LangGraph's `add_messages` reducer to manage message state updates.
- Used LangChain's `BaseMessage`, `HumanMessage`, `AIMessage`, `SystemMessage` and `ToolMessage` abstractions.
- Created a global `document_content` variable to maintain the current document content during execution.
- Created an `update` tool using LangChain's `@tool` decorator to replace the current document content.
- Created a `save` tool to write the current document content into a local `.txt` file.
- Implemented automatic `.txt` extension handling when saving files.
- Used `ChatOllama` with `bind_tools()` to provide the LLM with access to document operations.
- Created an `our_agent` node that combines system instructions, conversation history and new user input before invoking the model.
- Included the current document content in the system prompt so the LLM can work with the latest document state.
- Used LangGraph's prebuilt `ToolNode` to execute the document tools.
- Implemented a `should_continue` function to inspect tool messages and determine whether the document has been saved.
- Created a cyclic workflow between the agent and tools node.
- Used `app.stream()` with `stream_mode="values"` to observe state updates during execution.
- Implemented a `print_messages` function to display recent tool execution results.
- Created a `run_document_agent()` entry point to start the interactive document-writing session.

**Workflow:**

```text
             START
               |
               v
          Agent Node
               |
               v
          Model Invoke
               |
               v
        Tool Call Generated
               |
               v
           ToolNode
               |
          +----+----+
          |         |
          v         v
        update     save
          |         |
          v         v
    Update Current  Save .txt
      Document      File
          |         |
          v         v
       Continue    END
          |
          v
       Agent Node
          |
          v
     Next User Input
```

**Available tools:**

| Tool | Functionality |
|---|---|
| `update(content)` | Replaces the current document with the supplied content |
| `save(filename)` | Saves the current document to a local text file |

**Current capabilities:**

- Accepts natural language instructions through the terminal.
- Creates and modifies document content using an LLM.
- Uses tool calling to decide when document operations are required.
- Maintains the current document content during the running session.
- Updates the document through the `update` tool.
- Displays document modification results through tool messages.
- Saves documents locally as `.txt` files.
- Automatically appends the `.txt` extension when it is missing.
- Continues the interactive workflow after document modifications.
- Terminates the graph when the save operation is detected.
- Streams graph state updates during execution.

**Current limitations:**

- Document content is stored in a global Python variable.
- Document content is lost when the application terminates unless it has been saved.
- No database-backed document storage or persistent memory implemented.
- No document versioning or undo functionality.
- No human approval mechanism before file operations.
- No advanced file validation or path restrictions.
- The current implementation supports plain text documents rather than structured document formats.
- Tool routing and execution depend on the model's tool-calling capabilities.

This implementation introduces practical tool-driven workflows and demonstrates how an LLM can interact with application state and perform file operations through LangGraph.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| LangGraph | Graph-based workflows and agent orchestration |
| LangChain Core | Message abstractions, tool definitions and LLM integration |
| LangChain Ollama | Integration with locally running language models |
| Ollama | Local LLM inference |
| Qwen 2.5 1.5B | Language model used across the four agents |
| Jupyter Notebook | Graph experiments and implementations |
| python-dotenv | Environment variable loading |

---

## Core Concepts Explored

This repository progressively explores the following concepts:

- Graph construction and execution.
- Nodes, edges and graph compilation.
- State management using `TypedDict`.
- Message handling and message types.
- Reducers and state updates.
- Sequential and conditional workflows.
- Loops and cyclic graph execution.
- LLM integration using ChatOllama.
- Conversational history management.
- Tool definitions using the `@tool` decorator.
- Tool binding using `bind_tools()`.
- Tool execution using `ToolNode`.
- Conditional routing and execution control.
- ReAct architecture.
- Streaming graph execution.
- Application-level document state management.
- Local file operations through agent tools.

---

## Learning Roadmap

This repository is an evolving collection of practical implementations focused on understanding and building increasingly capable agentic systems.

Future areas of exploration include:

- LangGraph checkpointing and persistent memory.
- Database-backed conversation history.
- Conversation summarization and memory management.
- Advanced tool calling and error handling.
- Human-in-the-loop workflows and approval mechanisms.
- Multi-agent architectures.
- Retrieval-Augmented Generation (RAG).
- Vector databases and semantic search.
- Agent evaluation and reliability.
- Structured outputs and validation.
- Production-oriented agent architecture.

---

## Development Approach

Each implementation is built, tested and documented incrementally.

The repository is organized to maintain a clear progression from fundamental graph concepts to increasingly capable AI agents.

The focus is on understanding the underlying concepts, writing implementations, experimenting with different approaches and maintaining meaningful documentation and Git history.

<<<<<<< HEAD
---
=======
New experiments, implementations and improvements will be added as the lab evolves.

---

**Built as a continuous learning and engineering project.**
>>>>>>> 4aef170 (feat(agents): add tool-driven document drafting agent)

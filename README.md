# AI Automation Research Agent

An autonomous research assistant built with **LangChain**, **Google Gemini API** (`gemini-3.6-flash`), and **DuckDuckGo Web Search**. 

The agent accepts high-level research goals, breaks them down into sub-tasks, performs real-time internet searches, runs custom python calculation tools, and produces structured summary reports with complete workflow logging.

---

## 📌 Features

* **Autonomous Tool Usage:** Used the **ReAct (Reasoning + Acting)** pattern to decide when to search the web vs. when to use local tools.
* **Live Web Research:** Fetched up-to-date web data using zero-cost DuckDuckGo search integration.
* **Custom Python Tools:** Extensible architecture using LangChain's `@tool` decorator (e.g., custom word counter and calculator).
* **Automated Workflow Logging:** Captured step-by-step reasoning, executed tool calls, and final outputs in `agent_workflow.log`.
* **Isolated Development Environment:** Configured to run reliably inside a dedicated Conda virtual environment.

---

## 🛠️ System Architecture

```text
       [ User Research Prompt ]
                  │
                  ▼
   ┌─────────────────────────────┐
   │    Google Gemini API LLM    │
   │  (Reasoning & Task Planner) │
   └──────────────┬──────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
  ┌──────────────┐  ┌──────────────┐
  │ DuckDuckGo   │  │ Custom Python│
  │ Search Tool  │  │ Tools        │
  └──────┬───────┘  └──────┬───────┘
         │                 │
         └────────┬────────┘
                  ▼

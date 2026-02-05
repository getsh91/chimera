flowchart LR
  subgraph ControlPlane["Central Orchestrator (Control Plane)"]
    Dashboard["Operator Dashboard"]
    Policy["Governance & Policies
(.cursor/rules, CodeRabbit policy, specs)"]
    State["Global State & Tenant Config
(Postgres)"]
  end

  subgraph Swarm["Agent Swarm Runtime"]
    Planner["Planner Service
Decompose goals → Task DAG"]
    Queue["Queues
(Redis)"]
    Workers["Worker Pool (N)
Stateless Executors"]
    Judge["Judge Service
QA + Safety + OCC"]
  end

  subgraph Memory["Memory + Data Layer"]
    PG["PostgreSQL
Transactional truth
(tasks, audits, approvals)"]
    WV["Weaviate
Semantic memory
(persona, long-term recall)"]
    RD["Redis
Episodic cache + queues"]
  end

  subgraph MCP["MCP Servers (External World)"]
    Social["mcp-server-social
post / reply / mentions"]
    News["mcp-server-news
RSS / search resources"]
    Gen["mcp-server-generation
image / video tools"]
    Wallet["mcp-server-coinbase
wallet + actions"]
  end

  Dashboard --> Planner
  Policy --> Planner
  Policy --> Judge
  Planner --> Queue
  Queue --> Workers
  Workers --> Judge
  Judge --> PG
  Judge --> WV
  Queue <--> RD
  PG --> State
  Workers --> MCP
  MCP --> Workers

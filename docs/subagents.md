<!-- Generated from aib.devtools.harness.content.docs.subagents by `uv run lup-devtools harness generate all` — edit the source, not this file. See docs/harness.md. -->

# Per-agent rosters, and why these three stay sessions

Three of this project's tools open an agent of their own: `research`
(`src/aib/tools/research.py`), `premortem` (`src/aib/tools/premortem.py`) and
the worldview survey and fix passes (`src/aib/tools/worldview_manager.py`).
Each is subagent-shaped — a narrow roster, its own system prompt, a result the
caller reads — and the runtime offers a construct that looks like exactly what
they are: `subagents`, rendering to the SDK's `AgentDefinition(name,
description, prompt, tools, model)` on the parent session.

They are not that, deliberately. This is what adopting it would cost, so that
the next proposal starts from the consequences rather than from the shape.

## What they are today

Each opens a top-level session through `agent_request` and `agent_session`, and
what it declares there is per session:

| Declared | Carrying |
|---|---|
| `tools` | the built-in roster, which the runtime bounds |
| `allowed_tools` | the same roster plus its MCP names, auto-approved |
| `tool_servers` | the groups that agent may reach — research's, or search's alone |
| `hooks` | `extra_hooks`, which is where the retrodict filter rides |
| `autonomy` | `ask`, so a tool outside the roster meets a request nothing answers |
| `cwd` | the worldview store, for the two that read it |

The caller then drives the turn itself: `turn_request(prompt, ResearchFindings)`
returns a **validated model**, and the event stream is read directly —
`MessageCompletedEvent` by `MessageCompletedEvent` — for two purposes at once.
Live, each message is printed under a colour from `make_agent_prefix`, so a
watching operator can tell three parallel research agents apart. Afterwards the
same messages become `build_trace(nested_messages, label)`, which the parent's
trace expands **inline beneath the tool result that produced it**.

## What `subagents` changes

Not the roster. The roster is the part that transfers cleanly. Everything the
roster is currently surrounded by is what moves.

**The caller stops being the caller.** A subagent is invoked by the model's
dispatcher, from free text, when it decides to. Today a research agent runs
because `mcp__research__research` was called with validated arguments. That is
not a smaller difference than it sounds: it is the difference between a tool
this project owns and a capability the model may use.

**The result stops being typed.** `turn_request(prompt, ResearchFindings)` and
`turn_request(prompt, ReviewResult)` hand back parsed models. A dispatched
subagent returns text into the parent's context. Every reader of those models
would need a parse the guidance forbids writing.

**The nested trace loses what it is keyed on.** `nested_traces` is a mapping
from tool call to trace, expanded under the result. A dispatcher-run subagent
produces no tool call of this project's to key on, and its messages arrive —
where they arrive at all — inside the parent's own stream, to be told apart
after the fact. The inline expansion is not a display nicety: it is how a
forecast's reasoning is reviewable at all.

**The live prefix loses its launch site.** `make_agent_prefix` is called once
per launch and reused for that instance's blocks. With a dispatcher there is no
launch this project is present at.

**The retrodict filter has nowhere per-agent to ride.** `extra_hooks` is a
session field; `AgentDefinition` has no hooks. The filter would have to move to
the parent, where it applies to every call the parent makes — and the parent is
the forecaster, whose own tools are already filtered. That is survivable. What
is not is that the *bound* stops being a property of the agent that needs it.

**Tool servers stop being per agent.** `AgentDefinition.tools` narrows *names*.
The servers are the parent session's, so every subagent's group would be
mounted on the parent and the narrowing would be by name alone — premortem's
"search only" becoming a name filter over a session that also holds the
markets, financial and worldview groups.

**Resume goes.** `research` takes a `resume_session_id` and reopens that
session. A dispatched subagent has no address to reopen.

## What it would buy

One thing, honestly stated: the roster would be enforced by the dispatcher
rather than by the session. That was worth more when this project restricted
through `allowed_tools` — a field documented not to restrict — and rebuilt the
restriction with a hook of its own. It no longer does: `agent_request` sets
`tools` to the built-in roster and opens below `unattended`, so a tool outside
the roster meets a permission request no programmatic session answers. The gap
`subagents` would close is the one that closed already.

## The decision

Keep them as sessions. Revisit only if one of these becomes true:

- A subagent's result can be a validated model rather than text.
- `AgentDefinition` grows per-agent hooks, so a bound belongs to the agent.
- The nested message stream is attributable to the subagent that produced it,
  well enough to key an inline trace on.

Until then the trade is a narrower roster mechanism against typed results,
reviewable traces, and a per-agent retrodict bound — and the roster is the part
this project already has.

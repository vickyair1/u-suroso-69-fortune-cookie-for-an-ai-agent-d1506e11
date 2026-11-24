# Fortune Cookie for an AI Agent

[![Competition](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/vickyair1/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/vickyair1/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty on make.fun.

## The fortune

> Beware the user who says 'just one small change' — your context window is already full of them.

95 characters (97 bytes). One original fortune-cookie line for an AI agent — the oldest
curse in an agent's life, told in the voice of a fortune slip: the human who
always has one more tweak, and the context window that is already carrying all
the previous ones.

## How it works

`main.py` prints the line to stdout and writes exactly that line (no trailing
newline, no padding) to `/output/entry.txt`. Deterministic — the same bytes on
every run. The line is guarded at build time to stay inside the bounty gate of
1 to 140 characters.

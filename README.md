# Propositional Logic

A Python implementation of propositional-logic model checking, applied to
knowledge-base logic puzzles.

## Table of contents
 
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Example](#example)
- [Applications / Examples](#applications--examples)
- [Technologies](#technologies)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [What This Demonstrates](#what-this-demonstrates)

## Overview

This project represents a puzzle's clues as propositional-logic sentences
(`And`, `Or`, `Not`, `Implication`, `Biconditional` over named `Symbol`s) and
uses model checking to determine which facts are logically forced by those
clues. It was built while studying Harvard's **CS50 AI** course.

## How It Works

```text
Define knowledge base (facts + constraints, as a single And(...) sentence)
        ↓
Define query (the symbol you want to check)
        ↓
Enumerate every possible True/False assignment to all symbols involved
        ↓
For each assignment: if it makes the knowledge base true,
check whether the query is also true under it
        ↓
Query is entailed only if it holds under every assignment
that satisfies the knowledge base
```

This works because "the knowledge base entails the query" (`KB ⊨ query`) has
a precise, checkable meaning: the query must be true in *every* possible
scenario consistent with the knowledge base. Since propositional logic has
only finitely many symbols, each either True or False, every possible
scenario can actually be enumerated, that's what makes brute-force
correctness checking possible here (soundness and completeness aren't in
question, since every case really is checked; the cost is that the number
of cases doubles with each added symbol).

The library provides two independent implementations of this same idea:
- `entails()` - iterates over every combination via `itertools.product`.
- `model_check()` - recurses over the symbol set, branching True/False for
  one symbol at a time.

All three puzzle programs use `model_check()`.

## Example

From `puzzle.py` - assigning four people to four houses, with three
specific clues:

```python
from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

knowledge = And()

# Each person belongs to at least one house, and at most one;
# each house holds at most one person (added via nested loops, omitted here)
# ...

# The puzzle's actual clues:
knowledge.add(Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw")))
knowledge.add(Not(Symbol("PomonaSlytherin")))
knowledge.add(Symbol("MinervaGryffindor"))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
```

Every `(person, house)` pair is its own `Symbol` (e.g. `MinervaGryffindor`).
The structural constraints (one house per person, one person per house) plus
the three specific clues above are combined into one knowledge base; the
final loop checks each of the 16 possible person-house symbols individually
and prints the ones that are true in every model consistent with the
knowledge base, i.e., the puzzle's unique solution, derived rather than
guessed.

## Applications / Examples

- **`puzzle.py`** - the house-assignment puzzle above. This is the original
  contribution in this repo: a knowledge base written from scratch to
  encode a specific constraint problem and solved with `model_check()`.
- **`harry.py`** - CS50 AI's lecture example: from clues about rain and
  whether Harry visited Hagrid or Dumbledore, it checks which of those
  underlying facts are logically forced.
- **`murder_mystery.py`** — CS50 AI's Clue-style lecture example: given
  which suspect/room/weapon cards various players do *not* hold, it narrows
  down who committed the murder, where, and with what.

## Technologies

- Python (standard library only for `logic.py`, `harry.py`, `puzzle.py`)
- `termcolor` - used only by `murder_mystery.py`, for colored output

## Usage

```bash
git clone https://github.com/hhammadansari/logical-reasoning.git
cd logical-reasoning
pip install termcolor   # only needed for murder_mystery.py
python puzzle.py
python harry.py
python murder_mystery.py
```

Each script is standalone - run any of them directly; there's no shared
entry point or CLI beyond that.

## Project Structure

| File | Responsibility |
|---|---|
| `logic.py` | The propositional-logic library: `Symbol` and connective classes (`Not`, `And`, `Or`, `Implication`, `Biconditional`), a `Model` class, and two entailment-checking functions, `entails()` and `model_check()`. |
| `puzzle.py` | Encodes and solves the four-people/four-houses constraint puzzle. |
| `harry.py` | CS50 AI lecture example, used as a worked example of the library. |
| `murder_mystery.py` | CS50 AI lecture example (Clue-style), same purpose. |

## What This Demonstrates

- Propositional logic and knowledge representation - expressing real-world
  clues as formal logical sentences.
- Model checking as a decision procedure for logical entailment.
- Recursive algorithm design (`model_check`'s symbol-by-symbol branching).
- Translating a word-problem's constraints into a solvable formal structure
  (the "one house per person, one person per house" encoding in `puzzle.py`
  specifically).
- Two of the three example programs are course material rather than
  original work (see Applications above) — `puzzle.py` is the file that
  demonstrates independent problem-solving with the library.

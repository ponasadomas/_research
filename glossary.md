# Glossary

The words used in research here, each with one meaning. Agents and people use these words
and no others for these things. When a new word is needed, it is added here first.

## The material

| Word | Meaning | Not to be confused with |
|---|---|---|
| **Crowd** | A place, or a set of places, where people gather and write: for example 22 subreddits. Collected whole | A niche. A crowd has no subject |
| **Source** | One kind of place material comes from: Reddit, a forum, reviews, ads | |
| **Post** | One opening message of a thread, written by one person. The unit that is read and counted | A reply |
| **Reply** | A message under a post. "The poster's own replies" are those written by the post's author | |
| **Thread** | A post with all the replies under it | |
| **Pool** | All the posts a sample is drawn from. Its size is always written down | |
| **Sample** | The posts drawn from the pool at random to be read. Never chosen by a keyword | |
| **Seed** | The number that makes a random draw repeatable: same seed, same sample | |

## The people and programs doing the work

| Word | Meaning |
|---|---|
| **Owner** | The person who decides. Says yes at the end of each step |
| **Supervisor** | The agent in the conversation with the owner. Prepares the work, sends agents, checks and commits |
| **Agent** | A program instance sent to do one piece of work from a brief. Every agent below is one |
| **Reader** | An agent that reads posts and describes or marks each one |
| **Coder** | An agent that tags posts that were already read against a list. Used once, to test the pattern list |
| **Digest reader** | An agent that reads all the posts of one pattern and sorts them into forms |
| **Section writer** | An agent that merges one pattern's digests into one section |
| **Findings writer** | An agent that writes the findings page and her words from the sections |
| **Runner** | A script that sends a set of agents, checks each output, repeats a failed one once, commits, and stops by itself. `run_*.sh` |
| **Checker** | A script that tests an agent's output: every post accounted for, every quote word for word, counts adding up. `verify_*.py`, `check_*.py` |

## How the work is cut up

| Word | Meaning |
|---|---|
| **Brief** | The written instructions one kind of agent gets. Holds its rules and allowed values; names no product |
| **Share** | The set of posts given to one agent. About 150 posts for a reader, up to about 300 for a digest reader |
| **Block** | Several shares made and sent together (5 shares by default) |
| **Reading** | One run of readers over one sample, under one brief. It has a name and a folder: first reading, second reading, age re-read |
| **Re-read** | A reading of posts that were already read, under a corrected brief. Its rows replace the earlier ones |
| **Trial** | The first block of a reading, looked at before the rest is sent |
| **Usage** | The allowance of the agent provider's subscription. A run stops when it is used up |

## The two kinds of reading

| Word | Meaning |
|---|---|
| **Map reading** | Reading a sample of a crowd with no subject in mind. Every post is described; none is marked in or out. Step 2 of the five steps |
| **Map** | The counts made from a map reading: what the crowd writes about, in which situations, how often. Step 3 |
| **Deep reading** | Reading for one chosen niche: marks, patterns, quotes, digests, sections, findings. Step 5 |

## What a reader writes down

| Word | Meaning |
|---|---|
| **Mark** | In a deep reading, a reader's verdict on a post: **yes** (on the niche), **near** (touches it, or in doubt), **no** (off it) |
| **On-niche post** | A post marked yes |
| **Border** | For a near post, the one reason it is near and not yes: for example "sleep", "age unknown", "older than 48 months" |
| **Stage** | The situation the post is in, from a fixed list. For the mothers' crowd it is the child's age band |
| **Pattern** | One of a short numbered list of things on-niche posts are about, for example "Is this normal, or is something wrong with my child?". Every on-niche post gets one **main pattern** |
| **Pattern list** | That list. Drafted from a first reading, tested, then fixed for the main reading |
| **Quote** | A passage copied word for word from a post, with an id |
| **Quote record** | The stored form of one quote: id, post, source, date, stage, type, the words |
| **Tag** | Any fixed value a reader attaches to a post: a mark, a border, a stage, a pattern |

## What is made from the readings

| Word | Meaning | Where |
|---|---|---|
| **Counts page** | The numbers of one reading: marks, patterns, stages, borders, paying. Made by script | `evidence/<round>/<reading>/counts.md` |
| **Form** | One distinct situation, worry or wish inside a pattern, worded as one claim, with the number of posts that show it. Smaller than a pattern | inside a digest |
| **Digest** | One digest reader's sorting of one share of a pattern into forms, with quotes | `evidence/<round>/<reading>/digest-NN.md` |
| **Section** | One pattern's digests merged into one short page | `findings/<round>/patterns*/pattern-NN.md` |
| **Finding** | One claim with its count of posts, its quotes, and what cuts against it | in a section or the findings page |
| **Findings page** | All findings for one question, short enough to read in one sitting | `findings/<question>.md` |
| **Her words** | Phrases and sentences copied word for word, for use in copy | `her-words.md` |
| **Evidence** | Everything between the quotes and the findings: counts pages and digests | `evidence/` |
| **Count** | Always a number of posts in a random sample, written with what it is out of: "595 of 2,471 posts" | |

## The frame

| Word | Meaning |
|---|---|
| **Niche** | A slice of a crowd's map that the owner chose: a subject and its range |
| **Definition** | The one line that says a niche's subject and range. Never who she is or what her problem is. In `~/GitHub/_home/library/niches.md` |
| **The five steps** | Pick the crowd; map reading; the map; choose a niche; deep reading. `~/GitHub/_home/playbooks/new-niche.md` |
| **Round** | All the research done on a niche in one period, named by year and month: `2026-11` |
| **Avatar** | The portrait of the buyer, written from reviewed findings. Not research; lives in `_home` |
| **Run-book** | The page that lists each step with its command: `_tools/README.md` |

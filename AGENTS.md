# AGENTS.md

These instructions apply to learning materials and code in this repository.

## Project purpose and audience

`programmers-python-kit` teaches Python 3 through Programmers School problems, from first programming concepts to Skill Check and coding tests. The primary learner is a fifth-grade elementary school student with no Python experience.

The first goal is Skill Check Level 1 readiness through 50 problems. Learning means being able to explain an approach and solve the problem again without help, rather than merely collecting accepted solutions.

This is a repository of original solutions, explanations, and learning notes, not a mirror of official problem statements.

## Curriculum and scope

Keep the initial curriculum in this order:

| Stage | Location | Problems | Focus |
|---|---|---:|---|
| Python Prep | `prep/` | 20 | Numbers and functions, conditions, loops and lists, strings |
| Level 1 Core | `level-1/` | 25 | Numbers and iteration, number properties, strings, lists and sorting, problem-solving patterns |
| Level 1 Checkpoint | `level-1/checkpoint/` | 5 | Independent practice before Skill Check |

- Teach Python thinking first; increase algorithm study substantially from Level 2, including hash tables, stacks/queues, sorting, exhaustive search, greedy algorithms, and DFS/BFS.
- Order problems by prerequisites and interpretation difficulty, not acceptance rates alone. Explain unfamiliar syntax before relying on it.
- Identify each problem's prerequisites, core concepts, and review criteria.
- Check that Prep actually introduces its completion criteria: variables, functions, `return`, conditions, `for`, `while`, `range()`, strings, lists, indexing, slicing, `len()`, `sum()`, `min()`, `max()`, and `sorted()`. Do not assume a topic has been taught merely because it appears in a checklist.
- Complete the initial 50-problem curriculum before expanding into Levels 2–5, unless the user requests otherwise. Future stages are plans, not existing work.
- Do not create all planned directories or solve all problems as a side effect of an unrelated documentation task.

## Repository layout and naming

Use a problem directory containing `README.md` and `solution.py`:

```text
prep/01-two-sum/
level-1/01-even-or-odd/
level-1/02-average/
level-1/checkpoint/01-kth-number/
```

- Use two-digit curriculum numbers and short lowercase English kebab-case slugs. Number Prep, Core, and Checkpoint independently.
- Preserve official Korean problem titles in documents and record the Programmers ID to distinguish problems with similar names.
- The curriculum table determines numbering. The initial planning document's illustrative `level-1/01-average/` path conflicts with its table: Core problem 01 is 짝수와 홀수 and problem 02 is 평균 구하기. Do not copy that mismatch.
- Use `README.md` for root and stage indexes, rather than the C# repository's topic-based `index.md` layout or standalone `_CSharp_학습자료.md` filenames.
- Use `notes/` for reusable Python basics, problem-solving habits, complexity, and mistakes when those notes are needed.
- Keep paths portable across macOS, Linux, and Windows; avoid reserved characters such as `:` and links depending on an absolute local path.

## Teaching approach and language

- Write learner-facing explanations in natural Korean. Use English identifiers and Python API names. Keep this agent guidance in English.
- Explain inputs, expected output, and the approach before presenting code. Encourage a small hand-worked example and a verbal explanation first.
- Make the first solution explicit and easy to follow, using clear variable names, ordinary conditions, and loops where helpful.
- Add a second, more idiomatic Python solution only when it adds learning value. Do not force two versions of a trivial solution.
- Name alternatives for their actual benefit: readability, expression style, running time, or memory use. Do not call a version shorter or faster without checking that claim.
- Introduce comprehensions, `zip()`, sets, dictionaries, sorting keys, and other new constructs with explanations. Avoid unexplained advanced syntax, clever one-liners, or unnecessary abstraction.
- Use short, concrete sentences and step-by-step examples. Avoid repetitive boilerplate, translation-like prose, and generic encouragement.
- Use compact ASCII diagrams, flow diagrams, or memory maps when they make a relationship, sequence, branch, or state change easier to understand. Keep them simple, place them in fenced text blocks, and explain the takeaway in prose; do not add decorative diagrams or force one into every lesson. Line breaks that encode a diagram's structure are not prose hard-wrapping.
- Use emojis actively in learner-facing problem titles and section headings. Assign a consistent emoji to each section role so learners can scan the page quickly, and do not insert emojis into Python examples or identifiers.
- Do not hard-wrap prose or list items to a target column width. Keep each Markdown paragraph or list item on one source line, and use line breaks only where Markdown structure requires them, such as headings, lists, tables, block quotes, and fenced code.

## Required prose review before committing

- After drafting or revising a Korean post, including learner-facing problem explanations and learning notes, apply the `humanize-korean:humanize-korean` skill before committing. Read its `SKILL.md` and follow its review workflow; ordinary proofreading alone does not satisfy this requirement.
- Apply the review to the final prose. If the prose changes afterward, review the affected passages again before committing.
- Preserve technical meaning, problem metadata, code, links, complexity claims, and Checkpoint hint boundaries while polishing the language. Verify that the revised explanation still matches the code and the learner's level.
- If the skill is unavailable, report the missing dependency and stop before committing the affected post. Do not silently skip the review.
- This requirement covers Korean posts and learning materials, not code-only changes, configuration files, or this English agent guidance.

## Problem README structure

Use one top-level title and consistent subordinate headings. Adapt the sections to the problem while retaining the learning context and explanation:

```markdown
# 🧩 공식 문제명

- Programmers ID: ...
- Official link: ...
- Level: ...
- Stage: ...
- Prerequisites: ...
- Core concepts: ...

## 🎯 이 문제에서 배우는 것
## 🔎 문제 핵심
## 💭 먼저 생각해 보기
## 🧪 예제 이해하기

## 🛠️ 풀이 1. 이해하기 쉬운 방법
### 💡 아이디어
### 🐍 Python 코드
### 📖 코드 해설
### ⏱️ 시간 복잡도
### 💾 공간 복잡도

## ✨ 풀이 2. Python다운 방법
## ⚠️ 실수하기 쉬운 점
## ✅ 배운 것
## 🔁 다시 풀어보기

- [ ] 1주일 뒤 힌트 없이 다시 풀기
- [ ] 풀이 방법을 말로 설명하기

## 🚀 이어 풀어 볼 문제
```

- Include the official problem link in each problem README; stage indexes may link to the local README. Verify problem metadata rather than guessing it.
- Summarize the problem in original wording and use original small examples.
- Omit the optional second solution heading when there is no second solution. When included, explain its idea, code, and relevant tradeoffs as well.
- Keep code excerpts, variable names, data structures, and prose synchronized.
- Treat the template as a structure, not completed content: do not leave empty sections or mark a scaffold as solved.
- End each non-Checkpoint problem README with `## 🚀 이어 풀어 볼 문제` and two or three official Programmers links that practice the same concept or extend it by one small step. Verify every title, ID, and URL; explain the connection without revealing the solution.
- Follow the Checkpoint restrictions below before publishing solution sections.

## Python solution rules

- Target the Python 3 environment supported by the relevant Programmers problem. Match its `solution(...)` signature, parameter names where required, and return value. Use standard input/output only when the problem explicitly requires it.
- Keep `solution.py` directly usable for submission, with necessary imports only. Avoid top-level demonstrations, debug output, and local file dependencies.
- Use four-space indentation, descriptive `snake_case` names, and straightforward control flow. Do not compress unrelated statements to save lines.
- Prefer the standard library and built-in data structures. Do not introduce third-party packages or a framework for ordinary problem solutions.
- Explain Python-specific behavior when relevant: `/` versus `//`, mutation versus copying, indexing boundaries, and `list.sort()` versus `sorted()`.
- Explain meaningful input mutation and additional allocations. Do not conceal a performance regression behind shorter syntax.
- Keep the primary executable solution aligned with the first documented solution unless another choice is explicitly documented. Show alternatives separately; do not define multiple competing `solution` functions in one file.

## Complexity analysis

- From Level 1 onward, provide separate time and space complexity analyses for every presented solution. Define the input-size variables used in Big O.
- Explain the work in plain Korean before or alongside the notation. In Prep, prioritize syntax and simple descriptions of repetition and storage; formal analysis is optional when it would distract from the lesson.
- Count sorting, slicing, copied collections, temporary containers, and recursion where applicable. State whether output storage is included in space analysis.
- Match the analysis to the actual Python operations and implementation; do not carry over C# or LINQ assumptions.

## Checkpoint practice

Keep these five problems separate and in order: K번째수 (42748), 완주하지 못한 선수 (42576), 폰켓몬 (1845), 모의고사 (42840), 같은 숫자는 싫어 (12906).

- The learner first works without prior solutions or solution searches. Python syntax lookup is allowed.
- Ask the learner to work through an example by hand and explain an approach before coding.
- Do not reveal answer code, algorithm hints, or solution walkthroughs by default in Checkpoint landing pages or new unsolved problem READMEs. Initially provide metadata, the official link, practice instructions, and reflection prompts.
- For an unsolved Checkpoint, use only the title, ID, official link, level, and stage as problem metadata. Omit the general README template's prerequisites, core concepts, learning objectives, solution sections, and complexity analysis when they would disclose an approach. The Checkpoint hint boundary takes precedence over the general teaching template.
- Add solution material after the independent attempt or when explicitly requested. Keep it in a clearly labeled review section or separate linked material so the initial practice view does not immediately expose answers.
- Record assistance honestly. A guided solution is not an independent pass. Recommend Skill Check Level 1 after all five are solved without hints.

## Verification and progress

The initial learner workflow is: solve on Programmers, pass the judge, save `solution.py`, record learning in the README, and revisit the problem later.

- Do not create a `pytest` file for every problem or require test-framework setup as part of introductory learning.
- For code changes, perform focused syntax and behavior checks using lightweight local calls or assertions with original examples and relevant edge cases. Run existing affected tests if present; do not bypass established checks.
- Local checks do not prove acceptance by the Programmers judge. State exactly what was verified and what was not. Mark judge acceptance or independent completion only when supported by observed results or the user's report.
- When adding, moving, or changing a problem's status, update its stage README and the root README's relevant Progress entries. Keep links, numbering, counts, and actual files consistent. Distinguish planned, implemented, accepted, and independently reviewed work rather than conflating them.
- Checkpoint counts separately from the 25 Core problems; the initial total is 20 + 25 + 5 = 50.
- For documentation-only changes, review Markdown structure, links, metadata, examples, and consistency. Do not add tests solely for prose changes.
- After the affected checks and any required independent review pass, broaden or repeat verification only for a new change, failure, or unresolved concern. Reuse applicable results and state their limits.
- Consider GitHub Actions only when automation is needed; do not add Cloud Build configuration or CI infrastructure merely because a GitHub App is installed.

## Copyright and licensing

- Preserve the MIT License for original solution code, explanations, notes, curriculum, and repository documentation.
- Official problem statements, constraints, input/output examples, images, and test cases remain the content of Programmers and their respective owners; do not present them as covered by this repository's MIT License.
- Do not reproduce official content wholesale. Record titles, IDs, official links, original summaries, and original solutions instead.
- Preserve copyright guidance in README and LICENSE when editing related files.

## Change discipline and completion

- Inspect existing instructions, files, and Git status before editing. Preserve unrelated user changes and limit work to the requested scope.
- Before finishing, review the diff, verify affected materials, and report the changes, verification results, and any unresolved limitations.
- Commit and push only when explicitly requested. Preserve configured signing.
- Use concise English Conventional Commit subjects such as `docs:`, `fix:`, `refactor:`, or `chore:` and include a body explaining the changes and rationale.

When completing an authorized GitHub change, follow this order:

1. Push the working branch.
2. Open a pull request and use squash merge; merge commits and rebase merges are disabled.
3. After confirming the remote merge, update local `main` with `git pull --rebase`.
4. Confirm that local `main` matches `origin/main`.
5. Only then remove the task worktree and delete the local and remote task branches, in that order.

## Design references

These rules adapt the teaching and maintenance conventions from [`programmers-csharp-kit/AGENTS.md`](https://github.com/ruddyscent/programmers-csharp-kit/blob/HEAD/AGENTS.md) and the Obsidian note `Projects/programmers-python-kit/초기 구상.md` consulted on 2026-09-08. The guidance above is self-contained; working in this repository does not require access to the author's Obsidian vault. Reference documents describe design context, not authorization to execute their pending tasks.

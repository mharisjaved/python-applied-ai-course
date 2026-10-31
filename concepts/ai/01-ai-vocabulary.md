# AI Vocabulary in Plain Words

**What it is:** the words you need to talk about AI, data, machine learning and LLMs, each explained in one or two plain sentences.
**Why it exists:** most confusion in Weeks 9–12 comes from fuzzy words ("training", "label", "hallucination"), not from code.

**Taught on:** [Day 41](../../weeks/week-09/day-41-what-is-ai/lesson.md) (AI/ML/DL/GenAI) ·
[Day 42](../../weeks/week-09/day-42-datasets/lesson.md) (datasets, features, labels) ·
[Day 46](../../weeks/week-10/day-46-ml-workflow/lesson.md) (training, testing, baseline) ·
[Day 49](../../weeks/week-10/day-49-evaluation-overfitting/lesson.md) (overfitting, leakage) ·
[Day 51](../../weeks/week-11/day-51-how-llms-work/lesson.md)–[Day 52](../../weeks/week-11/day-52-prompt-design/lesson.md) (LLM words)

## The AI family

| Term | Plain meaning | Example |
|------|---------------|---------|
| **Rule-based program** | a person writes every rule by hand | `if amount > 500: flag it` |
| **AI** (artificial intelligence) | any computer system doing a task that seems to need intelligence | route planner, spam filter, chatbot |
| **ML** (machine learning) | AI that *learns the rules from examples* instead of being told them | predicting a final score from study habits |
| **DL** (deep learning) | ML with very large neural networks; needs lots of data and computing power | speech recognition, image recognition |
| **GenAI** (generative AI) | DL models that *create* new text, images or audio | Claude writing a summary |
| **LLM** (large language model) | a GenAI model trained on huge amounts of text to predict the next token | Claude |

Choosing: clear, stable rules → write rules. Patterns in examples you cannot write down → ML. Free text in or out → GenAI.

## Data words

| Term | Plain meaning |
|------|---------------|
| **Dataset** | a table of examples; each **row** is one example (one student), each **column** is one property |
| **Feature** | an input column the model may use (`study_hours`, `attendance_pct`) |
| **Target / label** | the column we want to predict (`final_score`, `passed`) |
| **Numeric vs categorical** | numbers you can do maths with (`sleep_hours`) vs a fixed set of groups (`program`) |
| **Data quality problems** | missing values, duplicate rows, impossible values (attendance 150 %), inconsistent text (`"Yes"`, `" yes"`) |
| **Bias** | the data or the model treats some groups unfairly, often because the examples were not representative |

## Training and evaluation words

| Term | Plain meaning |
|------|---------------|
| **Model** | the "learned rules": a function from features to a prediction |
| **Training (fit)** | showing the model examples *with* answers so it can adjust itself |
| **Inference / prediction** | using the trained model on new examples *without* answers |
| **Supervised learning** | learning from examples that include the correct answer |
| **Regression / classification** | predicting a number / predicting a category |
| **Train / test split** | keep some rows hidden during training, use them to check the model fairly |
| **Baseline** | the score of a simple guess (always predict the average); a model must beat it |
| **Metric** | the number that says how good predictions are (MAE, accuracy, precision, recall) |
| **Overfitting** | the model memorised the training rows (great training score) and fails on new rows |
| **Underfitting** | the model is too simple to capture the pattern; bad on training *and* test data |
| **Data leakage** | a feature secretly contains the answer (e.g. `final_score` when predicting `passed`): perfect test score, useless in real life |

## LLM words

| Term | Plain meaning |
|------|---------------|
| **Token** | a chunk of text (a word or part of a word) the model reads and writes; cost and limits are counted in tokens |
| **Next-token prediction** | an LLM writes by repeatedly guessing the most suitable next token |
| **Prompt** | the text you send to the model |
| **System message** | standing instructions for the model ("You are a helpful assistant that answers in JSON") |
| **Context window** | the maximum amount of text (prompt + reply) the model can handle at once |
| **Temperature** | how random the replies are: low = predictable, high = more varied |
| **Few-shot prompt** | a prompt that includes a few worked examples of input → desired output |
| **Hallucination** | a confident, fluent answer that is false or made up; always check facts |
| **API key** | a secret password that lets your program use a paid model; it lives in `.env`, never in code |
| **Mock model** | a fake, rule-based stand-in for the LLM so programs and tests run offline and free |

## Examples

### 1. Rules vs learning a rule from examples

```python
past = [(2, False), (5, False), (7, True), (9, True), (12, True), (4, False)]   # (study hours, passed?)

best_threshold, best_correct = 0, 0
for threshold in range(0, 15):          # "training": try every rule "passed if hours >= threshold"
    correct = 0
    for hours, passed in past:
        if (hours >= threshold) == passed:
            correct += 1
    if correct > best_correct:
        best_threshold, best_correct = threshold, correct
print(best_threshold, best_correct)     # 6 6
print(8 >= best_threshold)              # True   (inference: a new student who studies 8 hours)
```

### 2. Features vs target

```python
row = {"study_hours": 8.5, "attendance_pct": 92, "program": "science", "passed": 1}
target = "passed"
features = [column for column in row if column != target]
print(features)   # ['study_hours', 'attendance_pct', 'program']
```

### 3. Overfitting: memorising is not learning

```python
training_rows = {3: "fail", 8: "pass", 11: "pass"}   # hours -> result


def memoriser(hours):
    return training_rows.get(hours, "no idea")


print(memoriser(8), memoriser(9))   # pass no idea
```

Perfect on the rows it has seen, useless on a new student: that is overfitting in its purest form.

## Common mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Calling every program "AI" | rule-based code described as "learning" | Ask: did it learn from examples? |
| Mixing up feature and target | target column used as an input | Name the target first, everything else is a candidate feature |
| Judging a model on its training data | amazing score that disappears on new data | Always report the **test** score |
| Trusting an LLM answer because it sounds confident | hallucinated facts in your app | Validate, check against your data, keep a human in the loop |
| No baseline | "80 % accuracy" that a constant guess also gets | Compare with the baseline every time |

## See also

- [05 scikit-learn workflow](05-scikit-learn-workflow.md): metrics in code
- [06 LLM apps](06-llm-apps.md): prompts, mocks and validation
- [03 pandas](03-pandas.md): fixing data quality problems

# Brier Score Calculator

This project provides a Python function to compute the Brier Score, a measure used to quantify the accuracy of probabilistic predictions. 

## Background

The Brier score is named after Glenn W. Brier and measures the mean squared difference between predicted probabilities and actual outcomes. It's a proper score function, meaning it will reward you for being honest about your uncertainty. The formula to compute the Brier score is as follows:

<p>
Brier Score = (1/N) * Σ (f<sub>i</sub> - o<sub>i</sub>)<sup>2</sup>
</p>

where:
- \( N \) is the total number of questions,
- \( f_i \) is the forecasted probability for the \( i \)-th question,
- \( o_i \) is the actual outcome of the \( i \)-th question (1 for true, 0 for false).

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/a-jiwa/brier-score-calculator.git
cd brier-score-calculator
```

## Usage

The primary function brier_score(forecasts, outcomes) computes the Brier score given a list of forecasted probabilities and a corresponding list of actual outcomes.

## License

MIT
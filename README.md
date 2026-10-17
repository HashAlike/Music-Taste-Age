# Music Taste & Age

🚧 **Work in Progress**

An exploratory Data Science project investigating how music preferences change with age and which factors may explain these changes.

## Research Question

**How does music taste change as people get older, and which factors may explain these changes?**

The project aims to explore the relationship between age and music preferences while considering factors such as generation, musical era, and cultural background.

## Project Goals

- Explore patterns in music preferences across different age groups.
- Investigate potential generational and cultural differences.
- Collect and preprocess music-related data.
- Experiment with classification models for distinguishing music from non-music content as a supporting task.
- Identify limitations and potential biases in the collected data.

## Data Sources

- **Last.fm API:** Listening history and music metadata.
- **YouTube Data API:** Planned source for video metadata and a balanced music/non-music classification benchmark.

Data collection and preprocessing are ongoing. The availability of reliable age-related information remains a key challenge.

## Tools & Technologies

- Python
- pandas
- scikit-learn
- Hugging Face Transformers
- Last.fm API
- YouTube Data API (integration in progress)
- Jupyter Notebook
- Git & GitHub

## Current Status

- [x] Initial project structure
- [x] Last.fm API data collection experiments
- [x] Initial data exploration and preprocessing
- [x] Preliminary zero-shot classification experiments
- [ ] YouTube Data API integration and testing
- [ ] Build and validate a balanced classification benchmark
- [ ] Conduct exploratory analysis of age-related music preferences
- [ ] Evaluate findings, limitations, and potential biases

## Limitations

Listening history alone does not provide reliable information about a listener's age. Meaningful age-related analysis requires an appropriate data source with trustworthy age information.

Classification experiments are preliminary and require a carefully validated, representative test dataset.

## Project Status

This project is a work in progress. The primary goal is to investigate music taste and age; classification experiments are supporting work rather than the main research objective.

# Music Trends

🚧 **Work in Progress**

An exploratory Data Science project investigating how music genres evolve over time, how their popularity changes, and which factors may explain these trends.

## Research Question

**How do music genre trends evolve over time, and what factors may explain these changes?**

The project aims to explore changes in music genre popularity through listening behavior, artist-level patterns, and cross-platform observations.

Individual listening preferences will be examined as a way to understand broader music trends, while artist-level analysis will provide supporting evidence for genre-level findings.

## Project Goals

- Explore how the popularity of different music genres changes over time.
- Identify emerging, declining, and persistent genre trends.
- Analyze individual listening behavior to discover patterns behind broader trends.
- Examine artist-level popularity changes as supporting evidence for genre trends.
- Compare music-related patterns across Last.fm and YouTube.
- Investigate potential relationships between listening behavior and platform-level popularity signals.
- Experiment with time series analysis and predictive models where the collected data supports them.
- Identify limitations, sampling biases, and inconsistencies across data sources.

## Data Sources

- **Last.fm API:** Listening histories, track information, artist metadata, and individual listening behavior.
- **YouTube Data API:** Video metadata, channel information, publication dates, and available popularity metrics.
- **SSI-2012 Dataset:** A supplementary dataset for exploring relationships between age groups and music preferences, where relevant.

The datasets will be analyzed according to their respective scopes. Last.fm listening histories and YouTube platform metrics will not be treated as directly equivalent measures of music consumption.

## Tools & Technologies

- Python
- pandas
- NumPy
- scikit-learn
- Hugging Face Transformers
- Last.fm API
- YouTube Data API
- Jupyter Notebook
- Git & GitHub

## Project Roadmap

### Phase 1 — Data Collection & Preparation
- [x] Initial project structure
- [x] Last.fm API integration and data collection experiments
- [x] Initial data exploration and preprocessing
- [x] YouTube Data API integration and testing
- [ ] Define a consistent data collection strategy
- [ ] Expand and organize the collected datasets
- [ ] Evaluate data quality, coverage, and sampling limitations

### Phase 2 — Genre Identification & Data Integration
- [ ] Investigate genre metadata availability and reliability
- [ ] Develop a consistent genre mapping strategy
- [ ] Handle artists and tracks associated with multiple genres
- [ ] Connect relevant Last.fm and YouTube records using reliable identifiers
- [ ] Prepare analysis-ready datasets

### Phase 3 — Genre Trend Analysis
- [ ] Analyze genre popularity over time
- [ ] Identify emerging, declining, and persistent genres
- [ ] Explore changes in genre listening patterns
- [ ] Investigate similarities and differences across user groups
- [ ] Visualize temporal trends and relationships

### Phase 4 — Artist-Level Supporting Analysis
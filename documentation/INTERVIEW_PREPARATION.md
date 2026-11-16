# Interview preparation — Horizon Retail

1. **Why this project?** To practice Python analysis, reproducibility and business decision-making on a fictional case.
2. **Why no machine learning?** The case supplies aggregated facts and planning scores, not a suitable labeled dataset for model training.
3. **Weighted score formula?** Sum of each criterion score multiplied by its weight. Weights total 1.
4. **Why customer enquiries?** Highest original weighted score (3.80), conditional on policy/data readiness and human oversight.
5. **What changed in sensitivity analysis?** Customer data readiness decreased 3 to 1; its total decreased 0.40 to 3.40; inventory at 3.60 became first.
6. **What are the main limitations?** Fictional aggregate inputs, subjective scoring, unverified costs and no measured pilot outcomes.
7. **What Python engineering practices are shown?** Modular functions, validation, tests, reproducible input/output files and source control.
8. **What would be needed for an API?** Request schemas, persistent storage, endpoints, authentication where appropriate, integration tests and deployment. Not implemented here.

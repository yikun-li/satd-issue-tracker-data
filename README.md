# SATD Dataset in Issue Tracking Systems

##### Authors: Yikun Li, Mohamed Soliman, Paris Avgeriou

## Description of this dataset:

This dataset contains 23,180 issue sections (that includes 3,277 SATD issue sections) from seven large open-source
projects from two ecosystems: Apache and Google. We call each part of an issue (i.e. summary, description or comment) as
issue section. The number of different types/indicators of SATD is shown as below:

| Type of SATD       | Indicator of SATD                                     | Definition                                                                                                                                                                                            | Number |
|--------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Architecture debt  | Violation of modularity                               | Because shortcuts were taken, multiple modules became inter-dependent, while they should be independent.                                                                                              | 46     |
|                    | Using obsolete technology                             | Architecturally-significant technology has become obsolete.                                                                                                                                           | 41     |
| Build debt         | Over- or under-declared dependencies                  | Under-declared dependencies: dependencies in upstream libraries are not declared and rely on dependencies in lower level libraries. Over-declared dependencies: unneeded dependencies are declared.   | 25     |
|                    | Poor deployment practice                              | The quality of deployment is low that compile flags or build targets are not well organized.                                                                                                          | 39     |
| Code debt          | Complex code                                          | Code has accidental complexity and requires extra refactoring action to reduce this complexity.                                                                                                       | 30     |
|                    | Dead code                                             | Code is no longer used and needs to be removed.                                                                                                                                                       | 121    |
|                    | Duplicated code                                       | Code that occurs more than once instead of as a single reusable function.                                                                                                                             | 40     |
|                    | Low-quality code                                      | Code quality is low, for example because it is unreadable, inconsistent, or violating coding conventions.                                                                                             | 856    |
|                    | Multi-thread correctness                              | Thread-safe code is not correct and may potentially result in synchronization problems or efficiency problems.                                                                                        | 40     |
|                    | Slow algorithm                                        | A non-optimal algorithm is utilized that runs slowly.                                                                                                                                                 | 159    |
| Defect debt        | Uncorrected known defects                             | Defects are found by developers but ignored or deferred to be fixed.                                                                                                                                  | 25     |
| Design debt        | Non-optimal decisions                                 | Non-optimal design decisions are adopted.                                                                                                                                                             | 935    |
| Documentation debt | Low-quality documentation                             | The documentation has been updated reflecting the changes in the system, but quality of updated documentation is low.                                                                                 | 342    |
|                    | Outdated documentation                                | A function or class is added, removed, or modified in the system, but the documentation has not been updated to reflect the change.                                                                   | 144    |
| Requirement debt   | Requirements partially implemented                    | Requirements are implemented, but some are not fully implemented.                                                                                                                                     | 67     |
|                    | Non-functional requirements not being fully satisfied | Non-functional requirements (e.g. availability, capacity, concurrency, extensibility), as described by scenarios, are not fully satisfied.                                                            | 29     |
| Test debt          | Expensive tests                                       | Tests are expensive, resulting in slowing down testing activities. Extra refactoring actions are needed to simplify tests.                                                                            | 28     |
|                    | Flaky tests                                           | Tests fail or pass intermittently for the same configuration.                                                                                                                                         | 83     |
|                    | Lack of tests                                         | A function is added, but no tests are added to cover the new function.                                                                                                                                | 158    |
|                    | Low coverage                                          | Only part of the source code is executed during testing.                                                                                                                                              | 69     |

## Paper

Latest version available on [arXiv](https://arxiv.org/abs/2202.02180)

Please adequately refer to this paper any time this dataset is being used. If you publish a paper where this dataset
helps your research, we encourage you to cite the following paper in your publication:

```
@misc{https://doi.org/10.48550/arxiv.2202.02180,
  doi = {10.48550/ARXIV.2202.02180},
  url = {https://arxiv.org/abs/2202.02180},
  author = {Li, Yikun and Soliman, Mohamed and Avgeriou, Paris},
  keywords = {Software Engineering (cs.SE), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Identifying Self-Admitted Technical Debt in Issue Tracking Systems using Machine Learning},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Contact

- Please use the following email addresses if you have questions:
    - :email: <yikun.li@rug.nl>